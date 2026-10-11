/* Dark Brand Site – Seitenverhalten (Skill: designing-dark-brand-sites)
   - Mobiles Menü
   - Navigation beim Scrollen
   - Terminformular (Demo ohne Server)
   - OpenStreetMap-Karte (Leaflet), nur wenn #map vorhanden ist
*/
(function () {
  'use strict';
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
