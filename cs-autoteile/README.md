# Template: C & S Autoteile (hell + dunkel)

Statische Website (5 Seiten) für die C & S Autoteile Handelsgesellschaft GmbH, Oberhausen. Design aus dem Skill `designing-dark-brand-sites`, erweitert um einen Hell/Dunkel-Umschalter. Akzent ist das Karminrot aus dem Kundenlogo, Dunkelmodus in warmem Anthrazit, Hellmodus Weiß mit dunkelgrauem Text. Eigenes Stylesheet, kein Build-Schritt, kein `shared/ds.css`.

Zielgruppe laut Briefing (Oktober 2026): Privatkunden **und** Werkstätten. Texte sind Branchentexte für einen Autoteile-Fachhandel, keine Aussagen des Kunden. Vor Livegang alle Leistungsversprechen (Lieferservice, Touren, Pfand, Umtausch, Antwortzeit) mit dem Kunden abstimmen.

## Dateien
- `index.html` Start (Hero, Sortiment-Karten, Beratung, Werkstätten, Marken, Ablauf, Kontakt-CTA mit Bewertung, Standort mit Karte)
- `sortiment.html` Sechs Teilebereiche mit Sprungmarken (`#bremsen`, `#filter-oele`, `#fahrwerk`, `#elektrik`, `#motor`, `#zubehoer`)
- `kontakt.html` Teileanfrage-Formular mit HSN/TSN, Infokarten, Anfahrt mit Karte
- `impressum.html` · `datenschutz.html`
- `assets/style.css` komplettes System, Kundenfarben im Block „Kundenfarben" oben, Modus-Tokens direkt darunter
- `assets/site.js` Hell/Dunkel-Umschalter, mobiles Menü, Nav beim Scrollen, Demo-Formular, Leaflet-Karte, Jahr im Footer

## Hell/Dunkel
- Beim ersten Besuch folgt die Seite der Systemeinstellung (`prefers-color-scheme`). Ein Inline-Skript im `<head>` setzt `data-theme` am `<html>`, bevor die Seite rendert (kein Flackern).
- Der Umschalter (Sonne/Mond) sitzt in der Navigation. Die Wahl liegt im `localStorage` unter `cs-theme`. Ohne JavaScript bleibt es dunkel.
- Der Kontrastabschnitt `.section--light` ist im Dunkelmodus hell und im Hellmodus dunkel. Nichts von Hand umfärben, beide Token-Sätze stehen oben in `style.css`.
- Screenshot-Test eines Modus: `localStorage.setItem('cs-theme','light')` in der Konsole oder `document.documentElement.dataset.theme='light'`.

## Farben
- `--accent` #C62A43 C&S-Rot (aus dem Logo gemessen, ca. #C22D43). Weiß darauf 5,4:1, auf Hell 5:1.
- `--accent-deep` #951D30 für Hover im Hellmodus und den Kartenpin.
- Grautöne beider Modi werden aus `--accent-rgb` abgeleitet und sind leicht warm getönt.

## Vor dem Livegang ersetzen
- **Adresse**: Elsa-Brändström-Str. 114, 46045 Oberhausen stammt aus dasoertliche.de (Eintrag „C u. S Autoteile GmbH", gleiche Telefonnummer). Das Briefing nannte Goethestraße 2, 46047 Oberhausen. Noel hat sich für Elsa-Brändström-Str. entschieden; mit dem Kunden bestätigen. Steht in Topbar, Standort, Footer, Kontaktseite, Impressum, Datenschutz und als Google-Maps-Routenlink. Kartenkoordinaten 51.47959, 6.86218 (`data-*` am `#map`).
- **Logo**: Text-Nachbau `.brand--cs` („C&S" in Kaushan Script rot, „AUTOTEILE" in Barlow Condensed). Das gelieferte Logo ist nur 108 × 30 px. Vektordatei (SVG/EPS) anfordern, dann `<a class="brand"><img …></a>` wie im Skill-Beispiel einsetzen und die Google-Font Kaushan Script aus den `<link>`-Tags entfernen.
- **Öffnungszeiten** Mo–Fr 8:00–18:00, Sa 9:00–13:00 sind Platzhalter. Stehen in: Topbar (alle Seiten), `#standort` und Footer (alle Seiten), Hinweis unter dem Formular, Hero-Notiz „Telefonische Beratung" auf der Startseite. Vor Änderung nach `8:00` greppen.
- **E-Mail** `info@cs-autoteile.de` ist erfunden (Footer, Standort-Karten, Kontaktseite). Echte Adresse eintragen, auch in Impressum und Datenschutz (dort als `.todo`).
- **WhatsApp**: `wa.me/49208805959` nutzt die Festnetznummer als Platzhalter. Echte WhatsApp-Business-Nummer eintragen oder entfernen: `.icon-btn--wa` in der Nav, `.btn--whatsapp` in Mobile-Menü, Kontakt-CTA (index, sortiment) und Kontakt-Page-Head, WhatsApp-Zeilen in Footer und Infokarten, Tipp „Kein Fahrzeugschein zur Hand" im Ablauf, Datenschutz Abschnitt 3.
- **Google-Bewertung**: Platzhalter „4,6" in `index.html` (`#kontakt-cta`, HTML-Kommentar TODO). Echten Wert eintragen oder `.rating` entfernen.
- **Marken-Chips** in `index.html#marken` sind eine typische Liste (Bosch, Mann-Filter, Mahle, Brembo, ATE, TRW, Febi Bilstein, Sachs, SKF, Varta, Hella, NGK, Castrol, Liqui Moly). Mit dem Kunden abstimmen.
- **Fotos**: alle Bilder sind Unsplash-Hotlinks (Hero Motorraum, Teilelager, Mechaniker, Ölwechsel, Reifen, Page-Heads). Durch eigene Aufnahmen ersetzen, lokal ablegen, `alt`-Texte prüfen. Zwei Bereiche auf `sortiment.html` (Bremsen, Fahrwerk) haben kein Foto und nutzen `.media--placeholder` mit Icon.
- **Formular**: `kontakt.html` `#anfrage-form` hat keinen Server und zeigt nur die Demo-Erfolgsmeldung. `action`/`method` setzen oder Formulardienst anbinden; danach Datenschutz Abschnitt 4 ergänzen. HSN/TSN-Felder werden per JS in Großbuchstaben gesetzt (`data-upper`).
- **Impressum**: Geschäftsführer, E-Mail, HRB-Nummer (Amtsgericht Duisburg angenommen), USt-IdNr., Verantwortlicher nach § 18 Abs. 2 MStV, Bildnachweise (`<span class="todo">`).
- **Datenschutz**: Hosting-Anbieter, Löschfristen, Formulardienst, Stand-Datum. Google Fonts lokal einbinden und Abschnitt 6 streichen. Leaflet lokal ablegen, dann den unpkg-Hinweis in Abschnitt 5 streichen.
- **Lage-/Anfahrtstexte** („nahe Hauptbahnhof", „Kurzzeitparkplätze", Autobahnabfahrten) und das Liefergebiet (Oberhausen, Mülheim, Bottrop, Essen) sind Annahmen.

## Galerie
Karte in `templates/index.html` (Ordner `cs-autoteile/`). Dev-Server: Launch-Konfiguration „templates" (python http.server, Port 5510).
