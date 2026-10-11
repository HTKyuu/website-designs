/* Elektro Lüdtke — page behaviour on top of ds.js:
   extra icons, light/dark toggle, Leistungen jump bar, contact form prefill */
(function () {
  "use strict";

  var THEME_KEY = "luedtke-theme";

  /* Icons missing from the ds.js sprite --------------------------------- */
  var EXTRA_ICONS = {
    zap: '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
    sun: '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
    moon: '<path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/>',
    lightbulb: '<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.6 10.8c.6.5 1 1.2 1.1 2V16h5v-.2c.1-.8.5-1.5 1.1-2A6 6 0 0 0 12 3z"/>',
    network: '<rect x="9" y="3" width="6" height="5" rx="1"/><rect x="2" y="16" width="6" height="5" rx="1"/><rect x="16" y="16" width="6" height="5" rx="1"/><path d="M12 8v4M5 16v-2a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v2"/>',
    cpu: '<rect x="6" y="6" width="12" height="12" rx="1.5"/><rect x="9.5" y="9.5" width="5" height="5"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>',
    "clipboard-check": '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1M9 13l2 2 4-4"/>',
    camera: '<path d="M3 7h12v10H3zM15 10.5 21 7v10l-6-3.5"/>',
    flame: '<path d="M12 22a7 7 0 0 0 7-7c0-3-2-5.5-3.5-7-.3 2-1.3 3.2-2.5 3.7.3-3-1-6-4-8.7.2 3.6-4 6.4-4 12A7 7 0 0 0 12 22z"/>',
    printer: '<path d="M6 9V3h12v6M6 17H4a1 1 0 0 1-1-1v-6a1 1 0 0 1 1-1h16a1 1 0 0 1 1 1v6a1 1 0 0 1-1 1h-2"/><rect x="6" y="14" width="12" height="7"/>',
    smartphone: '<rect x="6" y="2" width="12" height="20" rx="2"/><path d="M11 18h2"/>',
    facebook: '<path d="M15 3h-2.5A3.5 3.5 0 0 0 9 6.5V10H6.5v3.5H9V21h3.5v-7.5H15l.5-3.5h-3V7a1 1 0 0 1 1-1H15z"/>',
    tv: '<rect x="3" y="6" width="18" height="12" rx="1.5"/><path d="m8 2 4 4 4-4M8 21h8"/>',
    thermometer: '<path d="M14 14.8V4a2 2 0 0 0-4 0v10.8a4 4 0 1 0 4 0z"/><path d="M12 9v8"/>',
    waves: '<path d="M2 8c2-2 4-2 6 0s4 2 6 0 4-2 6 0M2 16c2-2 4-2 6 0s4 2 6 0 4-2 6 0"/>',
    store: '<path d="M4 9h16l-1.5-5h-13zM5 9v11h14V9M9 20v-6h6v6"/>',
    door: '<path d="M5 21V3h11v18M3 21h18M13 12h.01"/>',
    battery: '<rect x="2" y="7" width="17" height="10" rx="2"/><path d="M22 11v2M7 10l-1.5 2h3L7 14"/>'
  };

  function addIcons() {
    var sprite = document.getElementById("ds-sprite");
    if (!sprite) return;
    var ns = "http://www.w3.org/2000/svg";
    Object.keys(EXTRA_ICONS).forEach(function (name) {
      if (document.getElementById("i-" + name)) return;
      var symbol = document.createElementNS(ns, "symbol");
      symbol.setAttribute("id", "i-" + name);
      symbol.setAttribute("viewBox", "0 0 24 24");
      symbol.innerHTML = EXTRA_ICONS[name];
      sprite.appendChild(symbol);
    });
  }

  /* Light / dark --------------------------------------------------------
     The inline <head> script sets data-theme before first paint. Here we
     wire the toggle buttons and follow the OS while no choice is stored. */
  function storedTheme() {
    try { return localStorage.getItem(THEME_KEY); } catch (e) { return null; }
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    var dark = theme === "dark";
    Array.prototype.forEach.call(document.querySelectorAll("[data-theme-toggle]"), function (btn) {
      btn.setAttribute("aria-pressed", dark ? "true" : "false");
      btn.setAttribute("aria-label", dark ? "Helles Design einschalten" : "Dunkles Design einschalten");
      btn.setAttribute("data-tooltip", dark ? "Hell" : "Dunkel");
    });
  }

  function initTheme() {
    applyTheme(document.documentElement.getAttribute("data-theme") === "dark" ? "dark" : "light");
    document.addEventListener("click", function (e) {
      if (!e.target.closest("[data-theme-toggle]")) return;
      var next = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
      applyTheme(next);
      try { localStorage.setItem(THEME_KEY, next); } catch (err) { /* private mode: choice lasts for this page only */ }
    });
    var mq = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)");
    if (mq && mq.addEventListener) {
      mq.addEventListener("change", function (e) {
        var s = storedTheme();
        if (s !== "light" && s !== "dark") applyTheme(e.matches ? "dark" : "light");
      });
    }
  }

  /* Leistungen jump bar: highlight the section in view ------------------ */
  function initSubnav() {
    var nav = document.querySelector("[data-subnav]");
    if (!nav || !("IntersectionObserver" in window)) return;
    var links = Array.prototype.slice.call(nav.querySelectorAll("a[href^='#']"));
    var byId = {};
    links.forEach(function (a) { byId[a.getAttribute("href").slice(1)] = a; });
    function mark(id) {
      links.forEach(function (a) {
        if (a === byId[id]) {
          a.setAttribute("aria-current", "true");
          // keep the active pill visible on narrow screens
          var list = a.parentElement.parentElement;
          var left = a.offsetLeft - list.clientWidth / 2 + a.clientWidth / 2;
          list.scrollTo({ left: left, behavior: "smooth" });
        } else {
          a.removeAttribute("aria-current");
        }
      });
    }
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) { if (entry.isIntersecting) mark(entry.target.id); });
    }, { rootMargin: "-35% 0px -60% 0px" });
    Object.keys(byId).forEach(function (id) {
      var section = document.getElementById(id);
      if (section) observer.observe(section);
    });
  }

  /* Contact form: preselect the service from ?leistung=… ---------------- */
  function initContactPrefill() {
    var select = document.getElementById("c-service");
    if (!select) return;
    var match = /[?&]leistung=([^&#]+)/.exec(window.location.search);
    if (!match) return;
    var value = decodeURIComponent(match[1]);
    Array.prototype.forEach.call(select.options, function (opt) {
      if (opt.value === value) select.value = value;
    });
  }

  function initYear() {
    Array.prototype.forEach.call(document.querySelectorAll("[data-year]"), function (el) {
      el.textContent = new Date().getFullYear();
    });
  }

  initTheme();
  document.addEventListener("ds:ready", function () {
    addIcons();
    initSubnav();
    initContactPrefill();
    initYear();
  });
})();
