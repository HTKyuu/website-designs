# Template: PTC PressEngineering GmbH (dunkel)

Statische Website (16 Seiten) für die PTC PressEngineering GmbH, Essener Str. 59, 46047 Oberhausen, Teil der SCHOLPP Gruppe. Dunkles Design aus dem Skill `designing-dark-brand-sites`, Akzent PTC-Rot `#E2001A` aus dem Logo. Eigenes Stylesheet, kein Build-Schritt, kein `shared/ds.css`.

Alle Texte und Fakten stammen von https://www.ptc.eu/ (Stand Oktober 2026): Leistungsbeschreibungen, Geschichte, Referenzen, Managementboard, SCHOLPP-Zahlen, Impressumsdaten, Datenschutzbeauftragter. Die Seitenstruktur folgt der Navigation von ptc.eu (Entscheidung Oktober 2026: „alle Unterseiten“).

## Seiten
| Datei | Entspricht auf ptc.eu |
|---|---|
| `index.html` | Startseite (Hero, Leistungen, Refurbishment, Automatisierung, SCHOLPP, Referenzen, Ablauf, Kontakt, Standort mit Karte) |
| `unternehmen.html` | /de/unternehmen/ |
| `managementboard.html` | /de/unternehmen/managementboard/ |
| `geschichte.html` | /de/unternehmen/geschichte/ (Zeitleiste) |
| `zertifikate-dokumente.html` | /de/unternehmen/zertifikate-dokumente/ |
| `scholpp-gruppe.html` | /de/unternehmen/scholpp-gruppe/ |
| `leistungsspektrum.html` | /de/leistungsspektrum/ |
| `pressen-und-bandanlagen.html` | /de/leistungsspektrum/pressen-und-bandanlagen/ |
| `flexible-montagelinien.html` | /de/leistungsspektrum/flexible-montagelinien/ |
| `robotik.html` | /de/leistungsspektrum/robotik/ |
| `referenzen.html` | /de/referenzen/ inkl. der vier Detailseiten (als Abschnitte mit Ankern) |
| `karriere.html` | /de/karriere/ |
| `news.html` | /de/news/, Newsarchiv und Publikationen (Anker `#archiv`, `#publikationen`) |
| `kontakt.html` | Kontaktformular (auf ptc.eu nur verlinkt) |
| `impressum.html` · `datenschutz.html` | /de/impressum/, /de/datenschutz/ (gekürzt und an die neue Seite angepasst) |

Nicht übernommen: Sitemap, Sprachumschalter Englisch (/en/), Cookie-Banner (kein Tracking im Template).

## Dateien
- `assets/style.css` – Skill-Stylesheet, Kundenfarben im Block „Kundenfarben“ oben; kundenspezifische Komponenten am Ende (`.sub-nav`, `.stats`, `.timeline`, `.refs/.ref`, `.brief`, `.person`, `.downloads/.download`, `.article`, `.gallery`, engere Navigation 900–1180 px, Logo-Höhe 40 px)
- `assets/site.js` – unverändert aus dem Skill: mobiles Menü, Nav beim Scrollen, Demo-Formular, Leaflet-Karte, Jahr im Footer
- `assets/logo-ptc.png` – aus `ptc_logo.png` von ptc.eu umgefärbt: Hintergrund transparent, „PTC PressEngineering“ rot, „SCHOLPP Group“ hellgrau; 3-fach hochskaliert (975 × 195 px)
- `docs/screenshot-*.png` – 1440 × 900 (headless Chrome)

## Farben
- `--accent` #E2001A PTC-Rot (Buttons, Eyebrows, Icons, Hero-Zeile „Händen.“, Schrittnummern, Zeitleiste)
- `--accent-deep` #B30014 für Pins und kleine Akzent-Schrift auf hellen Abschnitten
- Grautöne werden automatisch aus `--accent-rgb` abgeleitet, nicht von Hand ändern

## Vor dem Livegang ersetzen
- **Fotos**: alle Bilder sind Hotlinks auf ptc.eu (`/fileadmin/...`). Rechte liegen beim Kunden bzw. SCHOLPP; ein Teaserbild auf ptc.eu ist iStock Nr. 185236343 (hier nicht verwendet). Bilder lokal ablegen. Auflösungen: Hero 1920 px, Leistungsfotos 900 px, Referenzfotos nur 475 px und Managementfoto 350 px → Originale beim Kunden anfordern. Auf `pressen-und-bandanlagen.html` ist der Abschnitt Sicherheit ein `.media--placeholder`.
- **Logo**: `assets/logo-ptc.png` ist aus einer 325-px-PNG hochskaliert. Vektordaten (SVG/EPS) beim Kunden anfordern.
- **Bürozeiten**: auf ptc.eu nicht angegeben → `<span class="todo">` auf `index.html` (Standort) und `kontakt.html`. Ergänzen oder entfernen.
- **Telefon**: Zentrale 0208 810 60-0 überall, Service-Hotline 01805 758599 zusätzlich in CTA-Box, Footer, Kontakt (Entscheidung Oktober 2026: beide Nummern). Bei Änderung nach `810 60` und `758599` greppen.
- **Formular**: `kontakt.html` `#termin-form` hat keinen Server, zeigt nur die Demo-Erfolgsmeldung. `action`/`method` setzen oder Formulardienst anbinden; danach Datenschutz Abschnitt 4 ergänzen.
- **PDFs** (`zertifikate-dokumente.html`, `news.html`): verlinken auf ptc.eu. Lokal unter `assets/downloads/` ablegen.
- **Managementboard**: ptc.eu nennt nur Wolfgang E. Mueller (SCHOLPP Holding). Weitere Personen und Kontaktdaten beim Kunden erfragen; Hinweis-Kasten auf der Seite entfernen.
- **Karriere / News**: auf ptc.eu aktuell keine Stellen und keine Nachrichten. Bei neuen Inhalten Karten bzw. `.article` ergänzen, Hinweis-Kästen entfernen.
- **Datenschutz**: Hosting-Anbieter, Löschfrist Logfiles, E-Mail des Datenschutzbeauftragten (Sven Bartsch), Formulardienst, Stand-Datum. Google Fonts lokal einbinden und Abschnitt 7 streichen. Abschnitt 9 (externe Inhalte von ptc.eu) nach dem lokalen Ablegen der Bilder streichen.
- **Impressum**: Bildnachweise (`<span class="todo">`). Übrige Angaben sind von ptc.eu übernommen (Geschäftsführender Gesellschafter, HRB 13437 Duisburg, USt-IdNr. DE 212722514, Aufsichtsbehörde, MStV-Verantwortlicher SCHOLPP GmbH Chemnitz).
- **Karte**: Koordinaten 51.4868798, 6.8722333 (Nominatim-Treffer „59, Essener Straße, Oberhausen“). Zoom und Popup über `data-*` am `#map`.
- **Anfahrtstext** („zwischen Innenstadt und Neuer Mitte, A 42 / A 3“) ist nicht von ptc.eu, sondern aus der Lage abgeleitet. Mit dem Kunden prüfen.

## Entscheidungen (Oktober 2026)
- Seitenumfang wie ptc.eu statt kompakter 5-Seiten-Variante
- Logo umgefärbt (PTC rot, Rest weiß/hellgrau) statt Text-Logo oder weißer Box
- Beide Telefonnummern
- Fotos von ptc.eu verlinkt statt Unsplash-Platzhalter
- Kein WhatsApp, keine Google-Bewertungsbox (B2B); stattdessen Kennzahlen (`.stats`) und Trust-Leiste
