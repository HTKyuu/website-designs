/* Autohaus Pezzei – Seitenverhalten
   - Farbwelt-Umschalter (A Nacht / B Rot), gespeichert im Browser
   - Mobiles Menü
   - Navigation beim Scrollen
   - Terminformular (Demo ohne Server)
   - OpenStreetMap-Karte (Leaflet), nur wenn #map vorhanden ist
*/
(function () {
  'use strict';
  var root = document.documentElement;
  var STORAGE_KEY = 'pezzei-theme';

  /* ---- Farbwelt ---- */
  function applyTheme(name) {
    root.setAttribute('data-theme', name);
    try { localStorage.setItem(STORAGE_KEY, name); } catch (e) { /* privater Modus */ }
    document.querySelectorAll('[data-theme-set]').forEach(function (btn) {
      btn.setAttribute('aria-pressed', btn.getAttribute('data-theme-set') === name ? 'true' : 'false');
    });
  }
  document.querySelectorAll('[data-theme-set]').forEach(function (btn) {
    btn.addEventListener('click', function () { applyTheme(btn.getAttribute('data-theme-set')); });
  });
  // ?theme=rot oder ?theme=nacht in der Adresse überschreibt die gespeicherte Wahl (praktisch zum Teilen eines Links)
  var fromUrl = (location.search.match(/[?&]theme=(rot|nacht)/) || [])[1];
  applyTheme(fromUrl || root.getAttribute('data-theme') || 'nacht');

  /* ---- Navigation ---- */
  var nav = document.querySelector('.nav');
  var burger = document.querySelector('.nav__burger');
  var menu = document.getElementById('mobile-menu');
  function onScroll() { if (nav) nav.classList.toggle('is-scrolled', window.scrollY > 8); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  if (burger && menu) {
    burger.addEventListener('click', function () {
      var open = !menu.classList.contains('is-open');
      menu.classList.toggle('is-open', open);
      burger.setAttribute('aria-expanded', String(open));
      burger.querySelector('.i-open').style.display = open ? 'none' : '';
      burger.querySelector('.i-close').style.display = open ? '' : 'none';
      document.body.style.overflow = open ? 'hidden' : '';
    });
    menu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { burger.click(); });
    });
  }

  /* ---- Terminformular (Demo) ---- */
  var form = document.getElementById('termin-form');
  if (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var success = document.getElementById('form-success');
      var name = form.querySelector('[name="name"]').value.trim();
      success.querySelector('[data-name]').textContent = name ? ' ' + name.split(' ')[0] : '';
      form.hidden = true;
      success.classList.add('is-visible');
      success.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
  }

  /* ---- Karte ---- */
  var mapEl = document.getElementById('map');
  if (mapEl && window.L) {
    var pos = [51.484619, 6.879238]; // Im Lipperfeld 3a, 46047 Oberhausen
    var map = L.map(mapEl, { scrollWheelZoom: false }).setView(pos, 15);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>-Mitwirkende'
    }).addTo(map);
    var pin = L.divIcon({ className: '', html: '<div class="pz-pin"></div>', iconSize: [18, 18], iconAnchor: [9, 9] });
    L.marker(pos, { icon: pin }).addTo(map)
      .bindPopup('<strong>Autohaus Pezzei e.K.</strong><br>Im Lipperfeld 3a<br>46047 Oberhausen')
      .openPopup();
  } else if (mapEl) {
    mapEl.innerHTML = '<div class="map-fallback">Karte konnte nicht geladen werden.<br>Adresse: Im Lipperfeld 3a, 46047 Oberhausen</div>';
  }

  /* ---- Jahr im Footer ---- */
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
