# Template: Autohaus Pezzei

Statische Website (6 Seiten) für ein Autohaus mit Werkstatt. Eigenes Stylesheet, kein Build-Schritt.

## Dateien
- `index.html` Start · `leistungen.html` · `fahrzeuge.html` · `kontakt.html` · `impressum.html` · `datenschutz.html`
- `assets/style.css` – alle Styles, zwei Farbwelten über `data-theme` auf `<html>`
- `assets/site.js` – Farbwelt-Umschalter, mobiles Menü, Demo-Formular, Karte
- `assets/logo.png` – Original-Logo (weiß, transparent)

## Farbwelten
- **A Nacht** (`data-theme="nacht"`): fast schwarz, Pezzei-Rot als Akzent
- **B Rot** (`data-theme="rot"`): Pezzei-Rot als Fläche, Weiß als Akzent

Umschalter oben in der Infoleiste. Die Wahl wird im Browser gespeichert (`localStorage`, Schlüssel `pezzei-theme`).
Direktlink: `index.html?theme=rot` bzw. `?theme=nacht`. Zum Festlegen einer Variante den Umschalter entfernen und `data-theme` im `<html>`-Tag setzen.

## Vor dem Livegang ersetzen
- Fotos (aktuell Unsplash-Links) durch eigene Bilder, lokal ablegen
- Google-Bewertung (Platzhalter „4,8“ in `index.html` und `leistungen.html`/`fahrzeuge.html`, Abschnitt `#kontakt-cta`)
- Beispiel-Fahrzeuge und mobile.de-Link in `fahrzeuge.html`
- Formular-Ziel in `kontakt.html` (`#termin-form` hat keinen Server)
- Impressum: Registergericht, Handwerkskammer · Datenschutz: Hosting-Anbieter
- Google Fonts lokal einbinden (Datenschutz)
