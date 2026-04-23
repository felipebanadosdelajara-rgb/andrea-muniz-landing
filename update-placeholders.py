#!/usr/bin/env python3
"""
update-placeholders.py
----------------------
Reemplaza los placeholders de Andrea_Muniz_Completo_v2.html por los valores
reales (Formspree IDs, dominio, handles, WhatsApp, email) y genera un
`index.html` listo para subir al hosting.

USO:
  1. Editar el archivo `update-placeholders.config` (se crea automáticamente
     la primera vez que corres este script si no existe).
  2. Ejecutar:   python update-placeholders.py
  3. Se genera `index.html` en la misma carpeta.

Requiere Python 3.8+. Sin dependencias externas.
"""

import base64
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
SOURCE = ROOT / "Andrea_Muniz_Completo_v2.html"
OUTPUT = ROOT / "public" / "index.html"  # destino final (listo para firebase deploy)
CONFIG = ROOT / "update-placeholders.config"

CONFIG_TEMPLATE = """# Configuración de placeholders · Andrea Muñiz landing
# Edita los valores a la derecha del signo igual. No uses comillas.
# Cualquier línea que empiece con # se ignora.

# -- Formspree (obtener en https://formspree.io tras crear cada formulario) --
FORMSPREE_TALLER_ID   = XXXXXXXX
FORMSPREE_WORKSHOP_ID = XXXXXXXX

# -- Dominio real del sitio (sin https:// ni barras) --
DOMAIN = andreamuniz.cl

# -- Redes sociales --
INSTAGRAM_HANDLE = andreamuniz
# WhatsApp en formato internacional sin +, espacios ni guiones.
# Ejemplo: 56912345678
WHATSAPP_NUMBER  = 56900000000

# -- Email de contacto --
EMAIL = hola@andreamuniz.cl
"""


def load_config():
    if not CONFIG.exists():
        CONFIG.write_text(CONFIG_TEMPLATE, encoding="utf-8")
        print(f"[!] No se encontró {CONFIG.name}. Creado un template.")
        print("    Edítalo con tus datos reales y vuelve a correr el script.")
        sys.exit(0)

    cfg = {}
    for line in CONFIG.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        k, v = line.split("=", 1)
        cfg[k.strip()] = v.strip()

    required = [
        "FORMSPREE_TALLER_ID",
        "FORMSPREE_WORKSHOP_ID",
        "DOMAIN",
        "INSTAGRAM_HANDLE",
        "WHATSAPP_NUMBER",
        "EMAIL",
    ]
    missing = [k for k in required if not cfg.get(k)]
    if missing:
        print(f"[!] Faltan valores en {CONFIG.name}: {', '.join(missing)}")
        sys.exit(1)

    # Validaciones suaves
    for k in ("FORMSPREE_TALLER_ID", "FORMSPREE_WORKSHOP_ID"):
        if "XXXXXXXX" in cfg[k]:
            print(f"[!] {k} sigue con placeholder 'XXXXXXXX'. Reemplázalo.")
            sys.exit(1)

    if not cfg["WHATSAPP_NUMBER"].isdigit():
        print(f"[!] WHATSAPP_NUMBER debe ser solo dígitos (sin + ni espacios).")
        sys.exit(1)

    return cfg


REPLACEMENTS_PATTERN = [
    # (regex, template-con-{cfg-key})
    # -- Formspree endpoints (no usar en main — sólo existen en frames) --
    # -- Dominio --
    (r"https://andreamuniz\.cl", "https://{DOMAIN}"),
    (r"andreamuniz\.cl", "{DOMAIN}"),
    # -- Instagram --
    (r"https://instagram\.com/andreamuniz", "https://instagram.com/{INSTAGRAM_HANDLE}"),
    (r"@andreamuniz\b", "@{INSTAGRAM_HANDLE}"),
    # -- WhatsApp --
    (r"https://wa\.me/56900000000", "https://wa.me/{WHATSAPP_NUMBER}"),
    # -- Email --
    (r"hola@andreamuniz\.cl", "{EMAIL}"),
]


def apply_text_replacements(text, cfg):
    """Aplica reemplazos de texto plano (dominio, handles, email, WhatsApp)."""
    for pattern, template in REPLACEMENTS_PATTERN:
        replacement = template.format(**cfg)
        text = re.sub(pattern, replacement, text)
    return text


def replace_formspree_in_frame(html, new_id):
    """Reemplaza el action de Formspree dentro de un frame HTML decodificado."""
    return re.sub(
        r'action="https://formspree\.io/f/XXXXXXXX"',
        f'action="https://formspree.io/f/{new_id}"',
        html,
    )


def process_frames(main_html, cfg):
    """
    Los frames (postulacion / workshop) están embebidos como Base64 en el
    objeto JS `_frames`. Los decodificamos, les aplicamos reemplazos, los
    re-encodeamos y los reinsertamos.
    """
    pattern = re.compile(
        r'("(?P<key>taller|workshop)":\s*")(?P<b64>[A-Za-z0-9+/=]+)(")'
    )

    def replace_frame(m):
        key = m.group("key")
        b64 = m.group("b64")
        html = base64.b64decode(b64).decode("utf-8")

        # 1) Reemplazar Formspree ID según el frame
        if key == "taller":
            html = replace_formspree_in_frame(html, cfg["FORMSPREE_TALLER_ID"])
        elif key == "workshop":
            html = replace_formspree_in_frame(html, cfg["FORMSPREE_WORKSHOP_ID"])

        # 2) Reemplazos de texto (dominio, handles, etc.)
        html = apply_text_replacements(html, cfg)

        new_b64 = base64.b64encode(html.encode("utf-8")).decode("ascii")
        return m.group(1) + new_b64 + m.group(4)

    return pattern.sub(replace_frame, main_html)


def main():
    print(f"→ Leyendo config desde {CONFIG.name}...")
    cfg = load_config()

    if not SOURCE.exists():
        print(f"[!] No se encontró {SOURCE.name} en esta carpeta.")
        sys.exit(1)

    print(f"→ Leyendo {SOURCE.name} ({SOURCE.stat().st_size:,} bytes)...")
    content = SOURCE.read_text(encoding="utf-8")

    # Paso 1: frames embebidos (decodificar, reemplazar, re-encodear)
    print("→ Actualizando subpáginas Base64 (postulación + inscripción)...")
    content = process_frames(content, cfg)

    # Paso 2: reemplazos en el HTML principal (dominio, handles, email)
    print("→ Reemplazando dominio, handles, email y WhatsApp en el cuerpo...")
    content = apply_text_replacements(content, cfg)

    # Paso 3: escribir index.html
    OUTPUT.write_text(content, encoding="utf-8")
    print(f"→ Generado {OUTPUT.name} ({OUTPUT.stat().st_size:,} bytes)")

    # Reporte
    print()
    print("── Resumen de valores aplicados ──")
    print(f"  Dominio:              https://{cfg['DOMAIN']}")
    print(f"  Instagram:            @{cfg['INSTAGRAM_HANDLE']}")
    print(f"  WhatsApp:             https://wa.me/{cfg['WHATSAPP_NUMBER']}")
    print(f"  Email:                {cfg['EMAIL']}")
    print(f"  Formspree taller:     https://formspree.io/f/{cfg['FORMSPREE_TALLER_ID']}")
    print(f"  Formspree workshop:   https://formspree.io/f/{cfg['FORMSPREE_WORKSHOP_ID']}")
    print()
    print("✓ Listo. Sube `index.html` a Cloudflare Pages / Netlify / Vercel.")


if __name__ == "__main__":
    main()
