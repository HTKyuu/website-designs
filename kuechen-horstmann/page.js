/* Küchen Horstmann — page behaviour */
(function () {
  "use strict";

  function pad(n) { return String(n).padStart(2, "0"); }
  function isoDate(d) { return d.getFullYear() + "-" + pad(d.getMonth() + 1) + "-" + pad(d.getDate()); }

  document.addEventListener("ds:ready", function () {
    /* Appointment date: earliest tomorrow, no Sundays */
    var date = document.getElementById("b-date");
    if (date) {
      var tomorrow = new Date();
      tomorrow.setDate(tomorrow.getDate() + 1);
      date.min = isoDate(tomorrow);
      var max = new Date();
      max.setMonth(max.getMonth() + 6);
      date.max = isoDate(max);

      var check = function () {
        var msg = "";
        if (date.value) {
          var d = new Date(date.value + "T12:00:00");
          if (d.getDay() === 0) msg = "Sonntags sind unsere Ausstellungen geschlossen. Bitte wählen Sie einen anderen Tag.";
          else if (date.value < date.min) msg = "Bitte wählen Sie einen Termin ab morgen.";
          else if (date.value > date.max) msg = "Termine können bis zu sechs Monate im Voraus angefragt werden.";
        }
        date.setCustomValidity(msg);
      };
      date.addEventListener("input", check);
      date.addEventListener("change", check);
    }

    /* "Termin hier" preselects the showroom */
    document.querySelectorAll("[data-showroom]").forEach(function (link) {
      link.addEventListener("click", function () {
        var select = document.getElementById("b-showroom");
        if (select) select.value = link.getAttribute("data-showroom");
      });
    });

    /* Reference number on successful booking */
    var form = document.getElementById("booking-form");
    if (form) {
      form.addEventListener("ds:submitted", function () {
        var ref = document.getElementById("booking-ref");
        if (ref) ref.textContent = "HM-26-" + String(Math.floor(1000 + Math.random() * 9000));
      });
    }

    /* Jump to a tab from elsewhere in the portal preview */
    document.querySelectorAll("[data-tab-jump]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var tab = document.getElementById(btn.getAttribute("data-tab-jump"));
        if (tab) { tab.click(); tab.focus(); }
      });
    });

    /* Demo feedback for actions that would hit a backend */
    document.addEventListener("click", function (e) {
      var t = e.target.closest("[data-toast-demo]");
      if (!t) return;
      var kind = t.getAttribute("data-toast-demo");
      if (kind === "download") {
        DS.toast({ variant: "info", title: "Download gestartet", message: "Das Dokument wird in Ihrem Browser geöffnet." });
      } else if (kind === "cookies") {
        DS.toast({ variant: "info", title: "Cookie-Einstellungen", message: "Es werden nur technisch notwendige Cookies verwendet." });
      }
    });
  });
})();
