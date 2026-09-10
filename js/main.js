(function () {
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  function applyAffiliates() {
    var cfg = window.NORAVELLE_AFFILIATES;
    if (!cfg) return;
    document.querySelectorAll("[data-affiliate]").forEach(function (el) {
      var key = el.getAttribute("data-affiliate");
      if (!key || !Object.prototype.hasOwnProperty.call(cfg, key)) return;
      var url = cfg[key];
      if (typeof url === "string" && url.length) {
        el.setAttribute("href", url);
      }
      if (url && url !== "#") {
        el.setAttribute("rel", "nofollow sponsored noopener");
        if (!el.getAttribute("target")) el.setAttribute("target", "_blank");
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", applyAffiliates);
  } else {
    applyAffiliates();
  }
})();
