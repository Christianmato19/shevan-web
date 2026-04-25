# -*- coding: utf-8 -*-
"""
Page renderers and main build runner.

Each render_*_page() function returns the full HTML string for a page.
build_all() walks every entry in src/data.py and writes the rendered
HTML to <out_dir>/, mirroring the public URL structure.
"""
import json
import shutil
import urllib.parse
from pathlib import Path

from .shared import CSS, CONTACT
from .data import (
    CAMPERIZACIONES_SUB,
    ACCESORIOS,
    TALLER_SECCIONES,
)
from .templates import (
    ICONS,
    prefix,
    render_head,
    render_nav,
    render_footer,
    render_floating_wa,
    render_scripts,
)


# ============================================================
# PAGE: HOME
# ============================================================

def render_home_page() -> str:
    p = prefix(0)

    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "AutoRepair",
        "name": "SheVan",
        "image": f"https://{CONTACT['domain']}/logo-yellow.png",
        "url": f"https://{CONTACT['domain']}/",
        "telephone": CONTACT["phone_tel"],
        "email": CONTACT["email"],
        "priceRange": "€€",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": CONTACT["address_street"],
            "addressLocality": CONTACT["city"],
            "postalCode": "08202",
            "addressRegion": "Barcelona",
            "addressCountry": "ES"
        },
        "geo": {"@type": "GeoCoordinates", "latitude": 41.5479, "longitude": 2.1075},
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "08:00", "closes": "18:00"
        }],
        "areaServed": [
            {"@type": "City", "name": "Sabadell"},
            {"@type": "City", "name": "Barcelona"},
            {"@type": "AdministrativeArea", "name": "Catalunya"}
        ]
    }, ensure_ascii=False)

    head = render_head(
        title="SheVan — Camperizaciones a medida en Sabadell, Barcelona",
        description="Camperización completa, instalación de accesorios y taller de reparaciones para furgonetas y autocaravanas en Sabadell. La diseñamos contigo, la construimos para tu libertad.",
        depth=0, schema_jsonld=schema, canonical_path=""
    )
    nav = render_nav("home", 0)

    home_services = [
        ("Gran Volumen", "Ducato, Sprinter, Crafter. Camperización completa para vivienda total.", "camperizaciones/gran-volumen.html", "01", "van-large"),
        ("Medianas y Pequeñas", "VW T6, Vito, Trafic, Berlingo. Versatilidad para escapadas.", "camperizaciones/medianas-pequenas.html", "02", "van-small"),
        ("Accesorios e instalaciones", "Solar, baterías, calefacción, A/C, techo elevable… para campers y autocaravanas.", "accesorios.html", "03", "bolt"),
        ("Taller y reparaciones", "Mantenimiento, averías, filtraciones, mejoras… para campers y autocaravanas.", "taller.html", "04", "wrench"),
    ]
    services_grid = ""
    for title, desc, href, num, icon in home_services:
        services_grid += f'''
        <a href="{href}" class="card">
          <p class="card-num">{num} / Servicio</p>
          <div class="card-icon">{ICONS[icon]}</div>
          <h3>{title}</h3>
          <p>{desc}</p>
          <span class="card-cta">Más info <span class="btn-arrow">→</span></span>
        </a>'''

    return f'''
{head}
{nav}

<section class="hero">
  <div class="hero-inner">
    <p class="section-eyebrow">Camperizaciones · Sabadell · Barcelona</p>
    <h1>La diseñamos<br>contigo,<br>la construimos<br>para tu <em>libertad.</em></h1>
    <p class="hero-sub">Convertimos tu furgo en el hogar sobre ruedas que tienes en la cabeza. A medida, sin atajos, con el detalle de quien lo va a vivir contigo.</p>
    <div class="hero-actions">
      <a href="{p}contacto.html#presupuesto" class="btn btn-primary">Pide presupuesto <span class="btn-arrow">→</span></a>
      <a href="#servicios" class="btn btn-ghost">Ver qué hacemos</a>
    </div>
  </div>
</section>

<section id="servicios">
  <div class="container">
    <p class="section-eyebrow">Qué hacemos</p>
    <h2 class="section-title">Cuatro formas <em>de subirte</em> a la furgo.</h2>
    <p class="section-lead">Camperizaciones completas, mejoras de equipamiento e intervenciones de taller. Cada furgo es distinta — por eso ningún proyecto se sale igual.</p>
    <div class="cards-grid cols-4">
      {services_grid}
    </div>
  </div>
</section>

<section id="proceso" class="dark-section">
  <div class="container">
    <p class="section-eyebrow">Así trabajamos</p>
    <h2 class="section-title">De la idea <em>a la carretera.</em></h2>
    <p class="section-lead">Construir una camper a medida lleva tiempo y conversación. Te contamos cómo va el proceso para que sepas qué esperar.</p>
    <div class="process-steps">
      <div class="step"><span class="step-num">01</span><h3>Escuchamos</h3><p>Nos cuentas cómo viajas, qué necesitas y qué furgo tienes en mente. Sin compromiso.</p></div>
      <div class="step"><span class="step-num">02</span><h3>Diseñamos</h3><p>Plano a medida, presupuesto detallado y tiempos. Tú decides qué entra y qué no.</p></div>
      <div class="step"><span class="step-num">03</span><h3>Construimos</h3><p>Trabajamos en nuestra nave de Sabadell. Te enseñamos los avances con fotos y visitas.</p></div>
      <div class="step"><span class="step-num">04</span><h3>Conduces</h3><p>Entrega, homologación si toca, y a perderte. Seguimos a tu lado para mantenimiento.</p></div>
    </div>
  </div>
</section>

<section id="proyectos">
  <div class="container">
    <p class="section-eyebrow">Algunos proyectos</p>
    <h2 class="section-title">Cada furgo cuenta <em>una historia distinta.</em></h2>
    <div class="projects-grid">
      <a href="{p}proyectos.html" class="project-card"><div><p class="project-card-meta">Camperización</p><h4>VW T6 California</h4><p>Cama elevable, cocina, eléctrica solar.</p></div><span class="project-card-num">01</span></a>
      <a href="{p}proyectos.html" class="project-card"><div><p class="project-card-meta">Accesorios</p><h4>Ducato 2.3</h4><p>Solar 400W, baterías litio, claraboya.</p></div><span class="project-card-num">02</span></a>
      <a href="{p}proyectos.html" class="project-card"><div><p class="project-card-meta">Camperización</p><h4>Sprinter L2H2</h4><p>Vivienda total con baño y ducha.</p></div><span class="project-card-num">03</span></a>
      <a href="{p}proyectos.html" class="project-card"><div><p class="project-card-meta">Taller</p><h4>Reparación T5</h4><p>Renovación de instalación eléctrica.</p></div><span class="project-card-num">04</span></a>
      <a href="{p}proyectos.html" class="project-card"><div><p class="project-card-meta">Camperización</p><h4>Renault Trafic</h4><p>Camper compacta para 2.</p></div><span class="project-card-num">05</span></a>
      <a href="{p}proyectos.html" class="project-card"><div><p class="project-card-meta">Accesorios</p><h4>Crafter</h4><p>Calefacción Webasto + agua caliente.</p></div><span class="project-card-num">06</span></a>
    </div>
    <p style="margin-top:32px; padding:16px 20px; background: rgba(20,20,20,0.06); border-radius: 8px; font-size:13px; color:var(--muted); text-align:center; font-style:italic;">Los proyectos mostrados son un placeholder — aquí irá la galería real con fotos de cada furgo terminada.</p>
  </div>
</section>

<section id="sobre" class="about-section">
  <div class="container">
    <div class="about-grid">
      <div class="about-text">
        <p class="section-eyebrow">¿Quiénes somos?</p>
        <h2>Detrás de cada ruta, <em>hay una historia.</em> Conoce SheVan.</h2>
        <p>En <strong>SheVan</strong> no solo construimos muebles para furgonetas; creamos espacios de libertad. Somos apasionados del mundo <em>vanlife</em> y entendemos que tu furgo no es solo un vehículo: es tu pasaporte a lo desconocido y tu refugio al final del día.</p>
        <p>Nuestra filosofía es sencilla: escuchar tu idea y convertirla en realidad con nuestras manos. Combinamos el diseño artesanal con la tecnología más avanzada en instalaciones, cuidando cada detalle como si fuera para nosotros mismos. Queremos que, cuando cierres la puerta y arranques el motor, tu única preocupación sea elegir el siguiente destino en el mapa.</p>
        <p><strong>Tu proyecto es nuestro próximo viaje. ¿Arrancamos?</strong></p>
        <a href="{p}contacto.html#presupuesto" class="btn btn-primary" style="margin-top:24px;">Pide tu presupuesto <span class="btn-arrow">→</span></a>
      </div>
      <div class="about-side">
        <span class="quote-mark">"</span>
        <blockquote>Encuentra tu match sobre ruedas. Haz match y pierde el norte.</blockquote>
        <cite>— SheVan, Sabadell</cite>
      </div>
    </div>
  </div>
</section>

<section id="contacto-cta" class="dark-section" style="text-align:center;">
  <div class="container">
    <p class="section-eyebrow" style="justify-content:center;">Hablamos</p>
    <h2 class="section-title" style="margin-left:auto;margin-right:auto;">¿Cuál es <em>tu próximo destino?</em></h2>
    <p class="section-lead" style="margin:0 auto 36px;">Cuéntanos tu idea y te contestamos en menos de 24h con un primer presupuesto orientativo.</p>
    <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;">
      <a href="{p}contacto.html#presupuesto" class="btn btn-yellow">Pide presupuesto <span class="btn-arrow">→</span></a>
      <a href="https://wa.me/{CONTACT['phone_e164']}" target="_blank" rel="noopener" class="btn btn-ghost" style="color:var(--cream);border-color:rgba(245,241,232,0.3);">{ICONS['wa']} <span style="margin-left:4px;">WhatsApp directo</span></a>
    </div>
  </div>
</section>

{render_footer(0, CONTACT)}
{render_floating_wa(0, CONTACT)}
{render_scripts()}
'''


# ============================================================
# PAGE: OVERVIEW (parents: Camperizaciones / Accesorios / Taller)
# ============================================================

def render_overview_page(key, title_seo, description, intro_eyebrow,
                         intro_title, intro_lead, items, depth=0):
    p = prefix(depth)

    head = render_head(title=title_seo, description=description,
                       depth=depth, canonical_path=f"{key}.html")
    nav = render_nav(key, depth)

    grid_html = ""
    for i, item in enumerate(items, 1):
        href = f"{p}{item['category_slug']}/{item['slug']}.html"
        icon_svg = ICONS.get(item.get("icon", "package"), ICONS["package"])
        sub = item.get("subcategory", "")
        if sub:
            sub_html = f'<p class="card-num">{sub.upper()}</p>'
        else:
            sub_html = f'<p class="card-num">{i:02d} / {item["category"].upper()}</p>'
        grid_html += f'''
      <a href="{href}" class="card">
        {sub_html}
        <div class="card-icon">{icon_svg}</div>
        <h3>{item["title"]}</h3>
        <p>{item.get("lead", item.get("intro", ""))[:140]}…</p>
        <span class="card-cta">Más info <span class="btn-arrow">→</span></span>
      </a>'''

    cols = "cols-3" if len(items) <= 6 else "cols-4"
    title_label = ("Camperizaciones" if key == "camperizaciones"
                   else "Accesorios" if key == "accesorios"
                   else "Taller")

    return f'''
{head}
{nav}

<header class="subhero">
  <div class="subhero-inner">
    <nav class="breadcrumb" aria-label="breadcrumb">
      <a href="{p}index.html">Inicio</a>
      <span>/</span>
      <span>{title_label}</span>
    </nav>
    <p class="section-eyebrow">{intro_eyebrow}</p>
    <h1>{intro_title}</h1>
    <p class="lead">{intro_lead}</p>
  </div>
</header>

<section>
  <div class="container">
    <div class="cards-grid {cols}">{grid_html}</div>
  </div>
</section>

<section class="dark-section" style="text-align:center;">
  <div class="container">
    <p class="section-eyebrow" style="justify-content:center;">Hablamos</p>
    <h2 class="section-title" style="margin-left:auto;margin-right:auto;">¿Tienes <em>otra idea en mente?</em></h2>
    <p class="section-lead" style="margin:0 auto 36px;">Si lo que buscas no está en esta lista, cuéntanoslo. Estudiamos la viabilidad y te damos respuesta sin compromiso.</p>
    <a href="{p}contacto.html#presupuesto" class="btn btn-yellow">Consultar posibilidad <span class="btn-arrow">→</span></a>
  </div>
</section>

{render_footer(depth, CONTACT)}
{render_floating_wa(depth, CONTACT)}
{render_scripts()}
'''


# ============================================================
# PAGE: SERVICE DETAIL (single accessory or taller section)
# ============================================================

def render_detail_page(item, all_in_category, depth=1):
    p = prefix(depth)

    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": item["title"],
        "provider": {
            "@type": "AutoRepair",
            "name": "SheVan",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": CONTACT["address_street"],
                "addressLocality": CONTACT["city"],
                "postalCode": "08202",
                "addressCountry": "ES"
            },
            "telephone": CONTACT["phone_tel"]
        },
        "areaServed": "Barcelona, Sabadell, Catalunya",
        "description": item["meta"]
    }, ensure_ascii=False)

    head = render_head(
        title=item["title_seo"], description=item["meta"], depth=depth,
        schema_jsonld=schema,
        canonical_path=f"{item['category_slug']}/{item['slug']}.html"
    )
    nav = render_nav(item["category_slug"], depth)

    features_html = ""
    if item.get("features"):
        features_html = "<ul>"
        for f in item["features"]:
            features_html += f'<li><strong>{f["title"]}</strong>{f["desc"]}</li>'
        features_html += "</ul>"

    brands_html = ""
    if item.get("brands"):
        chips = "".join(f'<span class="brand-chip">{b}</span>' for b in item["brands"])
        brands_html = f'''
<section class="brands-bar">
  <div class="brands-bar-inner">
    <p>Trabajamos con</p>
    <div class="brands-list">{chips}</div>
  </div>
</section>'''

    quote_html = f'<div class="detail-quote">{item["quote"]}</div>' if item.get("quote") else ""
    cta_label = "Reservar cita en taller" if item["category_slug"] == "taller" else "Solicitar presupuesto"

    related_items = [x for x in all_in_category if x["slug"] != item["slug"]][:6]
    related_html = ""
    for rel in related_items:
        rel_href = f"{rel['slug']}.html"
        related_html += f'''
        <a href="{rel_href}" class="related-link">
          <span>{rel["title"]}</span>
          <span>→</span>
        </a>'''

    related_label = ("Otros accesorios" if item["category_slug"] == "accesorios"
                     else "Otros servicios del taller" if item["category_slug"] == "taller"
                     else "Otros servicios de camperización")

    body_html = f'<p>{item["body"]}</p>' if item.get("body") else ""
    intro_html = f'<p>{item["intro"]}</p>' if item.get("intro") else ""

    wa_text = f"Hola SheVan! Me interesa: {item['title']}. ¿Podríais pasarme un presupuesto orientativo?"
    wa_url = f"https://wa.me/{CONTACT['phone_e164']}?text={urllib.parse.quote(wa_text)}"

    return f'''
{head}
{nav}

<header class="subhero">
  <div class="subhero-inner">
    <nav class="breadcrumb" aria-label="breadcrumb">
      <a href="{p}index.html">Inicio</a>
      <span>/</span>
      <a href="{p}{item['category_slug']}.html">{item["category"]}</a>
      <span>/</span>
      <span>{item["title"]}</span>
    </nav>
    <p class="section-eyebrow">{item.get("subcategory", item["category"]).upper()}</p>
    <h1>{item["title_long"]}</h1>
    <p class="lead">{item["lead"]}</p>
  </div>
</header>

{brands_html}

<section class="detail-body">
  <div class="detail-grid">
    <div class="detail-img-placeholder">
      <svg class="ph-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.5-3.5L9 20"/></svg>
      <strong>{item["image_label"]}</strong>
      <p>Foto real del trabajo terminado<br>(sustituir por imagen final)</p>
    </div>
    <div class="detail-content">
      {intro_html}
      {body_html}
      {features_html}
      {quote_html}
      <div class="detail-cta">
        <h3>¿Te encaja para tu vehículo?</h3>
        <p>Pídenos un presupuesto sin compromiso. Te contestamos en menos de 24h con una primera estimación orientativa.</p>
        <div class="btn-row">
          <a href="{p}contacto.html#presupuesto?servicio={urllib.parse.quote(item['title'])}" class="btn btn-yellow">{cta_label} <span class="btn-arrow">→</span></a>
          <a href="{wa_url}" target="_blank" rel="noopener" class="btn btn-ghost" style="color:var(--cream);border-color:rgba(245,241,232,0.3);">{ICONS['wa']} <span style="margin-left:4px;">WhatsApp</span></a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="related">
  <div class="related-inner">
    <h3>{related_label}</h3>
    <div class="related-list">{related_html}</div>
  </div>
</section>

{render_footer(depth, CONTACT)}
{render_floating_wa(depth, CONTACT)}
{render_scripts()}
'''


# ============================================================
# PAGE: PROYECTOS
# ============================================================

def render_projects_page() -> str:
    p = prefix(0)
    head = render_head(
        title="Proyectos de camperización SheVan en Sabadell, Barcelona",
        description="Galería de campers terminadas en SheVan. VW T6, Ducato, Sprinter, Trafic y más. Cada furgo, una historia distinta.",
        depth=0, canonical_path="proyectos.html"
    )
    nav = render_nav("proyectos", 0)

    sample_projects = [
        ("Camperización completa", "VW T6 California", "Cama elevable, cocina exterior, eléctrica solar 300W, claraboya panorámica."),
        ("Accesorios", "Ducato 2.3 L3H2", "Instalación solar 400W, baterías litio LiFePO4 200Ah, calefacción Webasto."),
        ("Camperización completa", "Sprinter L2H2", "Vivienda total con baño y ducha integrados, suspensión neumática."),
        ("Taller", "Reparación VW T5", "Renovación completa de la instalación eléctrica y actualización a litio."),
        ("Camperización completa", "Renault Trafic", "Camper compacta para 2 personas con espacio de teletrabajo."),
        ("Accesorios", "VW Crafter", "Calefacción Webasto + sistema de agua caliente + techo elevable Reimo."),
        ("Camperización completa", "Mercedes Vito", "Solución compacta con cama abatible y mobiliario modular."),
        ("Accesorios", "Ford Transit Custom", "Aislamiento Kaiflex, ventanas laterales y claraboya."),
        ("Taller", "Filtraciones Hymer", "Localización y sellado de filtración en zona de claraboya."),
    ]
    cards = ""
    for i, (cat, title, desc) in enumerate(sample_projects, 1):
        cards += f'''
      <article class="project-card">
        <div>
          <p class="project-card-meta">{cat}</p>
          <h4>{title}</h4>
          <p>{desc}</p>
        </div>
        <span class="project-card-num">{i:02d}</span>
      </article>'''

    return f'''
{head}
{nav}

<header class="subhero">
  <div class="subhero-inner">
    <nav class="breadcrumb" aria-label="breadcrumb">
      <a href="{p}index.html">Inicio</a><span>/</span><span>Proyectos</span>
    </nav>
    <p class="section-eyebrow">Proyectos</p>
    <h1>Cada furgo cuenta <em>una historia distinta.</em></h1>
    <p class="lead">Algunos de los proyectos que han salido por nuestra nave de Sabadell. La mayoría no caben en un catálogo — cada cliente tenía su forma de viajar y diseñamos en función de eso.</p>
  </div>
</header>

<section>
  <div class="container">
    <div class="projects-grid">{cards}</div>
    <p style="margin-top:36px; padding:18px 22px; background: rgba(20,20,20,0.06); border-radius: 10px; font-size:13px; color:var(--muted); text-align:center; font-style:italic;">Galería con datos de placeholder — sustituir por fotos reales de proyectos terminados.</p>
  </div>
</section>

<section class="dark-section" style="text-align:center;">
  <div class="container">
    <h2 class="section-title" style="margin-left:auto;margin-right:auto;">¿La siguiente furgo <em>es la tuya?</em></h2>
    <p class="section-lead" style="margin:0 auto 36px;">Cuéntanos cómo viajas y empezamos a darle forma.</p>
    <a href="{p}contacto.html#presupuesto" class="btn btn-yellow">Pide presupuesto <span class="btn-arrow">→</span></a>
  </div>
</section>

{render_footer(0, CONTACT)}
{render_floating_wa(0, CONTACT)}
{render_scripts()}
'''


# ============================================================
# PAGE: CONTACTO
# ============================================================

def render_contact_page() -> str:
    p = prefix(0)
    head = render_head(
        title="Contacto · Pide presupuesto en SheVan Sabadell, Barcelona",
        description="Pide presupuesto a SheVan en Sabadell. Camperizaciones, accesorios y taller. Te respondemos en menos de 24h.",
        depth=0, canonical_path="contacto.html"
    )
    nav = render_nav("contacto", 0)
    wa_text = urllib.parse.quote('Hola SheVan! Me gustaría más info sobre vuestras camperizaciones.')

    return f'''
{head}
{nav}

<header class="subhero">
  <div class="subhero-inner">
    <nav class="breadcrumb" aria-label="breadcrumb">
      <a href="{p}index.html">Inicio</a><span>/</span><span>Contacto</span>
    </nav>
    <p class="section-eyebrow">Hablamos</p>
    <h1>Cuéntanos <em>tu idea.</em></h1>
    <p class="lead">Te respondemos en menos de 24h con un primer presupuesto orientativo. Si prefieres rapidez, escríbenos por WhatsApp.</p>
  </div>
</header>

<section class="contact-form-section" id="presupuesto">
  <div class="contact-form-grid">
    <div>
      <form class="form" action="https://formsubmit.co/{CONTACT['email']}" method="POST">
        <input type="hidden" name="_subject" value="Nuevo presupuesto desde la web">
        <input type="hidden" name="_captcha" value="true">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_next" value="https://{CONTACT['domain']}/contacto.html?ok=1">

        <p class="form-eyebrow">Pide presupuesto</p>
        <h3>4 datos básicos y te contestamos.</h3>
        <p class="form-sub">Cuanta más info nos des, más precisa será nuestra respuesta. Pero si prefieres una idea rápida, lo importante es que dejes un teléfono o email.</p>

        <div class="field">
          <label class="field-label" for="nombre">Tu nombre</label>
          <input type="text" id="nombre" name="nombre" required placeholder="Marc Pujol">
        </div>

        <div class="field">
          <label class="field-label" for="contacto">Email o teléfono *</label>
          <input type="text" id="contacto" name="email_o_telefono" required placeholder="marc@ejemplo.com / 600 123 456">
        </div>

        <div class="field">
          <label class="field-label" for="servicio">¿Qué te interesa?</label>
          <select id="servicio" name="servicio" required>
            <option value="">Elige un servicio…</option>
            <option>Camperización completa — Gran Volumen</option>
            <option>Camperización completa — Mediana / Pequeña</option>
            <option>Homologación</option>
            <option>Accesorios para camper</option>
            <option>Accesorios para autocaravana</option>
            <option>Taller — reparación de camper</option>
            <option>Taller — reparación de autocaravana</option>
            <option>Aún no lo sé</option>
          </select>
        </div>

        <div class="field">
          <label class="field-label" for="furgo">¿Tienes ya el vehículo?</label>
          <select id="furgo" name="vehiculo">
            <option>Sí, ya lo tengo (furgo / camper / autocaravana)</option>
            <option>Lo tengo elegido</option>
            <option>Estoy buscando</option>
            <option>Aún no</option>
          </select>
        </div>

        <div class="field">
          <label class="field-label" for="cuando">¿Cuándo te gustaría empezar?</label>
          <select id="cuando" name="cuando">
            <option>Lo antes posible</option>
            <option>En 1–3 meses</option>
            <option>En 3–6 meses</option>
            <option>Sin prisa</option>
          </select>
        </div>

        <div class="field">
          <label class="field-label" for="mensaje">Cuéntanos tu idea</label>
          <textarea id="mensaje" name="mensaje" placeholder="Lo que tengas en la cabeza: distribución, presupuesto orientativo, plazos, dudas…"></textarea>
        </div>

        <button type="submit" class="form-submit">Enviar solicitud <span class="btn-arrow">→</span></button>

        <div class="form-or">o</div>

        <a href="https://wa.me/{CONTACT['phone_e164']}?text={wa_text}" target="_blank" rel="noopener" class="wa-link">
          {ICONS['wa']} Hablar por WhatsApp
        </a>
      </form>
    </div>

    <div class="contact-info-block">
      <div class="contact-info-item">
        <p class="contact-info-label">Teléfono</p>
        <p class="contact-info-value"><a href="tel:{CONTACT['phone_tel']}">{CONTACT['phone_display']}</a></p>
      </div>
      <div class="contact-info-item">
        <p class="contact-info-label">Email</p>
        <p class="contact-info-value"><a href="mailto:{CONTACT['email']}">{CONTACT['email']}</a></p>
      </div>
      <div class="contact-info-item">
        <p class="contact-info-label">Dirección</p>
        <p class="contact-info-value">{CONTACT['address_street']}<br>{CONTACT['address_city']}<br><span style="font-size:14px;font-weight:400;opacity:.65;">{CONTACT['neighborhood']}</span></p>
      </div>
      <div class="contact-info-item">
        <p class="contact-info-label">Horario</p>
        <p class="contact-info-value">Lunes a viernes<br>8:00 — 18:00</p>
      </div>
      <div class="contact-info-item">
        <p class="contact-info-label">Cómo llegar</p>
        <p class="contact-info-value"><a href="https://maps.google.com/?q={urllib.parse.quote(CONTACT['address_street'] + ', ' + CONTACT['address_city'])}" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
      </div>
    </div>
  </div>
</section>

{render_footer(0, CONTACT)}
{render_floating_wa(0, CONTACT)}
{render_scripts()}
'''


# ============================================================
# BUILD RUNNER
# ============================================================

def build_all(out_dir: Path, assets_dir: Path) -> list:
    """Render every page to out_dir, mirroring the public URL structure."""
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "camperizaciones").mkdir(exist_ok=True)
    (out_dir / "accesorios").mkdir(exist_ok=True)
    (out_dir / "taller").mkdir(exist_ok=True)

    pages = []

    # Static assets
    (out_dir / "styles.css").write_text(CSS, encoding="utf-8")
    pages.append("styles.css")
    for asset in ("logo-yellow.png", "logo-black.png"):
        shutil.copy2(assets_dir / asset, out_dir / asset)
        pages.append(asset)

    # Home
    (out_dir / "index.html").write_text(render_home_page(), encoding="utf-8")
    pages.append("index.html")

    # Camperizaciones (overview + 3 details)
    (out_dir / "camperizaciones.html").write_text(render_overview_page(
        key="camperizaciones",
        title_seo="Camperizaciones a medida en Sabadell, Barcelona | SheVan",
        description="Camperización completa de furgonetas en Sabadell. Gran Volumen (Ducato, Sprinter), Medianas y Pequeñas (T6, Vito, Trafic) y homologaciones. Pide presupuesto.",
        intro_eyebrow="Camperizaciones",
        intro_title="Una furgo no es <em>un coche.</em> Es una casa con ruedas.",
        intro_lead="Hacemos camperización completa, desde cero, adaptando cada centímetro a cómo viajas. Tres planteamientos según el tamaño y la intención de tu vehículo.",
        items=CAMPERIZACIONES_SUB, depth=0,
    ), encoding="utf-8")
    pages.append("camperizaciones.html")
    for item in CAMPERIZACIONES_SUB:
        (out_dir / "camperizaciones" / f"{item['slug']}.html").write_text(
            render_detail_page(item, CAMPERIZACIONES_SUB, depth=1), encoding="utf-8")
        pages.append(f"camperizaciones/{item['slug']}.html")

    # Accesorios (overview + 11 details)
    (out_dir / "accesorios.html").write_text(render_overview_page(
        key="accesorios",
        title_seo="Accesorios e instalaciones para Camper y Autocaravana en Sabadell, Barcelona | SheVan",
        description="Instalación de accesorios para campers y autocaravanas en Sabadell: paneles solares, baterías litio, calefacción Webasto, aire acondicionado, techo elevable Reimo, ventanas, claraboyas. Pide presupuesto.",
        intro_eyebrow="Accesorios e instalaciones",
        intro_title="Mejora tu camper <em>o autocaravana,</em> a tu ritmo.",
        intro_lead="Si ya tienes camper o autocaravana y quieres mejorarla, instalamos los accesorios que la van a transformar. Energía, climatización, seguridad, exterior… Lo que necesite tu forma de viajar.",
        items=ACCESORIOS, depth=0,
    ), encoding="utf-8")
    pages.append("accesorios.html")
    for item in ACCESORIOS:
        (out_dir / "accesorios" / f"{item['slug']}.html").write_text(
            render_detail_page(item, ACCESORIOS, depth=1), encoding="utf-8")
        pages.append(f"accesorios/{item['slug']}.html")

    # Taller (overview + 5 details)
    (out_dir / "taller.html").write_text(render_overview_page(
        key="taller",
        title_seo="Taller de Reparaciones de Camper y Autocaravana en Sabadell, Barcelona | SheVan",
        description="Taller especializado en campers y autocaravanas en Sabadell. Reparaciones eléctricas, sistemas de agua, filtraciones, gas, mobiliario. Reserva cita.",
        intro_eyebrow="Taller y reparaciones",
        intro_title="Tu camper o autocaravana, <em>siempre a punto.</em>",
        intro_lead="No solo construimos furgonetas desde cero — también somos tu taller de confianza para mantenimiento, reparación y mejora de campers y autocaravanas. Diagnosticamos el problema y te devolvemos la tranquilidad.",
        items=TALLER_SECCIONES, depth=0,
    ), encoding="utf-8")
    pages.append("taller.html")
    for item in TALLER_SECCIONES:
        (out_dir / "taller" / f"{item['slug']}.html").write_text(
            render_detail_page(item, TALLER_SECCIONES, depth=1), encoding="utf-8")
        pages.append(f"taller/{item['slug']}.html")

    # Proyectos & contacto
    (out_dir / "proyectos.html").write_text(render_projects_page(), encoding="utf-8")
    pages.append("proyectos.html")
    (out_dir / "contacto.html").write_text(render_contact_page(), encoding="utf-8")
    pages.append("contacto.html")

    return pages
