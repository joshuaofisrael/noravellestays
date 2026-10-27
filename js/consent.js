(function () {
  var KEY = "mtm-analytics-consent";

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

  function gaCookieNames() {
    var names = [];
    document.cookie.split(";").forEach(function (part) {
      var name = part.split("=")[0].replace(/^\s+/, "");
      if (!name) return;
      if (name === "_ga" || name.indexOf("_ga_") === 0) names.push(name);
    });
    return names;
  }

  function eraseCookie(name) {
    var expired = name + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT; Max-Age=0";
    var host = location.hostname;
    var domains = [host, "." + host];
    var labels = host.split(".");
    if (labels.length > 2) domains.push("." + labels.slice(-2).join("."));
    var paths = ["/"];
    document.cookie = expired + "; path=/";
    domains.forEach(function (domain) {
      paths.forEach(function (path) {
        var cookie = expired + "; path=" + path + "; domain=" + domain;
        document.cookie = cookie;
        document.cookie = cookie + "; Secure";
      });
    });
  }

  function deleteGaCookies() {
    gaCookieNames().forEach(eraseCookie);
  }

  function removeBanner() {
    var existing = document.getElementById("mtm-consent");
    if (existing && existing.parentNode) existing.parentNode.removeChild(existing);
  }

  function insertBanner(moveFocus) {
    removeBanner();
    var choice = read();

    var banner = document.createElement("div");
    banner.id = "mtm-consent";
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
    accept.className = "acc";
    accept.textContent = "Accept";

    var reject = document.createElement("button");
    reject.type = "button";
    reject.className = "rej";
    reject.textContent = "Reject";

    if (choice === "granted" || choice === "denied") {
      accept.setAttribute("aria-pressed", choice === "granted" ? "true" : "false");
      reject.setAttribute("aria-pressed", choice === "denied" ? "true" : "false");
    }

    actions.appendChild(accept);
    actions.appendChild(reject);
    banner.appendChild(text);
    banner.appendChild(actions);

    accept.addEventListener("click", function () {
      write("granted");
      update("granted");
      removeBanner();
    });

    reject.addEventListener("click", function () {
      write("denied");
      update("denied");
      deleteGaCookies();
      removeBanner();
    });

    document.body.appendChild(banner);
    if (moveFocus) banner.focus();
  }

  function boot() {
    var choice = read();
    if (choice !== "granted" && choice !== "denied") insertBanner(false);

    document.addEventListener("click", function (event) {
      var node = event.target;
      if (!node || typeof node.closest !== "function") return;
      var opener = node.closest("[data-consent-open]");
      if (!opener || !document.body.contains(opener)) return;
      event.preventDefault();
      insertBanner(true);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
