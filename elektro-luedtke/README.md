# Elektro Lüdtke – Website-Vorlage

Statische Website für **Elektro Lüdtke** (Inhaber Thomas Lüdtke, Im Lipperfeld 34a, 46047 Oberhausen). Inhalte und Daten stammen von der alten Seite http://www.elektro-luedtke.de/ (Stand Oktober 2026). Das Design ist die Transvera-Vorlage (`templates/transvera`) mit Lüdtke-Farben und einem Hell/Dunkel-Umschalter.

Einfach `index.html` öffnen. Es gibt keinen Build-Schritt und kein Framework.

## Entscheidungen (Interview vom 11.10.2026)

| Thema | Entscheidung |
|---|---|
| Seiten | Kompakt: Start, Leistungen (alle 6 Bereiche auf einer Seite), 24h Notdienst, Kontakt, Impressum, Datenschutz. Die alte Partner-Seite ist entfallen. |
| Leistungsseite | Abschnitte untereinander, darüber eine klebende Sprungleiste (Anker `#hausinstallation`, `#knx`, `#netzwerk`, `#e-check`, `#sicherheit`, `#licht`) |
| Farben | Lüdtke-Gelb `#FCB913` und Anthrazit; Gelb nur als Fläche mit dunkler Schrift, Text/Icons im hellen Modus in Bernstein `#8A5A00` |
| Logo | Als SVG nachgebaut (graue/gelbe „EL“-Blöcke + Schriftzug), inline im Header/Footer und als Favicon |
| Hero-Box | Notdienst-Box (statt Transvera „Sendung verfolgen“) |
| Zahlen-Streifen | Platzhalter `[XX]` Jahre / `[XXX]` Projekte + echte Fakten 24/7 und 6 Fachbereiche |
| Partner | Marken-Leiste auf der Startseite (KNX, ABB, Siedle, Esser) als Textlogos |
| Texte | Original-Inhalte überarbeitet und gekürzt, Tippfehler und veraltete Stellen (ISDN, Zitate) entfernt |
| Fotos | Kundenfotos lokal (`assets/img/knx-bedienfeld.jpg`, `netzwerk.jpg`), Rest von Unsplash (verlinkt) |
| Hell/Dunkel | Erster Besuch folgt der System-Einstellung, Knopf im Header speichert die Wahl (`localStorage` `luedtke-theme`); kein Aufblitzen dank Inline-Skript im `<head>` |
| Dark Mode | Anthrazit `#16191D`, Karten `#1F2329`, Header/Footer `#0F1114` |
| Formular | Platzhalter: prüft Eingaben und zeigt eine Danke-Meldung, **versendet aber nichts** |
| Karte | Google Maps direkt eingebettet (Kontaktseite) |
| Extras | Notdienst-Leiste oben (nicht wegklickbar), Facebook-Link, Faxnummer, Bürozeiten-Platzhalter, feste Anrufleiste auf dem Handy |

## Platzhalter – vor Livegang klären

Platzhalter sind auf der Seite **gelb unterstrichen** (CSS-Klasse `.ph`).

- [ ] **Zahlen** auf der Startseite: `[XX]` Jahre Erfahrung, `[XXX]` Projekte (`index.html`)
- [ ] **Bürozeiten** `Mo–Fr 8:00–17:00` (Footer aller Seiten + `kontakt.html`)
- [ ] **Impressum:** USt-IdNr., Berufsbezeichnung, zuständige Handwerkskammer (vermutlich HWK Düsseldorf), Innung
- [ ] **Datenschutz:** Hoster, Löschfrist der Logfiles, Formular-Dienstleister, Rechtsgrundlage Google Maps, Stand – **rechtlich prüfen lassen**
- [ ] **Google Maps** lädt sofort. Nach DSGVO ist dafür eigentlich eine Einwilligung nötig (Consent-Banner oder „Karte erst nach Klick laden“).
- [ ] **Formular anschließen**, z. B. bei Formspree: in `kontakt.html` `action="https://formspree.io/f/XXXX" method="POST"` setzen und in einem kleinen Skript beim Event `ds:submit` per `fetch` absenden (das Transvera-Formular verhindert das normale Absenden).
- [ ] Ob die **Steuernummer** im Impressum stehen soll (stand auf der alten Seite, Pflicht ist sie nicht)
- [ ] Eigene **Fotos** vom Betrieb statt Unsplash, wenn vorhanden

## Aufbau

```
elektro-luedtke/
├── index.html, leistungen.html, notdienst.html, kontakt.html, impressum.html, datenschutz.html
└── assets/
    ├── ds.css / ds.js     unveränderte Kopie des Transvera-Designsystems
    ├── theme.css          Lüdtke-Tokens (hell + [data-theme="dark"]) und Seitenbausteine
    ├── site.js            Zusatz-Icons, Hell/Dunkel-Knopf, Sprungleiste, ?leistung= im Formular
    ├── fonts/             Public Sans 400–700 (lokal, keine Google-Fonts-Anfrage)
    └── img/               Kundenfotos
```

- Header, Footer, Notdienst-Leiste und Anrufleiste sind auf allen Seiten gleich. Wer Telefonnummern ändert, muss das in allen 6 Dateien tun (Suchen & Ersetzen).
- „Angebot anfragen“ auf der Leistungsseite verlinkt auf `kontakt.html?leistung=<id>` und wählt die Leistung im Formular vor.
- Farben ändern: nur die Tokens oben in `assets/theme.css` (`:root` und `:root[data-theme="dark"]`).
