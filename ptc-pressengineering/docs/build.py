# -*- coding: utf-8 -*-
"""Generator für das Template templates/ptc-pressengineering (Skill: designing-dark-brand-sites).
Inhalte stammen von https://www.ptc.eu/ (Stand Oktober 2026). Fotos sind Hotlinks auf ptc.eu."""
import os

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = "https://www.ptc.eu/"

PHONE = "0208 810 60-0";      TEL = "+492088106000"
HOTLINE = "01805 758599";     TEL_H = "+491805758599"
FAX = "0208 810 60-99"
MAIL = "ptc@ptc.eu"
ADDR_1 = "Essener Str. 59";   ADDR_2 = "46047 Oberhausen"
LAT, LNG = "51.4868798", "6.8722333"

HERO_IMG = IMG + "fileadmin/user_upload/header_ptc/Header_171211gs0043_opt2_1920x1080px.jpg"
IMG_PRESSEN = IMG + "fileadmin/user_upload/leistungsspektrum_ptc_pressengineering/ptc_pressengineering_pressen_bandanlagen_modernisierung_instandhaltung.jpg"
IMG_MONTAGE = IMG + "fileadmin/user_upload/leistungsspektrum_ptc_pressengineering/flexible_montagelinien_ptc_pressengineering.jpg"
IMG_ROBOTIK = IMG + "fileadmin/user_upload/leistungsspektrum_ptc_pressengineering/robotik_ptc_pressengineering.jpg"
IMG_NEWS_1 = IMG + "fileadmin/_processed_/8/3/csm_120917gs0049_800x533_637b4d579b.jpg"
IMG_NEWS_2 = IMG + "fileadmin/_processed_/4/0/csm_120917gs0033_800x533_0fb11f631e.jpg"
IMG_NEWS_3 = IMG + "fileadmin/_processed_/1/0/csm_120917gs0017_800x533_333b744754.jpg"
IMG_REF_DAIMLER = IMG + "fileadmin/_processed_/0/7/csm_005_scholpp_ptc_pressEngineering_mercedes_benz_pressenmodernisierung_02_457c787515.jpg"
IMG_REF_ELECTROLUX = IMG + "fileadmin/_processed_/1/6/csm_007_scholpp_ptc_pressEngineering_electrolux_modernisierung_automatisiertes_transfersystem_02_2c7174e81e.jpg"
IMG_REF_TRYOUT = IMG + "fileadmin/_processed_/f/b/csm_012_scholpp_ptc_pressEngineering_modernisierung_hydraulische_tryoutpresse_03_68244d90ba.jpg"
IMG_REF_WEISS = IMG + "fileadmin/_processed_/0/1/csm_140717gs0019_77479882e8.jpg"
IMG_MUELLER = IMG + "fileadmin/_processed_/5/d/csm_wolfgang-e-mueller-geschaeftsfuehrender-gesellschafter-scholpp-dietzenbach_3ad0db6651.jpg"
PDF_ISO = IMG + "fileadmin/user_upload/download/zertifikate/ptc_pressengineering/deutsch/zertifizierung-DIN-ISO-9001-2015-ptc-pressengineering.pdf"
PDF_AEB = IMG + "fileadmin/user_upload/download/dokumente/ptc_pressengineering/deutsch/Allgemeine-Einkaufsbedingungen-PTC-PressEngineering.pdf"

def I(name, cls="icon"):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'

SPRITE = """<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">
  <symbol id="i-wrench" viewBox="0 0 24 24"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></symbol>
  <symbol id="i-shield" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></symbol>
  <symbol id="i-phone" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.37 1.9.72 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.35 1.85.59 2.81.72A2 2 0 0 1 22 16.92z"/></symbol>
  <symbol id="i-mail" viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 7L2 7"/></symbol>
  <symbol id="i-pin" viewBox="0 0 24 24"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></symbol>
  <symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></symbol>
  <symbol id="i-check" viewBox="0 0 24 24"><path d="m5 12 5 5L20 7"/></symbol>
  <symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></symbol>
  <symbol id="i-menu" viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h16"/></symbol>
  <symbol id="i-close" viewBox="0 0 24 24"><path d="M18 6 6 18M6 6l12 12"/></symbol>
  <symbol id="i-users" viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></symbol>
  <symbol id="i-calendar" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></symbol>
  <symbol id="i-info" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></symbol>
  <symbol id="i-gauge" viewBox="0 0 24 24"><path d="m12 14 4-4"/><path d="M3.34 19a10 10 0 1 1 17.32 0"/></symbol>
  <symbol id="i-bolt" viewBox="0 0 24 24"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/></symbol>
  <symbol id="i-truck" viewBox="0 0 24 24"><path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M15 18H9"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.62l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/></symbol>
  <symbol id="i-press" viewBox="0 0 24 24"><path d="M4 3h16M12 3v5"/><rect x="7" y="8" width="10" height="5" rx="1"/><path d="M9 13v3M15 13v3"/><rect x="3" y="16" width="18" height="5" rx="1"/></symbol>
  <symbol id="i-robot" viewBox="0 0 24 24"><path d="M4 21h8"/><path d="M8 21v-5l6-7"/><circle cx="15" cy="8" r="2.5"/><path d="m17 6.5 3-2.5"/><path d="M20 4h1v3"/><circle cx="8" cy="16" r="1.5"/></symbol>
  <symbol id="i-line" viewBox="0 0 24 24"><path d="M2 17h20"/><rect x="4" y="11" width="5" height="6" rx="1"/><rect x="14" y="9" width="6" height="8" rx="1"/><path d="M6.5 11V7h5v10"/><path d="M11.5 7h2"/><circle cx="6" cy="20" r="1"/><circle cx="12" cy="20" r="1"/><circle cx="18" cy="20" r="1"/></symbol>
  <symbol id="i-cog" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/></symbol>
  <symbol id="i-file" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M12 18v-6M9 15l3 3 3-3"/></symbol>
  <symbol id="i-award" viewBox="0 0 24 24"><circle cx="12" cy="8" r="6"/><path d="M15.5 13 17 22l-5-3-5 3 1.5-9"/></symbol>
  <symbol id="i-globe" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></symbol>
  <symbol id="i-chart" viewBox="0 0 24 24"><path d="M3 3v18h18"/><path d="m7 15 4-5 4 3 5-7"/></symbol>
  <symbol id="i-layers" viewBox="0 0 24 24"><path d="m12 2 10 5-10 5L2 7z"/><path d="m2 12 10 5 10-5"/><path d="m2 17 10 5 10-5"/></symbol>
  <symbol id="i-cpu" viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M20 9h3M20 14h3M1 9h3M1 14h3"/></symbol>
  <symbol id="i-search" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></symbol>
  <symbol id="i-flag" viewBox="0 0 24 24"><path d="M4 22V4"/><path d="M4 4h12l-2 4 2 4H4"/></symbol>
  <symbol id="i-briefcase" viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/><path d="M2 13h20"/></symbol>
  <symbol id="i-external" viewBox="0 0 24 24"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><path d="M15 3h6v6"/><path d="M10 14 21 3"/></symbol>
  <symbol id="i-printer" viewBox="0 0 24 24"><path d="M6 9V2h12v7"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></symbol>
</svg>"""

NAV = [("unternehmen.html", "Unternehmen", {"unternehmen", "geschichte", "managementboard", "zertifikate-dokumente", "scholpp-gruppe"}),
       ("leistungsspektrum.html", "Leistungen", {"leistungsspektrum", "pressen-und-bandanlagen", "flexible-montagelinien", "robotik"}),
       ("referenzen.html", "Referenzen", {"referenzen"}),
       ("karriere.html", "Karriere", {"karriere"}),
       ("news.html", "News", {"news"}),
       ("kontakt.html", "Kontakt", {"kontakt"})]

def nav_links(active):
    return "".join(f'<a href="{h}"{" aria-current=\"page\"" if active in keys else ""}>{t}</a>' for h, t, keys in NAV)

def head(title, desc, map_=False):
    leaflet = '\n  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="anonymous">' if map_ else ""
    return f"""<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#E2001A">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23E2001A'/%3E%3Cpath d='M7 8h18M16 8v5M11 13h10v4H11zM13 17v3M19 17v3M7 20h18v4H7z' fill='none' stroke='white' stroke-width='2.2' stroke-linejoin='round'/%3E%3C/svg%3E">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Barlow:wght@400;500;600&display=swap" rel="stylesheet">{leaflet}
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip-link" href="#main">Zum Inhalt springen</a>
{SPRITE}
<div class="topbar">
  <div class="container">
    <div class="topbar__left">
      <span>{I("pin")} {ADDR_1} · {ADDR_2}</span>
      <span>{I("layers")} Teil der SCHOLPP Gruppe</span>
    </div>
    <div class="topbar__right">
      <a href="tel:{TEL}">{I("phone")} {PHONE}</a>
    </div>
  </div>
</div>
<header class="nav">
  <div class="container">
    <a class="brand" href="index.html" aria-label="PTC PressEngineering – Startseite"><img src="assets/logo-ptc.png" alt="PTC PressEngineering – SCHOLPP Group" width="975" height="195"></a>
    <nav class="nav__links" aria-label="Hauptnavigation">__NAV__</nav>
    <div class="nav__actions">
      <a class="btn btn--primary btn--sm" href="kontakt.html#anfrage">Anfrage senden</a>
      <button class="icon-btn nav__burger" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="Menü öffnen">
        <span class="i-open">{I("menu")}</span><span class="i-close" style="display:none">{I("close")}</span>
      </button>
    </div>
  </div>
</header>
<div class="mobile-menu" id="mobile-menu">
  <a href="index.html">Start</a>__NAV__
  <div class="btn-row">
    <a class="btn btn--primary" href="kontakt.html#anfrage">Anfrage senden</a>
    <a class="btn btn--ghost" href="tel:{TEL}">{I("phone")} {PHONE}</a>
  </div>
</div>
<main id="main">
"""

def foot(map_=False):
    leaflet = '<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin="anonymous"></script>\n' if map_ else ""
    return f"""
</main>
<footer class="footer" id="footer">
  <div class="container">
    <div class="footer__grid">
      <div class="footer__brand">
        <img src="assets/logo-ptc.png" alt="PTC PressEngineering – SCHOLPP Group" width="975" height="195">
        <p>Wartung, Modernisierung, Leistungsverbesserung und Zertifizierung von Pressen, Bandanlagen, Montagelinien und Roboteranlagen. Teil der SCHOLPP Gruppe.</p>
      </div>
      <div>
        <h3>Seiten</h3>
        <ul>
          <li><a href="unternehmen.html">Unternehmen</a></li>
          <li><a href="leistungsspektrum.html">Leistungsspektrum</a></li>
          <li><a href="referenzen.html">Referenzen</a></li>
          <li><a href="karriere.html">Karriere</a></li>
          <li><a href="news.html">News</a></li>
          <li><a href="kontakt.html">Kontakt &amp; Anfahrt</a></li>
        </ul>
      </div>
      <div>
        <h3>Rechtliches</h3>
        <ul>
          <li><a href="impressum.html">Impressum</a></li>
          <li><a href="datenschutz.html">Datenschutz</a></li>
          <li><a href="zertifikate-dokumente.html">Zertifikate / Dokumente</a></li>
          <li><a href="https://www.scholpp.de" target="_blank" rel="noopener">SCHOLPP Gruppe {I("external", "icon icon--sm")}</a></li>
        </ul>
      </div>
      <div>
        <h3>Kontakt</h3>
        <ul>
          <li>PTC PressEngineering GmbH<br>{ADDR_1}<br>{ADDR_2}</li>
          <li>Zentrale: <a href="tel:{TEL}">{PHONE}</a></li>
          <li>Service-Hotline: <a href="tel:{TEL_H}">{HOTLINE}</a></li>
          <li>Fax: {FAX}</li>
          <li><a href="mailto:{MAIL}">{MAIL}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© <span data-year>2026</span> PTC PressEngineering GmbH · SCHOLPP Unternehmensgruppe. Alle Rechte vorbehalten.</span>
      <span>Registergericht Duisburg, HRB 13437 · USt-IdNr. DE 212722514</span>
    </div>
  </div>
</footer>
<div class="sticky-cta" aria-label="Schnellkontakt">
  <a href="tel:{TEL}">{I("phone")} Anrufen</a>
  <a class="is-brand" href="kontakt.html#anfrage">{I("mail")} Anfrage</a>
</div>
{leaflet}<script src="assets/site.js"></script>
</body>
</html>
"""

def page(name, title, desc, body, map_=False):
    html = head(title, desc, map_).replace("__NAV__", nav_links(name)) + body + foot(map_)
    with open(os.path.join(OUT, name + ".html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name + ".html", len(html))

def page_head(eyebrow, h1, lead, img=None, alt="", subnav=None, buttons=None):
    media = f'<div class="page-head__media"><img src="{img}" alt="{alt}" width="900" height="600"></div>' if img else ""
    cls = "page-head" if img else "page-head page-head--plain"
    sub = ""
    if subnav:
        sub = '<nav class="sub-nav" aria-label="Unternavigation">' + "".join(
            f'<a href="{h}"{" aria-current=\"page\"" if cur else ""}>{t}</a>' for h, t, cur in subnav) + "</nav>"
    btn = f'<div class="btn-row" style="margin-top:28px">{buttons}</div>' if buttons else ""
    return f"""
<section class="{cls}">
  {media}
  <div class="container">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    {f'<p class="lead">{lead}</p>' if lead else ''}
    {btn}
    {sub}
  </div>
</section>
"""

def subnav_unternehmen(cur):
    items = [("unternehmen.html", "Überblick", "unternehmen"), ("managementboard.html", "Managementboard", "managementboard"),
             ("geschichte.html", "Geschichte", "geschichte"), ("zertifikate-dokumente.html", "Zertifikate / Dokumente", "zertifikate-dokumente"),
             ("scholpp-gruppe.html", "SCHOLPP Gruppe", "scholpp-gruppe")]
    return [(h, t, k == cur) for h, t, k in items]

def subnav_leistungen(cur):
    items = [("leistungsspektrum.html", "Überblick", "leistungsspektrum"), ("pressen-und-bandanlagen.html", "Pressen und Bandanlagen", "pressen-und-bandanlagen"),
             ("flexible-montagelinien.html", "Flexible Montagelinien", "flexible-montagelinien"), ("robotik.html", "Robotik", "robotik")]
    return [(h, t, k == cur) for h, t, k in items]

def checks(items):
    return '<ul class="checks">' + "".join(f'<li>{I("check")} <span>{t}</span></li>' for t in items) + "</ul>"

def chips(items, label):
    return f'<ul class="chips" aria-label="{label}">' + "".join(f'<li>{I("check")} {t}</li>' for t in items) + "</ul>"

CTA_BOX = f"""
<section class="section" id="kontakt-cta">
  <div class="container">
    <div class="cta-box">
      <p class="eyebrow" style="justify-content:center">Kontakt</p>
      <h2>Was können wir für Sie tun?</h2>
      <p class="lead">Rufen Sie an, schreiben Sie uns oder nutzen Sie das Kontaktformular. Wir besprechen Ihr Vorhaben und schlagen einen Termin für den Pressencheck oder ein erstes Gespräch vor Ort vor.</p>
      <ul class="facts">
        <li>{I("check")} Zentrale Oberhausen: {PHONE}</li>
        <li>{I("check")} Service-Hotline: {HOTLINE}</li>
        <li>{I("check")} E-Mail: {MAIL}</li>
      </ul>
      <div class="btn-row">
        <a class="btn btn--primary" href="tel:{TEL}">{I("phone")} Anrufen</a>
        <a class="btn btn--ghost" href="kontakt.html#anfrage">{I("mail")} Zum Kontaktformular</a>
        <a class="btn btn--ghost" href="mailto:{MAIL}">{I("mail")} E-Mail schreiben</a>
      </div>
    </div>
  </div>
</section>
"""

def location_section(light=True, headline="So finden Sie uns", lead=""):
    return f"""
<section class="section{' section--light' if light else ''}" id="standort">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Standort</p>
      <h2>{headline}</h2>{f'<p class="lead">{lead}</p>' if lead else ''}
    </div>
    <div class="location">
      <div class="location__info">
        <div class="info-card">
          <h3>{I("pin")} Adresse</h3>
          <p>PTC PressEngineering GmbH<br>{ADDR_1}<br>{ADDR_2}</p>
          <p class="muted" style="margin-top:10px">Essener Straße in Alt-Oberhausen, zwischen Innenstadt und Neuer Mitte. Anbindung über A 42 und A 3.</p>
          <div class="btn-row" style="margin-top:18px">
            <a class="btn btn--primary btn--sm" href="https://www.google.com/maps/dir/?api=1&destination=Essener+Str.+59,+46047+Oberhausen" target="_blank" rel="noopener">Route planen {I("arrow")}</a>
          </div>
        </div>
        <div class="info-card">
          <h3>{I("phone")} Erreichbarkeit</h3>
          <p>Zentrale: <a href="tel:{TEL}">{PHONE}</a><br>Service-Hotline: <a href="tel:{TEL_H}">{HOTLINE}</a><br>Fax: {FAX}<br><a href="mailto:{MAIL}">{MAIL}</a></p>
          <!-- TODO: Bürozeiten vom Kunden erfragen; auf ptc.eu sind keine Öffnungszeiten angegeben. -->
          <p class="muted" style="margin-top:12px;font-size:.92rem">Bürozeiten: <span class="todo">vom Kunden ergänzen</span></p>
        </div>
        <div class="info-card">
          <h3>{I("layers")} SCHOLPP Gruppe</h3>
          <p class="muted">Verlagerung durch SCHOLPP, Modernisierung durch PTC: beides aus einer Hand. Niederlassungen der SCHOLPP GmbH in Dietzenbach, Leonberg, Chemnitz, Berlin, Jena, Dresden und Rostock.</p>
        </div>
      </div>
      <div class="map" id="map" data-lat="{LAT}" data-lng="{LNG}" data-zoom="15" data-title="PTC PressEngineering GmbH" data-address="{ADDR_1}&lt;br&gt;{ADDR_2}" aria-label="Karte: {ADDR_1}, Oberhausen"></div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- Startseite
index_body = f"""
<section class="hero">
  <div class="hero__media"><img src="{HERO_IMG}" alt="" width="1920" height="1080" fetchpriority="high"></div>
  <span class="hero__badge">{I("layers")} Teil der SCHOLPP Gruppe</span>
  <div class="container">
    <h1 class="is-long"><span class="line">Ihre Maschinen</span><span class="line">in den besten</span><span class="line line--accent">Händen.</span></h1>
    <p class="lead">PTC PressEngineering aus Oberhausen ist Ihre Adresse für Wartung, Modernisierung, Leistungsverbesserung und Zertifizierung von Pressen, Bandanlagen, Montagelinien und Roboteranlagen. Mit der SCHOLPP Gruppe: Verlagerung und Retrofit von der einzelnen Maschine bis zur Produktionsstraße aus einer Hand.</p>
    <div class="btn-row">
      <a class="btn btn--primary" href="kontakt.html#anfrage">{I("mail")} Anfrage senden <span class="hint">Antwort per Telefon oder E-Mail</span></a>
      <a class="btn btn--ghost" href="tel:{TEL}">{I("phone")} {PHONE}</a>
    </div>
    <ul class="trust">
      <li>{I("flag")} <span><strong>Seit 2000</strong> Pressen-Know-how mit Wurzeln bei Krupp</span></li>
      <li>{I("users")} <span><strong>Über 50</strong> Ingenieure, Techniker und Monteure</span></li>
      <li>{I("award")} <span><strong>DIN ISO 9001</strong> zertifiziertes Qualitätsmanagement</span></li>
      <li>{I("globe")} <span><strong>SCHOLPP Gruppe</strong> über 700 Mitarbeiter, 50 Länder</span></li>
    </ul>
  </div>
</section>

<section class="section" id="leistungen">
  <div class="container">
    <div class="section-head section-head--center">
      <p class="eyebrow">Leistungsspektrum</p>
      <h2>Engineering, Modernisierung und Automatisierung</h2>
      <p class="lead">Wir finden mit Ihnen technische Lösungen, die hohe Anlagenverfügbarkeit garantieren und gleichzeitig Kosten und Sicherheit im Blick behalten.</p>
    </div>
    <div class="cards">
      <a class="card" href="pressen-und-bandanlagen.html#pressencheck">
        <span class="card__icon">{I("search")}</span>
        <h3>Pressencheck &amp; Instandhaltung</h3>
        <p>Alle Baugruppen prüfen, Einzel- und Gesamtspiele messen, Funktions- und Sichtprüfung. Daraus entsteht ein detaillierter Maßnahmenkatalog.</p>
        <span class="card__meta">Ist-Zustand als Basis {I("arrow")}</span>
      </a>
      <a class="card" href="pressen-und-bandanlagen.html#modernisierung">
        <span class="card__icon">{I("press")}</span>
        <h3>Retrofit &amp; Modernisierung</h3>
        <p>Neukonstruktion von Mechanik, Hydraulik, Pneumatik und Elektrik, neue Steuerungstechnik, Verschleißteiltausch und eigene Ersatzteilfertigung.</p>
        <span class="card__meta">Bis zu 85 % einer Neumaschine {I("arrow")}</span>
      </a>
      <a class="card" href="pressen-und-bandanlagen.html#bandanlagen">
        <span class="card__icon">{I("cog")}</span>
        <h3>Retrofit von Bandanlagen</h3>
        <p>Aufrüstung und Anpassung an neue Applikationen Ihrer Fertigung mit modernsten Steuerungen. Kostengünstiger als eine Neuanschaffung.</p>
        <span class="card__meta">Pressen und Bandanlagen {I("arrow")}</span>
      </a>
      <a class="card" href="flexible-montagelinien.html">
        <span class="card__icon">{I("line")}</span>
        <h3>Flexible Montagelinien</h3>
        <p>Verkettung der Prozessschritte zu einem Anlagenkonzept, Umbau auf neue Produktderivate, Integration in Leitsysteme, Taktzeituntersuchung.</p>
        <span class="card__meta">Montageautomation {I("arrow")}</span>
      </a>
      <a class="card" href="robotik.html">
        <span class="card__icon">{I("robot")}</span>
        <h3>Robotik &amp; Automatisierung</h3>
        <p>Inbetriebnahme von Roboteranlagen aller gängigen Hersteller, SPS- und Roboterprogrammierung, Simulation, Taktzeitoptimierung.</p>
        <span class="card__meta">Automatisierungskonzepte {I("arrow")}</span>
      </a>
      <a class="card" href="pressen-und-bandanlagen.html#sicherheit">
        <span class="card__icon">{I("shield")}</span>
        <h3>Sicherheit &amp; Zertifizierung</h3>
        <p>CE-Zertifizierung, Performance Level nach EN ISO 13849-1, Prüfungen nach BGI/GUV-I 724 und Betriebssicherheitsverordnung, Risikobeurteilung.</p>
        <span class="card__meta">Unabhängig vom Maschinentyp {I("arrow")}</span>
      </a>
    </div>
    <div class="tip">
      {I("truck")}
      <p><strong>Verlagerung geplant?</strong> Wer Maschinen mit SCHOLPP verlagert, bekommt die Modernisierung von PTC gleich dazu. Umgekehrt bestellen Sie zur Modernisierung die Verlagerung einfach mit. Ein günstigerer Zeitpunkt für beides kommt selten.</p>
    </div>
  </div>
</section>

<section class="section section--light" id="refurbishment">
  <div class="container">
    <div class="split">
      <div>
        <p class="eyebrow">Refurbishment</p>
        <h2>85 % der Leistung einer neuen Presse. Für rund 30 % der Kosten.</h2>
        <p class="lead">Vom einzelnen Bauteil bis zur kompletten Baugruppe: Wir konstruieren mechanische, pneumatische, hydraulische und elektrische Komponenten neu und legen sie besser aus. Neue Steuerungstechnik, getauschte Verschleißteile und optimierte Getriebe verlängern den Lebenszyklus Ihrer Maschine.</p>
        {checks(["Leistungserhöhung auf bis zu 85 % einer fabrikneuen Presse", "Refurbishment-Kosten bei etwa 30 % einer Neuanschaffung", "Ersatzteile für alle Maschinentypen, bei Bedarf aus eigener Fertigung", "Verbesserter Kühl- und Schmiermittel-Service, optimierte Getriebe"])}
        <div class="btn-row">
          <a class="btn btn--primary" href="pressen-und-bandanlagen.html">Pressen und Bandanlagen {I("arrow")}</a>
          <a class="btn btn--ghost" href="kontakt.html#anfrage">Pressencheck anfragen</a>
        </div>
      </div>
      <div class="split__media">
        <img src="{IMG_PRESSEN}" alt="Techniker bei der Instandhaltung einer Presse" width="900" height="600" loading="lazy">
        <span class="tag">Pressen &amp; Bandanlagen</span>
      </div>
    </div>
  </div>
</section>

<section class="section" id="automatisierung">
  <div class="container">
    <div class="split split--reverse">
      <div>
        <p class="eyebrow">Montagelinien &amp; Robotik</p>
        <h2>Kompetenzzentrum für vernetzte Produktionssysteme</h2>
        <p class="lead">Seit der Integration der Bratz Engineering GmbH im Jahr 2015 verketten wir Montagelinien, binden Anlagen in Leitsysteme ein und automatisieren Prozessketten mit Industrierobotern. Digitalisierung, Automatisierung und Verkettung auf allen Prozessebenen.</p>
        {chips(["Anlagenkonzepte", "Umbau auf Produktderivate", "Leitsystem-Integration", "Kamera- und Prüfsysteme", "Taktzeituntersuchung", "Visualisierung", "Roboterinbetriebnahme", "SPS-Programmierung", "Simulation und Test"], "Leistungen Automatisierung")}
        <div class="btn-row">
          <a class="btn btn--primary" href="flexible-montagelinien.html">Montagelinien {I("arrow")}</a>
          <a class="btn btn--ghost" href="robotik.html">Robotik {I("arrow")}</a>
        </div>
      </div>
      <div class="split__media">
        <img src="{IMG_ROBOTIK}" alt="Industrieroboter in einer automatisierten Fertigung" width="900" height="600" loading="lazy">
        <span class="tag tag--bottom">Roboter verschiedenster Hersteller</span>
      </div>
    </div>
  </div>
</section>

<section class="section section--surface" id="scholpp">
  <div class="container">
    <div class="split">
      <div class="split__media">
        <img src="{IMG_NEWS_3}" alt="Montage einer Pressenanlage in einer Werkhalle" width="900" height="600" loading="lazy">
        <span class="tag">SCHOLPP Gruppe</span>
      </div>
      <div>
        <p class="eyebrow">Gemeinsam stark</p>
        <h2>Verlagern, modernisieren, wieder anfahren. Aus einer Hand.</h2>
        <p class="lead">Seit 2012 gehört PTC PressEngineering zur SCHOLPP Gruppe, dem führenden Dienstleister für Verlagerung und Montage von Industrieanlagen. Über 700 Mitarbeiter an sieben deutschen und vier internationalen Standorten, nahezu 20.000 Transport- und Montageleistungen pro Jahr.</p>
        {checks(["Demontage, Zwischenlagerung, Remontage und Inbetriebnahme durch SCHOLPP", "Überholung und Modernisierung während der Zwischenlagerung durch PTC", "Ein Ansprechpartner für Transport, Montage und Technik"])}
        <div class="btn-row">
          <a class="btn btn--primary" href="scholpp-gruppe.html">Die SCHOLPP Gruppe {I("arrow")}</a>
          <a class="btn btn--ghost" href="referenzen.html#daimler">Projekt Mercedes-Benz Bremen</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="referenzen">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Referenzen</p>
      <h2>Besser machen ist unser Geschäft.</h2>
      <p class="lead">Viele namhafte Kunden verlassen sich auf unser Know-how. Einige Beispiele aus Automotive und Weißer Ware.</p>
    </div>
    <div class="refs">
      <a class="ref" href="referenzen.html#daimler">
        <div class="ref__media"><img src="{IMG_REF_DAIMLER}" alt="Pressenmodernisierung im Mercedes-Benz-Werk Bremen" width="475" height="343" loading="lazy"></div>
        <div class="ref__body"><span class="ref__client">Daimler</span><h3>Pressenverlagerung und -modernisierung</h3><p>800-Tonnen-Einarbeitungspresse im Mercedes-Benz-Werk Bremen</p></div>
      </a>
      <a class="ref" href="referenzen.html#electrolux">
        <div class="ref__media"><img src="{IMG_REF_ELECTROLUX}" alt="Automatisiertes Transfersystem der Pressenstraße bei Electrolux" width="475" height="343" loading="lazy"></div>
        <div class="ref__body"><span class="ref__client">Electrolux</span><h3>Modernisierung einer Pressenstraße</h3><p>Neues Transfersystem mit Platinenlader in drei Wochen Umbauzeit</p></div>
      </a>
      <a class="ref" href="referenzen.html#tryoutpresse">
        <div class="ref__media"><img src="{IMG_REF_TRYOUT}" alt="Hydraulische Tryoutpresse nach der Modernisierung" width="475" height="343" loading="lazy"></div>
        <div class="ref__body"><span class="ref__client">Automotive</span><h3>Modernisierung einer Tryoutpresse</h3><p>2.300-Tonnen-Presse: schneller und mit Sechs-Punkt-Tischkissen</p></div>
      </a>
      <a class="ref" href="referenzen.html#weisse-ware">
        <div class="ref__media"><img src="{IMG_REF_WEISS}" alt="Getriebeinstandsetzung an einer Mossini-Presse" width="475" height="317" loading="lazy"></div>
        <div class="ref__body"><span class="ref__client">Weiße Ware</span><h3>Modernisierte Presse für Premiumhersteller</h3><p>Getriebe einer 12.500-kN-Mossini-Presse komplett instand gesetzt</p></div>
      </a>
    </div>
    <div class="btn-row" style="margin-top:32px">
      <a class="btn btn--ghost" href="referenzen.html">Alle Referenzen {I("arrow")}</a>
    </div>
  </div>
</section>

<section class="section section--surface" id="ablauf">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Ablauf</p>
      <h2>Vom Pressencheck zur Abnahme</h2>
      <p class="lead">Modernisierung planen wir vom Ist-Zustand aus. So wissen Sie vor dem ersten Handgriff, was gemacht wird, wann und mit welchem Ergebnis.</p>
    </div>
    <ol class="steps">
      <li class="step"><span class="step__num">01</span><h3>Pressencheck</h3><p>Unsere Techniker untersuchen alle Baugruppen, messen Einzel- und Gesamtspiele und führen Funktions- und Sichtprüfungen durch.</p></li>
      <li class="step"><span class="step__num">02</span><h3>Maßnahmenkatalog</h3><p>Aus dem Ist-Zustand entsteht ein detaillierter Katalog. Gemeinsam legen wir den optimalen Zeitpunkt für Wartung und Modernisierung fest.</p></li>
      <li class="step"><span class="step__num">03</span><h3>Umsetzung</h3><p>Konstruktion, Fertigung, Umbau und Programmierung aus einem Team. Ersatzteile fertigen wir bei Bedarf selbst, auch in engen Zeitfenstern.</p></li>
      <li class="step"><span class="step__num">04</span><h3>Inbetriebnahme &amp; Abnahme</h3><p>Inbetriebnahme, Sicherheitsabnahme, Schulung Ihrer Mitarbeiter und auf Wunsch CE-Zertifizierung des Umbaus.</p></li>
    </ol>
    <div class="tip">
      {I("shield")}
      <p><strong>Sicherheit inklusive:</strong> Performance Level nach EN ISO 13849-1, Prüfungen nach BGI/GUV-I 724 und Betriebssicherheitsverordnung sowie eine belastbare Risikobeurteilung gehören bei jedem Umbau dazu.</p>
    </div>
  </div>
</section>
{CTA_BOX}
{location_section()}
"""
page("index", "PTC PressEngineering GmbH | Pressen, Bandanlagen, Montagelinien und Robotik aus Oberhausen",
     "PTC PressEngineering aus Oberhausen, Teil der SCHOLPP Gruppe: Wartung, Modernisierung, Leistungsverbesserung und Zertifizierung von Pressen, Bandanlagen, Montagelinien und Roboteranlagen.",
     index_body, map_=True)

# ---------------------------------------------------------------- Unternehmen
unternehmen_body = page_head("Unternehmen", "Gemeinsam stark.",
    "PTC PressEngineering ist Teil der SCHOLPP Gruppe: ein Spezialistenteam für Maschinen der Umformtechnik, seit 2012 in der SCHOLPP Gruppe und seit 2015 verstärkt um die Automatisierungskompetenz der Bratz Engineering.",
    IMG_NEWS_2, "Werkhalle mit Pressenanlage", subnav_unternehmen("unternehmen")) + f"""
<section class="section">
  <div class="container">
    <div class="split">
      <div>
        <p class="eyebrow">Wer wir sind</p>
        <h2>Von sechs Mitarbeitern auf über fünfzig</h2>
        <p class="lead">Im Jahr 2000 startete PTC PressEngineering mit einem Team aus sechs Mitarbeitern rund um Gründer Dr. Jürgen Pielen. Heute ist das Unternehmen auf über 50 Mitarbeiter gewachsen.</p>
        <p style="margin-top:18px;color:var(--muted)">Hinter PTC steht ein Spezialistenteam für Maschinen der Umformtechnik. Profitieren Sie von seiner Erfahrung in Konstruktion, Neubau und Überholung von Maschinen für die Blech- und Massivumformung sowie für die Verarbeitung glasfaserverstärkter Kunststoffe.</p>
        <p style="margin-top:14px;color:var(--muted)">Im Juni 2015 wurde die Bratz Engineering GmbH in die PTC PressEngineering GmbH integriert. Neue Schwerpunkte sind seitdem flexible Montagelinien zur Automatisierung von Anlagen, deren mechanische oder elektronische Umrüstung sowie Robotik und Roboterautomatisierungsanlagen.</p>
        <div class="btn-row">
          <a class="btn btn--primary" href="geschichte.html">Unsere Geschichte {I("arrow")}</a>
          <a class="btn btn--ghost" href="leistungsspektrum.html">Leistungsspektrum</a>
        </div>
      </div>
      <div class="split__media">
        <img src="{IMG_PRESSEN}" alt="PTC-Techniker an einer Presse" width="900" height="600" loading="lazy">
        <span class="tag">Umformtechnik seit 2000</span>
      </div>
    </div>
  </div>
</section>

<section class="section section--light">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Zahlen</p>
      <h2>PTC und SCHOLPP auf einen Blick</h2>
    </div>
    <ul class="stats">
      <li><strong>2000</strong><span>Gründung der PTC, Wurzeln bei Krupp seit den 1980er Jahren</span></li>
      <li><strong>50+</strong><span>Ingenieure, Techniker und Monteure in Mechanik, Hydraulik, Steuerungstechnik und Robotik</span></li>
      <li><strong>700+</strong><span>Mitarbeiter in der SCHOLPP Gruppe an elf Standorten weltweit</span></li>
      <li><strong>9001</strong><span>Qualitätsmanagement zertifiziert nach DIN ISO 9001</span></li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Aus einer Hand</p>
      <h2>Verlagerung und Modernisierung kombinieren</h2>
      <p class="lead">Als Teil der SCHOLPP Gruppe kann PTC seine Expertise mit anderen Dienstleistungen von SCHOLPP kombinieren. Wer Maschinen mit SCHOLPP verlagert, erhält die Modernisierung aus einer Hand. Wer mit PTC modernisiert, bestellt eine erforderliche Verlagerung gleich mit. Denn wenn ohnehin Veränderungen anstehen, ist das auch ein günstiger Zeitpunkt für die Modernisierung.</p>
    </div>
    <div class="cards cards--4">
      <a class="card" href="managementboard.html"><span class="card__icon">{I("users")}</span><h3>Managementboard</h3><p>Wer die PTC PressEngineering GmbH und die SCHOLPP Holding führt.</p><span class="card__meta">Mehr {I("arrow")}</span></a>
      <a class="card" href="geschichte.html"><span class="card__icon">{I("flag")}</span><h3>Geschichte</h3><p>Von Krupp über Erfurt Krupp Umformtechnik zur PTC in der SCHOLPP Gruppe.</p><span class="card__meta">Zeitleiste {I("arrow")}</span></a>
      <a class="card" href="zertifikate-dokumente.html"><span class="card__icon">{I("award")}</span><h3>Zertifikate / Dokumente</h3><p>DIN ISO 9001-Zertifikat und Allgemeine Einkaufsbedingungen als PDF.</p><span class="card__meta">Downloads {I("arrow")}</span></a>
      <a class="card" href="scholpp-gruppe.html"><span class="card__icon">{I("globe")}</span><h3>SCHOLPP Gruppe</h3><p>Marktführer für weltweite Industriemontagen mit über 700 Mitarbeitern.</p><span class="card__meta">Die Gruppe {I("arrow")}</span></a>
    </div>
  </div>
</section>
{CTA_BOX}
"""
page("unternehmen", "Unternehmen | PTC PressEngineering GmbH, Oberhausen",
     "PTC PressEngineering: Spezialistenteam für Maschinen der Umformtechnik, gegründet 2000, seit 2012 Teil der SCHOLPP Gruppe, über 50 Mitarbeiter in Oberhausen.", unternehmen_body)

# ---------------------------------------------------------------- Managementboard
management_body = page_head("Unternehmen", "Wir wissen, wovon wir sprechen.",
    "Das Managementboard der PTC PressEngineering GmbH.", IMG_NEWS_1, "Pressenanlage", subnav_unternehmen("managementboard")) + f"""
<section class="section">
  <div class="container">
    <article class="person">
      <div class="person__media"><img src="{IMG_MUELLER}" alt="Wolfgang E. Mueller, Geschäftsführender Gesellschafter der SCHOLPP Holding GmbH" width="350" height="195" loading="lazy"></div>
      <div>
        <h2>Wolfgang E. Mueller</h2>
        <p class="role">Geschäftsführender Gesellschafter · SCHOLPP Holding GmbH</p>
        <p>Wolfgang E. Mueller wurde 1951 in Frankfurt am Main geboren. Seine berufliche Laufbahn begann er mit dem Studium der Betriebswirtschaft. 13 Jahre lang war Mueller Vorsitzender des Vorstandes der DIW Deutsche Industriewartung AG, Stuttgart, einer Beteiligung von Salamander.</p>
        <p>1997 wurde Mueller in den Vorstand der Salamander AG Kornwestheim berufen, wo er zuletzt die Position des Vorsitzenden des Vorstandes innehatte. 2004 wechselte er als Geschäftsführender Gesellschafter in die SCHOLPP Dienstleistungsgruppe. SCHOLPP erzielte zu diesem Zeitpunkt einen Umsatz von 50 Mio. Euro.</p>
        <p>Durch die Entwicklung zum weltweiten Montagedienstleister und den Einsatz eines professionellen Managements gelang es ihm und seinen Mitarbeitern, heute einen Umsatz von 135 Mio. Euro zu erzielen.</p>
      </div>
    </article>
    <!-- TODO: Weitere Mitglieder des Managementboards (z. B. Geschäftsführung der PTC vor Ort) beim Kunden erfragen; ptc.eu nennt nur Wolfgang E. Mueller. -->
    <div class="tip" style="margin-top:32px">
      {I("info")}
      <p><strong>Hinweis für die Freigabe:</strong> ptc.eu nennt im Managementboard aktuell nur Wolfgang E. Mueller. Weitere Personen, Foto in höherer Auflösung und Kontaktdaten bitte beim Kunden anfordern. <span class="todo">Platzhalter</span></p>
    </div>
  </div>
</section>
{CTA_BOX}
"""
page("managementboard", "Managementboard | PTC PressEngineering GmbH",
     "Das Managementboard der PTC PressEngineering GmbH: Wolfgang E. Mueller, Geschäftsführender Gesellschafter der SCHOLPP Holding GmbH.", management_body)

# ---------------------------------------------------------------- Geschichte
geschichte_body = page_head("Unternehmen", "Modernisierung hat bei uns Tradition.",
    "Das Team der PTC PressEngineering blickt auf jahrzehntelange Erfahrung in Wartung, Modernisierung, Leistungsverbesserung und Zertifizierung von Pressen zur Metallbearbeitung zurück.",
    IMG_NEWS_3, "Montage einer Pressenanlage", subnav_unternehmen("geschichte")) + f"""
<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Zeitleiste</p>
      <h2>Von Krupp zur SCHOLPP Gruppe</h2>
    </div>
    <ol class="timeline">
      <li><time>1980er</time><h3>Pressenbau bei der Friedrich Krupp AG</h3><p>Der harte Kern unserer Experten baut Pressen und bietet Serviceleistungen im Bereich der Umformtechnik an, noch als Teil der Friedrich Krupp AG.</p></li>
      <li><time>1990er</time><h3>Erfurt Krupp Umformtechnik</h3><p>Die Aktivitäten werden unter dem Namen Erfurt Krupp Umformtechnik fortgesetzt.</p></li>
      <li><time>2000</time><h3>Gründung der PTC</h3><p>PTC PressEngineering startet mit sechs Mitarbeitern rund um Gründer Dr. Jürgen Pielen in Oberhausen. Seither wächst das Unternehmen kontinuierlich.</p></li>
      <li><time>2012</time><h3>Teil der SCHOLPP Gruppe</h3><p>Die PTC PressEngineering GmbH wird Teil der SCHOLPP Gruppe, Spezialist für weltweite Industriemontagen. Verlagerung und Modernisierung kommen seitdem aus einer Hand.</p></li>
      <li><time>2015</time><h3>Integration der Bratz Engineering GmbH</h3><p>Im Juni 2015 wird die Bratz Engineering GmbH integriert. Neue Schwerpunkte: flexible Montagelinien, elektrische und mechanische Umrüstung sowie Robotik. Alle Arbeitsplätze werden gesichert; mehr als 50 Ingenieure, Techniker und Monteure stehen in Mechanik, Hydraulik, Steuerungstechnik und Robotik zur Verfügung.</p></li>
      <li><time>Heute</time><h3>Komplettanbieter aus einer Hand</h3><p>Der Zusammenschluss erlaubt es, das Leistungsspektrum weiter auszubauen und sämtliche Kundenwünsche rund um Pressen, Bandanlagen, Montagelinien und Roboteranlagen als Komplettanbieter zu erfüllen.</p></li>
    </ol>
  </div>
</section>
<section class="section section--light">
  <div class="container">
    <div class="split">
      <div>
        <p class="eyebrow">News 2015</p>
        <h2>Die Fusion mit Bratz Engineering</h2>
        <p class="lead">„Die PTC und Bratz verbindet seit vielen Jahren eine kooperative Zusammenarbeit. Durch die Fusion werden die Kompetenzen beider Unternehmen optimal zusammengeführt“, so Lars Gerlach, Geschäftsführer SCHOLPP, im Juni 2015.</p>
        <div class="btn-row"><a class="btn btn--primary" href="news.html#fusion">Zur Meldung {I("arrow")}</a></div>
      </div>
      <div class="split__media"><img src="{IMG_NEWS_1}" alt="Pressenanlage in der Werkhalle" width="900" height="600" loading="lazy"><span class="tag">Juni 2015</span></div>
    </div>
  </div>
</section>
{CTA_BOX}
"""
page("geschichte", "Geschichte | PTC PressEngineering GmbH",
     "Die Geschichte der PTC PressEngineering: Pressenbau bei Krupp seit den 1980ern, Gründung 2000, SCHOLPP Gruppe seit 2012, Integration der Bratz Engineering 2015.", geschichte_body)

# ---------------------------------------------------------------- Zertifikate
zert_body = page_head("Unternehmen", "Zertifikate und Dokumente",
    "Qualitätsmanagement nach DIN ISO 9001 und unsere Allgemeinen Einkaufsbedingungen zum Herunterladen.", None, "", subnav_unternehmen("zertifikate-dokumente")) + f"""
<section class="section section--tight">
  <div class="container">
    <div class="cards cards--2">
      <div class="card">
        <span class="card__icon">{I("award")}</span>
        <h3>Qualitätsmanagement</h3>
        <p>Die PTC PressEngineering GmbH ist nach DIN ISO 9001 zertifiziert. Das Zertifikat können Sie hier herunterladen.</p>
        <div class="downloads" style="margin-top:18px">
          <a class="download" href="{PDF_ISO}" target="_blank" rel="noopener">{I("file")}<span><strong>Zertifizierung nach DIN ISO 9001</strong><small>PTC PressEngineering GmbH</small></span><span class="download__meta">PDF · 268 KB</span></a>
        </div>
      </div>
      <div class="card">
        <span class="card__icon">{I("briefcase")}</span>
        <h3>Unternehmen</h3>
        <p>Unsere Allgemeinen Einkaufsbedingungen für Lieferanten und Dienstleister.</p>
        <div class="downloads" style="margin-top:18px">
          <a class="download" href="{PDF_AEB}" target="_blank" rel="noopener">{I("file")}<span><strong>Allgemeine Einkaufsbedingungen</strong><small>PTC PressEngineering GmbH</small></span><span class="download__meta">PDF · 58 KB</span></a>
        </div>
      </div>
    </div>
    <!-- Die PDFs sind Hotlinks auf ptc.eu. Vor dem Livegang lokal unter assets/downloads/ ablegen. -->
    <div class="tip" style="margin-top:32px">
      {I("info")}
      <p><strong>Dokumente:</strong> Die PDFs verlinken aktuell auf die bestehende Website ptc.eu. Für den Livegang lokal ablegen. <span class="todo">Platzhalter</span></p>
    </div>
  </div>
</section>
<section class="section section--light">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Sicherheit &amp; Zertifizierung</p>
      <h2>Zertifizierung ist auch eine Leistung für Ihre Maschinen</h2>
      <p class="lead">Unabhängig vom Maschinentyp erbringen wir Leistungen rund um Sicherheit und Zertifizierung Ihrer Anlagen.</p>
    </div>
    {checks(["CE-Zertifizierungen", "Performance Level gemäß EN ISO 13849-1", "Prüfungen nach BGI/GUV-I 724", "Prüfung von Arbeitsmitteln nach Betriebssicherheitsverordnung", "Belastbare Risikobeurteilung von Umbauten"])}
    <div class="btn-row" style="margin-top:28px"><a class="btn btn--primary" href="pressen-und-bandanlagen.html#sicherheit">Mehr zu Sicherheit {I("arrow")}</a></div>
  </div>
</section>
{CTA_BOX}
"""
page("zertifikate-dokumente", "Zertifikate / Dokumente | PTC PressEngineering GmbH",
     "DIN ISO 9001-Zertifikat und Allgemeine Einkaufsbedingungen der PTC PressEngineering GmbH als PDF-Download.", zert_body)

# ---------------------------------------------------------------- SCHOLPP Gruppe
scholpp_body = page_head("Unternehmen", "Wir kümmern uns um Ihre Lasten.",
    "Die SCHOLPP Gruppe ist der führende Dienstleister für die Verlagerung und Montage von Industrieanlagen und Marktführer im Bereich der weltweiten Industriemontagen.",
    IMG_NEWS_3, "Montage einer Industrieanlage", subnav_unternehmen("scholpp-gruppe"),
    buttons=f'<a class="btn btn--primary" href="https://www.scholpp.de" target="_blank" rel="noopener">{I("external")} scholpp.de</a>') + f"""
<section class="section">
  <div class="container">
    <ul class="stats">
      <li><strong>700+</strong><span>Mitarbeiter an sieben deutschen und vier weltweiten Standorten</span></li>
      <li><strong>20.000</strong><span>Transport- und Montageleistungen pro Jahr</span></li>
      <li><strong>50</strong><span>Länder, in denen SCHOLPP bislang im Einsatz war</span></li>
      <li><strong>65+</strong><span>Jahre Erfahrung, gestartet als Kranunternehmen</span></li>
    </ul>
  </div>
</section>
<section class="section section--light">
  <div class="container">
    <div class="split">
      <div>
        <p class="eyebrow">Die Gruppe</p>
        <h2>Mittelständisch, inhabergeführt, weltweit vor Ort</h2>
        <p class="lead">SCHOLPP hilft seit mehr als 65 Jahren anderen Unternehmen bei ihren Herausforderungen. Gestartet als Kranunternehmen, ist die Gruppe mit zufriedenen Kunden zum internationalen Dienstleister gewachsen und pflegt als mittelständisches, inhabergeführtes Unternehmen eine besondere Nähe zu seinen Kunden.</p>
        <p style="margin-top:16px;color:var(--muted)">Maschinenverlagerungen und Industriemontagen übernimmt die SCHOLPP GmbH mit ihren deutschen Niederlassungen. Im Ausland ist SCHOLPP ständig vor Ort in Barcelona, Mailand, Kuala Lumpur und Shanghai.</p>
        <h3 style="margin-top:28px;font-size:1.1rem;letter-spacing:.1em;text-transform:uppercase">Standorte Deutschland</h3>
        {chips(["Dietzenbach bei Frankfurt/M.", "Leonberg", "Chemnitz", "Berlin", "Jena", "Dresden", "Rostock"], "Standorte Deutschland")}
        <h3 style="margin-top:22px;font-size:1.1rem;letter-spacing:.1em;text-transform:uppercase">Standorte international</h3>
        {chips(["Barcelona, Spanien", "Mailand, Italien", "Kuala Lumpur, Malaysia", "Shanghai, China"], "Standorte international")}
      </div>
      <div class="split__media">
        <img src="{IMG_NEWS_2}" alt="Industriemontage einer Pressenanlage" width="900" height="600" loading="lazy">
        <span class="tag">Weltweite Industriemontagen</span>
      </div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="split split--reverse">
      <div>
        <p class="eyebrow">PTC in der Gruppe</p>
        <h2>Modernisierung, Wartung und Retrofit für Pressen und andere Maschinen</h2>
        <p class="lead">Die ebenfalls zur SCHOLPP Gruppe gehörende PTC PressEngineering GmbH in Oberhausen erweitert das Leistungsspektrum um Modernisierung, Wartung und Retrofitting/Refurbishment von Pressen und anderen Maschinen. Gemeinsam mit der Bratz Engineering etablierte PTC in der Gruppe ein Kompetenzzentrum für vernetzte Produktionssysteme.</p>
        <div class="btn-row">
          <a class="btn btn--primary" href="leistungsspektrum.html">Leistungsspektrum PTC {I("arrow")}</a>
          <a class="btn btn--ghost" href="referenzen.html#daimler">Gemeinsames Projekt in Bremen</a>
        </div>
      </div>
      <div class="split__media">
        <img src="{IMG_REF_DAIMLER}" alt="Pressenverlagerung und -modernisierung im Mercedes-Benz-Werk Bremen" width="475" height="343" loading="lazy">
        <span class="tag tag--bottom">SCHOLPP verlagert, PTC modernisiert: Mercedes-Benz-Werk Bremen</span>
      </div>
    </div>
  </div>
</section>
{CTA_BOX}
"""
page("scholpp-gruppe", "SCHOLPP Gruppe | PTC PressEngineering GmbH",
     "Die SCHOLPP Gruppe: über 700 Mitarbeiter, elf Standorte, nahezu 20.000 Transport- und Montageleistungen pro Jahr. PTC PressEngineering erweitert das Spektrum um Modernisierung und Retrofit.", scholpp_body)

# ---------------------------------------------------------------- Leistungsspektrum
def service_block(id_, img, alt, eyebrow, h2, lead, facts, href, reverse=False):
    return f"""
<article class="service" id="{id_}">
  <div class="service__media"><img src="{img}" alt="{alt}" width="900" height="600" loading="lazy"></div>
  <div>
    <p class="eyebrow">{eyebrow}</p>
    <h2>{h2}</h2>
    <p class="lead">{lead}</p>
    <ul class="service__facts">{"".join(f'<li>{I("check")} {t}</li>' for t in facts)}</ul>
    <div class="btn-row" style="margin-top:26px"><a class="btn btn--primary" href="{href}">Mehr erfahren {I("arrow")}</a></div>
  </div>
</article>"""

leistungen_body = page_head("Leistungsspektrum", "Engineering, Modernisierung, Automatisierung.",
    "Ihr Partner für vernetzte Produktion: Mit dem Leistungsspektrum der PTC PressEngineering entwickeln wir Ihre Fähigkeiten weiter, Produkte zu individualisieren sowie die Produktion flexibel und modern zu halten.",
    IMG_PRESSEN, "Instandhaltung einer Presse", subnav_leistungen("leistungsspektrum")) + f"""
<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Unser Ansatz</p>
      <h2>Wertschöpfung durch vorausschauende Planung</h2>
      <p class="lead">Wir finden mit unseren Kunden gemeinsam technische Lösungen, die eine hohe Anlagenverfügbarkeit garantieren und gleichzeitig Kosten und Sicherheit gewährleisten. Als Partner für Digitalisierung, Automatisierung und Verkettung von Anlagen ermöglichen wir Flexibilität, Modernisierung und Optimierung auf allen Prozessebenen.</p>
      <p class="lead" style="margin-top:14px">Unsere Erfahrungen in der intelligenten Nutzung von Maschinendaten, im Engineering und Refurbishing generieren neue Potenziale für Leistungssteigerung und Kostensenkung in Ihrer Produktion.</p>
    </div>
    {service_block("pressen", IMG_PRESSEN, "Techniker bei der Instandhaltung einer Presse", "Leistungsmodul 1", "Pressen und Bandanlagen",
        "Instandhaltung, Retrofit und Modernisierung für Pressen: vom hochpräzisen Pressencheck über Neukonstruktion und Verschleißteiltausch bis zur Leistungserhöhung auf bis zu 85 % einer Neumaschine. Dazu Retrofit von Bandanlagen sowie Sicherheit und Zertifizierung.",
        ["Pressencheck", "Refurbishment ca. 30 % der Neuanschaffung", "Eigene Ersatzteilfertigung", "CE &amp; EN ISO 13849-1"], "pressen-und-bandanlagen.html")}
    {service_block("montagelinien", IMG_MONTAGE, "Flexible Montagelinie in der Produktion", "Leistungsmodul 2", "Flexible Montagelinien",
        "Verkettungen und Anlagenkonzepte für Montageautomationen: Prozessschritte zu einem ganzheitlichen Anlagenkonzept verbinden, Linien auf neue Produktderivate anpassen, in Leitsysteme integrieren und per Taktzeituntersuchung optimieren.",
        ["Anlagenkonzepte", "Umbau auf Produktderivate", "Leitsystem-Integration", "Taktzeituntersuchung", "Visualisierung"], "flexible-montagelinien.html")}
    {service_block("robotik", IMG_ROBOTIK, "Industrieroboter in der Fertigung", "Leistungsmodul 3", "Robotik",
        "Automatisierte Fertigungsprozesse und Industrieroboter: Inbetriebnahme von Roboteranlagen verschiedenster Hersteller, SPS- und Roboterprogrammierung, Simulation und Test, Taktzeitoptimierung sowie individuelle Automatisierungskonzepte.",
        ["Inbetriebnahme &amp; Teach-in", "SPS- und Roboterprogrammierung", "Simulation und Test", "Automatisierungskonzepte"], "robotik.html")}
  </div>
</section>
<section class="section section--light">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Kompetenzzentrum</p>
      <h2>Vernetzte Produktionssysteme in der SCHOLPP Gruppe</h2>
      <p class="lead">Gemeinsam mit der Bratz Engineering etablierte PTC PressEngineering in der SCHOLPP Unternehmensgruppe ein Kompetenzzentrum für vernetzte Produktionssysteme: Pressen-Know-how, Automatisierung und Robotik aus einem Haus, ergänzt um Verlagerung und Montage durch SCHOLPP.</p>
    </div>
    <ul class="stats">
      <li><strong>85 %</strong><span>Leistung einer fabrikneuen Presse nach Refurbishment</span></li>
      <li><strong>30 %</strong><span>der Kosten einer Neuanschaffung</span></li>
      <li><strong>3</strong><span>Leistungsmodule: Pressen &amp; Bandanlagen, Montagelinien, Robotik</span></li>
      <li><strong>1</strong><span>Ansprechpartner für Verlagerung, Modernisierung und Automatisierung</span></li>
    </ul>
  </div>
</section>
{CTA_BOX}
"""
page("leistungsspektrum", "Leistungsspektrum | PTC PressEngineering GmbH",
     "Drei Leistungsmodule der PTC PressEngineering: Pressen und Bandanlagen, Flexible Montagelinien, Robotik. Engineering, Modernisierung und Automatisierung aus Oberhausen.", leistungen_body)

# ---------------------------------------------------------------- Pressen und Bandanlagen
pressen_body = page_head("Pressen und Bandanlagen", "Instandhaltung und Modernisierung.",
    "Für Ihre Pressen und Bandanlagen: vom hochpräzisen Pressencheck bis zur Leistungserhöhung auf bis zu 85 % einer fabrikneuen Presse. Für rund 30 % der Kosten einer Neuanschaffung.",
    IMG_PRESSEN, "Techniker bei der Instandhaltung einer Presse", subnav_leistungen("pressen-und-bandanlagen"),
    buttons=f'<a class="btn btn--primary" href="kontakt.html#anfrage">{I("search")} Pressencheck anfragen</a><a class="btn btn--ghost" href="tel:{TEL}">{I("phone")} {PHONE}</a>') + f"""
<section class="section" id="pressencheck">
  <div class="container">
    <div class="split">
      <div>
        <p class="eyebrow">Pressencheck</p>
        <h2>Erst messen, dann planen</h2>
        <p class="lead">Die Techniker der PTC PressEngineering untersuchen in einem hochpräzisen Pressencheck alle Baugruppen, messen Einzel- und Gesamtspiele und führen Funktions- und Sichtprüfungen durch. Aufgrund des Maschinen-Ist-Zustands erarbeiten unsere Experten einen detaillierten Maßnahmenkatalog.</p>
        <p style="margin-top:16px;color:var(--muted)">Zusammen mit Ihnen legen wir den optimalen Zeitpunkt für Wartungs- und Modernisierungsmaßnahmen fest, abgestimmt auf Ihre Produktion.</p>
        <div class="btn-row"><a class="btn btn--primary" href="kontakt.html#anfrage">Pressencheck anfragen {I("arrow")}</a></div>
      </div>
      <div class="split__media"><img src="{IMG_REF_TRYOUT}" alt="Pressencheck an einer hydraulischen Tryoutpresse" width="475" height="343" loading="lazy"><span class="tag">Messen · Prüfen · Bewerten</span></div>
    </div>
  </div>
</section>

<section class="section section--surface" id="modernisierung">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Leistungsmodule</p>
      <h2>Vom einzelnen Bauteil bis zur kompletten Baugruppe</h2>
    </div>
    <div class="cards">
      <div class="card"><span class="card__icon">{I("cog")}</span><h3>Neukonstruktion &amp; Auslegung</h3><p>Neukonstruktion und verbesserte Auslegung von mechanischen, pneumatischen, hydraulischen und elektrischen Komponenten.</p></div>
      <div class="card"><span class="card__icon">{I("cpu")}</span><h3>Steuerungstechnik</h3><p>Integration neuer Steuerungstechnik, inklusive Visualisierung und Sicherheitssteuerung.</p></div>
      <div class="card"><span class="card__icon">{I("wrench")}</span><h3>Verschleißteiltausch</h3><p>Dichtungen, Schläuche, Ventile, Kabel, Sensoren und Aktoren. Verbesserter Kühl- und Schmiermittel-Service, optimierte Getriebe.</p></div>
      <div class="card"><span class="card__icon">{I("gauge")}</span><h3>Leistungserhöhung</h3><p>Mit diesem Set von Maßnahmen bringen wir Ihre Presse auf bis zu 85 % der Leistung einer fabrikneuen Presse.</p></div>
      <div class="card"><span class="card__icon">{I("press")}</span><h3>Ersatzteile</h3><p>Ersatzteile für alle Maschinentypen fertigen wir wenn nötig selbst, nach höchsten Qualitätsansprüchen und in engen Zeitfenstern.</p></div>
      <div class="card"><span class="card__icon">{I("line")}</span><h3>Automatisierung &amp; Verkettung</h3><p>Vom automatisierten Werkzeugwechsel bis zum Verbundbetrieb mehrerer Systeme: einzelne Pressen digitalisiert zur Pressenlinie mit flexiblem Bedienhandling verkettet.</p></div>
    </div>
    <div class="tip">{I("chart")}<p><strong>Rechnung:</strong> Im Vergleich zur Neuanschaffung liegen die Kosten für Refurbishment bei ca. 30 %, bei bis zu 85 % der Leistung einer Neumaschine.</p></div>
  </div>
</section>

<section class="section section--light" id="bandanlagen">
  <div class="container">
    <div class="split split--reverse">
      <div>
        <p class="eyebrow">Bandanlagen</p>
        <h2>Retrofit statt Neuanschaffung</h2>
        <p class="lead">Kostengünstiger als eine Neuanschaffung ist der Retrofit von Bandanlagen. Unser Know-how umfasst die Aufrüstung und Anpassung des Systems auf neue spezifische Applikationen Ihrer Fertigung. Selbstverständlich integrieren wir dabei modernste Steuerungen und Technologien.</p>
        {checks(["Aufrüstung und Anpassung an neue Applikationen", "Integration moderner Steuerungen und Technologien", "Auch für Stapler, Abstapler und Schrottfördersysteme"])}
        <div class="btn-row"><a class="btn btn--primary" href="kontakt.html#anfrage">Bandanlage anfragen {I("arrow")}</a></div>
      </div>
      <div class="split__media"><img src="{IMG_REF_ELECTROLUX}" alt="Automatisiertes Transfersystem einer Pressenstraße" width="475" height="343" loading="lazy"><span class="tag tag--bottom">Transfersystem mit Platinenlader, Electrolux Rothenburg</span></div>
    </div>
  </div>
</section>

<section class="section" id="sicherheit">
  <div class="container">
    <div class="split">
      <div>
        <p class="eyebrow">Sicherheit &amp; Zertifizierung</p>
        <h2>Unabhängig vom Maschinentyp</h2>
        <p class="lead">Wir erbringen Leistungen rund um Sicherheit und Zertifizierung Ihrer Anlagen, bei Umbauten genauso wie im laufenden Betrieb.</p>
        {checks(["CE-Zertifizierungen", "Performance Level gemäß EN ISO 13849-1", "Prüfungen nach BGI/GUV-I 724", "Prüfung von Arbeitsmitteln nach Betriebssicherheitsverordnung", "Belastbare Risikobeurteilung von Umbauten"])}
        <div class="btn-row"><a class="btn btn--primary" href="kontakt.html#anfrage">Prüfung anfragen {I("arrow")}</a><a class="btn btn--ghost" href="zertifikate-dokumente.html">Unsere Zertifikate</a></div>
      </div>
      <div class="split__media media--placeholder" aria-hidden="true">{I("shield")}</div>
    </div>
  </div>
</section>
{CTA_BOX}
"""
page("pressen-und-bandanlagen", "Pressen und Bandanlagen | PTC PressEngineering GmbH",
     "Pressencheck, Instandhaltung, Retrofit und Modernisierung von Pressen und Bandanlagen: bis zu 85 % der Leistung einer Neumaschine für rund 30 % der Kosten. CE, EN ISO 13849-1.", pressen_body)

# ---------------------------------------------------------------- Flexible Montagelinien
montage_body = page_head("Flexible Montagelinien", "Montagelinien: So flexibel wie Sie es wünschen.",
    "Für Ihre Montageautomation konzipiert PTC PressEngineering die Verkettung der einzelnen Prozessschritte zu einem ganzheitlichen Anlagenkonzept.",
    IMG_MONTAGE, "Flexible Montagelinie", subnav_leistungen("flexible-montagelinien"),
    buttons=f'<a class="btn btn--primary" href="kontakt.html#anfrage">{I("mail")} Projekt anfragen</a>') + f"""
<section class="section">
  <div class="container">
    <div class="split">
      <div>
        <p class="eyebrow">Anlagenkonzept</p>
        <h2>Effizienz, Wirtschaftlichkeit, Qualitätssicherung</h2>
        <p class="lead">Wir wissen, dass bei einer Modernisierung Effizienz, Wirtschaftlichkeit und Qualitätssicherung im Vordergrund stehen. Von der Prüfstandstechnik über Einzelfertigungen bis hin zur Endmontage im In- und Ausland setzen wir individuelle Lösungen um.</p>
        <p style="margin-top:16px;color:var(--muted)">Sie wünschen die Anpassung von Montagelinien auf neue Produktderivate? Ihre Anlagen benötigen einen elektrischen und mechanischen Umbau, neue Messtechnik und weitere Schraubersysteme? Wir kümmern uns darum. Flexibel austauschbare Funktionseinheiten ermöglichen dann ein Produktionsspektrum mit unterschiedlichen Größen und Varianten.</p>
      </div>
      <div class="split__media"><img src="{IMG_MONTAGE}" alt="Montagelinie mit verketteten Stationen" width="900" height="600" loading="lazy"><span class="tag">Verkettung der Prozessschritte</span></div>
    </div>
  </div>
</section>
<section class="section section--light">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Leistungen</p><h2>Was wir für Ihre Montagelinie tun</h2></div>
    <div class="cards">
      <div class="card"><span class="card__icon">{I("line")}</span><h3>Verkettung zum Anlagenkonzept</h3><p>Einzelne Prozessschritte werden zu einer durchgängigen Gesamtlösung verbunden, von der Prüfstandstechnik bis zur Endmontage.</p></div>
      <div class="card"><span class="card__icon">{I("cog")}</span><h3>Anpassung an Produktderivate</h3><p>Elektrischer und mechanischer Umbau, neue Messtechnik, zusätzliche Schraubersysteme und austauschbare Funktionseinheiten.</p></div>
      <div class="card"><span class="card__icon">{I("layers")}</span><h3>Integration in Leitsysteme</h3><p>Maschinen, Zellen oder Linien, Kamera- und Prüfsysteme sowie Steuerungen mit Schnittstellenprogrammierung werden systematisch eingebunden.</p></div>
      <div class="card"><span class="card__icon">{I("clock")}</span><h3>Taktzeituntersuchung</h3><p>Wir ermitteln Optimierungspotenziale Ihrer Montageautomation, steigern die Produktivität und senken Herstellungs- und Wartungskosten.</p></div>
      <div class="card"><span class="card__icon">{I("cpu")}</span><h3>Visualisierungen</h3><p>Übersichtliche und bedienerfreundliche Oberflächen, gestaltet nach den Anforderungen Ihrer Automatisierungsaufgabe.</p></div>
      <div class="card"><span class="card__icon">{I("globe")}</span><h3>Im In- und Ausland</h3><p>Umsetzung vor Ort, auch an internationalen Standorten, auf Wunsch zusammen mit SCHOLPP für Transport und Montage.</p></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="split split--reverse">
      <div>
        <p class="eyebrow">Referenz</p>
        <h2>Pressenstraße PV05 bei Electrolux</h2>
        <p class="lead">Ein Acht-Mann-Team aus Mechanikern, Elektrikern und Programmierern modernisierte die Pressenstraße in Rothenburg ob der Tauber: neues Transfersystem mit acht Schließgeräten, Platinenlader, S7-Software, Visualisierung und Sicherheitssteuerung. Drei Wochen vom Abbau bis zum Wiederanlauf.</p>
        <div class="btn-row"><a class="btn btn--primary" href="referenzen.html#electrolux">Zum Projekt {I("arrow")}</a></div>
      </div>
      <div class="split__media"><img src="{IMG_REF_ELECTROLUX}" alt="Automatisiertes Transfersystem bei Electrolux" width="475" height="343" loading="lazy"><span class="tag tag--bottom">16 taktsynchrone Servoachsen</span></div>
    </div>
  </div>
</section>
{CTA_BOX}
"""
page("flexible-montagelinien", "Flexible Montagelinien | PTC PressEngineering GmbH",
     "Verkettung, Anlagenkonzepte, Anpassung an Produktderivate, Leitsystem-Integration, Taktzeituntersuchung und Visualisierung für Ihre Montageautomation.", montage_body)

# ---------------------------------------------------------------- Robotik
robotik_body = page_head("Robotik", "Robotik: Wir automatisieren Ihre Prozesskette.",
    "Automatisierte Fertigungsprozesse und Industrieroboter reduzieren kostenintensive Arbeitsschritte und erhöhen die Qualität Ihrer Produkte. Roboter sind wartungsarm, technisch ausgereift, präzise und von langer Lebensdauer.",
    IMG_ROBOTIK, "Industrieroboter", subnav_leistungen("robotik"),
    buttons=f'<a class="btn btn--primary" href="kontakt.html#anfrage">{I("mail")} Automatisierung anfragen</a>') + f"""
<section class="section">
  <div class="container">
    <div class="split">
      <div>
        <p class="eyebrow">SPS- und Roboterprogrammierung</p>
        <h2>Herstellerunabhängig in Betrieb nehmen</h2>
        <p class="lead">PTC PressEngineering gewährleistet eine individuelle, zügige Inbetriebnahme von Roboteranlagen, denn wir sind mit Robotern verschiedenster Hersteller vertraut. Beim Thema SPS- und Roboterprogrammierung unterstützen wir Sie gewinnbringend:</p>
        {checks(["Umprogrammierung und Retrofit", "Simulation und Test", "Robotertaktzeitoptimierung und Produktionsqualitätsoptimierung", "Inbetriebnahme und Teach-in der Roboter", "Erstellung und Optimierung von Applikationsparametern und Werkzeugzuordnung", "Beratung zu Applikationen, Robotern, Steuerungen und Bildverarbeitungssystemen"])}
        <p class="note">{I("clock")} Immer mit dem Ziel effektiver, schnell kombinierter Bewegungsabläufe für möglichst kurze Taktzeiten.</p>
      </div>
      <div class="split__media"><img src="{IMG_ROBOTIK}" alt="Industrieroboter in der automatisierten Fertigung" width="900" height="600" loading="lazy"><span class="tag">Roboter verschiedenster Hersteller</span></div>
    </div>
  </div>
</section>
<section class="section section--light">
  <div class="container">
    <div class="split split--reverse">
      <div>
        <p class="eyebrow">Automatisierungskonzepte</p>
        <h2>Teilbereich oder ganzer Prozess</h2>
        <p class="lead">Automatisieren lassen sich Teilbereiche der Fertigung oder ganze Produktionsprozesse, je nach Qualitäts- und Kundenanforderung oder Investitionsvolumen. Als Spezialist für Automatisierung erstellen wir Ihnen unter Maßgabe wirtschaftlicher Aspekte ein individuelles Automatisierungskonzept.</p>
        <p style="margin-top:16px;color:var(--muted)">Basis dafür ist unsere langjährige Erfahrung aus erfolgreich umgesetzten Automatisierungsprojekten. Oft ist schon die Verlagerung von Teilprozessen auf einen einzelnen Roboter, der autark arbeitet oder mit anderen Komponenten zum Gesamtprozess verbunden wird, ein enormer Effizienzfaktor.</p>
        <div class="btn-row"><a class="btn btn--primary" href="kontakt.html#anfrage">Konzept anfragen {I("arrow")}</a><a class="btn btn--ghost" href="flexible-montagelinien.html">Montagelinien</a></div>
      </div>
      <div class="split__media"><img src="{IMG_MONTAGE}" alt="Automatisierte Montagelinie" width="900" height="600" loading="lazy"><span class="tag tag--bottom">Vom autarken Einzelroboter bis zum Gesamtprozess</span></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Vorteile</p><h2>Warum Roboter in der Prozesskette</h2></div>
    <div class="cards cards--4">
      <div class="card"><span class="card__icon">{I("chart")}</span><h3>Weniger Kosten</h3><p>Kostenintensive Arbeitsschritte werden reduziert oder auf den Roboter verlagert.</p></div>
      <div class="card"><span class="card__icon">{I("award")}</span><h3>Höhere Qualität</h3><p>Präzise, reproduzierbare Abläufe erhöhen die Qualität Ihrer Produkte.</p></div>
      <div class="card"><span class="card__icon">{I("wrench")}</span><h3>Wartungsarm</h3><p>Technisch ausgereift und von langer Lebensdauer.</p></div>
      <div class="card"><span class="card__icon">{I("bolt")}</span><h3>Kurze Taktzeiten</h3><p>Effektive, schnell kombinierte Bewegungsabläufe durch Taktzeitoptimierung.</p></div>
    </div>
  </div>
</section>
{CTA_BOX}
"""
page("robotik", "Robotik | PTC PressEngineering GmbH",
     "Inbetriebnahme von Roboteranlagen, SPS- und Roboterprogrammierung, Simulation, Taktzeitoptimierung und individuelle Automatisierungskonzepte von PTC PressEngineering.", robotik_body)

# ---------------------------------------------------------------- Referenzen
def ref_detail(id_, img, alt, client, branche, h2, paras, aufgabe, besonderheiten, reverse=False):
    return f"""
<article class="service" id="{id_}">
  <div class="service__media"><img src="{img}" alt="{alt}" width="475" height="343" loading="lazy"></div>
  <div>
    <p class="eyebrow">{client} · {branche}</p>
    <h2>{h2}</h2>
    {"".join(f'<p class="{"lead" if i == 0 else ""}" style="{"" if i == 0 else "margin-top:14px;color:var(--muted)"}">{p}</p>' for i, p in enumerate(paras))}
    <dl class="brief">
      <dt>Kunde</dt><dd>{client}</dd>
      <dt>Branche</dt><dd>{branche}</dd>
      <dt>Projektart</dt><dd>Modernisierung / Retrofit</dd>
      <dt>Aufgabe</dt><dd>{aufgabe}</dd>
      <dt>Besonderheiten</dt><dd>{besonderheiten}</dd>
    </dl>
    <div class="btn-row" style="margin-top:22px"><a class="btn btn--ghost btn--sm" href="kontakt.html#anfrage">Frage zu diesem Projekt {I("arrow")}</a></div>
  </div>
</article>"""

referenzen_body = page_head("Referenzen", "Besser machen ist unser Geschäft.",
    "Unser Angebotsspektrum hat die Kernelemente Engineering und Refurbishment. Wir optimieren bestehende Anlagen, führen Schwachstellenanalysen und Sicherheitsprüfungen durch und übernehmen jede Art von Service oder Wartung von Pressen, Bandanlagen, Montagelinien und Roboteranlagen.",
    IMG_NEWS_1, "Pressenanlage in der Werkhalle") + f"""
<section class="section section--tight">
  <div class="container">
    <div class="refs">
      <a class="ref" href="#daimler"><div class="ref__media"><img src="{IMG_REF_DAIMLER}" alt="" width="475" height="343" loading="lazy"></div><div class="ref__body"><span class="ref__client">Daimler</span><h3>Pressenverlagerung und -modernisierung</h3><p>Mercedes-Benz-Werk Bremen</p></div></a>
      <a class="ref" href="#electrolux"><div class="ref__media"><img src="{IMG_REF_ELECTROLUX}" alt="" width="475" height="343" loading="lazy"></div><div class="ref__body"><span class="ref__client">Electrolux</span><h3>Modernisierung einer Pressenstraße</h3><p>Rothenburg ob der Tauber</p></div></a>
      <a class="ref" href="#tryoutpresse"><div class="ref__media"><img src="{IMG_REF_TRYOUT}" alt="" width="475" height="343" loading="lazy"></div><div class="ref__body"><span class="ref__client">Automotive</span><h3>Modernisierung einer Tryoutpresse</h3><p>2.300-Tonnen-Hydraulikpresse</p></div></a>
      <a class="ref" href="#weisse-ware"><div class="ref__media"><img src="{IMG_REF_WEISS}" alt="" width="475" height="317" loading="lazy"></div><div class="ref__body"><span class="ref__client">Weiße Ware</span><h3>Modernisierte Presse für Premiumhersteller</h3><p>Mossini-Presse, 12.500 kN</p></div></a>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Projekte</p><h2>Vier Beispiele aus der Praxis</h2></div>
    {ref_detail("daimler", IMG_REF_DAIMLER, "800-Tonnen-Einarbeitungspresse im Mercedes-Benz-Werk Bremen", "Daimler", "Automotive",
        "Pressenverlagerung und Pressenmodernisierung im Mercedes-Benz-Werk Bremen",
        ["Im Mercedes-Benz-Werk in Bremen stellten SCHOLPP und PTC PressEngineering die Vorteile ihrer Zusammengehörigkeit bei einer Pressenverlagerung mit gleichzeitiger technischer Modernisierung eindrucksvoll unter Beweis.",
         "In der ersten Phase wurde eine 800-Tonnen-Einarbeitungspresse, auf der Werkzeuge für die Produktion getestet werden, demontiert, zwischengelagert und just in time am neuen Standort im Werk remontiert und wieder in Betrieb genommen. Die einmonatige Zwischenlagerung wurde für eine intensive Verjüngungskur inklusive konstruktiver Änderungen an der über 20 Jahre alten Presse genutzt: Überholungsarbeiten am Stößel, Tausch diverser Sicherheitskomponenten auf den neuesten Stand der Technik sowie ein komplett neu konstruiertes und eingebautes Schmieraggregat mit neuen Windkesseln."],
        "Demontage, Zwischenlagerung, konstruktive Überholung und Remontage einer 800-t-Presse im Mercedes-Benz-Werk Bremen.",
        "Umfangreiche konstruktive Modernisierungsarbeiten an der Presse während der Zwischenlagerung.")}
    {ref_detail("electrolux", IMG_REF_ELECTROLUX, "Automatisiertes Transfersystem der Pressenstraße PV05 bei Electrolux", "Electrolux", "Weiße Ware",
        "Modernisierung einer Pressenstraße",
        ["Ein Acht-Mann-Team aus Mechanikern, Elektrikern und Programmierern betreute das Projekt „Modernisierung der Pressenstraße PV05“ von Electrolux in Rothenburg ob der Tauber, auf der Backofen-Teile hergestellt werden. Im Auftragsbuch: ein neues Transfersystem inklusive Platinenlader und dessen komplette Automatisierung.",
         "Neben der Demontage der alten Anlage umfasste die Aufgabe die Konstruktion und Fertigung eines neuen Transfersystems mit acht Schließgeräten und einem Transfervorschub sowie eines Platinenladers, der auf zwei Stapelnestern vollautomatisch zugreift. Das elektrische Engineering mit Stromlaufplan, S7-Software, Visualisierung und Sicherheitssteuerung, der Schaltschrankbau, die Installation und die Inbetriebnahme gehörten ebenfalls dazu. Drei Wochen blieben vom Abbau bis zum Wiederanlauf; die Programmierer realisierten den taktsynchronen Lauf der 2 x 8 Servoachsen."],
        "Demontage des alten Transfersystems, Konstruktion, Installation und Inbetriebnahme eines automatisierten neuen Transfersystems mit neuen Platinenladern.",
        "Kurze Umbauzeit, hohe Taktzahl der automatisierten Pressenlinie, Synchronlauf von 16 Servoachsen.")}
    {ref_detail("tryoutpresse", IMG_REF_TRYOUT, "Hydraulische 2.300-Tonnen-Tryoutpresse", "Automotive", "Automotive",
        "Modernisierung einer Tryoutpresse",
        ["Ziel dieses Projekts für einen namhaften deutschen Automobilhersteller war eine deutliche Erhöhung der Arbeitsgeschwindigkeit und die Erweiterung des Tischkissens auf sechs Regelachsen der hydraulischen 2.300-Tonnen-Tryoutpresse im Werkzeugbau.",
         "Das Projekt umfasste das komplette Engineering der Presse, die Simulation des Umbaus, die Neukonstruktion hydraulischer Steuerblöcke und Kolbenspeicherstationen, Modifikationen der Stößelzylinder, das neue Rohrleitungssystem, den mechanischen Umbau des Tischkissens mit zusätzlichen Zylindern sowie die neue elektronische Regelung, Visualisierung und Verkabelung. Inbetriebnahme, Sicherheitsabnahme und Schulung der Mitarbeiter gehörten ebenfalls dazu. Die Sicherheit der hydraulischen Steuerung hatte dabei einen besonders hohen Stellenwert."],
        "Erhöhung der Arbeitsgeschwindigkeit, Umbau des Tischkissens von 4-Punkt- auf 6-Punkt-Kissen.",
        "Neukonstruktion der Steuerblöcke und Umlenkadaptionen; Koordination von Stahlbau, mechanischen und hydraulischen Umbauten, elektrischem Retrofit, Klemmkästen und Rohrleitungen.")}
    {ref_detail("weisse-ware", IMG_REF_WEISS, "Getriebeinstandsetzung an einer Mossini-Presse", "Premiumhersteller Weiße Ware", "Weiße Ware",
        "Modernisierte Presse für Premiumhersteller „Weißer Ware“",
        ["Mit einer optimierten Mossini-Presse (Presskraft 12.500 kN) arbeitet ein deutscher Premiumhersteller von Waschmaschinen, Geschirrspülern und Kühlschränken jetzt dank PTC PressEngineering. Nach fünf Monaten Vorlauf wurde das komplette Getriebe de- und remontiert; wegen der besonderen Hallenkonstruktion kam ein spezieller Mobilkran zum Einsatz, Fördertrassen unter dem Hallendach mussten demontiert werden.",
         "Beim Retrofit wurden Zahnradbandagen eingesetzt, Vorlege- und Antriebswellen erneuert und Passfederverbindungen durch spielfreie Spannelemente ersetzt. Die Sicherheit der Verzahnung stieg von ca. 0,367 auf ca. 1,128. Zusätzliche Lagerstellen und optimierte Schmierung minimieren den Verschleiß. Das PTC-Team betreute den Umbau von den ersten Beratungsgesprächen bis zur Endabnahme vor Ort."],
        "De- und Remontage Schallschutz, Abkoppeln des Stößels, De- und Remontage des kompletten Getriebes am Standort, Erneuerung beider Getriebestufen bei kürzester Stillstandzeit.",
        "Alle Maße der Fertigungsteile ohne Demontage der Presse im Vorfeld festgelegt; zweischichtige Montage wegen enger Terminschiene; fehlerhaft gefertigte Lagergassen während der Bauarbeiten durch Anpassen der Verzahnung korrigiert.")}
  </div>
</section>
<section class="section section--light">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Branchen &amp; Projektarten</p><h2>Wofür wir angefragt werden</h2><p class="lead">Die Referenzdatenbank von SCHOLPP und PTC gliedert sich nach Projektart und Branche.</p></div>
    <h3 style="font-size:1.05rem;letter-spacing:.1em;text-transform:uppercase">Projektarten</h3>
    {chips(["Regionale Projekte", "Nationale Verlagerungsprojekte", "Internationale Verlagerungsprojekte", "Neumontageprojekte", "Modernisierung / Retrofit"], "Projektarten")}
    <h3 style="margin-top:26px;font-size:1.05rem;letter-spacing:.1em;text-transform:uppercase">Branchen</h3>
    {chips(["Automotive", "Druckindustrie", "Maschinenbau", "Verpackungsindustrie", "Umformindustrie", "Fahrtreppenindustrie", "Medizin / Pharma", "Kunst", "Anlagenbau", "Halbleiter- / Solarindustrie"], "Branchen")}
  </div>
</section>
{CTA_BOX}
"""
page("referenzen", "Referenzen | PTC PressEngineering GmbH",
     "Referenzprojekte der PTC PressEngineering: Pressenmodernisierung bei Daimler in Bremen, Pressenstraße bei Electrolux, Tryoutpresse Automotive, Mossini-Presse für Weiße Ware.", referenzen_body)

# ---------------------------------------------------------------- Karriere
karriere_body = page_head("Karriere", "PTC PressEngineering als Arbeitgeber.",
    "Über 50 Ingenieure, Techniker und Monteure in Mechanik, Hydraulik, Steuerungstechnik und Robotik arbeiten bei PTC in Oberhausen an Pressen, Bandanlagen, Montagelinien und Roboteranlagen.",
    IMG_NEWS_3, "Montageteam an einer Pressenanlage",
    buttons=f'<a class="btn btn--primary" href="mailto:{MAIL}?subject=Initiativbewerbung">{I("mail")} Initiativ bewerben</a>') + f"""
<section class="section">
  <div class="container">
    <div class="tip">
      {I("info")}
      <!-- Stand Oktober 2026 laut ptc.eu/de/karriere/: keine offenen Stellen. Bei neuen Ausschreibungen hier Karten mit Titel, Standort, Aufgaben und Profil ergänzen. -->
      <p><strong>Aktuell sind keine Stellenausschreibungen online</strong> bzw. freie Stellen zu besetzen. Wir freuen uns trotzdem über Ihre Initiativbewerbung.</p>
    </div>
    <div class="split" style="margin-top:56px">
      <div>
        <p class="eyebrow">Arbeiten bei PTC</p>
        <h2>Mechanik, Hydraulik, Steuerungstechnik, Robotik</h2>
        <p class="lead">Wer bei PTC arbeitet, modernisiert Maschinen, die seit Jahrzehnten laufen, und bringt sie auf den Stand der Technik: von der Pressenmechanik über Hydraulik und Elektrik bis zu SPS- und Roboterprogrammierung. Projekte bei namhaften Kunden in Deutschland und im Ausland, als Teil einer Gruppe mit über 700 Mitarbeitern.</p>
        {chips(["Konstruktion", "Mechanik", "Hydraulik", "Elektrik", "Steuerungstechnik", "SPS-Programmierung", "Robotik", "Montage im In- und Ausland", "Inbetriebnahme"], "Fachbereiche")}
      </div>
      <div class="split__media"><img src="{IMG_PRESSEN}" alt="Techniker bei der Arbeit an einer Presse" width="900" height="600" loading="lazy"><span class="tag">Über 50 Kolleginnen und Kollegen</span></div>
    </div>
  </div>
</section>
<section class="section section--light">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Bewerbung</p><h2>So erreichen Sie uns</h2><p class="lead">Schicken Sie Ihre Unterlagen per E-Mail oder rufen Sie vorher kurz an. Hinweise zur Verarbeitung Ihrer Daten im Bewerbungsverfahren finden Sie in der <a href="datenschutz.html#bewerbung" style="color:var(--brand)">Datenschutzerklärung</a>.</p></div>
    <div class="cards cards--2">
      <div class="info-card"><h3>{I("mail")} Per E-Mail</h3><p><a href="mailto:{MAIL}?subject=Initiativbewerbung">{MAIL}</a></p><p class="muted" style="margin-top:8px">Betreff „Initiativbewerbung“, Lebenslauf und Zeugnisse als PDF.</p></div>
      <div class="info-card"><h3>{I("phone")} Per Telefon</h3><p>Zentrale: <a href="tel:{TEL}">{PHONE}</a><br>Service-Hotline: <a href="tel:{TEL_H}">{HOTLINE}</a></p></div>
    </div>
  </div>
</section>
{CTA_BOX}
"""
page("karriere", "Karriere | PTC PressEngineering GmbH",
     "PTC PressEngineering als Arbeitgeber: Mechanik, Hydraulik, Steuerungstechnik und Robotik in Oberhausen. Aktuelle Stellen und Initiativbewerbung.", karriere_body)

# ---------------------------------------------------------------- News
news_body = page_head("News", "Unsere Konstante heißt Veränderung.",
    "Auch bei SCHOLPP ist die wichtigste Konstante die Veränderung. Nur so kann ein Unternehmen heute mit seinem Know-how in der globalisierten Welt mit ihren sich ständig verändernden Märkten bestehen. Hier erfahren Sie, was es Neues in der SCHOLPP-Gruppe, bei unseren Kunden oder in der Branche gibt.",
    IMG_NEWS_2, "Pressenanlage", [("news.html", "Aktuell", True), ("#archiv", "Newsarchiv", False), ("#publikationen", "Publikationen", False)]) + f"""
<section class="section section--tight" id="aktuell">
  <div class="container">
    <!-- Stand Oktober 2026: ptc.eu/de/news/ meldet „Keine Nachrichten verfügbar.“ Neue Meldungen hier als .article ergänzen. -->
    <div class="tip">{I("info")}<p><strong>Keine aktuellen Nachrichten verfügbar.</strong> Die letzte Meldung finden Sie im Newsarchiv.</p></div>
  </div>
</section>
<section class="section" id="archiv">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Newsarchiv</p><h2>PTC PressEngineering fusioniert mit Bratz Engineering</h2></div>
    <article class="article" id="fusion">
      <div class="article__meta"><span>{I("calendar", "icon icon--sm")} 30.06.2015</span><span>von SCHOLPP</span><span>Kategorie: PTC</span></div>
      <p class="lead">Die Bratz Engineering GmbH ist Ende Juni in die PTC PressEngineering GmbH integriert worden und gehört damit zukünftig zur SCHOLPP Gruppe. Für den Pressenspezialisten PTC bedeutet dies einen Zuwachs an Kompetenzen, Leistungsumfang und Mitarbeitern.</p>
      <blockquote>„Die PTC und Bratz verbindet seit vielen Jahren eine kooperative Zusammenarbeit. Durch die Fusion werden die Kompetenzen beider Unternehmen optimal zusammengeführt.“<footer>Lars Gerlach, Geschäftsführer SCHOLPP</footer></blockquote>
      <p>Bereits seit Mai 2015 fungiert Ralf Bratz, der bisherige Inhaber von Bratz Engineering, einem der Spezialisten in Nordrhein-Westfalen für Automatisierungstechnik und Maschinenbau, als Geschäftsführer der PTC PressEngineering.</p>
      <p>Damit kann die PTC zukünftig Retrofits, Reparaturen sowie Wartung, Instandhaltung und Umrüstung von Steuerungen nicht mehr nur für Pressen anbieten. Diese Leistungen sind auch für Bandanlagen, Stapler und Abstapler sowie alle gängigen Automatisierungsanlagen bis hin zu Schrottfördersystemen abrufbar. Ein neuer Schwerpunkt sind flexible Montagelinien zur Automatisierung von Anlagen und deren elektrische oder mechanische Umrüstung sowie Robotik bzw. Roboterautomatisierungslösungen.</p>
      <p>Mit nunmehr 20 Standorten kann SCHOLPP dadurch seine flächendeckende Präsenz in Deutschland strategisch verstärken. „Zusätzlich werden wir im Sommer 2015 eine Niederlassung der PTC im Kölner Norden gründen. In Verbindung mit dem Standort in Oberhausen bieten wir unseren Kunden in der Region eine leistungsstarke Allianz“, stellte Gerlach in Aussicht.</p>
      <blockquote>„Insgesamt stehen jetzt in den Bereichen Mechanik, Hydraulik, Steuerungstechnik und Robotik mehr als 50 Ingenieure, Techniker und 20 Monteure zur Verfügung. Das sichert unser fachliches Wissen auf ganzer Linie und ergänzt das Leistungsspektrum von SCHOLPP.“<footer>Ralf Bratz, Geschäftsführer PTC PressEngineering</footer></blockquote>
      <p>Bei der Übernahme wurden alle bisherigen Arbeitsplätze gesichert.</p>
    </article>
    <div class="gallery">
      <img src="{IMG_NEWS_1}" alt="Pressenanlage: Die Fusion führt die Kompetenzen beider Unternehmen zusammen" width="900" height="600" loading="lazy">
      <img src="{IMG_NEWS_2}" alt="Retrofits und Wartung künftig auch für Bandanlagen und Automatisierungsanlagen" width="900" height="600" loading="lazy">
      <img src="{IMG_NEWS_3}" alt="SCHOLPP verstärkt mit 20 Standorten seine Präsenz in Deutschland" width="900" height="600" loading="lazy">
    </div>
  </div>
</section>
<section class="section section--light" id="publikationen">
  <div class="container">
    <div class="split">
      <div>
        <p class="eyebrow">Publikationen</p>
        <h2>Wenn Sie noch mehr über PTC erfahren möchten …</h2>
        <p class="lead">Momentan stehen keine aktuellen Broschüren zum Download zur Verfügung. Möchten Sie sich ein genaueres Bild von unserem Leistungsprofil machen? Dann finden Sie weiterführende Informationen in unserem Leistungsspektrum, bei den Referenzen und auf der Website der SCHOLPP Gruppe.</p>
        <div class="btn-row">
          <a class="btn btn--primary" href="leistungsspektrum.html">Leistungsspektrum {I("arrow")}</a>
          <a class="btn btn--ghost" href="https://www.scholpp.de" target="_blank" rel="noopener">{I("external")} scholpp.de</a>
        </div>
      </div>
      <div>
        <div class="downloads">
          <a class="download" href="{PDF_ISO}" target="_blank" rel="noopener">{I("file")}<span><strong>Zertifizierung nach DIN ISO 9001</strong><small>PTC PressEngineering GmbH</small></span><span class="download__meta">PDF · 268 KB</span></a>
          <a class="download" href="{PDF_AEB}" target="_blank" rel="noopener">{I("file")}<span><strong>Allgemeine Einkaufsbedingungen</strong><small>PTC PressEngineering GmbH</small></span><span class="download__meta">PDF · 58 KB</span></a>
        </div>
      </div>
    </div>
  </div>
</section>
{CTA_BOX}
"""
page("news", "News | PTC PressEngineering GmbH",
     "Neuigkeiten von PTC PressEngineering und der SCHOLPP Gruppe, Newsarchiv und Publikationen.", news_body)

# ---------------------------------------------------------------- Kontakt
kontakt_body = page_head("Kontakt", "Was können wir für Sie tun?",
    "Rufen Sie an oder schicken Sie uns Ihre Anfrage über das Formular. Wir melden uns per Telefon oder E-Mail und vereinbaren bei Bedarf einen Termin vor Ort.",
    HERO_IMG, "Pressenhalle",
    buttons=f'<a class="btn btn--primary" href="tel:{TEL}">{I("phone")} {PHONE}</a><a class="btn btn--ghost" href="mailto:{MAIL}">{I("mail")} {MAIL}</a>') + f"""
<section class="section" id="anfrage">
  <div class="container">
    <div class="contact-grid">
      <div>
        <!-- Demo-Formular: ohne Server. Für den Live-Betrieb action/method setzen oder einen Formulardienst anbinden; danach Datenschutz Abschnitt 4 ergänzen. -->
        <form class="form" id="termin-form" novalidate>
          <h2 style="font-size:2rem">Anfrage senden</h2>
          <div class="form__row">
            <div class="field"><label for="f-name">Name</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
            <div class="field"><label for="f-company">Unternehmen</label><input id="f-company" name="company" type="text" autocomplete="organization"></div>
          </div>
          <div class="form__row">
            <div class="field"><label for="f-mail">E-Mail</label><input id="f-mail" name="email" type="email" autocomplete="email" required></div>
            <div class="field"><label for="f-phone">Telefon <small>(optional)</small></label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
          </div>
          <div class="form__row">
            <div class="field">
              <label for="f-topic">Thema</label>
              <select id="f-topic" name="topic" required>
                <option value="">Bitte wählen</option>
                <option>Pressencheck / Instandhaltung</option>
                <option>Retrofit / Modernisierung Presse</option>
                <option>Retrofit Bandanlage</option>
                <option>Flexible Montagelinien</option>
                <option>Robotik / Automatisierung</option>
                <option>Sicherheit / Zertifizierung</option>
                <option>Ersatzteile</option>
                <option>Verlagerung mit SCHOLPP</option>
                <option>Bewerbung</option>
                <option>Sonstiges</option>
              </select>
            </div>
            <div class="field"><label for="f-machine">Maschine / Anlage <small>(optional)</small></label><input id="f-machine" name="machine" type="text" placeholder="z. B. hydraulische Presse 2.300 t, Baujahr 1998"></div>
          </div>
          <div class="field"><label for="f-msg">Nachricht</label><textarea id="f-msg" name="message" required placeholder="Was steht an? Stillstand, geplante Modernisierung, Verlagerung, Prüfung?"></textarea></div>
          <label class="check"><input type="checkbox" name="privacy" required> <span>Ich habe die <a href="datenschutz.html">Datenschutzerklärung</a> gelesen. Meine Angaben werden nur zur Bearbeitung der Anfrage verwendet.</span></label>
          <div class="form__foot">
            <button class="btn btn--primary" type="submit">Anfrage senden {I("arrow")}</button>
            <small>Unverbindlich. Antwort per Telefon oder E-Mail.</small>
          </div>
        </form>
        <div class="form-success" id="form-success" role="status" aria-live="polite">
          <h3>Danke<span data-name></span>, Ihre Anfrage ist angekommen.</h3>
          <p>Wir melden uns per Telefon oder E-Mail bei Ihnen. Eilig? Rufen Sie uns an: <a href="tel:{TEL}">{PHONE}</a>.</p>
        </div>
      </div>
      <div class="location__info">
        <div class="info-card">
          <h3>{I("phone")} Direkt erreichen</h3>
          <p>Zentrale: <a href="tel:{TEL}">{PHONE}</a><br>Service-Hotline: <a href="tel:{TEL_H}">{HOTLINE}</a><br>Fax: {FAX}<br><a href="mailto:{MAIL}">{MAIL}</a></p>
        </div>
        <div class="info-card">
          <h3>{I("pin")} Anschrift</h3>
          <p>PTC PressEngineering GmbH<br>{ADDR_1}<br>{ADDR_2}</p>
        </div>
        <div class="info-card">
          <h3>{I("clock")} Bürozeiten</h3>
          <!-- TODO: Bürozeiten vom Kunden erfragen; auf ptc.eu sind keine angegeben. -->
          <p class="muted"><span class="todo">vom Kunden ergänzen</span></p>
        </div>
        <div class="info-card">
          <h3>{I("info")} Gut zu wissen</h3>
          {checks(["Pressencheck vor Ort als Basis für den Maßnahmenkatalog", "Verlagerung zusammen mit SCHOLPP aus einer Hand", "Ersatzteile bei Bedarf aus eigener Fertigung"]).replace('class="checks"', 'class="checks" style="margin-top:0"')}
        </div>
      </div>
    </div>
  </div>
</section>
{location_section(light=True, headline="Anfahrt", lead="Essener Straße 59 in Alt-Oberhausen, zwischen Innenstadt und Neuer Mitte. Über die A 42 (Anschlussstelle Oberhausen-Zentrum) oder die A 3.")}
"""
page("kontakt", "Kontakt und Anfahrt | PTC PressEngineering GmbH, Oberhausen",
     f"Kontakt zu PTC PressEngineering: Telefon {PHONE}, Service-Hotline {HOTLINE}, {MAIL}. Essener Str. 59, 46047 Oberhausen. Anfrageformular und Anfahrt.",
     kontakt_body, map_=True)

# ---------------------------------------------------------------- Impressum
impressum_body = page_head("Rechtliches", "Impressum", "") + f"""
<section class="section section--tight">
  <div class="container">
    <div class="prose">
      <h2>Angaben gemäß § 5 DDG</h2>
      <dl>
        <dt>Firma</dt><dd>PTC PressEngineering GmbH</dd>
        <dt>Anschrift</dt><dd>{ADDR_1}<br>{ADDR_2}</dd>
        <dt>Telefon</dt><dd><a href="tel:{TEL}">+49 (0) 208 810 60-0</a></dd>
        <dt>Telefax</dt><dd>+49 (0) 208 810 60-99</dd>
        <dt>E-Mail</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd>
        <dt>Geschäftsführender Gesellschafter</dt><dd>Wolfgang E. Mueller</dd>
        <dt>Registergericht</dt><dd>Amtsgericht Duisburg</dd>
        <dt>Registernummer</dt><dd>HRB 13437</dd>
        <dt>USt-IdNr.</dt><dd>DE 212722514 (gemäß § 27 a Umsatzsteuergesetz)</dd>
        <dt>Zuständige Aufsichtsbehörde</dt><dd>Agentur für Arbeit Düsseldorf<br>40180 Düsseldorf</dd>
      </dl>

      <h2>Verantwortlich für den Inhalt</h2>
      <p>Verantwortlich nach § 18 Abs. 2 MStV:<br>SCHOLPP GmbH<br>Carl-von-Bach-Straße 2<br>09116 Chemnitz</p>

      <h2>Streitschlichtung</h2>
      <p>Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit: <a href="https://ec.europa.eu/consumers/odr/" target="_blank" rel="noopener">https://ec.europa.eu/consumers/odr/</a>. Unsere E-Mail-Adresse finden Sie oben im Impressum.</p>
      <p>Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>

      <h2>Urheberrechte</h2>
      <p>Alle Inhalte und Werke auf dieser Website sind urheberrechtlich geschützt. Alle Texte, Bilder, Grafiken und Animationsdateien unterliegen dem Urheberrecht und anderen Gesetzen zum Schutz des geistigen Eigentums. Kein Teil der hier abrufbaren Inhalte darf ohne ausdrückliche vorherige schriftliche Erlaubnis der SCHOLPP Holding GmbH bzw. des jeweiligen Autors oder Erstellers zu kommerziellen Zwecken reproduziert, gedruckt, übersetzt, in digitaler Form weiter bearbeitet, in Archive übernommen oder Dritten zugänglich gemacht werden.</p>

      <h2>Haftung</h2>
      <p>Die SCHOLPP Holding GmbH übernimmt keine Haftung für die Aktualität, Richtigkeit und Vollständigkeit der auf dieser Website bereitgestellten Informationen. Gleiches gilt auch für die Inhalte externer Websites, auf die diese Website über Hyperlinks direkt oder indirekt verweist und auf die die SCHOLPP Holding GmbH keinen Einfluss hat. Weiterhin wird jegliche Haftung für Schäden, die direkt oder indirekt aus der Benutzung dieser Website entstehen, ausgeschlossen. Dies gilt nicht, wenn diese Schäden auf Vorsatz oder grober Fahrlässigkeit beruhen.</p>

      <h2>Bildnachweise</h2>
      <p>Fotos: PTC PressEngineering GmbH / SCHOLPP Gruppe (Bestand der Website ptc.eu). <span class="todo">Vor dem Livegang: Bilder lokal ablegen, Rechte und Fotografennennung mit dem Kunden klären; ein Teaserbild stammt von iStock (Nr. 185236343).</span></p>
      <p>Kartendaten: © <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a>-Mitwirkende.</p>
    </div>
  </div>
</section>
"""
page("impressum", "Impressum | PTC PressEngineering GmbH",
     "Impressum der PTC PressEngineering GmbH, Essener Str. 59, 46047 Oberhausen. Registergericht Duisburg HRB 13437, USt-IdNr. DE 212722514.", impressum_body)

# ---------------------------------------------------------------- Datenschutz
datenschutz_body = page_head("Rechtliches", "Datenschutzerklärung", "Für Nutzerinnen und Nutzer der Website der PTC PressEngineering GmbH.") + f"""
<section class="section section--tight">
  <div class="container">
    <div class="prose">
      <h2>1. Verantwortlicher</h2>
      <p>Verantwortlicher gemäß Art. 4 Abs. 7 EU-Datenschutz-Grundverordnung (DSGVO) und den geltenden landesspezifischen Datenschutzbestimmungen ist die:</p>
      <p>PTC PressEngineering GmbH<br>{ADDR_1}<br>{ADDR_2}<br>Deutschland<br>Tel.: <a href="tel:{TEL}">+49 208 81060-0</a><br>E-Mail: <a href="mailto:{MAIL}">{MAIL}</a></p>
      <p>Allgemeine Fragen zum Datenschutz in der PTC PressEngineering GmbH senden Sie bitte an <a href="mailto:{MAIL}">{MAIL}</a>.</p>
      <h3>Datenschutzbeauftragter</h3>
      <p>Unseren Datenschutzbeauftragten Herrn Sven Bartsch erreichen Sie per Post unter der oben genannten Adresse mit dem Zusatz „Datenschutzbeauftragter“ oder per E-Mail: <span class="todo">E-Mail-Adresse des Datenschutzbeauftragten eintragen</span></p>

      <h2>2. Allgemeines zur Datenverarbeitung</h2>
      <p>Personenbezogene Daten unserer Nutzer erheben und verwenden wir nur, soweit dies zur Bereitstellung einer funktionsfähigen Website sowie zur Darstellung unserer Inhalte und Erbringung von Leistungen erforderlich ist. Die Erhebung und Verwendung personenbezogener Daten erfolgt regelmäßig nur nach Einwilligung des Nutzers. Eine Ausnahme gilt in solchen Fällen, in denen eine vorherige Einholung einer Einwilligung aus tatsächlichen Gründen nicht möglich ist und die Verarbeitung der Daten durch gesetzliche Vorschriften gestattet ist.</p>
      <p>Rechtsgrundlagen sind je nach Fall Art. 6 Abs. 1 lit. a DSGVO (Einwilligung), lit. b (Vertrag und vorvertragliche Maßnahmen), lit. c (rechtliche Verpflichtung) oder lit. f (berechtigtes Interesse). Berechtigte Interessen sind insbesondere die korrekte Auslieferung der Inhalte, die Sicherheit unserer Systeme, die Beantwortung von Anfragen sowie die Vermeidung und Aufdeckung von Betrugsfällen und Straftaten.</p>
      <p>Ihre personenbezogenen Daten übertragen wir verschlüsselt (TLS, Transport Layer Security). Wir verarbeiten und speichern sie, solange es für die Erfüllung unserer vertraglichen und gesetzlichen Pflichten erforderlich ist. Danach werden sie regelmäßig gelöscht oder gesperrt, sofern keine gesetzlichen Aufbewahrungspflichten entgegenstehen.</p>

      <h2>3. Hosting und Server-Logfiles</h2>
      <p>Beim Aufruf dieser Website erfasst der Server automatisch Informationen in sogenannten Logfiles: IP-Adresse, Browsertyp und -version, Referrer-URL, aufgerufene Unterseiten, Datenmenge, Datum und Uhrzeit des Zugriffs. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO (Sicherstellung des Betriebs, Gefahrenabwehr). Die Daten werden gelöscht, sobald sie für den Zweck ihrer Erhebung nicht mehr erforderlich sind.</p>
      <p>Hosting-Anbieter: <span class="todo">Anbieter und Serverstandort eintragen</span>. Löschfrist der Logfiles: <span class="todo">eintragen</span>.</p>

      <h2 id="kontaktformular">4. Kontaktformular und E-Mail</h2>
      <p>Auf unserer Website steht Ihnen ein Kontaktformular zur Verfügung. Die eingegebenen Daten (Name, E-Mail-Adresse, Nachricht als Pflichtfelder; Unternehmen, Telefon und Maschinenangaben freiwillig) werden an uns übermittelt und gespeichert. Rechtsgrundlage ist Ihre Einwilligung, Art. 6 Abs. 1 lit. a DSGVO, bei Anbahnung eines Vertrags zusätzlich Art. 6 Abs. 1 lit. b DSGVO. Alternativ können Sie uns per E-Mail kontaktieren; hier ist Art. 6 Abs. 1 lit. f DSGVO die Rechtsgrundlage. Die Daten speichern wir nur, bis die jeweilige Korrespondenz beendet ist. Einwilligungen können Sie jederzeit widerrufen.</p>
      <p><span class="todo">Formulardienst / Empfänger-Postfach eintragen, sobald das Formular angebunden ist. Aktuell ist das Formular eine Demo ohne Datenübertragung.</span></p>

      <h2 id="bewerbung">5. Bewerbungen</h2>
      <p>Bewerbungsunterlagen, die Sie uns per E-Mail oder Post zusenden, verarbeiten wir ausschließlich zur Durchführung des Bewerbungsverfahrens (Art. 6 Abs. 1 lit. b DSGVO, § 26 BDSG). Alle personenbezogenen Daten werden durch technische und organisatorische Maßnahmen gegen unberechtigte Zugriffe und Manipulation geschützt. Kommt es nicht zu einer Einstellung, löschen wir Ihre Unterlagen spätestens sechs Monate nach Abschluss des Verfahrens, sofern Sie nicht in eine längere Aufbewahrung eingewilligt haben.</p>

      <h2>6. Cookies</h2>
      <p>Diese Website setzt keine Tracking- oder Analyse-Cookies ein. Technisch notwendige Speicherung erfolgt nur, soweit sie für die Darstellung der Seite erforderlich ist (Art. 6 Abs. 1 lit. f DSGVO, § 25 Abs. 2 TDDDG). <span class="todo">Bei Einsatz von Google Analytics oder anderen Diensten: Abschnitt und Cookie-Banner ergänzen.</span></p>

      <h2>7. Schriftarten (Google Fonts)</h2>
      <p>Zur einheitlichen Darstellung werden Schriftarten von Google Fonts geladen. Dabei stellt Ihr Browser eine Verbindung zu Servern von Google her und übermittelt Ihre IP-Adresse. Anbieter: Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland. Rechtsgrundlage: Art. 6 Abs. 1 lit. f DSGVO. <span class="todo">Empfehlung: Schriften vor dem Livegang lokal einbinden, dann entfällt dieser Abschnitt.</span></p>

      <h2>8. Karte (OpenStreetMap / Leaflet)</h2>
      <p>Auf den Seiten Start und Kontakt binden wir eine Karte ein. Die Kartenkacheln werden von den Servern der OpenStreetMap Foundation (St John’s Innovation Centre, Cowley Road, Cambridge, CB4 0WS, Vereinigtes Königreich) geladen; dabei wird Ihre IP-Adresse übermittelt. Die Bibliothek Leaflet wird über unpkg.com (Cloudflare, Inc.) geladen. Rechtsgrundlage: Art. 6 Abs. 1 lit. f DSGVO (Darstellung unseres Standorts).</p>

      <h2>9. Externe Inhalte und Links</h2>
      <p>Fotos und PDF-Dokumente dieser Vorschau werden von der bestehenden Website ptc.eu geladen. <span class="todo">Vor dem Livegang lokal ablegen; dann entfällt dieser Hinweis.</span> Für die Inhalte verlinkter externer Websites (z. B. scholpp.de) ist der jeweilige Anbieter verantwortlich.</p>

      <h2>10. Ihre Rechte</h2>
      <p>Sie haben das Recht auf Auskunft (Art. 15 DSGVO), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) und Widerspruch (Art. 21 DSGVO). Beim Auskunfts- und Löschungsrecht gelten die Einschränkungen nach §§ 34 und 35 BDSG. Eine erteilte Einwilligung können Sie jederzeit widerrufen. Darüber hinaus besteht ein Beschwerderecht bei einer Datenschutzaufsichtsbehörde (Art. 77 DSGVO i. V. m. § 19 BDSG), für uns zuständig: Landesbeauftragte für Datenschutz und Informationsfreiheit Nordrhein-Westfalen, Kavalleriestraße 2–4, 40213 Düsseldorf.</p>

      <p style="margin-top:32px">Stand: <span class="todo">Datum eintragen</span></p>
    </div>
  </div>
</section>
"""
page("datenschutz", "Datenschutzerklärung | PTC PressEngineering GmbH",
     "Datenschutzerklärung der PTC PressEngineering GmbH: Verantwortlicher, Server-Logfiles, Kontaktformular, Bewerbungen, Google Fonts, OpenStreetMap, Ihre Rechte.", datenschutz_body)

print("done")
