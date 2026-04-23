# Auditoría · Andrea_Muniz_Completo.html

**Cliente:** Andrea Muñiz Berguecio · Artista, diseñadora y coach en formación
**Archivo auditado:** `Andrea_Muniz_Completo.html` (single-file HTML, 1.321 líneas, 1.1 MB)
**Entregable corregido:** `Andrea_Muniz_Completo_v2.html` (1.932 líneas, ~1.16 MB)
**Fecha:** 2026-04-20

---

## 1 · Resumen ejecutivo — hallazgos críticos

1. **Formularios sin backend real.** Los dos formularios embebidos simulaban envío con un mock JS. Cualquier postulación o inscripción se perdía. → **RESUELTO**: ambos forms apuntan a un endpoint Formspree configurable (`action="https://formspree.io/f/XXXXXXXX"`) con `fetch` real, estados de carga, mensajes de error y éxito persistente.
2. **Sin protección anti-spam ni consentimiento legal.** Se recolectaban RUT, dirección y teléfono sin honeypot, sin reCAPTCHA y sin nota legal conforme a la Ley 19.628. → **RESUELTO**: honeypot `_honeypot` oculto, campo `_subject`, nota legal visible bajo cada submit y política de privacidad mínima en el footer del sitio principal.
3. **Accesibilidad débil.** Faltaban `aria-expanded` en el hamburguesa, `role="dialog"` en el overlay de iframe, skip-link, `lang` consistente, y no se cerraba con ESC. → **RESUELTO**: skip-link, landmark `<main>`, `aria-expanded` sincronizado, overlay con `role=dialog` + `aria-modal`, cierre con ESC y con botón dedicado, foco restaurado al cerrar.
4. **SEO ausente.** Sin Open Graph, Twitter Card, canonical, favicon, schema.org ni keywords. Cualquier compartido en WhatsApp/Instagram se veía sin preview. → **RESUELTO**: meta completas, OG + Twitter Card, `<link rel="canonical">`, favicon SVG embebido, JSON-LD con Person + LocalBusiness + Offer (taller y coaching).
5. **19 emojis en el sitio (ruido visual).** Cada emoji se renderiza distinto en iOS/Android/Windows y degrada la percepción editorial. → **RESUELTO**: 100% reemplazados por SVG inline 1.5px stroke, heredando `currentColor`. Ver mapa en `Andrea_Muniz_MAPA_EMOJIS.md`.
6. **Hovers agresivos (`transform: scale(1.04)`).** Comportamiento propio de sitios promocionales, no editoriales. → **RESUELTO**: toda interacción usa `translateY(-1px)` + cambio de `box-shadow` con curva unificada `cubic-bezier(.4,0,.2,1)`.
7. **Tablas como divs flex.** `.pago-row` y el resumen de jornada se leían como bloques, no como tablas. → **RESUELTO**: resumen de pago convertido a `<table>` semántica con `<thead>`, `<tbody>`, fila total destacada. Coaching cards duplicadas con una tabla comparativa real. Proceso de ingreso con círculos editoriales bordeados (1.5px) reemplazando los sólidos.

---

## 2 · Informe detallado (tabla de auditoría)

| # | Ítem | Estado actual (original) | Riesgo | Recomendación / acción aplicada |
|---|------|--------------------------|--------|---------------------------------|
| 1 | **Envío real de formularios** | Handler mock con `setTimeout`. Datos perdidos. | **Crítico** — postulaciones y pagos no llegan. | Integrar Formspree (plan gratis: 50/mes; plan Gold USD 10/mes ilimitado). Reemplazar `XXXXXXXX` en `action` por el ID del endpoint. Alternativas: Netlify Forms (nativo, sin config), Web3Forms (gratis, sin cuenta), Formsubmit.co (gratis, 50/día). |
| 2 | **Validación client-side** | Sólo `required` básicos. Sin mensajes. Sin patrón RUT ni teléfono CL. | Medio — datos inválidos llegan al correo. | ✅ Agregado `pattern` para RUT chileno (`^(\d{1,2}\.?\d{3}\.?\d{3}-?[\dkK])$`), teléfono CL (`^(\+?56)?\s?9\s?\d{4}\s?\d{4}$`), `minlength` en textareas, mensajes en español bajo cada input con `[data-error]`. |
| 3 | **Alt en imágenes** | Las 2 imágenes inline ya tenían alt. Badges decorativos (`.bg-circle`) no marcados. | Bajo. | ✅ `aria-hidden="true"` en elementos decorativos (círculos, date-blocks, icon-boxes). |
| 4 | **Contraste WCAG AA (lava sobre claro)** | `--lava-mid` #9B8FCA sobre `--lava-pale` #EDEAF8 ~2.5:1 (falla AA). | Medio — accesibilidad. | ✅ Textos pasados a `--lava-deep` #6B5CA5 (ratio >4.5:1 sobre fondos pale). Badges `ws-badge-open` en featured usan `--lava-deep` sólido. |
| 5 | **Navegación por teclado** | Sin skip-link; focus-visible no marcado. | Medio. | ✅ Skip-link antes del nav; `:focus-visible` con outline 2px `--sage-deep`; botones con `aria-label`. |
| 6 | **ARIA en overlay iframe** | `div` sin rol, sin modal semantics, ESC no cierra. | Alto — lector de pantalla anuncia "vacío". | ✅ `role="dialog"`, `aria-modal="true"`, `aria-hidden` sincronizado, ESC cierra, foco retorna al trigger, botón X visible. |
| 7 | **`lang` en subpáginas** | Ya presentes (`lang="es"`). | Bajo. | ✅ Mantenido + añadido `<html lang="es">` verificado, `<meta name="robots" content="noindex,nofollow">` en ambas subpáginas (no son landings públicas). |
| 8 | **Meta description** | Presente. | Bajo. | ✅ Ampliada + añadidas keywords, author, theme-color. |
| 9 | **Open Graph + Twitter Card** | Ausentes. | Alto — compartir en IG/WS da preview vacío. | ✅ OG completo (`og:image`, `og:url`, `og:type`, `og:locale=es_CL`) + Twitter Card `summary_large_image`. Falta generar una imagen `/og-cover.jpg` 1200×630 (ver guía de despliegue). |
| 10 | **Schema.org** | Ausente. | Medio — Google no muestra rich results. | ✅ JSON-LD con `Person` + `LocalBusiness` + dos `Offer` (taller, coaching). |
| 11 | **Favicon** | Ausente. | Bajo — pestaña sin icono. | ✅ Favicon SVG embebido (inline data URI, sin request extra). |
| 12 | **Canonical URL** | Ausente. | Bajo. | ✅ `<link rel="canonical" href="https://yoteescucho.com/">`. |
| 13 | **Carga de Google Fonts** | `display=swap` ya presente + preconnect. OK. | Bajo. | Mantenido. No conviene autohospedar por ahora (complejidad >> beneficio). |
| 14 | **Tamaño del archivo (1.1 MB)** | 2 imágenes JPEG Base64 (180 KB + 850 KB) y 2 subpáginas Base64 (~43 KB). | Medio — primer render lento en 3G. | **Recomendación no aplicada (requiere aprobación):** extraer las 2 imágenes a archivos reales (`/img/andrea.jpg`, `/img/casa-taller.jpg`), reemplazar por `<img src="...">` con `loading="lazy"`. Eso baja el HTML a ~120 KB. Las subpáginas Base64 **se mantienen** (arquitectura correcta para single-file). |
| 15 | **Imágenes optimizadas** | JPEGs embebidos no optimizados. | Medio. | Convertir a WebP + JPG fallback (usar `<picture>`). Estimado: ~40% menos peso. (Fuera de scope de este pase; requiere acceso a los originales.) |
| 16 | **`will-change` en animaciones** | No usado. Ya correcto. | — | Mantenido. |
| 17 | **Sanitización inputs** | Se envía a Formspree (sanitiza server-side). | Bajo. | ✅ OK. Nunca se inyecta input del usuario en el DOM. |
| 18 | **Protección anti-spam** | Ausente. | Alto — cualquier bot envía. | ✅ Honeypot `_honeypot`. Recomendación complementaria: activar en Formspree el filtro Akismet integrado, o agregar Cloudflare Turnstile (gratis) si aumenta el spam. |
| 19 | **Headers de seguridad** | Ausentes (HTML estático). | Medio si se aloja mal. | Configurar en el host (ver guía de despliegue): CSP, `Referrer-Policy`, `X-Content-Type-Options`. |
| 20 | **Base64 vs archivos separados** | Subpáginas Base64 en objeto `_frames`. | **Pros**: portabilidad absoluta, zero-config deploy, no hay navegación rota. **Contras**: no indexables, no compartibles vía URL, costo de decodificación en cada `showFrame`, más pesado para primer load. | **Mantener** la arquitectura actual por la propuesta de valor (single-file). Si Felipe quiere indexar los formularios por separado (para que Andrea los comparta por URL directa en IG, por ejemplo), pasar a `/postulacion.html` y `/inscripcion.html` separados. Recomendación: no separar ahora, revisar en 3 meses según tráfico. |
| 21 | **Datos personales y Ley 19.628** | Se recolectan RUT, dirección, teléfono sin nota legal. | **Alto** — incumplimiento Ley de Protección de Datos Personales de Chile. | ✅ Nota legal visible bajo cada submit enlazando a la sección `#privacidad` del footer; política de privacidad mínima en footer; texto conforme a Ley 19.628. |
| 22 | **Emojis como iconos** | 19 emojis distintos (🌱 🌿 🎨 🎯 🏡 👥 💛 💡 💬 💰 📅 📍 🕙 🖼 🧱 ✨ ✦ ★ ✓). | Medio — inconsistencia visual entre OS. | ✅ 100% reemplazados por SVG inline con `stroke-width:1.5` y `currentColor`. Ver mapa detallado. |
| 23 | **Sistema de sombras** | 5 sombras distintas inline en distintos elementos. | Bajo — inconsistencia. | ✅ 3 tokens CSS: `--shadow-sm`, `--shadow-md`, `--shadow-lg`. |
| 24 | **Radios de borde** | 8, 10, 12, 14, 16, 20, 24, 32 px conviviendo. | Bajo. | ✅ Sistema reducido: `--radius-sm/md/lg/xl/pill` (8/12/16/24/9999). |
| 25 | **Transiciones** | Diversas curvas y duraciones. | Bajo. | ✅ Curva única `cubic-bezier(.4,0,.2,1)` + 3 duraciones (`--dur-fast/base/slow`). |
| 26 | **Hover `scale(1.04)`** | Agresivo en botones. | Bajo — percepción editorial. | ✅ Reemplazado por `translateY(-1px)` + `box-shadow`. |
| 27 | **Tabla resumen de pago** | `div.pago-row` con flex. | Bajo — semántica. | ✅ `<table>` con `<thead>`/`<tbody>`, montos con `text-align:right` + `tabular-nums`, fila total en `var(--bg-alt)` con Playfair. |
| 28 | **Cronograma jornada (`.taller-exp`)** | Separador `1px solid`. | Bajo. | ✅ Separador `1px dotted`, horario en Playfair 700 (no caps), mayor alineamiento baseline. |
| 29 | **Proceso de ingreso (`.process-steps`)** | Círculos sólidos 24×24 `var(--earth-warm)` fondo. | Bajo — visual publicitario. | ✅ Círculos 28×28, borde 1.5px, número en Playfair en `var(--earth-warm)` sobre transparente. Variante `.inverted` disponible. |
| 30 | **Taller-quote (borde izq 3px)** | Barra sólida. | Bajo. | ✅ Comilla tipográfica `"` en Playfair itálico 5rem, opacidad .22, posición absoluta top-left. Padding interior 46px. |
| 31 | **Ws-card-header (bloque sólido lava-pale)** | Demasiado contrastado. | Bajo. | ✅ Fondo transparente + borde inferior 1px, badges refinados con borde. |
| 32 | **Aviso-box (subpágina)** | 🌿 emoji + padding 24×28. | Bajo. | ✅ SVG hoja dentro de contenedor 44×44 sage-pale; padding 28×32; shadow-sm. |
| 33 | **Testimonial stars (★★★★★)** | Caracteres Unicode. | Bajo. | ✅ 5 SVG filled stars con `role="img"` y `aria-label="5 de 5 estrellas"`. |
| 34 | **`<main>` landmark** | Ausente. | Bajo — a11y. | ✅ `<main id="main-content">` envuelve todas las secciones. |
| 35 | **`id` duplicado (`agenda`)** | `coaching-price-row` y `coaching-cta-row` ambos con `id="agenda"`. | Bajo — HTML inválido. | ✅ Eliminado el duplicado. |

---

## 3 · Accesibilidad resumen (WCAG 2.1 AA)

- **1.1.1 Non-text content**: todas las imágenes decorativas `aria-hidden`, informativas con `alt`. ✅
- **1.4.3 Contrast**: ratios recalculados; textos mínimos 4.5:1. ✅
- **2.1.1 Keyboard**: navegación completa sin mouse; ESC cierra modal. ✅
- **2.4.1 Bypass blocks**: skip-link activo. ✅
- **2.4.3 Focus order**: preservado en el flujo natural + `autofocus` evitado. ✅
- **3.3.1 Error identification**: cada error con `[data-error]` + mensaje bajo el campo. ✅
- **4.1.2 Name, role, value**: botones con `aria-label`, modal con `role=dialog`. ✅

---

## 4 · Pendientes recomendados (fuera de scope de este pase)

1. **Generar `og-cover.jpg`** de 1200×630 con el branding del sitio (usar Figma o Canva; subir a `/og-cover.jpg`).
2. **Reemplazar `XXXXXXXX` en los dos `action`** de los formularios por el ID real de Formspree/Netlify.
3. **Actualizar teléfono WhatsApp real** en `wa.me/56900000000` (link en footer).
4. **Separar imágenes Base64** a archivos para bajar el peso del HTML de 1.1 MB a ~120 KB (requiere aprobación explícita porque rompe la condición "single-file autocontenido").
5. **Configurar reCAPTCHA v3 o Cloudflare Turnstile** si aparece spam en producción.
6. **Sincronizar enlace `#privacidad`** dentro de las subpáginas para que, al hacer clic, cierre el modal y haga scroll en la página principal (actualmente envía `postMessage('back#privacidad')` pero requiere handler adicional en el JS del padre si se quiere auto-scroll).
