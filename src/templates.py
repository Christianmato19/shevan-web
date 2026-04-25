# -*- coding: utf-8 -*-
"""
SheVan multipage — Part 3: Template renderers.
Functions take depth (0 or 1) and return HTML chunks with correct
relative paths to assets, nav links and form actions.
"""
import urllib.parse


# Imported into final builder; shape:  prefix(0) -> "" ; prefix(1) -> "../"
def prefix(depth):
    return "../" * depth


# ============================================================
# ICONS — inline SVGs used in cards / forms
# ============================================================
ICONS = {
    "van-large": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M2 8h13l4 4v6H2z"/><circle cx="6" cy="19" r="1.5"/><circle cx="17" cy="19" r="1.5"/><path d="M2 13h17"/></svg>',
    "van-small": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="10" width="13" height="7" rx="1"/><path d="M16 12h3l2 2v3h-5"/><circle cx="6" cy="19" r="1.4"/><circle cx="17" cy="19" r="1.4"/></svg>',
    "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" y1="14" x2="15" y2="14"/><line x1="9" y1="17" x2="13" y2="17"/></svg>',
    "battery": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="18" height="10" rx="2"/><path d="M22 11v2"/><path d="M6 10v4"/><path d="M10 10v4"/></svg>',
    "sun": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>',
    "plug": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M9 2v6M15 2v6M6 8h12v3a6 6 0 0 1-12 0V8zM12 17v5"/></svg>',
    "fire": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>',
    "snowflake": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="2" x2="12" y2="22"/><line x1="4" y1="6" x2="20" y2="18"/><line x1="20" y1="6" x2="4" y2="18"/><polyline points="9 5 12 2 15 5"/><polyline points="15 19 12 22 9 19"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L4 6v6c0 5 3.5 9.5 8 10 4.5-.5 8-5 8-10V6l-8-4z"/></svg>',
    "window": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 12h18M12 3v18"/></svg>',
    "expand": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9V5a2 2 0 0 1 2-2h4M21 9V5a2 2 0 0 0-2-2h-4M3 15v4a2 2 0 0 0 2 2h4M21 15v4a2 2 0 0 1-2 2h-4"/></svg>',
    "lock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>',
    "umbrella": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12a10 10 0 1 0-20 0"/><path d="M12 12v6a2 2 0 1 1-4 0"/><path d="M2 12h20"/></svg>',
    "wave": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12c2 0 2-2 4-2s2 2 4 2 2-2 4-2 2 2 4 2 2-2 4-2"/><path d="M2 18c2 0 2-2 4-2s2 2 4 2 2-2 4-2 2 2 4 2 2-2 4-2"/></svg>',
    "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h7l-1 8 10-12h-7l1-8z"/></svg>',
    "drop": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.5s6 6.5 6 11.5a6 6 0 0 1-12 0c0-5 6-11.5 6-11.5z"/></svg>',
    "drop-shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L4 6v6c0 5 3.5 9.5 8 10 4.5-.5 8-5 8-10V6l-8-4z"/><path d="M12 8.5s2 2.5 2 4.5a2 2 0 0 1-4 0c0-2 2-4.5 2-4.5z"/></svg>',
    "flame": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2c0 4-3 6-3 9a3 3 0 0 0 6 0c0-1.5-1-2.5-1-2.5s2 1 2 4a6 6 0 0 1-12 0c0-3 3-5 3-8 0-1 1-2 1-2"/></svg>',
    "tools": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>',
    "wrench": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>',
    "package": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M16.5 9.4 7.55 4.24M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.6 6.3A7.85 7.85 0 0 0 12 4a7.94 7.94 0 0 0-6.78 12.06L4 21l5.05-1.32a7.92 7.92 0 0 0 11.94-6.85 7.87 7.87 0 0 0-3.39-6.53zM12 19.5a6.6 6.6 0 0 1-3.36-.92l-.24-.14-2.49.65.66-2.43-.16-.25a6.59 6.59 0 1 1 5.59 3.09zm3.62-4.93c-.2-.1-1.17-.58-1.35-.65s-.31-.1-.45.1-.51.65-.62.78-.23.15-.43.05a5.42 5.42 0 0 1-1.59-1 6 6 0 0 1-1.1-1.37c-.11-.2 0-.31.09-.4s.2-.23.3-.35a1.36 1.36 0 0 0 .2-.33.36.36 0 0 0 0-.35c0-.1-.45-1.08-.62-1.48s-.33-.34-.45-.34-.25 0-.38 0a.74.74 0 0 0-.53.25 2.2 2.2 0 0 0-.69 1.65 3.83 3.83 0 0 0 .8 2.05A8.81 8.81 0 0 0 12.4 16.6c1.85.79 1.85.53 2.18.49a2 2 0 0 0 1.34-.93 1.65 1.65 0 0 0 .12-.93c-.05-.07-.18-.13-.42-.23z"/></svg>',
}


def render_head(title, description, depth, og_image=None, schema_jsonld=None, canonical_path=""):
    """Render the <head> section with proper SEO tags."""
    p = prefix(depth)
    canonical = f"https://shevanbarcelona.es/{canonical_path}" if canonical_path is not None else ""
    schema_block = ""
    if schema_jsonld:
        schema_block = f'\n  <script type="application/ld+json">{schema_jsonld}</script>'
    og_img = og_image or f"{p}logo-yellow.png"
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{canonical}">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{og_img}">
  <meta property="og:locale" content="es_ES">
  <meta property="og:site_name" content="SheVan">

  <!-- Twitter card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">

  <!-- Geo -->
  <meta name="geo.region" content="ES-CT">
  <meta name="geo.placename" content="Sabadell">
  <meta name="geo.position" content="41.5479;2.1075">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,200..800&family=Inter:wght@300..900&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="{p}styles.css">
  <link rel="icon" type="image/png" href="{p}logo-yellow.png">{schema_block}
</head>
<body>'''


def render_nav(active_key, depth):
    """Render the top nav. active_key in {'home','camperizaciones','accesorios','taller','proyectos','contacto'}."""
    p = prefix(depth)
    classes = lambda k: ' class="active"' if k == active_key else ""
    return f'''
<nav class="site" id="siteNav">
  <a href="{p}index.html" class="nav-logo" aria-label="SheVan inicio">
    <img src="{p}logo-black.png" alt="SheVan logo">
  </a>
  <ul class="nav-links">
    <li{classes('camperizaciones')}>
      <a href="{p}camperizaciones.html">Camperizaciones</a>
      <ul class="submenu">
        <li><a href="{p}camperizaciones/gran-volumen.html">Gran Volumen</a></li>
        <li><a href="{p}camperizaciones/medianas-pequenas.html">Medianas y Pequeñas</a></li>
        <li><a href="{p}camperizaciones/homologaciones.html">Homologaciones</a></li>
      </ul>
    </li>
    <li{classes('accesorios')}><a href="{p}accesorios.html">Accesorios</a></li>
    <li{classes('taller')}><a href="{p}taller.html">Taller</a></li>
    <li{classes('proyectos')}><a href="{p}proyectos.html">Proyectos</a></li>
    <li{classes('contacto')}><a href="{p}contacto.html">Contacto</a></li>
    <li><a href="{p}contacto.html#presupuesto" class="nav-cta">Pide presupuesto</a></li>
  </ul>
  <button class="menu-btn" onclick="toggleMobileMenu()" aria-label="Menú">
    <span></span><span></span><span></span>
  </button>
</nav>
<div class="mobile-menu" id="mobileMenu">
  <a href="{p}camperizaciones.html"><strong>Camperizaciones</strong></a>
  <div class="submenu-mobile">
    <a href="{p}camperizaciones/gran-volumen.html">Gran Volumen</a>
    <a href="{p}camperizaciones/medianas-pequenas.html">Medianas y Pequeñas</a>
    <a href="{p}camperizaciones/homologaciones.html">Homologaciones</a>
  </div>
  <a href="{p}accesorios.html"><strong>Accesorios</strong></a>
  <a href="{p}taller.html"><strong>Taller</strong></a>
  <a href="{p}proyectos.html"><strong>Proyectos</strong></a>
  <a href="{p}contacto.html"><strong>Contacto</strong></a>
</div>
'''


def render_footer(depth, contact):
    p = prefix(depth)
    return f'''
<footer class="site">
  <div class="footer-grid">
    <div class="footer-brand">
      <img src="{p}logo-yellow.png" alt="SheVan">
      <p>Camperizaciones a medida en Sabadell. También accesorios y taller de reparaciones para campers y autocaravanas. Diseñamos y construimos pensando en cómo viajas — no en un catálogo.</p>
    </div>
    <div class="footer-col">
      <h5>Servicios</h5>
      <ul>
        <li><a href="{p}camperizaciones/gran-volumen.html">Gran Volumen</a></li>
        <li><a href="{p}camperizaciones/medianas-pequenas.html">Medianas y Pequeñas</a></li>
        <li><a href="{p}accesorios.html">Accesorios</a></li>
        <li><a href="{p}taller.html">Taller</a></li>
        <li><a href="{p}camperizaciones/homologaciones.html">Homologaciones</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h5>SheVan</h5>
      <ul>
        <li><a href="{p}index.html#sobre">Quiénes somos</a></li>
        <li><a href="{p}proyectos.html">Proyectos</a></li>
        <li><a href="{p}contacto.html">Contacto</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h5>Visítanos</h5>
      <ul>
        <li>{contact["address_street"]}</li>
        <li>{contact["address_city"]}</li>
        <li>{contact["neighborhood"]}</li>
        <li><a href="tel:{contact["phone_tel"]}">{contact["phone_display"]}</a></li>
        <li><a href="mailto:{contact["email"]}">{contact["email"]}</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <span>© 2026 SheVan · Sabadell, Barcelona</span>
    <span><a href="#">Aviso legal</a> · <a href="#">Política de privacidad</a> · <a href="#">Cookies</a></span>
  </div>
</footer>
'''


def render_floating_wa(depth, contact, default_text="Hola SheVan! Me gustaría más info sobre vuestras camperizaciones."):
    """The persistent WhatsApp bubble (bottom-right of every page)."""
    txt = urllib.parse.quote(default_text)
    return f'''
<a href="https://wa.me/{contact["phone_e164"]}?text={txt}"
   target="_blank" rel="noopener"
   class="float-wa" aria-label="Habla con nosotros por WhatsApp">
  {ICONS["wa"]}
</a>'''


def render_scripts():
    return '''
<script>
  // Sticky nav background on scroll
  const nav = document.getElementById('siteNav');
  if (nav) {
    window.addEventListener('scroll', () => {
      nav.classList.toggle('scrolled', window.scrollY > 40);
    });
  }
  // Mobile menu toggle
  function toggleMobileMenu() {
    document.getElementById('mobileMenu').classList.toggle('open');
  }
</script>
</body>
</html>'''
