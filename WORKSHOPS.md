# Guía · Administrar workshops

Cómo agregar, editar o eliminar workshops en la landing de Andrea Muñiz.

---

## El flujo general

1. Editar `Andrea_Muniz_Completo_v2.html` (el **template**)
2. `git add`, `git commit`, `git push`
3. GitHub Actions regenera `public/index.html` y deploya a Firebase (~40 seg)
4. El cambio aparece en [andreamuniz.cl](https://andreamuniz.cl/)

> No editás `public/index.html` — se regenera automático en cada push.

---

## Dónde vive cada workshop en el código

Dentro de la sección `<!-- ══ WORKSHOP ══ -->`, hay **2 lugares** donde puede vivir un workshop:

| Ubicación | Visibilidad | Para qué |
|---|---|---|
| Directo dentro de `<div class="ws-calendar reveal">` | **Visible siempre** por default | Workshops con fecha confirmada |
| Dentro de `<details class="detail-toggle lava">...</details>` | **Colapsado** bajo "Ver próximas fechas" | Workshops sin fecha confirmada ("próximamente") |

Cuando se confirma la fecha de un workshop "próximamente", se saca del `<details>` y pasa a ser visible.

---

## Tareas comunes · copy-paste ready

### 1. Editar un workshop existente

Busca en el HTML el `<article class="ws-card ...">` del workshop que quieres editar. Los campos principales:

```html
<!-- Badge (arriba a la derecha): "Agotado" / "Cupos disponibles" / "Próximamente" -->
<span class="ws-badge" style="background:var(--coral-pale);color:var(--coral);border-color:var(--coral)">
  Agotado
</span>
<span class="ws-cupos" style="color:var(--coral)">Sin cupos disponibles</span>

<!-- Bloque de fecha -->
<div class="ws-month">JUN</div>
<div class="ws-day">14</div>
<div class="ws-year">2026</div>

<!-- Título y subtítulo -->
<h3>Pinta tu Arcano</h3>
<p class="ws-subtitle">Workshop vivencial de arte + coaching · Primera edición</p>

<!-- Los 4 datos con ícono (lugar, horario, cupo, precio) -->
<div class="ws-meta">
  <span class="ws-meta-item">... ubicación</span>
  <span class="ws-meta-item">... horario (21:00 – 23:00 hrs)</span>
  <span class="ws-meta-item">... cupo (Máximo 10 personas)</span>
  <span class="ws-meta-item">... precio ($35.000 – $45.000 por persona)</span>
</div>

<!-- Descripción narrativa -->
<p class="ws-desc">Un sábado por la noche, una actividad con tu pareja...</p>
```

Cambia solo el **texto entre los tags**, no las clases ni los `<svg>`.

### 2. Marcar un workshop como AGOTADO

Reemplaza el bloque del badge:

```html
<!-- ANTES (cupos disponibles): -->
<span class="ws-badge ws-badge-open">Cupos abiertos</span>
<span class="ws-cupos">5 cupos disponibles</span>

<!-- DESPUÉS (agotado): -->
<span class="ws-badge" style="background:var(--coral-pale);color:var(--coral);border-color:var(--coral)">
  <svg class="icon icon-xs" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 3h10M7 21h10M7 3v3a5 5 0 0 0 10 0V3M7 21v-3a5 5 0 0 1 10 0v3"/></svg>
  Agotado
</span>
<span class="ws-cupos" style="color:var(--coral)">Sin cupos disponibles</span>
```

### 3. Marcar como "cupos disponibles"

```html
<span class="ws-badge ws-badge-open">
  <svg class="icon icon-xs" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 3h10M7 21h10M7 3v3a5 5 0 0 0 10 0V3M7 21v-3a5 5 0 0 1 10 0v3"/></svg>
  Cupos abiertos
</span>
<span class="ws-cupos">5 cupos disponibles</span>
```

### 4. Agregar un workshop nuevo CON fecha confirmada

Copia esta plantilla dentro de `<div class="ws-calendar reveal">`, **antes** de `<!-- Workshops sin fecha confirmada -->`:

```html
<article class="ws-card ws-card-featured">
  <div class="ws-card-header">
    <span class="ws-badge ws-badge-open">
      <svg class="icon icon-xs" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 3h10M7 21h10M7 3v3a5 5 0 0 0 10 0V3M7 21v-3a5 5 0 0 1 10 0v3"/></svg>
      Cupos abiertos
    </span>
    <span class="ws-cupos">6 cupos disponibles</span>
  </div>
  <div class="ws-card-body">
    <div class="ws-date-block" aria-hidden="true">
      <div class="ws-month">SEP</div>
      <div class="ws-day">20</div>
      <div class="ws-year">2026</div>
    </div>
    <div class="ws-info">
      <h3>Nombre del Workshop</h3>
      <p class="ws-subtitle">Workshop vivencial de arte + coaching · N° edición</p>
      <div class="ws-meta">
        <span class="ws-meta-item"><svg class="icon icon-sm" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-7.5-7-12a7 7 0 1 1 14 0c0 4.5-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/></svg> Casa Taller · Pedro de Valdivia Norte, Santiago</span>
        <span class="ws-meta-item"><svg class="icon icon-sm" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg> 10:00 – 14:00 hrs</span>
        <span class="ws-meta-item"><svg class="icon icon-sm" viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 19a6 6 0 0 1 12 0M15 19a5 5 0 0 1 6.5-4.8"/></svg> Máximo 8 personas</span>
        <span class="ws-meta-item"><svg class="icon icon-sm" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="6" width="18" height="13" rx="2"/><circle cx="12" cy="12.5" r="3"/></svg> $35.000 – $45.000 por persona · incluye materiales</span>
      </div>
      <p class="ws-desc">Descripción narrativa del workshop en 2-3 líneas. Qué se va a hacer, para quién, qué ofrece.</p>
      <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:16px">
        <a href="#" onclick="showFrame('workshop');return false;" class="btn btn-ghost">Anotarme →</a>
        <a href="https://wa.me/56900000000?text=Hola%20Andrea%2C%20me%20interesa%20el%20workshop%20NOMBRE_URL_ENCODED.%20Te%20escribo%20desde%20andreamuniz.cl" class="btn btn-ghost" target="_blank" rel="noopener">
          <svg class="icon icon-sm" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 15a3 3 0 0 1-3 3H9l-5 4V6a3 3 0 0 1 3-3h10a3 3 0 0 1 3 3v9z"/></svg>
          WhatsApp
        </a>
      </div>
    </div>
  </div>
</article>
```

**IMPORTANTE sobre el WhatsApp**:
- El número `56900000000` es un placeholder. GitHub Actions lo reemplaza con el real de Andrea. **No tocarlo**.
- `NOMBRE_URL_ENCODED` hay que reemplazarlo con el nombre del workshop escapado. Ejemplo:
  - `Creatividad y Decisiones` → `Creatividad%20y%20Decisiones`
  - `Arte para Sanar` → `Arte%20para%20Sanar`
  - (Los espacios son `%20`. Acentos y ñ se escapan también: `ñ` → `%C3%B1`, `á` → `%C3%A1`)
  - Si tienes dudas, usa [urlencoder.org](https://www.urlencoder.org/) — pegas el texto y te da el escape.

### 5. Agregar un workshop SIN fecha confirmada (próximamente)

Mismo HTML que el caso 4, pero:

1. Cambiar `class="ws-card ws-card-featured"` por `class="ws-card ws-card-soon"`
2. Reemplazar el badge por:
   ```html
   <span class="ws-badge ws-badge-soon">
     <svg class="icon icon-xs" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 3h10M7 21h10M7 3v3a5 5 0 0 0 10 0V3M7 21v-3a5 5 0 0 1 10 0v3"/></svg>
     Próximamente
   </span>
   <span class="ws-cupos">Fecha por confirmar</span>
   ```
3. Reemplazar `<div class="ws-date-block"` por `<div class="ws-date-block ws-date-muted"` (queda visualmente atenuado)
4. En el bloque de fecha poner el mes estimado + `—` en el día:
   ```html
   <div class="ws-month">AGO</div>
   <div class="ws-day">—</div>
   <div class="ws-year">2026</div>
   ```
5. **Pégalo dentro** del `<details class="detail-toggle lava">...</details>` (bajo "Ver próximas fechas")

### 6. Mover un workshop de "próximamente" a visible (confirmar fecha)

Cuando Andrea confirma la fecha de un workshop que estaba colapsado:

1. Corta todo el `<article class="ws-card ws-card-soon">...</article>` de dentro del `<details>`
2. Pégalo **antes** del `<details>` (dentro de `<div class="ws-calendar reveal">`)
3. Cambiar `ws-card-soon` por `ws-card-featured`
4. Cambiar el badge `ws-badge-soon` / "Próximamente" por `ws-badge-open` / "Cupos abiertos" (o agotado, según corresponda)
5. Sacar `ws-date-muted` de la `ws-date-block`
6. Actualizar `<div class="ws-day">—</div>` con el día real: `<div class="ws-day">20</div>`
7. Ajustar `<span class="ws-cupos">Fecha por confirmar</span>` → `<span class="ws-cupos">6 cupos disponibles</span>` (o el número real)

### 7. Eliminar un workshop pasado

Borra todo el bloque `<article class="ws-card ...">...</article>` (incluyendo los tags). Si era el único workshop visible y solo quedaban "próximamente", la sección sigue funcionando bien — pero revisá que el `<details>` siga teniendo contenido adentro.

---

## Antes de pushear · checklist

- [ ] Los tags HTML están balanceados (cada `<article>` cerrado, cada `<div>` cerrado)
- [ ] El WhatsApp link tiene el texto URL-encoded correcto (sin espacios ni acentos literales)
- [ ] La fecha (mes/día/año) está escrita con el formato correcto (`JUN` mayúsculas, 3 letras)
- [ ] Si agregaste un workshop nuevo: lo pusiste en el lugar correcto (visible vs colapsado)
- [ ] Probaste abrir el HTML local en el navegador para ver que no se rompió nada visualmente:
  ```bash
  python update-placeholders.py   # regenera public/index.html con valores reales
  python -m http.server 8000 -d public
  # abrir http://localhost:8000/
  ```

## Después del push

1. Esperar ~40 segundos que GitHub Actions deploye (mirar en [Actions](https://github.com/felipebanadosdelajara-rgb/andrea-muniz-landing/actions))
2. Abrir [andreamuniz.cl](https://andreamuniz.cl/) **con Ctrl+Shift+R** (hard refresh, ignora caché) y verificar que el cambio aparece

---

## Troubleshooting

**El deploy falla con "Quedó Formspree sin resolver" o "Quedó WhatsApp placeholder":**
Introdujiste literalmente `XXXXXXXX` o `56900000000` en un lugar nuevo. Esos placeholders solo deben aparecer en los lugares que el script ya sabe reemplazar (los `wa.me/...` existentes). Revisá el diff y saca el placeholder.

**El workshop no aparece en el sitio pero el deploy dijo "Success":**
1. Hard refresh (Ctrl+Shift+R) en el browser
2. Verificar que editaste `Andrea_Muniz_Completo_v2.html` (el template), no `public/index.html`
3. Si editaste ambos, al próximo deploy el template sobrescribe al public

**El workshop aparece pero roto visualmente:**
Probablemente falta cerrar un `<div>` o `<article>`. Abre el HTML en un editor con indentación automática y mira si los tags te balancean.

**El link de WhatsApp no funciona o falta el número:**
El número real (`56985028131`) se inyecta solo al deployar via GitHub Secrets. Si lo ves roto en tu preview local es porque no corriste `python update-placeholders.py` antes.

---

## Si necesitás hacer algo que no está acá

Pégame el cambio que quieres hacer y te digo si es manejable con esta guía o si vale el salto a Opción 2 (JSON + build script) o Opción 3 (CMS).
