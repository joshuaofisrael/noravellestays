(function () {
  var KEY = "nv_ga_consent";

  function read() {
    try {
      return localStorage.getItem(KEY);
    } catch (e) {
      return null;
    }
  }

  function write(value) {
    try {
      localStorage.setItem(KEY, value);
      return true;
    } catch (e) {
      return false;
    }
  }

  function update(value) {
    if (typeof window.gtag !== "function") return;
    window.gtag("consent", "update", { analytics_storage: value });
  }

  function build() {
    var banner = document.createElement("div");
    banner.id = "cookie-banner";
    banner.className = "cookie-banner";
    banner.setAttribute("role", "region");
    banner.setAttribute("aria-label", "Cookie consent");
    banner.tabIndex = -1;

    var text = document.createElement("p");
    text.id = "cookie-banner-text";
    text.textContent = "We use Google Analytics cookies only if you accept. Reject leaves those cookies off. ";
    var privacy = document.createElement("a");
    privacy.href = "/privacy/";
    privacy.textContent = "Privacy";
    text.appendChild(privacy);

    var actions = document.createElement("div");
    actions.className = "cookie-banner-actions";

    var accept = document.createElement("button");
    accept.type = "button";
    accept.id = "cookie-accept";
    accept.className = "cookie-accept";
    accept.textContent = "Accept";

    var reject = document.createElement("button");
    reject.type = "button";
    reject.id = "cookie-reject";
    reject.className = "cookie-reject";
    reject.textContent = "Reject";

    actions.appendChild(accept);
    actions.appendChild(reject);
    banner.appendChild(text);
    banner.appendChild(actions);

    var manage = document.createElement("button");
    manage.type = "button";
    manage.id = "cookie-manage";
    manage.className = "cookie-manage";
    manage.textContent = "Cookie choices";

    function syncPressed() {
      var choice = read();
      accept.setAttribute("aria-pressed", choice === "granted" ? "true" : "false");
      reject.setAttribute("aria-pressed", choice === "denied" ? "true" : "false");
    }

    function showBanner() {
      syncPressed();
      banner.hidden = false;
      manage.hidden = true;
    }

    function hideBanner() {
      banner.hidden = true;
      manage.hidden = false;
    }

    accept.addEventListener("click", function () {
      write("granted");
      update("granted");
      hideBanner();
    });

    reject.addEventListener("click", function () {
      write("denied");
      update("denied");
      hideBanner();
    });

    manage.addEventListener("click", function () {
      showBanner();
      banner.focus();
    });

    document.body.appendChild(banner);
    document.body.appendChild(manage);

    if (read() === "granted" || read() === "denied") {
      hideBanner();
    } else {
      showBanner();
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", build);
  } else {
    build();
  }
})();
