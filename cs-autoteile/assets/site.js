/* C & S Autoteile – Seitenverhalten (Basis: Skill designing-dark-brand-sites)
   - Hell/Dunkel-Umschalter (data-theme am <html>, gespeichert unter "cs-theme")
   - Mobiles Menü
   - Navigation beim Scrollen
   - Anfrageformular (Demo ohne Server)
   - OpenStreetMap-Karte (Leaflet), nur wenn #map vorhanden ist
*/
(function () {
  'use strict';
  var root = document.documentElement;

  /* ---- Hell/Dunkel ---- */
  var STORAGE_KEY = 'cs-theme';
  function applyTheme(theme) {
    root.setAttribute('data-theme', theme);
    document.querySelectorAll('[data-theme-toggle]').forEach(function (btn) {
      btn.setAttribute('aria-label', theme === 'light' ? 'Dunklen Modus einschalten' : 'Hellen Modus einschalten');
    });
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', theme === 'light' ? '#F5F5F5' : '#181818');
  }
  function storedTheme() {
    try { var t = localStorage.getItem(STORAGE_KEY); return (t === 'light' || t === 'dark') ? t : null; } catch (e) { return null; }
  }
  applyTheme(root.getAttribute('data-theme') === 'light' ? 'light' : 'dark');
  document.querySelectorAll('[data-theme-toggle]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
      applyTheme(next);
      try { localStorage.setItem(STORAGE_KEY, next); } catch (e) { /* privater Modus */ }
    });
  });
  if (window.matchMedia) {
    var mq = window.matchMedia('(prefers-color-scheme: light)');
    var onChange = function (ev) { if (!storedTheme()) applyTheme(ev.matches ? 'light' : 'dark'); };
    if (mq.addEventListener) mq.addEventListener('change', onChange); else if (mq.addListener) mq.addListener(onChange);
  }

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

  /* ---- Anfrageformular (Demo) ---- */
  var form = document.getElementById('anfrage-form');
  if (form) {
    // HSN/TSN: Großschreibung, keine Leerzeichen
    form.querySelectorAll('[data-upper]').forEach(function (input) {
      input.addEventListener('input', function () { input.value = input.value.toUpperCase().replace(/\s+/g, ''); });
    });
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
    // Koordinaten und Text kommen aus data-Attributen: <div id="map" data-lat=".." data-lng=".." data-title=".." data-address="Straße<br>Ort">
    var pos = [parseFloat(mapEl.dataset.lat), parseFloat(mapEl.dataset.lng)];
    var map = L.map(mapEl, { scrollWheelZoom: false }).setView(pos, parseInt(mapEl.dataset.zoom || '15', 10));
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>-Mitwirkende'
    }).addTo(map);
    var pin = L.divIcon({ className: '', html: '<div class="map-pin"></div>', iconSize: [18, 18], iconAnchor: [9, 9] });
    L.marker(pos, { icon: pin }).addTo(map)
      .bindPopup('<strong>' + (mapEl.dataset.title || '') + '</strong><br>' + (mapEl.dataset.address || ''))
      .openPopup();
  } else if (mapEl) {
    mapEl.innerHTML = '<div class="map-fallback">Karte konnte nicht geladen werden.<br>' + (mapEl.dataset.address || '') + '</div>';
  }

  /* ---- Jahr im Footer ---- */
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
