/* ==========================================================================
   Enterprise Design System — interactions
   Dependency-free. Behaviour is attached via data attributes:
     data-dropdown / data-dropdown-trigger   disclosure menus
     role="tablist" (inside [data-tabs])     tabs with arrow-key support
     data-modal-open="id" / data-modal-close native <dialog> modals
     data-tooltip="text"                     tooltips
     form[data-validate]                     inline validation
     data-nav-toggle="id"                    mobile navigation
   Public API: window.DS.toast(), DS.setLoading(), DS.icon()
   ========================================================================== */
(function () {
  "use strict";

  /* ------------------------------------------------------------------------
     Icons — injected as an inline sprite so <use href="#i-name"> works
     from file:// as well as from a server.
     ------------------------------------------------------------------------ */
  var ICONS = {
    search: '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    "chevron-down": '<path d="m6 9 6 6 6-6"/>',
    "chevron-up": '<path d="m6 15 6-6 6 6"/>',
    "chevron-right": '<path d="m9 6 6 6-6 6"/>',
    "chevron-left": '<path d="m15 6-6 6 6 6"/>',
    "chevrons-up-down": '<path d="m7 15 5 5 5-5M7 9l5-5 5 5"/>',
    check: '<path d="M20 6 9 17l-5-5"/>',
    x: '<path d="M18 6 6 18M6 6l12 12"/>',
    info: '<circle cx="12" cy="12" r="9"/><path d="M12 16v-5M12 8h.01"/>',
    "alert-circle": '<circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16h.01"/>',
    "alert-triangle": '<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/>',
    "check-circle": '<circle cx="12" cy="12" r="9"/><path d="m8.5 12.5 2.5 2.5 5-5"/>',
    menu: '<path d="M4 6h16M4 12h16M4 18h16"/>',
    "arrow-right": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    calendar: '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 10h18"/>',
    clock: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "file-text": '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h6"/>',
    truck: '<path d="M3 6h11v10H3zM14 9h4l3 3v4h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    package: '<path d="M21 8 12 3 3 8v8l9 5 9-5z"/><path d="m3 8 9 5 9-5M12 13v8"/>',
    ship: '<path d="M3 17c1.5 1.5 3 2 4.5 2s3-.5 4.5-2c1.5 1.5 3 2 4.5 2s3-.5 4.5-2"/><path d="M5 15 4 10h16l-1 5M8 10V6h8v4M12 3v3"/>',
    plane: '<path d="M10.5 13.5 3 11l1.5-1.5 8 1 4-4a2.1 2.1 0 0 1 3 3l-4 4 1 8L15 23l-2.5-7.5L9 19v3l-1.5 1L6 19l-4-1.5L3 16h3z"/>',
    train: '<rect x="5" y="3" width="14" height="14" rx="3"/><path d="M5 11h14M9 17l-2 4M15 17l2 4M9 14h.01M15 14h.01"/>',
    "map-pin": '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    phone: '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    mail: '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    shield: '<path d="M12 3 4 6v6c0 5 3.4 8.5 8 9 4.6-.5 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
    lock: '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
    users: '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M21.5 20a6.5 6.5 0 0 0-4-6"/>',
    user: '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    sliders: '<path d="M4 6h10M18 6h2M4 12h4M12 12h8M4 18h12"/><circle cx="16" cy="6" r="2"/><circle cx="10" cy="12" r="2"/><circle cx="18" cy="18" r="2"/>',
    home: '<path d="M3 11 12 4l9 7"/><path d="M5 10v10h14V10"/>',
    "bar-chart": '<path d="M3 20h18M7 16v-5M12 16V6M17 16v-8"/>',
    filter: '<path d="M3 5h18l-7 8v6l-4 2v-8z"/>',
    download: '<path d="M12 4v11M7 10l5 5 5-5M4 20h16"/>',
    upload: '<path d="M12 20V9M7 14l5-5 5 5M4 4h16"/>',
    more: '<circle cx="5" cy="12" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/>',
    external: '<path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/>',
    ruler: '<path d="M3 17 17 3l4 4L7 21z"/><path d="m7 13 2 2M10 10l2 2M13 7l2 2"/>',
    layers: '<path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/>',
    wrench: '<path d="M15 4a5 5 0 0 0-4.6 6.9L3 18.3 5.7 21l7.4-7.4A5 5 0 0 0 20 9l-3 3-3-1-1-3z"/>',
    plus: '<path d="M12 5v14M5 12h14"/>',
    refresh: '<path d="M20 11a8 8 0 0 0-14.6-4.6L4 8M4 4v4h4M4 13a8 8 0 0 0 14.6 4.6L20 16M20 20v-4h-4"/>',
    globe: '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z"/>',
    building: '<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M9 7h1M14 7h1M9 11h1M14 11h1M9 15h1M14 15h1M10 21v-3h4v3"/>',
    "credit-card": '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20M6 15h4"/>',
    inbox: '<path d="M3 13h5l1.5 3h5L16 13h5"/><path d="M5.5 5h13L21 13v6a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1v-6z"/>',
    grid: '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
    plug: '<path d="M9 3v5M15 3v5M6 8h12v3a6 6 0 0 1-12 0zM12 17v4"/>',
    route: '<circle cx="6" cy="19" r="2"/><circle cx="18" cy="5" r="2"/><path d="M8 19h8a3.5 3.5 0 0 0 0-7H8a3.5 3.5 0 0 1 0-7h8"/>',
    message: '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>',
    bell: '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a2 2 0 0 0 3.4 0"/>',
    activity: '<path d="M3 12h4l3-8 4 16 3-8h4"/>',
    receipt: '<path d="M5 3h14v18l-3-2-2 2-2-2-2 2-2-2-3 2z"/><path d="M9 8h6M9 12h6M9 16h3"/>',
    workflow: '<rect x="3" y="3" width="7" height="6" rx="1"/><rect x="14" y="15" width="7" height="6" rx="1"/><path d="M6.5 9v3a3 3 0 0 0 3 3H14"/>',
    key: '<circle cx="8" cy="15" r="4"/><path d="m11 12 9-9M17 6l3 3M14 9l2 2"/>',
    server: '<rect x="3" y="4" width="18" height="7" rx="1"/><rect x="3" y="13" width="18" height="7" rx="1"/><path d="M7 7.5h.01M7 16.5h.01"/>',
    "log-in": '<path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4M10 17l5-5-5-5M15 12H3"/>',
    euro: '<path d="M17 6.5A7 7 0 1 0 17 17.5M4 10h9M4 14h9"/>',
    pencil: '<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="m13.5 6.5 4 4"/>',
    eye: '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    award: '<circle cx="12" cy="9" r="6"/><path d="m8.5 14-1.5 7 5-3 5 3-1.5-7"/>',
    leaf: '<path d="M5 19c0-8 5-14 15-15-1 10-7 15-15 15z"/><path d="M5 19 13 11"/>',
    box: '<path d="M3 7h18v13H3zM3 7l2-4h14l2 4M10 11h4"/>',
    sparkle: '<path d="M12 3v4M12 17v4M3 12h4M17 12h4"/>',
    copy: '<rect x="8" y="8" width="13" height="13" rx="2"/><path d="M16 8V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h3"/>',
    "trending-up": '<path d="m3 17 6-6 4 4 8-8M15 7h6v6"/>'
  };

  function injectSprite() {
    if (document.getElementById("ds-sprite")) return;
    var symbols = Object.keys(ICONS).map(function (name) {
      return '<symbol id="i-' + name + '" viewBox="0 0 24 24">' + ICONS[name] + "</symbol>";
    }).join("");
    var wrap = document.createElement("div");
    wrap.innerHTML = '<svg id="ds-sprite" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" style="position:absolute;width:0;height:0;overflow:hidden">' + symbols + "</svg>";
    document.body.insertBefore(wrap.firstChild, document.body.firstChild);
  }

  function icon(name, cls) {
    return '<svg class="icon' + (cls ? " " + cls : "") + '" aria-hidden="true"><use href="#i-' + name + '"/></svg>';
  }

  /* ------------------------------------------------------------------------
     Helpers
     ------------------------------------------------------------------------ */
  var FOCUSABLE = 'a[href], button:not([disabled]), input:not([disabled]):not([type="hidden"]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])';

  function $all(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }

  function setLoading(btn, isLoading) {
    if (!btn) return;
    btn.classList.toggle("is-loading", !!isLoading);
    btn.setAttribute("aria-busy", isLoading ? "true" : "false");
    if (isLoading) btn.setAttribute("disabled", ""); else btn.removeAttribute("disabled");
  }

  /* ------------------------------------------------------------------------
     Toasts
     ------------------------------------------------------------------------ */
  var toastRegion;
  function getToastRegion() {
    if (toastRegion) return toastRegion;
    toastRegion = document.createElement("div");
    toastRegion.className = "toast-region";
    toastRegion.setAttribute("role", "region");
    toastRegion.setAttribute("aria-label", "Benachrichtigungen");
    toastRegion.setAttribute("aria-live", "polite");
    document.body.appendChild(toastRegion);
    return toastRegion;
  }

  function toast(opts) {
    opts = opts || {};
    var variant = opts.variant || "info";
    var iconName = { success: "check-circle", warning: "alert-triangle", danger: "alert-circle", info: "info" }[variant];
    var el = document.createElement("div");
    el.className = "toast toast--" + variant;
    el.setAttribute("role", variant === "danger" ? "alert" : "status");
    el.innerHTML = icon(iconName) +
      '<div class="toast-body">' +
        (opts.title ? '<div class="toast-title"></div>' : "") +
        (opts.message ? '<div class="toast-message"></div>' : "") +
      "</div>" +
      '<button type="button" class="toast-close" aria-label="Benachrichtigung schließen">' + icon("x", "icon--sm") + "</button>";
    if (opts.title) el.querySelector(".toast-title").textContent = opts.title;
    if (opts.message) el.querySelector(".toast-message").textContent = opts.message;

    function dismiss() {
      if (!el.isConnected) return;
      el.classList.add("is-leaving");
      setTimeout(function () { el.remove(); }, 160);
    }
    el.querySelector(".toast-close").addEventListener("click", dismiss);
    getToastRegion().appendChild(el);

    var timeout = opts.timeout === undefined ? 6000 : opts.timeout;
    if (timeout) {
      var timer = setTimeout(dismiss, timeout);
      el.addEventListener("mouseenter", function () { clearTimeout(timer); });
      el.addEventListener("mouseleave", function () { timer = setTimeout(dismiss, 3000); });
    }
    return { dismiss: dismiss };
  }

  /* ------------------------------------------------------------------------
     Dropdowns (disclosure pattern)
     ------------------------------------------------------------------------ */
  function initDropdowns() {
    $all("[data-dropdown]").forEach(function (root) {
      var trigger = root.querySelector("[data-dropdown-trigger]");
      var menu = document.getElementById(trigger.getAttribute("aria-controls"));
      if (!trigger || !menu) return;

      function items() { return $all(FOCUSABLE, menu); }
      function open(focusFirst) {
        closeAllDropdowns(root);
        menu.hidden = false;
        trigger.setAttribute("aria-expanded", "true");
        if (focusFirst && items()[0]) items()[0].focus();
      }
      function close(returnFocus) {
        if (menu.hidden) return;
        menu.hidden = true;
        trigger.setAttribute("aria-expanded", "false");
        if (returnFocus) trigger.focus();
      }
      root._dsClose = close;

      trigger.addEventListener("click", function (e) {
        e.stopPropagation();
        if (menu.hidden) open(false); else close(false);
      });
      trigger.addEventListener("keydown", function (e) {
        if (e.key === "ArrowDown") { e.preventDefault(); open(true); }
      });
      menu.addEventListener("keydown", function (e) {
        var list = items();
        var idx = list.indexOf(document.activeElement);
        if (e.key === "Escape") { e.preventDefault(); close(true); }
        else if (e.key === "ArrowDown") { e.preventDefault(); (list[idx + 1] || list[0]).focus(); }
        else if (e.key === "ArrowUp") { e.preventDefault(); (list[idx - 1] || list[list.length - 1]).focus(); }
        else if (e.key === "Home") { e.preventDefault(); list[0].focus(); }
        else if (e.key === "End") { e.preventDefault(); list[list.length - 1].focus(); }
        else if (e.key === "Tab") { close(false); }
      });
      menu.addEventListener("click", function (e) {
        if (e.target.closest("a, button")) close(false);
      });
    });

    document.addEventListener("click", function (e) {
      $all("[data-dropdown]").forEach(function (root) {
        if (!root.contains(e.target) && root._dsClose) root._dsClose(false);
      });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key !== "Escape") return;
      $all("[data-dropdown]").forEach(function (root) {
        var t = root.querySelector("[data-dropdown-trigger]");
        if (t && t.getAttribute("aria-expanded") === "true") root._dsClose(true);
      });
    });
  }

  function closeAllDropdowns(except) {
    $all("[data-dropdown]").forEach(function (root) {
      if (root !== except && root._dsClose) root._dsClose(false);
    });
  }

  /* ------------------------------------------------------------------------
     Tabs (automatic activation, roving tabindex)
     ------------------------------------------------------------------------ */
  function initTabs() {
    $all('[role="tablist"]').forEach(function (list) {
      var tabs = $all('[role="tab"]', list);

      function select(tab, focus) {
        var activePanel = tab.getAttribute("aria-controls");
        tabs.forEach(function (t) {
          var selected = t === tab;
          t.setAttribute("aria-selected", selected ? "true" : "false");
          t.tabIndex = selected ? 0 : -1;
          // Several tabs may share one panel (filter tabs) — keep it visible then.
          var panel = document.getElementById(t.getAttribute("aria-controls"));
          if (panel) panel.hidden = t.getAttribute("aria-controls") !== activePanel;
        });
        var shown = document.getElementById(activePanel);
        if (shown) shown.setAttribute("aria-labelledby", tab.id);
        if (focus) tab.focus();
        list.dispatchEvent(new CustomEvent("ds:tabchange", { detail: { tab: tab }, bubbles: true }));
      }

      tabs.forEach(function (tab) {
        tab.tabIndex = tab.getAttribute("aria-selected") === "true" ? 0 : -1;
        tab.addEventListener("click", function () { select(tab, false); });
        tab.addEventListener("keydown", function (e) {
          var i = tabs.indexOf(tab);
          var next;
          if (e.key === "ArrowRight") next = tabs[(i + 1) % tabs.length];
          else if (e.key === "ArrowLeft") next = tabs[(i - 1 + tabs.length) % tabs.length];
          else if (e.key === "Home") next = tabs[0];
          else if (e.key === "End") next = tabs[tabs.length - 1];
          if (next) { e.preventDefault(); select(next, true); }
        });
      });
    });
  }

  /* ------------------------------------------------------------------------
     Modals (native <dialog>: focus trap, Esc and top-layer for free)
     ------------------------------------------------------------------------ */
  function initModals() {
    document.addEventListener("click", function (e) {
      var opener = e.target.closest("[data-modal-open]");
      if (opener) {
        var dialog = document.getElementById(opener.getAttribute("data-modal-open"));
        if (dialog && typeof dialog.showModal === "function") {
          e.preventDefault();
          dialog._dsOpener = opener;
          dialog.showModal();
          var auto = dialog.querySelector("[autofocus]") || dialog.querySelector(".modal-body " + FOCUSABLE);
          if (auto) auto.focus();
        }
        return;
      }
      var closer = e.target.closest("[data-modal-close]");
      if (closer) {
        var d = closer.closest("dialog");
        if (d) d.close();
      }
    });

    $all("dialog.modal").forEach(function (dialog) {
      // Backdrop click closes (click lands on the dialog element itself)
      dialog.addEventListener("mousedown", function (e) {
        if (e.target !== dialog) return;
        var r = dialog.getBoundingClientRect();
        var inside = e.clientX >= r.left && e.clientX <= r.right && e.clientY >= r.top && e.clientY <= r.bottom;
        if (!inside) dialog.close();
      });
      dialog.addEventListener("close", function () {
        document.documentElement.style.overflow = "";
        if (dialog._dsOpener && dialog._dsOpener.isConnected) dialog._dsOpener.focus();
      });
      // Lock page scroll while open
      new MutationObserver(function () {
        document.documentElement.style.overflow = dialog.open ? "hidden" : "";
      }).observe(dialog, { attributes: true, attributeFilter: ["open"] });
    });
  }

  /* ------------------------------------------------------------------------
     Tooltips
     ------------------------------------------------------------------------ */
  function initTooltips() {
    var tip = null;
    var counter = 0;

    function show(target) {
      hide();
      var text = target.getAttribute("data-tooltip");
      if (!text) return;
      tip = document.createElement("div");
      tip.className = "tooltip";
      tip.setAttribute("role", "tooltip");
      tip.id = "ds-tooltip-" + (++counter);
      tip.textContent = text;
      document.body.appendChild(tip);
      target.setAttribute("aria-describedby", tip.id);
      tip._target = target;

      var r = target.getBoundingClientRect();
      var t = tip.getBoundingClientRect();
      var top = r.top - t.height - 8;
      if (top < 8) top = r.bottom + 8;
      var left = Math.min(Math.max(8, r.left + r.width / 2 - t.width / 2), window.innerWidth - t.width - 8);
      tip.style.top = top + "px";
      tip.style.left = left + "px";
    }
    function hide() {
      if (!tip) return;
      if (tip._target) tip._target.removeAttribute("aria-describedby");
      tip.remove();
      tip = null;
    }

    document.addEventListener("mouseover", function (e) {
      var t = e.target.closest("[data-tooltip]");
      if (t) show(t);
    });
    document.addEventListener("mouseout", function (e) {
      var t = e.target.closest("[data-tooltip]");
      if (t && !t.contains(e.relatedTarget)) hide();
    });
    document.addEventListener("focusin", function (e) {
      var t = e.target.closest && e.target.closest("[data-tooltip]");
      if (t) show(t); else hide();
    });
    document.addEventListener("focusout", hide);
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") hide(); });
    window.addEventListener("scroll", hide, { passive: true });
  }

  /* ------------------------------------------------------------------------
     Form validation
     - Uses the Constraint Validation API, with German messages.
     - Custom message per field: data-msg-required, data-msg-type, data-msg-pattern
     - On valid submit: dispatches "ds:submit" (cancelable). If not prevented,
       simulates a request and shows the element referenced by data-success.
     ------------------------------------------------------------------------ */
  var DEFAULT_MESSAGES = {
    required: "Dieses Feld ist erforderlich.",
    email: "Bitte geben Sie eine gültige E-Mail-Adresse ein, z. B. name@firma.de.",
    tel: "Bitte geben Sie eine gültige Telefonnummer ein.",
    pattern: "Bitte prüfen Sie das Format.",
    tooShort: "Die Eingabe ist zu kurz.",
    checkbox: "Bitte bestätigen Sie diese Angabe."
  };

  function fieldMessage(input) {
    var v = input.validity;
    if (v.valueMissing) {
      return input.getAttribute("data-msg-required") ||
        (input.type === "checkbox" ? DEFAULT_MESSAGES.checkbox : DEFAULT_MESSAGES.required);
    }
    if (v.typeMismatch) return input.getAttribute("data-msg-type") || DEFAULT_MESSAGES[input.type] || DEFAULT_MESSAGES.pattern;
    if (v.patternMismatch) return input.getAttribute("data-msg-pattern") || DEFAULT_MESSAGES.pattern;
    if (v.tooShort) return input.getAttribute("data-msg-short") || DEFAULT_MESSAGES.tooShort;
    return input.validationMessage;
  }

  function validateField(input) {
    var field = input.closest(".field");
    if (!field) return true;
    var valid = input.checkValidity();
    var err = field.querySelector(".field-error");
    if (!err) {
      err = document.createElement("div");
      err.className = "field-error";
      err.id = (input.id || input.name) + "-error";
      field.appendChild(err);
    }
    // A field (e.g. a checkbox group) is invalid while any of its controls is.
    var fieldValid = $all("input, select, textarea", field).every(function (c) { return !c.willValidate || c.checkValidity(); });
    field.classList.toggle("is-invalid", !fieldValid);
    input.setAttribute("aria-invalid", valid ? "false" : "true");
    if (valid && !fieldValid) return true;

    var describedBy = (input.getAttribute("aria-describedby") || "").split(" ").filter(function (id) { return id && id !== err.id; });
    if (!valid) {
      err.innerHTML = icon("alert-circle", "icon--sm") + "<span></span>";
      err.querySelector("span").textContent = fieldMessage(input);
      describedBy.push(err.id);
    }
    if (describedBy.length) input.setAttribute("aria-describedby", describedBy.join(" "));
    else input.removeAttribute("aria-describedby");
    return valid;
  }

  function initForms() {
    $all("form[data-validate]").forEach(function (form) {
      form.setAttribute("novalidate", "");
      var controls = function () { return $all("input, select, textarea", form).filter(function (c) { return c.willValidate; }); };
      var summary = form.querySelector("[data-error-summary]");

      form.addEventListener("blur", function (e) {
        if (form._dsSubmitted && e.target.willValidate) validateField(e.target);
      }, true);
      form.addEventListener("input", function (e) {
        var field = e.target.closest && e.target.closest(".field");
        if (field && field.classList.contains("is-invalid")) validateField(e.target);
      });
      form.addEventListener("change", function (e) {
        var field = e.target.closest && e.target.closest(".field");
        if (field && field.classList.contains("is-invalid")) validateField(e.target);
      });

      form.addEventListener("submit", function (e) {
        e.preventDefault();
        form._dsSubmitted = true;
        var invalid = controls().filter(function (c) { return !validateField(c); });

        if (summary) {
          if (invalid.length) {
            var items = invalid.map(function (c) {
              var label = form.querySelector('label[for="' + c.id + '"]');
              var name = c.getAttribute("data-label") || (label ? label.textContent.replace(/\*|\(optional\)/g, "").trim() : c.name);
              return '<li><a href="#' + c.id + '">' + escapeHtml(name) + "</a>: " + escapeHtml(fieldMessage(c)) + "</li>";
            }).join("");
            summary.innerHTML =
              '<div class="alert alert--danger" role="alert" tabindex="-1">' + icon("alert-circle") +
              '<div><div class="alert-title">Bitte prüfen Sie ' + (invalid.length === 1 ? "1 Angabe" : invalid.length + " Angaben") + "</div><ul>" + items + "</ul></div></div>";
            summary.hidden = false;
            summary.querySelector(".alert").focus();
            $all("a", summary).forEach(function (a) {
              a.addEventListener("click", function (ev) {
                ev.preventDefault();
                var target = document.getElementById(a.getAttribute("href").slice(1));
                if (target) target.focus();
              });
            });
          } else {
            summary.hidden = true;
            summary.innerHTML = "";
          }
        }

        if (invalid.length) {
          if (!summary) invalid[0].focus();
          return;
        }

        var evt = new CustomEvent("ds:submit", { cancelable: true, detail: { form: form } });
        if (!form.dispatchEvent(evt)) return;

        var btn = form.querySelector('[type="submit"]');
        setLoading(btn, true);
        setTimeout(function () {
          setLoading(btn, false);
          var successId = form.getAttribute("data-success");
          var success = successId && document.getElementById(successId);
          if (success) {
            form.hidden = true;
            success.hidden = false;
            var focusTarget = success.querySelector("[tabindex='-1']") || success;
            if (!focusTarget.hasAttribute("tabindex")) focusTarget.setAttribute("tabindex", "-1");
            focusTarget.focus();
          }
          var msg = form.getAttribute("data-success-toast");
          if (msg) toast({ variant: "success", title: msg.split("|")[0], message: msg.split("|")[1] });
          var dialog = form.closest("dialog");
          // Close the dialog unless it shows its own success panel
          if (dialog && dialog.open && !(success && dialog.contains(success))) dialog.close();
          form.dispatchEvent(new CustomEvent("ds:beforereset", { detail: { form: form } }));
          form.reset();
          form._dsSubmitted = false;
          form.dispatchEvent(new CustomEvent("ds:submitted", { detail: { form: form } }));
        }, 1100);
      });

      form.addEventListener("reset", function () {
        $all(".field.is-invalid", form).forEach(function (f) { f.classList.remove("is-invalid"); });
        $all("[aria-invalid]", form).forEach(function (c) { c.setAttribute("aria-invalid", "false"); });
        if (summary) { summary.hidden = true; summary.innerHTML = ""; }
      });
    });

    // "Start again" buttons inside success panels
    document.addEventListener("click", function (e) {
      var resetBtn = e.target.closest("[data-form-restart]");
      if (!resetBtn) return;
      var form = document.getElementById(resetBtn.getAttribute("data-form-restart"));
      var panel = resetBtn.closest("[hidden], .form-success") || resetBtn.parentElement;
      if (form) {
        panel.hidden = true;
        form.hidden = false;
        var first = form.querySelector("input, select, textarea");
        if (first) first.focus();
      }
    });
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  /* ------------------------------------------------------------------------
     Mobile navigation
     ------------------------------------------------------------------------ */
  function initMobileNav() {
    $all("[data-nav-toggle]").forEach(function (btn) {
      var panel = document.getElementById(btn.getAttribute("data-nav-toggle"));
      if (!panel) return;
      btn.setAttribute("aria-controls", panel.id);
      btn.setAttribute("aria-expanded", "false");
      function set(open) {
        panel.classList.toggle("is-open", open);
        btn.setAttribute("aria-expanded", open ? "true" : "false");
        btn.setAttribute("aria-label", open ? "Menü schließen" : "Menü öffnen");
        var use = btn.querySelector("use");
        if (use) use.setAttribute("href", open ? "#i-x" : "#i-menu");
      }
      btn.addEventListener("click", function () { set(!panel.classList.contains("is-open")); });
      panel.addEventListener("click", function (e) { if (e.target.closest("a")) set(false); });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && panel.classList.contains("is-open")) { set(false); btn.focus(); }
      });
      window.addEventListener("resize", function () { if (window.innerWidth > 1024) set(false); });
    });
  }

  /* ------------------------------------------------------------------------
     Boot
     ------------------------------------------------------------------------ */
  function init() {
    injectSprite();
    initDropdowns();
    initTabs();
    initModals();
    initTooltips();
    initForms();
    initMobileNav();
    document.dispatchEvent(new CustomEvent("ds:ready"));
  }

  window.DS = { toast: toast, setLoading: setLoading, icon: icon, escapeHtml: escapeHtml, validateField: validateField };

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
