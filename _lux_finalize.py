
# Executed via runpy from _expand_luxury.py with its globals, OR standalone.
from pathlib import Path as _Path

def write_homepage():
    schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "name": "%(BRAND)s",
      "url": "%(DOMAIN)s/",
      "legalName": "%(LLC)s",
      "description": "Luxury and boutique US stay guidance with soft affiliate comparison CTAs. Not a merchant of record."
    },
    {
      "@type": "WebSite",
      "name": "%(BRAND)s",
      "url": "%(DOMAIN)s/",
      "publisher": {"@type": "Organization", "name": "%(LLC)s"}
    }
  ]
}
</script>
""" % {"BRAND": BRAND, "DOMAIN": DOMAIN, "LLC": LLC}

    body = """
    <section class="hero">
      <div class="wrap">
        <p class="section-label" style="color:#a8e6df;">Boutique · luxury · design hotels</p>
        <h1>Plan a high-end US stay — then compare partner rates</h1>
        <p>Noravelle Stays publishes neighborhood guidance for boutique, five-star-leaning, and design-hotel trips in elevated US cities. Soft Compare CTAs only. We are an affiliate referral site operated by %(LLC)s: we do not take payment or confirm bookings.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="/hotels/miami/">Explore Miami luxury hotels</a>
          <a class="btn btn-ghost" href="/how-pricing-works/">How pricing works</a>
        </div>
      </div>
    </section>
<div class="wrap">

      %(disc)s
      <p class="section-label">Featured high-AOV destinations</p>
      <div class="card-grid">
        <article class="card">
          <h2>Miami &amp; Miami Beach</h2>
          <p>South Beach icons, Brickell skyline suites, and Coral Gables calm for a true splurge.</p>
          <a class="card-link" href="/destinations/us/miami/">Miami hub →</a>
        </article>
        <article class="card">
          <h2>Charleston</h2>
          <p>Historic District boutiques and Mount Pleasant resort-caliber stays for anniversary weekends.</p>
          <a class="card-link" href="/destinations/us/charleston/">Charleston hub →</a>
        </article>
        <article class="card">
          <h2>Nashville</h2>
          <p>The Gulch, Music Row, and premium downtown floors — luxury first, neon second.</p>
          <a class="card-link" href="/destinations/us/nashville/">Nashville hub →</a>
        </article>
        <article class="card">
          <h2>Austin</h2>
          <p>South Congress boutiques and downtown design hotels for festival-aware leisure trips.</p>
          <a class="card-link" href="/destinations/us/austin/">Austin hub →</a>
        </article>
        <article class="card">
          <h2>New Orleans</h2>
          <p>French Quarter courtyards, Warehouse District design, and Garden District elegance.</p>
          <a class="card-link" href="/hotels/new-orleans/">New Orleans hotels →</a>
        </article>
        <article class="card">
          <h2>Tampa, Raleigh &amp; more</h2>
          <p>Waterfront towers and Hyde Park boutiques, plus Denver, Savannah, and San Antonio.</p>
          <a class="card-link" href="/hotels/tampa/">Tampa luxury hotels →</a>
        </article>
      </div>

      <div class="content-block" style="margin-top:1.5rem;">
        <h2>What Noravelle Stays is</h2>
        <p>We help travelers shortlist <strong>where to stay</strong> for boutique and high-ticket trips, then point you to partner sites to <strong>compare hotel rates</strong>. Affiliate-only MVP: we are <strong>not</strong> the merchant of record and we do not process payments.</p>
        <ul>
          <li><strong>Hotels</strong> — luxury city and near-airport editorial pages</li>
          <li><strong>Guides</strong> — where-to-stay and weekend-trip planning for a splurge</li>
          <li><strong>Flights</strong> — light route context paired with premium hotel planning</li>
        </ul>
        <p class="note">We do not claim to undercut any major OTA’s hotel commission today. Read <a href="/how-pricing-works/">how pricing works</a>. Affiliate deep links live in <code>NORAVELLE_AFFILIATES</code> placeholders until programs are approved.</p>
      </div>

      <p class="section-label" style="margin-top:2rem;">Flights</p>
      <div class="card-grid">
        <article class="card">
          <h3>Flights to Miami</h3>
          <p>MIA timing tips paired with Beach and Brickell luxury bases.</p>
          <a class="card-link" href="/flights/to/miami/">Miami flights →</a>
        </article>
        <article class="card">
          <h3>NYC to Miami</h3>
          <p>Busy East Coast leisure corridor — verify fares on partners.</p>
          <a class="card-link" href="/flights/nyc-to-miami/">Route guide →</a>
        </article>
        <article class="card">
          <h3>Charleston, Nashville &amp; Austin</h3>
          <p>More US destination flight pages with Compare flights CTAs.</p>
          <a class="card-link" href="/flights/to/charleston/">Browse flight pages →</a>
        </article>
      </div>
      %(flight_cta)s

      <p class="section-label" style="margin-top:2rem;">Popular luxury guides</p>
      <div class="card-grid">
        <article class="card">
          <h3>Where to stay in Miami</h3>
          <p>Miami Beach, Brickell, and quieter luxury neighborhoods.</p>
          <a class="card-link" href="/guides/where-to-stay-in-miami/">Read guide →</a>
        </article>
        <article class="card">
          <h3>Where to stay in Charleston</h3>
          <p>Historic District boutiques and Mount Pleasant premium alternatives.</p>
          <a class="card-link" href="/guides/where-to-stay-in-charleston/">Read guide →</a>
        </article>
        <article class="card">
          <h3>New Orleans luxury bases</h3>
          <p>French Quarter courtyards vs. Garden District elegance.</p>
          <a class="card-link" href="/guides/where-to-stay-in-new-orleans/">Read guide →</a>
        </article>
      </div>

      %(hotel_cta)s

    </div>
""" % {
        "LLC": LLC,
        "disc": soft_disclaimer(),
        "flight_cta": flight_cta("flight deals"),
        "hotel_cta": hotel_cta("luxury hotel rates"),
    }

    html = head(
        "Noravelle Stays — Boutique & Luxury US Hotel Guides",
        "Boutique, luxury, and design-hotel guides for high-ticket US trips. Soft Compare CTAs on partners. Affiliate referral only — Joshua Israel Ventures LLC.",
        "/",
        extra=schema,
    ) + "\n<body>\n" + header() + "\n  <main id=\"main\">\n" + body + "\n  </main>\n" + footer() + "\n</body>\n</html>\n"
    write("index.html", html)
    if "/" not in NEW_PATHS:
        NEW_PATHS.append("/")

def write_sitemap_and_page_list():
    routes = set()
    for hp in ROOT.rglob("index.html"):
        rel = hp.relative_to(ROOT)
        if any(part.startswith("_") or part.startswith(".") for part in rel.parts):
            continue
        if str(rel) == "index.html":
            routes.add("/")
        else:
            routes.add("/" + str(rel.parent).replace("\\", "/") + "/")
    routes = sorted(routes)

    def pri(r):
        if r == "/":
            return "1.0"
        if r.startswith("/destinations/"):
            return "0.9"
        if r.startswith("/hotels/") or r.startswith("/guides/"):
            return "0.8"
        if r.startswith("/flights/"):
            return "0.75"
        if r == "/how-pricing-works/":
            return "0.7"
        if r in ("/about/", "/contact/"):
            return "0.5"
        return "0.3"

    def fr(r):
        if r == "/" or r.startswith(("/destinations/", "/hotels/", "/flights/")):
            return "weekly"
        if r.startswith("/guides/") or r == "/how-pricing-works/":
            return "monthly"
        return "yearly"

    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for r in routes:
        lines.append(f"  <url><loc>{DOMAIN}{r}</loc><changefreq>{fr(r)}</changefreq><priority>{pri(r)}</priority></url>")
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("sitemap", len(routes))

    md = [
        "# Noravelle Stays — page list",
        "",
        "Every URL path created for the static site (`noravellestays.com`):",
        "",
        "## HTML routes",
        "",
    ]
    for r in routes:
        md.append(f"- `{r}`")
    md += [
        "",
        "## Assets / meta",
        "",
        "- `/css/styles.css`",
        "- `/js/main.js`",
        "- `/js/affiliates.js`",
        "- `/robots.txt`",
        "- `/sitemap.xml`",
        "- `/README.md`",
        "- `/PAGE_LIST.md`",
        "",
        f"**Total HTML routes:** {len(routes)}",
        "",
        f"**Brand:** {BRAND} · {LLC} · Contact subject `[Contact: Noravelle Stays]`",
        "",
        "**Positioning:** Boutique / luxury / design hotels / high-ticket US stays — soft Compare CTAs only; `NORAVELLE_AFFILIATES` placeholders; no false Expedia undercut claims; LLC in footer.",
        "",
    ]
    (ROOT / "PAGE_LIST.md").write_text("\n".join(md), encoding="utf-8")
    print("PAGE_LIST", len(routes))
    (ROOT / "_luxury_report.txt").write_text(
        f"paths_from_generator={len(NEW_PATHS)}\nsitemap_routes={len(routes)}\n" + "\n".join(NEW_PATHS) + "\n",
        encoding="utf-8",
    )

write_homepage()
write_sitemap_and_page_list()
print("FINALIZE_DONE", len(NEW_PATHS))
