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

No hay build step. La única fuente de verdad del contenido es `Andrea_Muniz_Completo_v2.html` (template con placeholders). `public/index.html` se **genera** a partir del template más `update-placeholders.config` (valores reales: WhatsApp, email, IDs de Formspree, dominio).

### Preview local

1. Corre el script una vez — si no existe `update-placeholders.config` te crea un template:
   ```bash
   python update-placeholders.py
   ```
2. Edita `update-placeholders.config` con los valores reales (IDs de Formspree, dominio, WhatsApp, email) y vuelve a correr:
   ```bash
   python update-placeholders.py
   ```
3. Servilo:
   ```bash
   npx serve public
   # o
   python -m http.server 8000 -d public
   ```

> `update-placeholders.config` está en `.gitignore` — tiene datos privados de Andrea (teléfono, email).

## Conectar servicios externos

Los dos formularios (postulación al taller y inscripción al workshop) apuntan a `https://formspree.io/f/XXXXXXXX` como placeholder. El script los reemplaza con los IDs reales. También reemplaza dominio, handle de Instagram, número WhatsApp y email.

Detalle completo en `Guia_Despliegue_Andrea_Muniz.docx` (7 pasos guiados).

## Deploy a Firebase Hosting

### Automático (recomendado)

Cada `git push` a `main` dispara GitHub Actions que:

1. Genera `update-placeholders.config` desde los **GitHub Secrets** del repo.
2. Corre `python update-placeholders.py` → regenera `public/index.html`.
3. Valida que no queden placeholders sin resolver (Formspree `XXXXXXXX`, WhatsApp `56900000000`).
4. Publica a Firebase Hosting en el canal `live`.

**Secrets requeridos** (Settings → Secrets and variables → Actions):

| Secret | Valor actual |
|---|---|
| `FORMSPREE_TALLER_ID` | ID del form de postulación al taller |
| `FORMSPREE_WORKSHOP_ID` | ID del form de inscripción al workshop |
| `DOMAIN` | `andreamuniz.cl` (sin `https://`) |
| `INSTAGRAM_HANDLE` | `andreamuniz` (sin `@`) |
| `WHATSAPP_NUMBER` | Ej `56985028131` — solo dígitos, con código país |
| `EMAIL` | Email de contacto de Andrea |
| `FIREBASE_SERVICE_ACCOUNT_ANDREA_MUNIZ_LANDING` | JSON del service account de Firebase |

PRs en el mismo repo disparan un preview temporal (URL única, expira a los 7 días).

### Manual (emergencia)

Requiere [Firebase CLI](https://firebase.google.com/docs/cli) y `update-placeholders.config` local.

```bash
firebase login
firebase use andrea-muniz-landing
python update-placeholders.py   # regenera public/index.html
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
