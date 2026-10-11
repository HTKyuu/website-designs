# Template: Küchen Horstmann (dunkel)

Statische Website (5 Seiten) für das Küchenhaus Küchen Horstmann, Oberhausen-Sterkrade. Dunkles Design aus dem Skill `designing-dark-brand-sites`, Akzent Rot + Gelb aus dem Kundenlogo. Eigenes Stylesheet, kein Build-Schritt, kein `shared/ds.css`.

Alle Texte und Fakten stammen von https://www.kuechen-horstmann.com/ (Stand Oktober 2026): Adresse, Telefon, E-Mail, Öffnungszeiten, Impressumsdaten, Leistungen, Marken, Show-Küche, Stellenangebote.

## Dateien
- `index.html` Start (Hero, Leistungen, Ausstellung, Preise & Service, Show-Küche, Marken, Ablauf, Kontakt-CTA, Standort)
- `kontakt.html` Formular, Infokarten, Karte
- `jobs.html` Zwei Stellenanzeigen, Über uns
- `impressum.html` · `datenschutz.html`
- `assets/style.css` – komplettes System, Kundenfarben im Block „Kundenfarben“ oben
- `assets/site.js` – mobiles Menü, Nav beim Scrollen, Demo-Formular, Leaflet-Karte, Jahr im Footer

## Farben
- `--accent` #DC2B1B Horstmann-Rot (Buttons, Eyebrows, Icons, Schrittnummern)
- `--accent-2` #FFD60A Horstmann-Gelb, nur für: Hero-Zeile „Horstmann!“, Badge „Küchen auf 3 Etagen“, Sterne der Bewertungsbox
- Grautöne werden automatisch aus `--accent-rgb` abgeleitet, nicht von Hand ändern

## Vor dem Livegang ersetzen
- **Fotos**: alle Bilder sind Unsplash-Platzhalter (Hotlinks). Durch eigene Aufnahmen ersetzen, lokal ablegen, `alt`-Texte prüfen. Stellen: Hero und `page-head` auf jeder Seite, drei `split__media` auf der Startseite.
- **Foto Familie Behmer** in `jobs.html` (Abschnitt `#ueber-uns`, aktuell `.media--placeholder`). Original auf der alten Seite: `grafiken/wir/neu/behmer_kuechen-horstmann.jpg`, Rechte klären.
- **Logo**: `assets/logo-horstmann.png` (Wortmarke, weiß) und `assets/slogan-3-etagen.png` (Schriftzug „Küchen auf 3 Etagen“, gelb) sind aus der Kopfgrafik der alten Website freigestellt, niedrig aufgelöst (720 px bzw. 186 px breit). Vom Kunden Vektordaten (SVG/EPS) anfordern und ersetzen. Die Wortmarke steht in Header und Footer, der Slogan oben rechts im Hero (`.hero__slogan`, unter 520 px ausgeblendet).
- **Google-Bewertung**: Platzhalter „4,7“ in `index.html` (`#kontakt-cta`, HTML-Kommentar TODO). Echten Wert eintragen oder `.rating` entfernen.
- **Formular**: `kontakt.html` `#termin-form` hat keinen Server, zeigt nur die Demo-Erfolgsmeldung. `action`/`method` setzen oder Formulardienst anbinden; danach Datenschutz Abschnitt 4 ergänzen.
- **Impressum**: Verantwortlich nach § 18 Abs. 2 MStV, Bildnachweise (`<span class="todo">`).
- **Datenschutz**: Hosting-Anbieter, Löschfrist Logfiles, Formulardienst, Stand-Datum. Google Fonts lokal einbinden und Abschnitt 6 streichen.
- **Öffnungszeiten** stehen an fünf Stellen (Topbar, Hero-Notiz Ausstellung, Hours-Karten, Footer, Kontaktseite). Bei Änderung nach `10:00` greppen.
- **Karte**: Koordinaten 51.51889, 6.84672 (Nominatim-Treffer „Küchen Horstmann“). Zoom und Popup über `data-*` am `#map`.
- Prospekt-PDFs sind bewusst nicht verlinkt (Entscheidung Oktober 2026). Bei Bedarf Kachel mit Links auf `pdf/prospekte/…` der Kundenseite ergänzen.

## Nicht enthalten (vom Original)
Eigene Seiten für Küchen, E-Geräte, Granit, Zubehör, Ausstellung, Marken, Service, Anfahrt, Prospekt – alles als Abschnitte auf der Startseite zusammengefasst. WhatsApp gibt es beim Kunden nicht, daher kein Button.
