# Guía de despliegue

## Opción 1 — GitHub Pages (la más fácil, gratis)

**El repo ya está preparado para esto.** Solo tienes que:

1. Subir el repo a GitHub (ya hecho si estás leyendo esto)
2. En tu repo → **Settings** → **Pages**
3. En "Source":
   - Branch: `main`
   - Folder: `/ (root)`
4. Click **Save**
5. Espera 1–2 minutos
6. La URL pública aparece en la misma página de Pages, tipo:
   ```
   https://tu-usuario.github.io/nombre-del-repo/
   ```

Esa URL ya es pública. Pasa el link a tu prima, ábrelo en cualquier móvil — funciona.

### Cambios automáticos
Cada vez que hagas push al branch `main`, GitHub Pages regenera la web automáticamente en 1–2 minutos. No tienes que hacer nada más.

### Dominio propio (shevanbarcelona.es)
Cuando tu prima tenga el dominio:
1. En **Settings → Pages**, en "Custom domain" escribe `shevanbarcelona.es`
2. Configura los DNS del dominio apuntando a GitHub Pages:
   - Tipo `A` apuntando a las 4 IPs de GitHub:
     - `185.199.108.153`
     - `185.199.109.153`
     - `185.199.110.153`
     - `185.199.111.153`
   - O un `CNAME` `www` apuntando a `tu-usuario.github.io`
3. Activar HTTPS (checkbox en la misma página) — gratis, certificado de Let's Encrypt

---

## Opción 2 — Netlify

Si prefieres Netlify (a veces más rápido y con mejores herramientas):

1. Cuenta gratis en [netlify.com](https://netlify.com)
2. "Add new site" → "Import from Git" → conecta tu repo de GitHub
3. Build settings:
   - Build command: `python build.py`
   - Publish directory: `.` (raíz)
4. Deploy → URL inmediata tipo `https://amazing-tesla-1234.netlify.app`

Para dominio propio: igual que en GitHub Pages, "Domain settings" → Add custom domain.

**Para URLs sin `.html`** (ej: `/accesorios/techo-elevable` en vez de `/accesorios/techo-elevable.html`), crea un archivo `_redirects` en la raíz del repo con:
```
/*.html       /:splat       200
```

---

## Opción 3 — Vercel

Casi idéntico a Netlify:

1. Cuenta gratis en [vercel.com](https://vercel.com)
2. "New Project" → conecta el repo
3. Framework preset: "Other"
4. Build command: `python build.py`
5. Output directory: `.`
6. Deploy

---

## Opción 4 — Hosting tradicional (IONOS, Hostinger, Banahosting…)

1. Local: `python build.py`
2. Conecta por FTP
3. Sube **todos los archivos de la raíz del repo** (excepto `src/`, `assets/`, `build.py`, `README.md` — esos no hacen falta en producción) a `public_html/` o `www/`

Para URLs sin `.html`, crea un `.htaccess` en `public_html/`:
```apache
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME}.html -f
RewriteRule ^(.+)$ $1.html [L]
```

---

## Después de desplegar — checklist

### Activar el formulario de contacto
1. Entra en la web desplegada → `/contacto.html`
2. Manda un envío de prueba con datos reales
3. Llega un email a `info@shevanbarcelona.es` de FormSubmit pidiendo activar
4. Click en el enlace de activación
5. A partir de ahora, los envíos del formulario llegan al email automáticamente

### SEO básico
1. **Google Search Console** ([search.google.com/search-console](https://search.google.com/search-console))
   - Añade el dominio
   - Verifica la propiedad
   - Envía el sitemap.xml *(generar con [xml-sitemaps.com](https://www.xml-sitemaps.com))*

2. **Google Business Profile** ([business.google.com](https://business.google.com))
   - Crear ficha para SheVan
   - Categoría: "Taller de reparaciones de vehículos" + "Camperizadora"
   - Subir fotos del taller, proyectos, equipo
   - Verificar la dirección física

3. **robots.txt** — crear en la raíz:
   ```
   User-agent: *
   Allow: /

   Sitemap: https://shevanbarcelona.es/sitemap.xml
   ```

### Contenido pendiente
- Sustituir los placeholders de imágenes por fotos reales con `alt` descriptivo
- Crear las páginas legales (Aviso legal, Política de privacidad, Cookies — obligatorio en España por RGPD)

---

## Regenerar el sitio

Si actualizas algo en `src/data.py` (textos) o `src/shared.py` (estilos / contacto):

```bash
python build.py
```

Tarda menos de un segundo. Después haces commit + push y GitHub Pages republica solo.
