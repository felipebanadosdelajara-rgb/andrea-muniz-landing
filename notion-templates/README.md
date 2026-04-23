# Plantillas de Notion · CRM Andrea Muñiz

Tres tablas listas para importar en Notion. Andrea usa estas como su **sistema de gestión** para ver en todo momento quién es alumna, quién tiene sesiones pendientes, quién está en lista de espera, quién debe pago, etc.

---

## 📦 Archivos

| Archivo | Base de datos resultante |
|---|---|
| `1_Alumnas_Taller.csv` | Alumnas activas del Taller de Escultura Efímera |
| `2_Clientes_Coaching.csv` | Clientes de Coaching online (sesión única o proceso) |
| `3_Inscritas_Workshop.csv` | Inscritas a Workshops Vivenciales (Pinta tu Arcano, etc.) |

---

## 🚀 Cómo importar (5 minutos)

### Paso 1 · Crear workspace y página principal
1. Si Andrea aún no tiene cuenta: https://www.notion.so/signup (Free plan, Google login)
2. Dentro del workspace, click **"+ New page"** en el menú lateral
3. Título de la página: **`Andrea Muñiz · CRM`**
4. En el cuerpo, escribir:
   - Un párrafo breve de introducción (opcional)
   - Dejar espacio para tres sub-páginas (una por cada CSV)

### Paso 2 · Importar cada CSV
1. Dentro de la página "Andrea Muñiz · CRM", click **"+ Add a subpage"** o `/` para abrir el selector de bloques
2. Elegir **"Import"** → **"CSV"** → seleccionar `1_Alumnas_Taller.csv`
3. Notion detecta columnas automáticamente y crea una base de datos. Demora 2 segundos.
4. Renombrar la base resultante a: **"Alumnas Taller"**
5. Repetir con `2_Clientes_Coaching.csv` → "Clientes Coaching"
6. Repetir con `3_Inscritas_Workshop.csv` → "Inscritas Workshop"

### Paso 3 · Ajustar tipos de columna
Notion importa todo como "Text" por defecto. Mejor convertir algunos a tipos nativos:

**Todas las tablas:**
- **WhatsApp** → tipo `Phone`
- **Correo** → tipo `Email`
- Fechas → tipo `Date`

**Específicos:**
- `1_Alumnas_Taller.csv`:
  - **Día de taller** → `Select` (opciones: Lunes, Miércoles, Viernes)
  - **Estado pago** → `Select` (Al día, Pendiente, Vencido)
  - **Origen** → `Select` (Instagram, Landing, Recomendación, Google, Otro)
- `2_Clientes_Coaching.csv`:
  - **Etapa** → `Select` (Primera sesión agendada, Primera sesión hecha, Proceso 4 sesiones, Finalizado)
  - **Estado pago** → `Select` (Pagado por adelantado, Por pagar, Primera gratis)
- `3_Inscritas_Workshop.csv`:
  - **Workshop** → `Select` (Pinta tu Arcano, Creatividad y Toma de Decisiones, Otro)
  - **Estado** → `Select` (Lista de espera, Confirmada, Pagada, Asistió, No asistió)
  - **Método pago** → `Select` (Transferencia, Flow, Efectivo)

### Paso 4 · Borrar los 2 registros ficticios
Los CSVs incluyen 2 filas de ejemplo para mostrar cómo se ven los datos. Selecciónalos y eliminarlos antes de usar de verdad.

---

## 🔗 Flujo de trabajo recomendado

```
1. Llega postulación por formulario Formspree
   ↓
2. Andrea recibe email → copia datos a Notion (tabla correspondiente)
   ↓
3. Etiqueta WhatsApp del contacto según sección
   ↓
4. Actualiza "Estado" y "Fecha" conforme avanza el caso
   ↓
5. Cuando paga → marca "Estado pago" como "Al día"
```

**Futuro (cuando volumen lo justifique):** conectar Formspree → Notion con Zapier para que las postulaciones entren automáticamente a la tabla correspondiente. Esto se hace en ~30 min cuando lleguen las primeras 5-10 postulaciones reales.

---

## 📊 Vistas recomendadas (crear después)

Notion permite crear múltiples vistas sobre la misma base de datos. Al lado del título "Alumnas Taller" hay un "+ New view". Crear estas:

**Alumnas Taller:**
- **Vista "Por día"** → agrupar por "Día de taller" (ver todas las del miércoles juntas)
- **Vista "Pagos pendientes"** → filtrar por "Estado pago = Pendiente"

**Clientes Coaching:**
- **Vista "Próximas sesiones"** → filtrar por "Próxima sesión" > hoy, ordenar ascendente
- **Vista "Por etapa"** → agrupar por "Etapa"

**Inscritas Workshop:**
- **Vista "Próximo workshop"** → filtrar por "Estado = Confirmada" y "Fecha workshop" próxima
- **Vista "Lista de espera"** → filtrar por "Estado = Lista de espera"

---

## 🔐 Privacidad

Estas tablas contienen datos personales (RUT, teléfono, correo). En Notion Free:
- Los datos viven en el workspace privado de Andrea
- Nadie más tiene acceso (a menos que ella comparta explícitamente)
- Notion usa cifrado en reposo y en tránsito
- Cumple con GDPR y estándares internacionales

Conforme a la Ley 19.628 chilena, Andrea debe:
- Usar los datos solo para la gestión de los servicios (lo que está haciendo)
- No compartir con terceros
- Eliminar datos cuando la persona lo solicite
- La política de privacidad del sitio ya cubre esto

---

## 🆘 Soporte

Si Andrea o Felipe se traba con la importación, basta con enviar screenshot del paso donde quedó y yo guío paso a paso.
