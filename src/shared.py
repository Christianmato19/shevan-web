# -*- coding: utf-8 -*-
"""
SheVan multipage website generator — Part 1: Shared templates.
Generates: head, nav, footer, modal, CSS — all parametrized by page depth
so links resolve correctly from /index.html, /accesorios.html and
/accesorios/segunda-bateria.html alike.
"""

# ============================================================
# CONTACT INFO (single source of truth)
# ============================================================
CONTACT = {
    "phone_display": "665 42 15 21",
    "phone_tel": "+34665421521",
    "phone_e164": "34665421521",
    "email": "info@shevanbarcelona.es",
    "address_street": "Carrer de Ca n'Alzina 116F",
    "address_city": "08202 Sabadell",
    "neighborhood": "Polígono Can Roqueta",
    "hours": "Lunes a Viernes · 8:00 — 18:00",
    "city": "Sabadell",
    "province": "Barcelona",
    "domain": "shevanbarcelona.es",
}

SITE_NAME = "SheVan"
SITE_TAGLINE = "Camperizaciones a medida en Sabadell, Barcelona"

# ============================================================
# CSS — shared across all pages
# ============================================================
CSS = """
:root {
  --yellow: #fadc57;
  --yellow-deep: #e8c645;
  --black: #0a0a0a;
  --ink: #141414;
  --cream: #f5f1e8;
  --cream-dark: #ede7d6;
  --muted: rgba(20,20,20,0.55);
  --line: rgba(20,20,20,0.12);
  --shadow: 0 30px 80px -28px rgba(0,0,0,0.18);
}
* { box-sizing: border-box; margin: 0; padding: 0; }
*::selection { background: var(--yellow); color: var(--black); }
html { scroll-behavior: smooth; -webkit-font-smoothing: antialiased; text-rendering: optimizeLegibility; }
body {
  font-family: 'Inter', -apple-system, sans-serif;
  background: var(--cream); color: var(--ink); line-height: 1.6;
}
a { color: inherit; text-decoration: none; }
img { max-width: 100%; display: block; }

/* ====== NAV ====== */
nav.site {
  position: fixed; top: 0; left: 0; right: 0; z-index: 100;
  display: flex; align-items: center; justify-content: space-between;
  padding: 18px clamp(20px, 5vw, 56px);
  transition: background .3s, backdrop-filter .3s, border .3s;
  border-bottom: 1px solid transparent;
}
nav.site.scrolled, nav.site.solid {
  background: rgba(245, 241, 232, 0.92);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--line);
}
.nav-logo { display: flex; align-items: center; gap: 12px; }
.nav-logo img { height: 36px; width: auto; }
.nav-links { display: flex; gap: 28px; align-items: center; }
.nav-links > li { list-style: none; position: relative; }
.nav-links > li > a, .nav-links a.toplink {
  font-size: 14px; font-weight: 500; padding: 10px 0;
  display: inline-block; position: relative;
}
.nav-links > li > a::after {
  content: ''; position: absolute; bottom: 4px; left: 0;
  width: 0; height: 1.5px; background: var(--ink); transition: width .3s;
}
.nav-links > li > a:hover::after,
.nav-links > li.active > a::after { width: 100%; }
.nav-links > li.active > a { font-weight: 600; }

.submenu {
  position: absolute; top: 100%; left: -18px; min-width: 240px;
  background: var(--cream); border: 1px solid var(--line);
  border-radius: 10px; padding: 8px; box-shadow: var(--shadow);
  opacity: 0; pointer-events: none; transform: translateY(8px);
  transition: opacity .2s, transform .2s; z-index: 110;
}
.nav-links > li:hover .submenu { opacity: 1; pointer-events: auto; transform: translateY(0); }
.submenu li { list-style: none; }
.submenu a {
  display: block; padding: 10px 14px; border-radius: 6px;
  font-size: 14px; transition: background .15s;
}
.submenu a:hover { background: rgba(20,20,20,0.05); }

.nav-cta {
  background: var(--ink); color: var(--cream);
  padding: 10px 20px; border-radius: 100px;
  display: inline-flex; align-items: center; gap: 8px;
  font-size: 14px; font-weight: 500;
  transition: transform .2s, background .2s;
}
.nav-cta::before {
  content: ''; width: 7px; height: 7px; background: var(--yellow);
  border-radius: 50%; animation: pulse 2s infinite;
}
.nav-cta:hover { background: var(--yellow); color: var(--ink); transform: translateY(-1px); }
.nav-cta:hover::before { background: var(--ink); animation: none; }
@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(250,220,87,0.6); }
  70% { box-shadow: 0 0 0 7px rgba(250,220,87,0); }
  100% { box-shadow: 0 0 0 0 rgba(250,220,87,0); }
}
.menu-btn { display: none; background: none; border: 0; padding: 8px; cursor: pointer; }
.menu-btn span { display: block; width: 26px; height: 2px; background: var(--ink); margin: 5px 0; transition: .3s; }

/* ====== HERO ====== */
.hero { min-height: 100vh; background: var(--yellow); position: relative; display: flex; align-items: center; padding: 120px clamp(20px,5vw,56px) 80px; overflow: hidden; }
.hero::before { content: ''; position: absolute; inset: 0; background-image: radial-gradient(circle at 15% 30%, rgba(255,255,255,0.4) 0%, transparent 40%), radial-gradient(circle at 85% 80%, rgba(232,198,69,0.4) 0%, transparent 40%); pointer-events: none; }
.hero::after { content: ''; position: absolute; inset: 0; background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence baseFrequency='0.9' numOctaves='2'/></filter><rect width='100%25' height='100%25' filter='url(%23n)' opacity='0.08'/></svg>"); pointer-events: none; mix-blend-mode: multiply; }
.hero-inner { position: relative; z-index: 2; max-width: 1200px; width: 100%; margin: 0 auto; }
.hero h1 { font-family: 'Bricolage Grotesque', sans-serif; font-size: clamp(48px,10vw,148px); line-height: .92; letter-spacing: -0.05em; font-weight: 400; margin-bottom: 32px; color: var(--ink); }
.hero h1 strong { font-weight: 800; }
.hero h1 em { font-style: italic; font-weight: 800; font-variation-settings: "opsz" 96; }
.hero-sub { font-size: clamp(16px,1.4vw,19px); line-height: 1.55; color: var(--ink); opacity: .75; max-width: 540px; margin-bottom: 40px; }
.hero-actions { display: flex; gap: 16px; flex-wrap: wrap; align-items: center; }

/* Sub-page headers (smaller hero) */
.subhero { background: var(--yellow); padding: 140px clamp(20px,5vw,56px) 64px; position: relative; overflow: hidden; }
.subhero::after { content: ''; position: absolute; inset: 0; background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence baseFrequency='0.9' numOctaves='2'/></filter><rect width='100%25' height='100%25' filter='url(%23n)' opacity='0.06'/></svg>"); pointer-events: none; mix-blend-mode: multiply; }
.subhero-inner { position: relative; z-index: 2; max-width: 1200px; margin: 0 auto; }
.breadcrumb { display: flex; gap: 10px; align-items: center; font-size: 13px; opacity: .65; margin-bottom: 24px; flex-wrap: wrap; }
.breadcrumb a:hover { text-decoration: underline; }
.breadcrumb span { opacity: .5; }
.subhero h1 { font-family: 'Bricolage Grotesque', sans-serif; font-size: clamp(36px,6vw,72px); line-height: .96; letter-spacing: -0.04em; font-weight: 700; margin-bottom: 20px; max-width: 920px; }
.subhero h1 em { font-style: italic; font-weight: 300; }
.subhero .lead { font-size: clamp(16px,1.3vw,18px); line-height: 1.6; max-width: 640px; opacity: .8; }

/* ====== BUTTONS ====== */
.btn { display: inline-flex; align-items: center; gap: 10px; padding: 16px 28px; border-radius: 100px; font-size: 15px; font-weight: 600; cursor: pointer; border: 0; transition: transform .2s, background .2s, color .2s; font-family: inherit; }
.btn-primary { background: var(--ink); color: var(--cream); }
.btn-primary:hover { background: var(--cream); color: var(--ink); transform: translateY(-2px); box-shadow: 0 12px 32px -8px rgba(0,0,0,0.3); }
.btn-yellow { background: var(--yellow); color: var(--ink); }
.btn-yellow:hover { background: var(--ink); color: var(--yellow); transform: translateY(-2px); }
.btn-ghost { background: transparent; color: var(--ink); border: 1.5px solid rgba(0,0,0,0.2); }
.btn-ghost:hover { border-color: var(--ink); transform: translateY(-2px); }
.btn-arrow { display: inline-block; transition: transform .2s; }
.btn:hover .btn-arrow { transform: translateX(4px); }

/* ====== SECTIONS ====== */
section { padding: clamp(70px,9vw,120px) clamp(20px,5vw,56px); position: relative; }
.container { max-width: 1200px; margin: 0 auto; }
.section-eyebrow { display: inline-flex; align-items: center; gap: 12px; font-size: 12px; font-weight: 600; letter-spacing: 0.32em; text-transform: uppercase; margin-bottom: 22px; }
.section-eyebrow::before { content: ''; width: 28px; height: 1.5px; background: currentColor; opacity: .5; }
.section-title { font-family: 'Bricolage Grotesque', sans-serif; font-size: clamp(36px,5.5vw,68px); line-height: .98; letter-spacing: -0.04em; font-weight: 700; max-width: 880px; margin-bottom: 28px; }
.section-title em { font-style: italic; font-weight: 300; color: var(--muted); }
.section-lead { font-size: clamp(16px,1.2vw,18px); line-height: 1.65; color: var(--muted); max-width: 640px; margin-bottom: 48px; }

/* ====== SERVICE CARDS ====== */
.cards-grid { display: grid; gap: 22px; }
.cards-grid.cols-3 { grid-template-columns: repeat(3, 1fr); }
.cards-grid.cols-4 { grid-template-columns: repeat(4, 1fr); }
.card {
  background: white; border: 1px solid var(--line); border-radius: 14px;
  padding: 32px 28px; display: flex; flex-direction: column;
  transition: transform .3s, box-shadow .3s, border-color .3s;
  position: relative; overflow: hidden;
}
.card:hover { transform: translateY(-6px); box-shadow: var(--shadow); border-color: rgba(20,20,20,0.3); }
.card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: var(--yellow); transform: scaleX(0); transform-origin: left; transition: transform .4s; }
.card:hover::before { transform: scaleX(1); }
.card-num { font-family: 'Bricolage Grotesque', sans-serif; font-size: 12px; font-weight: 600; color: var(--muted); letter-spacing: 0.05em; margin-bottom: 18px; }
.card-icon { width: 52px; height: 52px; background: var(--yellow); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 22px; }
.card-icon svg { width: 26px; height: 26px; }
.card h3 { font-family: 'Bricolage Grotesque', sans-serif; font-size: 24px; font-weight: 700; letter-spacing: -0.02em; line-height: 1.12; margin-bottom: 12px; }
.card p { font-size: 14px; line-height: 1.6; color: var(--muted); margin-bottom: 18px; flex-grow: 1; }
.card-cta { display: inline-flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600; color: var(--ink); margin-top: auto; }

/* ====== DETAIL PAGE ====== */
.detail-body { padding: clamp(70px,8vw,120px) clamp(20px,5vw,56px); background: var(--cream); }
.detail-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: start; max-width: 1200px; margin: 0 auto; }
.detail-img-placeholder {
  aspect-ratio: 4/5; background: var(--ink); color: var(--cream);
  border-radius: 14px; display: flex; flex-direction: column;
  align-items: center; justify-content: center; padding: 32px; text-align: center;
  position: sticky; top: 120px;
}
.detail-img-placeholder .ph-icon { width: 64px; height: 64px; opacity: .35; margin-bottom: 18px; }
.detail-img-placeholder p { font-size: 13px; opacity: .55; line-height: 1.5; }
.detail-img-placeholder strong { display: block; font-size: 14px; opacity: .85; margin-bottom: 6px; }

.detail-content h2 { font-family: 'Bricolage Grotesque', sans-serif; font-size: clamp(28px,3.5vw,40px); line-height: 1.05; letter-spacing: -0.03em; font-weight: 700; margin-bottom: 18px; }
.detail-content h3 { font-family: 'Bricolage Grotesque', sans-serif; font-size: 22px; font-weight: 700; letter-spacing: -0.02em; margin: 32px 0 12px; }
.detail-content p { font-size: 16px; line-height: 1.75; color: var(--ink); margin-bottom: 18px; }
.detail-content p strong { font-weight: 600; }
.detail-content ul { list-style: none; margin: 18px 0 24px; }
.detail-content ul li { padding: 12px 0; border-top: 1px solid var(--line); padding-left: 24px; position: relative; line-height: 1.55; }
.detail-content ul li:last-child { border-bottom: 1px solid var(--line); }
.detail-content ul li::before { content: '+'; position: absolute; left: 0; top: 12px; font-weight: 700; color: var(--yellow-deep); font-size: 18px; line-height: 1; }
.detail-content ul li strong { font-weight: 600; display: block; margin-bottom: 2px; }
.detail-quote {
  font-family: 'Bricolage Grotesque', serif;
  font-style: italic; font-weight: 400;
  font-size: clamp(20px,2vw,26px); line-height: 1.3;
  letter-spacing: -0.02em;
  background: var(--yellow); padding: 32px 36px;
  border-radius: 14px; margin: 36px 0;
  position: relative;
}
.detail-quote::before {
  content: '"'; font-size: 80px; line-height: 0.4; position: absolute;
  top: 38px; left: 14px; opacity: .35;
}
.detail-cta {
  background: var(--ink); color: var(--cream); border-radius: 14px;
  padding: 36px; margin-top: 24px;
}
.detail-cta h3 { font-family: 'Bricolage Grotesque', sans-serif; font-size: 26px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 8px; line-height: 1.1; }
.detail-cta p { color: rgba(245,241,232,0.7); margin-bottom: 22px; line-height: 1.55; }
.detail-cta .btn-row { display: flex; gap: 12px; flex-wrap: wrap; }

/* ====== BRANDS BAR ====== */
.brands-bar { background: var(--cream-dark); padding: 36px clamp(20px,5vw,56px); }
.brands-bar-inner { max-width: 1200px; margin: 0 auto; }
.brands-bar p { font-size: 12px; font-weight: 600; letter-spacing: .24em; text-transform: uppercase; color: var(--muted); margin-bottom: 18px; text-align: center; }
.brands-list { display: flex; flex-wrap: wrap; gap: 16px 28px; justify-content: center; }
.brand-chip {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-size: 18px; font-weight: 600; letter-spacing: -0.01em;
  padding: 10px 18px; background: white; border: 1px solid var(--line);
  border-radius: 100px;
}

/* ====== PROCESS / OTHER SECTIONS ====== */
.dark-section { background: var(--ink); color: var(--cream); }
.dark-section .section-title em { color: var(--yellow); opacity: .6; }
.dark-section .section-eyebrow { color: var(--yellow); }
.dark-section .section-lead { color: rgba(245,241,232,0.65); }

.process-steps { display: grid; grid-template-columns: repeat(4,1fr); gap: 24px; margin-top: 56px; position: relative; }
.process-steps::before { content: ''; position: absolute; top: 32px; left: 0; right: 0; height: 1px; background: var(--yellow); opacity: .25; }
.step { position: relative; }
.step-num { font-family: 'Bricolage Grotesque', sans-serif; font-size: 80px; font-weight: 200; letter-spacing: -0.05em; line-height: .85; color: var(--yellow); margin-bottom: 14px; display: block; }
.step h3 { font-family: 'Bricolage Grotesque', sans-serif; font-size: 24px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 8px; }
.step p { font-size: 14px; line-height: 1.6; color: rgba(245,241,232,0.65); }

/* ====== PROJECTS GRID ====== */
.projects-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 18px; margin-top: 48px; }
.project-card { aspect-ratio: 4/5; background: var(--ink); color: var(--cream); border-radius: 10px; padding: 26px; display: flex; flex-direction: column; justify-content: space-between; position: relative; overflow: hidden; cursor: pointer; }
.project-card:nth-child(2), .project-card:nth-child(4), .project-card:nth-child(6) { background: var(--yellow); color: var(--ink); }
.project-card-num { font-family: 'Bricolage Grotesque', sans-serif; font-size: 60px; font-weight: 300; letter-spacing: -0.04em; line-height: 1; opacity: .85; }
.project-card-meta { font-size: 11px; letter-spacing: .18em; text-transform: uppercase; font-weight: 500; opacity: .6; margin-bottom: 8px; }
.project-card h4 { font-family: 'Bricolage Grotesque', sans-serif; font-size: 21px; font-weight: 700; letter-spacing: -0.02em; line-height: 1.1; margin-bottom: 8px; }
.project-card p { font-size: 13px; opacity: .7; line-height: 1.5; }

/* ====== CONTACT FORMS ====== */
.contact-form-section { background: var(--cream); padding: clamp(70px,9vw,120px) clamp(20px,5vw,56px); }
.contact-form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; max-width: 1200px; margin: 0 auto; align-items: start; }
.contact-info-block { display: flex; flex-direction: column; gap: 26px; }
.contact-info-item { border-top: 1px solid var(--line); padding-top: 22px; }
.contact-info-label { font-size: 11px; letter-spacing: .24em; text-transform: uppercase; font-weight: 600; color: var(--muted); margin-bottom: 6px; }
.contact-info-value { font-family: 'Bricolage Grotesque', sans-serif; font-size: 22px; font-weight: 600; letter-spacing: -0.02em; line-height: 1.25; }
.contact-info-value a:hover { color: var(--yellow-deep); }

.form { background: white; border: 1px solid var(--line); border-radius: 14px; padding: 36px; }
.form-eyebrow { font-size: 11px; letter-spacing: .24em; text-transform: uppercase; font-weight: 600; color: var(--muted); margin-bottom: 12px; }
.form h3 { font-family: 'Bricolage Grotesque', sans-serif; font-size: 28px; font-weight: 700; letter-spacing: -0.02em; line-height: 1.1; margin-bottom: 8px; }
.form-sub { font-size: 14px; color: var(--muted); margin-bottom: 28px; line-height: 1.55; }
.field { margin-bottom: 18px; }
.field-label { display: block; font-size: 12px; font-weight: 600; letter-spacing: .14em; text-transform: uppercase; margin-bottom: 8px; color: var(--ink); }
.field input, .field select, .field textarea {
  width: 100%; padding: 13px 16px;
  border: 1.5px solid var(--line); border-radius: 8px;
  background: var(--cream); font-family: inherit;
  font-size: 15px; color: var(--ink); transition: border-color .2s;
}
.field input:focus, .field select:focus, .field textarea:focus { outline: 0; border-color: var(--ink); background: white; }
.field textarea { resize: vertical; min-height: 100px; }
.form-submit { width: 100%; background: var(--ink); color: var(--cream); padding: 16px; border-radius: 100px; border: 0; font-size: 16px; font-weight: 600; cursor: pointer; font-family: inherit; transition: background .2s, transform .2s; margin-top: 8px; }
.form-submit:hover { background: var(--yellow); color: var(--ink); transform: translateY(-1px); }
.form-or { text-align: center; padding: 14px 0; font-size: 13px; color: var(--muted); position: relative; margin: 12px 0; }
.form-or::before, .form-or::after { content: ''; position: absolute; top: 50%; width: 35%; height: 1px; background: var(--line); }
.form-or::before { left: 0; }
.form-or::after { right: 0; }
.wa-link { display: flex; align-items: center; justify-content: center; gap: 10px; width: 100%; background: #25D366; color: white; padding: 14px; border-radius: 100px; font-size: 15px; font-weight: 600; text-decoration: none; transition: background .2s, transform .2s; }
.wa-link:hover { background: #1FB855; transform: translateY(-1px); }
.wa-link svg { width: 20px; height: 20px; }

/* ====== ABOUT TEASER (home) ====== */
.about-section { background: var(--yellow); }
.about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center; }
.about-text h2 { font-family: 'Bricolage Grotesque', sans-serif; font-size: clamp(34px,5vw,56px); line-height: .98; letter-spacing: -0.04em; font-weight: 700; margin-bottom: 26px; }
.about-text h2 em { font-style: italic; font-weight: 400; }
.about-text p { font-size: 17px; line-height: 1.7; margin-bottom: 16px; max-width: 480px; }
.about-text p strong { font-weight: 600; }
.about-side { aspect-ratio: 4/5; background: var(--ink); color: var(--cream); border-radius: 14px; padding: 44px; display: flex; flex-direction: column; justify-content: space-between; position: relative; overflow: hidden; }
.about-side .quote-mark { font-family: 'Bricolage Grotesque', serif; font-size: 200px; line-height: .6; color: var(--yellow); font-style: italic; font-weight: 800; position: absolute; top: 30px; left: 36px; opacity: .4; }
.about-side blockquote { font-family: 'Bricolage Grotesque', serif; font-size: 26px; line-height: 1.2; font-style: italic; font-weight: 400; letter-spacing: -0.02em; position: relative; z-index: 2; margin-top: 80px; }
.about-side cite { font-style: normal; font-size: 12px; letter-spacing: .18em; text-transform: uppercase; opacity: .65; font-weight: 500; display: block; margin-top: 22px; }

/* ====== RELATED SERVICES (bottom of detail pages) ====== */
.related { background: var(--cream-dark); padding: 80px clamp(20px,5vw,56px); }
.related-inner { max-width: 1200px; margin: 0 auto; }
.related h3 { font-family: 'Bricolage Grotesque', sans-serif; font-size: 32px; font-weight: 700; letter-spacing: -0.03em; margin-bottom: 32px; }
.related-list { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }
.related-link { background: white; border: 1px solid var(--line); padding: 20px 22px; border-radius: 10px; transition: transform .2s, border-color .2s; display: flex; justify-content: space-between; align-items: center; gap: 12px; }
.related-link:hover { transform: translateX(4px); border-color: var(--ink); }
.related-link span:first-child { font-weight: 600; font-size: 15px; }
.related-link span:last-child { font-size: 18px; opacity: .5; }

/* ====== FOOTER ====== */
footer.site { background: var(--ink); color: rgba(245,241,232,0.65); padding: 64px clamp(20px,5vw,56px) 32px; }
.footer-grid { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1.4fr 1fr 1fr 1fr; gap: 40px; padding-bottom: 40px; border-bottom: 1px solid rgba(245,241,232,0.08); }
.footer-brand img { height: 42px; margin-bottom: 18px; }
.footer-brand p { font-size: 14px; line-height: 1.6; max-width: 300px; }
.footer-col h5 { font-size: 11px; letter-spacing: .24em; text-transform: uppercase; font-weight: 600; color: var(--yellow); margin-bottom: 18px; }
.footer-col ul { list-style: none; }
.footer-col li { padding: 5px 0; }
.footer-col a { font-size: 14px; transition: color .15s; }
.footer-col a:hover { color: var(--yellow); }
.footer-bottom { max-width: 1200px; margin: 24px auto 0; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 12px; font-size: 12px; }

/* ====== FLOATING WHATSAPP ====== */
.float-wa { position: fixed; bottom: 24px; right: 24px; z-index: 50; width: 58px; height: 58px; border-radius: 50%; background: #25D366; color: white; display: flex; align-items: center; justify-content: center; box-shadow: 0 8px 24px rgba(37,211,102,0.4); border: 0; cursor: pointer; transition: transform .2s, box-shadow .2s; }
.float-wa:hover { transform: scale(1.08); box-shadow: 0 12px 32px rgba(37,211,102,0.6); }
.float-wa svg { width: 28px; height: 28px; }

/* ====== RESPONSIVE ====== */
@media (max-width: 980px) {
  .nav-links, .nav-cta { display: none; }
  .menu-btn { display: block; }
  .mobile-menu { position: fixed; inset: 60px 0 0 0; background: var(--cream); z-index: 99; padding: 32px; display: none; flex-direction: column; gap: 20px; overflow-y: auto; }
  .mobile-menu.open { display: flex; }
  .mobile-menu a { font-size: 18px; padding: 12px 0; border-bottom: 1px solid var(--line); }
  .mobile-menu .submenu-mobile { padding-left: 16px; display: flex; flex-direction: column; gap: 10px; margin-top: 4px; }
  .mobile-menu .submenu-mobile a { font-size: 15px; padding: 6px 0; border: 0; opacity: .7; }
  .cards-grid.cols-3, .cards-grid.cols-4 { grid-template-columns: 1fr; }
  .detail-grid, .contact-form-grid, .about-grid { grid-template-columns: 1fr; gap: 36px; }
  .detail-img-placeholder { position: static; aspect-ratio: 16/10; }
  .process-steps, .related-list { grid-template-columns: 1fr 1fr; gap: 28px; }
  .process-steps::before { display: none; }
  .projects-grid { grid-template-columns: 1fr 1fr; }
  .footer-grid { grid-template-columns: 1fr 1fr; }
  .about-side { aspect-ratio: auto; padding: 32px; }
}
@media (max-width: 560px) {
  .process-steps, .related-list, .projects-grid, .footer-grid { grid-template-columns: 1fr; }
}
"""
