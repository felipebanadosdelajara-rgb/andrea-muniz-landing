# Guía de despliegue · Andrea_Muniz_Completo_v2.html

Esta guía te lleva de un archivo HTML a `https://yoteescucho.com` con formularios que funcionan, SSL gratuito, dominio propio y analítica respetuosa con la privacidad. Tiempo estimado: 45 min – 1 h.

---

## 1 · Hosting (elegir UNO)

| Host | Costo | Pros | Contras | Recomendación |
|------|-------|------|---------|---------------|
| **Cloudflare Pages** | Gratis ilimitado | CDN global, SSL auto, analytics incluido, fácil conectar dominio Cloudflare | No tiene "Forms" nativo (hay que usar Formspree/Web3Forms) | ⭐ **Recomendado si Andrea ya tiene dominio o está dispuesta a mover DNS a Cloudflare** |
| **Netlify** | Gratis 100 GB/mes | Forms nativos (100 envíos gratis/mes), buena DX | Tier gratis genera subdominio `.netlify.app` si no se conecta dominio | Alternativa si prefieres forms incluidos |
| **Vercel** | Gratis hobby | Rápido, excelente DX | No tiene forms nativos, más orientado a apps | No es lo más directo para este caso |

### Pasos rápidos — Cloudflare Pages
1. Crear cuenta en https://dash.cloudflare.com (gratis).
2. **Workers & Pages → Create → Pages → Upload assets**.
3. Subir el archivo `Andrea_Muniz_Completo_v2.html` renombrado a **`index.html`**.
4. Deploy → obtienes URL tipo `andrea-muniz.pages.dev`.
5. **Custom domain → Add → `yoteescucho.com`** (sigue las instrucciones DNS).
6. SSL se activa automáticamente en ~2 min.

### Pasos rápidos — Netlify
1. https://app.netlify.com → **Sites → Add new → Deploy manually**.
2. Arrastrar la carpeta con `index.html` al dropzone.
3. **Site settings → Domain management → Add custom domain**.
4. Para **forms nativos**, añadir al `<form>`: `netlify` y `name="postulacion"`. Requiere editar el HTML o duplicarlo.

---

## 2 · Configurar los formularios reales

Hay **2 formularios** para conectar: postulación al taller y inscripción al workshop. Recomiendo **Formspree** por simplicidad, precio y features.

### Opción A · Formspree (recomendada)
1. Cuenta gratis en https://formspree.io. Plan gratis = 50 envíos/mes. Plan Gold (USD 10/mes) = ilimitado + dashboard + export CSV.
2. **New Form → Nombre: "Postulación Taller"**. Copia el endpoint tipo `https://formspree.io/f/mvgpxxxx`.
3. Editar `Andrea_Muniz_Completo_v2.html` — buscar los dos `action="https://formspree.io/f/XXXXXXXX"` (uno en la subpágina taller, otro en workshop) y reemplazar `XXXXXXXX` con el ID real de cada formulario.
   - Los forms están **embebidos en Base64** dentro del objeto `_frames`. Para editarlos:
     - **Opción simple**: editar los archivos `_tmp/frame_taller_v2.html` y `_tmp/frame_workshop_v2.html`, luego re-encodear y sustituir en el main (te puedo entregar un script `update-frames.sh` si lo necesitas).
     - **Opción rápida**: pedirme que te regenere el main con los endpoints reales ya inyectados.
4. **Activar verificación de email**: Formspree te envía un correo al email registrado, con "confirm your email address". Necesario para recibir envíos.
5. **Spam protection**: en Formspree → Settings → Protection → activar **Akismet** (gratis).
6. **Destino del correo**: Settings → Integrations → Email → añadir el correo de Andrea (o varios — ella y Felipe).

### Opción B · Netlify Forms (si hosteas en Netlify)
1. Al `<form>` añadir: `netlify` y `data-netlify-honeypot="_honeypot"`.
2. Añadir un `<input type="hidden" name="form-name" value="postulacion">`.
3. El honeypot ya existe (`name="_honeypot"`); sólo cambiar el nombre del atributo en Netlify.
4. Notificaciones en Netlify UI → Forms → Notifications → Email.

### Opción C · Web3Forms (sin cuenta, totalmente gratis)
1. https://web3forms.com → Get Access Key (sólo email).
2. Reemplazar `action` por `https://api.web3forms.com/submit` y agregar `<input type="hidden" name="access_key" value="TU_KEY">`.

---

## 3 · Dominio + SSL

**Si Andrea ya tiene `yoteescucho.com`:**
1. Ir al registrador (NIC.cl, GoDaddy, Namecheap, etc.).
2. Cambiar nameservers a los de Cloudflare (te los dan al añadir el sitio en CF).
3. En Cloudflare → SSL/TLS → **Full (strict)**.
4. Propagación: 30 min – 24 h. Verificar con https://dnschecker.org.

**Si hay que comprar dominio:**
- **NIC.cl** (`.cl`): ~CLP 10.000/año, ideal para marca chilena.
- **Namecheap/Cloudflare Registrar**: ~USD 10/año para `.com`.

**Email profesional `hola@yoteescucho.com`:**
- Opción barata: forwarder gratis de Cloudflare Email Routing (redirige `hola@yoteescucho.com` a su Gmail).
- Opción pro: Google Workspace (~USD 6/mes por usuario).

---

## 4 · Analytics ligero y respetuoso

**No usar Google Analytics.** Es pesado, invasivo y ya no entrega datos útiles sin consentimiento GDPR/Ley 19.628.

| Servicio | Precio | Pros |
|----------|--------|------|
| **Plausible** | USD 9/mes (10k visitas) | Open source, no cookies, GDPR-ready, dashboard hermoso | ⭐ Recomendado |
| **Simple Analytics** | USD 9/mes | Más simple, sin cookies, UI minimalista | Alternativa |
| **Cloudflare Web Analytics** | Gratis | Gratis, no cookies, integrado a CF Pages | ⭐ Si ya usas Cloudflare, empieza acá |
| **Umami** (self-host) | Gratis | Open source, gratis si lo hosteas tú | Requiere VPS |

### Instalar Plausible (ejemplo)
Agregar antes de `</head>` en `index.html`:
```html
<script defer data-domain="yoteescucho.com" src="https://plausible.io/js/script.js"></script>
```

### Cloudflare Web Analytics
- CF → **Analytics & Logs → Web Analytics → Add a site → Paste tag**. Si el sitio está en CF Pages, se activa con un checkbox (sin código).

---

## 5 · Headers de seguridad (Cloudflare Pages)

Crear un archivo `_headers` junto al `index.html`:
```
/*
  Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' https://plausible.io; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https:; connect-src 'self' https://formspree.io https://plausible.io; frame-src blob:;
```

**Notas CSP**:
- `'unsafe-inline'` en `script-src` es necesario porque el handler de forms está inline. Si quieres pasar a script externo en un v3, se puede endurecer.
- `frame-src blob:` es crítico para que funcione el overlay de subpáginas (usan `Blob` URLs).
- Si cambias de Formspree a otro servicio, ajustar `connect-src`.

---

## 6 · Recursos faltantes que debes subir

Sube estos archivos junto al `index.html`:

1. **`og-cover.jpg`** — 1200×630px, representa la marca. Lo usa el preview de WhatsApp/Instagram/Twitter. Sugerencia: foto de Andrea en el taller + título "El arte sana. El coaching transforma." en Playfair.
2. **`favicon.ico` (opcional)** — el sitio ya tiene favicon SVG inline, pero algunos navegadores antiguos piden `.ico`. Convertir con https://realfavicongenerator.net.
3. **`robots.txt`** — texto simple:
   ```
   User-agent: *
   Allow: /
   Sitemap: https://yoteescucho.com/sitemap.xml
   ```
4. **`sitemap.xml`** — mínimo:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
     <url><loc>https://yoteescucho.com/</loc><lastmod>2026-04-20</lastmod></url>
   </urlset>
   ```

---

## 7 · Checklist pre-lanzamiento

- [ ] Endpoints Formspree reales inyectados en los dos `action`
- [ ] Número WhatsApp real en el footer (`wa.me/56900000000` → número de Andrea)
- [ ] `og-cover.jpg` subido
- [ ] Dominio apuntando al host
- [ ] SSL activo (candado verde en Chrome)
- [ ] Probar envío de postulación con email real → llega a inbox de Andrea
- [ ] Probar envío de inscripción con email real → llega a inbox de Andrea
- [ ] Probar apertura y cierre del modal (botón, ESC, "Volver")
- [ ] Probar en Chrome, Safari, Firefox (desktop + iPhone + Android)
- [ ] Probar narrador (VoiceOver en Mac, NVDA en Windows) — al menos hero, nav y primer form
- [ ] Enviar a https://validator.w3.org/ → 0 errores
- [ ] Enviar a https://pagespeed.web.dev → objetivo LCP < 2.5s en móvil (si el peso de imágenes Base64 tira el score abajo, separar a archivos reales)
- [ ] Primer envío de prueba confirmado → desactivar modo test de Formspree si aplica

---

## 8 · Post-lanzamiento (primera semana)

- Revisar dashboard Formspree / Cloudflare Analytics diariamente.
- Si aparece spam: activar Akismet en Formspree o añadir Cloudflare Turnstile.
- Compartir URL en Instagram de Andrea, en su bio, por WhatsApp status.
- Monitorear: tasa de apertura del modal vs envío real (si muchas abren y pocas envían → el form es muy largo, iterar).
