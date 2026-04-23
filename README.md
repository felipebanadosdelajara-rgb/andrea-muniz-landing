# Andrea Muñiz · Landing

Sitio web estático (single-page) de **Andrea Muñiz Berguecio** — artista plástica, diseñadora y coach en formación. Promociona sus tres ejes de trabajo: Casa Taller de Escultura Efímera, Sesiones de Coaching Online y Workshops Vivenciales.

> "El arte sana. El coaching transforma. La mezcla es única."

---

## Stack

- **HTML5 / CSS3 / JS vanilla** — sin frameworks, sin build step
- **Single-file**: `public/index.html` contiene el sitio completo más 2 subpáginas (postulación al taller + inscripción al workshop) embebidas en Base64
- **Tipografías**: Playfair Display (titulares) + Inter (cuerpo), vía Google Fonts con `font-display: swap`
- **Iconografía**: SVG inline (stroke 1.5px, hereda `currentColor`) — cero emojis
- **Paleta**: Variante C "Manuscrito Cálido" — crema cálido `#F0E8D6` como protagonista, navy profundo `#2A3554`, ocre `#D9A43C`, teal-grey neutro `#5F6E70`, coral `#CC5249` como micro-acento

## Estructura

```
.
├── public/
│   └── index.html               ← Sitio desplegado (555 KB)
├── Andrea_Muniz_Completo_v2.html ← Archivo fuente maestro (idéntico a public/index.html)
├── update-placeholders.py       ← Script Python para inyectar IDs/dominio reales
├── update-placeholders.config   ← Config local (ignorada por git)
├── firebase.json                ← Config de Firebase Hosting
├── .firebaserc                  ← Alias del proyecto Firebase
├── Andrea_Muniz_AUDITORIA.md    ← Informe de auditoría (35 ítems)
├── Andrea_Muniz_GUIA_DESPLIEGUE.md
├── Andrea_Muniz_MAPA_EMOJIS.md
└── Guia_Despliegue_Andrea_Muniz.docx
```

## Desarrollo

No hay build step. Edita directamente `Andrea_Muniz_Completo_v2.html` y luego copia a `public/index.html` antes del deploy.

```bash
cp Andrea_Muniz_Completo_v2.html public/index.html
```

Para servirlo localmente:

```bash
npx serve public
# o
python -m http.server 8000 -d public
```

## Conectar servicios externos

Los dos formularios (postulación al taller y inscripción al workshop) apuntan a `https://formspree.io/f/XXXXXXXX` como placeholder.

1. Edita `update-placeholders.config` con los datos reales:
   - IDs de Formspree de cada formulario
   - Dominio, handle de Instagram, número WhatsApp, email
2. Corre el script:
   ```bash
   python update-placeholders.py
   ```
3. Se genera un `index.html` con todo inyectado. Cópialo a `public/` y deploya.

Detalle completo en `Guia_Despliegue_Andrea_Muniz.docx` (7 pasos guiados).

## Deploy a Firebase Hosting

Requiere [Firebase CLI](https://firebase.google.com/docs/cli) instalado.

```bash
# Primera vez
firebase login
firebase use TU-PROJECT-ID

# Cada deploy
firebase deploy --only hosting
```

## Características técnicas destacadas

- **SEO**: meta description, Open Graph, Twitter Card, canonical, JSON-LD con `Person` + `LocalBusiness` + `Offer`
- **A11Y**: skip-link, landmarks, focus-visible, ARIA en overlay modal (role=dialog, aria-modal, ESC para cerrar), validación de formularios con mensajes en español
- **Formularios reales**: `fetch` a Formspree con estados de carga, error y éxito persistente + honeypot antispam
- **Privacidad**: nota legal Ley 19.628 bajo cada submit + política de privacidad en el footer
- **Performance**: archivo único de ~555 KB con 2 fotos optimizadas embebidas

## Créditos

- Cliente: **Andrea Muñiz Berguecio**
- Desarrollo: **Felipe Bañados**
- Abril 2026
