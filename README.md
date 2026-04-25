# SheVan — Web

Sitio web multipágina para **SheVan**, camperizadora artesanal en Sabadell, Barcelona.

25 páginas, optimizado para SEO local, listo para servir desde GitHub Pages, Netlify, Vercel o cualquier hosting estático.

---

## 🚀 Cómo verlo online (GitHub Pages — gratis, en 2 minutos)

Una vez subido este repo a tu cuenta de GitHub:

1. Ve a tu repo → pestaña **Settings**
2. En el menú lateral → **Pages**
3. En "Source" → selecciona:
   - Branch: `main`
   - Folder: `/ (root)`
4. Click **Save**
5. Espera 1–2 minutos
6. La URL aparecerá en la misma página, algo como:
   ```
   https://TU-USUARIO.github.io/NOMBRE-DEL-REPO/
   ```
7. **Esa URL es la que pasas a tu prima.** Funciona en móvil, tablet y desktop.

> 💡 Si la URL devuelve 404 los primeros minutos, espera un poco — GitHub Pages tarda algo de tiempo la primera vez.

---

## 📁 Estructura del repo

```
shevan-web/
├── index.html                  ← HOME (raíz del sitio)
├── styles.css
├── logo-yellow.png
├── logo-black.png
├── camperizaciones.html
├── camperizaciones/
│   ├── gran-volumen.html
│   ├── medianas-pequenas.html
│   └── homologaciones.html
├── accesorios.html
├── accesorios/
│   ├── segunda-bateria.html
│   ├── paneles-solares.html
│   ├── inversor.html
│   ├── calefaccion.html
│   ├── aire-acondicionado.html
│   ├── aislamiento.html
│   ├── ventanas-claraboyas.html
│   ├── techo-elevable.html
│   ├── cierres-seguridad.html
│   ├── toldo-portabicis.html
│   └── suspension-neumatica.html
├── taller.html
├── taller/
│   ├── electrica.html
│   ├── agua.html
│   ├── filtraciones.html
│   ├── gas.html
│   └── mobiliario.html
├── proyectos.html
├── contacto.html
│
├── .nojekyll                   ← le dice a GitHub Pages: sirve los archivos tal cual
├── README.md
├── DEPLOY.md                   ← guía de otras opciones de despliegue
├── .gitignore
├── build.py                    ← script para regenerar el sitio
│
├── src/                        ← código Python del generador
│   ├── shared.py               ← CSS + datos de contacto
│   ├── data.py                 ← contenido editable (servicios, textos)
│   ├── templates.py            ← head, nav, footer, iconos
│   ├── builder.py              ← lógica de renderizado
│   └── inliner.py              ← inliner opcional para previews offline
│
└── assets/                     ← logos fuente (PNG)
    ├── logo-yellow.png
    └── logo-black.png
```

GitHub Pages servirá automáticamente todos los HTML de la raíz. Las carpetas `src/` y `assets/` son código del generador — no afectan al sitio público.

---

## ✏️ Editar el contenido

**Los textos están en `src/data.py`** — un archivo Python con diccionarios. Por ejemplo:

```python
{
    "slug": "techo-elevable",
    "title": "Techo Elevable",
    "lead": "¿Sientes que a tu aventura le falta espacio?",
    # ...edita aquí
}
```

**Datos de contacto** (teléfono, email, dirección): `src/shared.py` → `CONTACT`.

**CSS / colores**: `src/shared.py` → variable `CSS`. Los tokens del principio (`--yellow`, `--ink`, etc.) son los colores base.

Después de editar, regenera el sitio:

```bash
python build.py
```

Luego haz commit y push de los HTML actualizados — GitHub Pages republica solo.

---

## 🔧 Otras formas de desplegarlo

Si prefieres un dominio propio o más control, mira [DEPLOY.md](./DEPLOY.md) para Netlify, Vercel y hosting tradicional.

---

## 🔍 SEO

Cada página tiene `<title>` y `<meta description>` únicos optimizados por keyword, schema.org JSON-LD, Open Graph, geo tags y canonical URLs.

**Pendiente para SEO completo** (no es código, es configuración externa):
- Google Business Profile (es el 50% del SEO local)
- Google Search Console + sitemap.xml
- Reseñas en Google de clientes
- Sustituir las imágenes placeholder por fotos reales

---

## 📬 Formulario de contacto

El formulario en `/contacto.html` envía a `info@shevanbarcelona.es` mediante **FormSubmit** (gratuito, sin registro).

**Activación inicial — solo la primera vez:**
1. Manda un envío de prueba desde la web ya desplegada
2. Llega un email a `info@shevanbarcelona.es` pidiendo confirmación
3. Click en el enlace de confirmación
4. A partir de ahí, todos los envíos llegan al email automáticamente

---

## 🛠️ Stack técnico

- **Lenguaje del generador**: Python 3.8+ (solo stdlib, sin dependencias)
- **Output**: HTML5 + CSS3 + JS mínimo, todo estático
- **Tipografías**: Bricolage Grotesque + Inter (Google Fonts)

No hace falta Node, npm, frameworks ni nada externo.
