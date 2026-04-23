# Mapa de reemplazo de emojis · Andrea_Muniz_Completo.html

Todos los emojis del sitio original fueron reemplazados por SVG inline con `stroke-width:1.5`, `stroke:currentColor` (hereda color del contexto) y `fill:none`. Tamaños: `icon-xs` 14px · `icon-sm` 16px · `icon-md` 20px · `icon-lg` 24px · `icon-xl` 28px.

El SVG está definido en `.icon` + modificadores de tamaño dentro de `<style>` en el archivo principal y también replicado dentro de cada subpágina Base64.

> **Nota:** La tabla siguiente lista los **patrones** de reemplazo. Como varios emojis se usan en múltiples lugares (por ejemplo 🧱 aparece en 5 ubicaciones distintas), se indica "ver ubicaciones" al final de cada fila. El código SVG es idéntico en todas las ocurrencias del mismo emoji, sólo cambia `.icon-xs/sm/md/lg` según el contexto.

---

| # | Ubicación en el archivo | Emoji | Reemplazo SVG (inline) | Contexto / tamaño |
|---|-------------------------|-------|------------------------|-------------------|
| 1 | `hero-note` (línea ~1152 del main) | 📍 | `<svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M12 21s-7-7.5-7-12a7 7 0 1 1 14 0c0 4.5-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>` | MapPin · 16px al lado de "Santiago, Chile" |
| 2 | `.sobre-pills` (6 pills) | 🎨 | `<svg class="icon icon-xs" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="7.5" cy="10" r="1" fill="currentColor" stroke="none"/><circle cx="12" cy="7" r="1" fill="currentColor" stroke="none"/><circle cx="16.5" cy="10" r="1" fill="currentColor" stroke="none"/><circle cx="16" cy="15" r="1" fill="currentColor" stroke="none"/><path d="M12 21c-1.5 0-2-1.2-1.3-2.2.7-1 .1-2.3-.9-2.3H8"/></svg>` | Palette · 14px pill "Artista Plástica" |
| 3 | `.sobre-pills` + `svc-card earth` + `taller-feature` + `taller-badge` | 🧱 | `<svg class="icon icon-xs" viewBox="0 0 24 24"><rect x="3" y="5" width="7" height="5" rx="1"/><rect x="10" y="5" width="11" height="5" rx="1"/><rect x="3" y="10" width="11" height="5" rx="1"/><rect x="14" y="10" width="7" height="5" rx="1"/><rect x="3" y="15" width="7" height="4" rx="1"/><rect x="10" y="15" width="11" height="4" rx="1"/></svg>` | Bricks (stacked blocks). 14/20/24px según contexto. Usado en pill, svc-icon, taller-feature, taller-badge, subpágina taller tag |
| 4 | `.sobre-pills` pill "Pintura Onírica" | 🖼️ | `<svg class="icon icon-xs" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="1.5"/><path d="M20 18l-5-6-4 5-2-2-5 5"/></svg>` | Frame / picture · 14px |
| 5 | `.sobre-pills` pill "Diplomado Coaching" | 💡 | `<svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 1 3.5 10.9c-.6.4-.9 1-.9 1.7V17h-5.2v-1.4c0-.7-.3-1.3-.9-1.7A6 6 0 0 1 12 3z"/></svg>` | Lightbulb line · 14px |
| 6 | `.sobre-pills` pill "Talleres Vivenciales" + `svc-card lava` + `taller-price` cupos + `ws-vivir-item` + `ws-badge-open` | ✨ / ✦ | `<svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M12 3l1.5 5 5 1.5-5 1.5-1.5 5-1.5-5-5-1.5 5-1.5 1.5-5z"/></svg>` (+ sparkles adicionales en svc-card lg) | Sparkle (4-pointed star). 14/20/24px. En `.svc-card lava` se usa versión compuesta con 3 sparkles. |
| 7 | `.sobre-pills` pill "Pedro de Valdivia Norte" + `ws-meta-item` (2 ocurrencias workshop) + subpágina taller tag | 📍 | (mismo SVG MapPin del #1) | 14px/16px según contexto |
| 8 | `.svc-card sage` + `.ws-vivir-item` "Escucharte hacia adentro" | 💬 | `<svg class="icon icon-lg" viewBox="0 0 24 24"><path d="M20 15a3 3 0 0 1-3 3H9l-5 4V6a3 3 0 0 1 3-3h10a3 3 0 0 1 3 3v9z"/></svg>` | Speech bubble · 20px |
| 9 | `.svc-card earth` cupos-badge + subpágina workshop badge "Próximamente" | ⏳ | `<svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M7 3h10M7 21h10M7 3v3a5 5 0 0 0 10 0V3M7 21v-3a5 5 0 0 1 10 0v3"/></svg>` | Hourglass · 14px |
| 10 | `.taller-feature` "Espacio en casa" + subpágina taller tag "Pedro de Valdivia Norte" | 🏡 | `<svg class="icon icon-md" viewBox="0 0 24 24"><path d="M3 11l9-7 9 7v9a2 2 0 0 1-2 2h-4v-6h-6v6H5a2 2 0 0 1-2-2v-9z"/></svg>` | Home · 14/20px |
| 11 | `.taller-feature` "Grupos pequeños" + `ws-meta-item` (2 ocurrencias) + subpágina taller tag "Máximo 6 personas" | 👥 | `<svg class="icon icon-md" viewBox="0 0 24 24"><circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 19a6 6 0 0 1 12 0M15 19a5 5 0 0 1 6.5-4.8"/></svg>` | Users · 14/16/20px |
| 12 | `.taller-feature` "4 clases al mes" + `coaching-cta-row` + subpágina taller tag + `ws-card` date-block (decorativo) | 📅 | `<svg class="icon icon-md" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 9h18M8 3v4M16 3v4"/></svg>` | Calendar · 14/16/20px |
| 13 | `ws-meta-item` "10:00 – 14:00 hrs" (2 ocurrencias) | 🕙 | `<svg class="icon icon-sm" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>` | Clock · 16px |
| 14 | `ws-meta-item` "$35.000 por persona" (2 ocurrencias) | 💰 | `<svg class="icon icon-sm" viewBox="0 0 24 24"><rect x="3" y="6" width="18" height="13" rx="2"/><circle cx="12" cy="12.5" r="3"/><path d="M6 10v-.01M18 15v-.01"/></svg>` | Banknote (billete con círculo central) · 16px |
| 15 | `coaching-card` "Claridad de propósito" | 🎯 | `<svg class="icon icon-md" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5.5"/><circle cx="12" cy="12" r="2"/></svg>` | Target (3 círculos concéntricos) · 20px en `.icon-box` |
| 16 | `coaching-card` "Vocación de vida" | 🌱 | `<svg class="icon icon-md" viewBox="0 0 24 24"><path d="M12 21V11M12 11c-3 0-5-2-5-5 3 0 5 2 5 5zM12 11c3 0 5-1.5 5-4.5-3 0-5 1.5-5 4.5z"/></svg>` | Seedling · 20px |
| 17 | `coaching-card` "Acompañamiento personal" + columna tabla comparativa | 💛 | `<svg class="icon icon-md" viewBox="0 0 24 24"><path d="M12 21s-8-5-8-11a5 5 0 0 1 9-3 5 5 0 0 1 9 3c0 6-8 11-8 11h-2z"/></svg>` | Heart line · 16/20px |
| 18 | `ws-vivir-item` "Crear con las manos" | 🎨 | (mismo SVG Palette del #2) | 20px |
| 19 | `ws-vivir-item` "Comunidad pequeña" + subpágina taller aviso-box | 🌿 | `<svg class="icon icon-md" viewBox="0 0 24 24"><path d="M5 21c3-3 5-6 5-10s-2-7-5-8c-1 3-1 6 0 10s3 6 8 8zM10 11c2-1 4-2 6-2"/></svg>` | Leaf · 20px |
| 20 | `ws-vivir-item` "Llevar algo tuyo" + `ws-badge-open` "Inscripciones abiertas" | ✦ | (mismo SVG Sparkle del #6) | 14/20px |
| 21 | `testimonio-stars` (3 cards × 5 estrellas = 15 ocurrencias) | ★ | `<svg class="icon icon-sm icon-star-solid" viewBox="0 0 24 24"><path d="M12 3.5l2.6 5.6 6.1.6-4.6 4.2 1.3 6-5.4-3.2-5.4 3.2 1.3-6L3.3 9.7l6.1-.6L12 3.5z"/></svg>` | Star solid (única excepción con `fill:currentColor`) · 16px. Envuelto en `role="img" aria-label="5 de 5 estrellas"` |
| 22 | Form submit button original "✓ ¡Enviado!" (reemplazado por handler real) | ✓ | Ya no aparece en el botón. En subpágina workshop (fila "Incluye materiales"): `<svg class="icon icon-sm check-ico" viewBox="0 0 24 24"><path d="M5 12.5l4 4 10-10"/></svg>` color `--sage-deep` | Check · 16px en tabla pago |
| 23 | Subpágina taller success msg `.s-icon` | 🌿 | (mismo SVG Leaf del #19) dentro de `.s-icon` 72×72 con background `--sage-pale`, color `--sage-deep` | Leaf · 40px |
| 24 | Subpágina workshop success msg `.s-icon` | ✦ | (mismo SVG Sparkle del #6) dentro de `.s-icon` 72×72 con background `--lava-pale`, color `--lava-deep` | Sparkle · 40px |
| 25 | Navegación "← Volver" en ambas subpáginas | ← | `<svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M15 6l-6 6 6 6"/></svg>` | Chevron-left · 14px |
| 26 | Botones submit "→" (`.btn-submit`) en ambas subpáginas | → | `<svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>` | Arrow-right · 16px |
| 27 | `frame-close-btn` (X del overlay iframe) | — | `<svg class="icon icon-md" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></svg>` | X close · 20px |

---

## Total: 19 emojis distintos → 100% reemplazados

**Ubicaciones auditadas (en los 3 archivos):**
- `Andrea_Muniz_Completo_v2.html` (cuerpo principal): 0 emojis visibles.
- Subpágina `taller` (embebida): 0 emojis visibles.
- Subpágina `workshop` (embebida): 0 emojis visibles.

Verificado con script Python que escanea rangos Unicode de emojis (Miscellaneous Symbols, Dingbats, Supplemental Symbols, Emoticons, Transport & Map Symbols, Alchemical, etc.).
