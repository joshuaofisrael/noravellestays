#!/usr/bin/env python3
"""Reusable 'Best rooms at [Hotel]' page builder for Noravelle Stays.

Each page is a dict with: slug, hotel, city, city_url, official_url, title, description,
quick, floors (dicts with confirms, recommend, ask html), dest_url, coverage, compare (list of rows: name, size, beds, view, notes),
request and avoid (lists of dicts with label, confirms, recommend, ask), compare rows end with the official source URL,
ask (list of html items), faq (list of (q, a) plain text), sources (list of (label, url)),
checked (date string). Sections render in a fixed order: quick answer, room types compared,
best floors and views, rooms or stacks to request, rooms to avoid and why, how to ask, sources.
Never pass a room number, floor or view that a listed source does not state.
Run: python3 scripts/best_rooms_page.py  (rebuilds every page in PAGES)
"""
import html, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://noravellestays.com"


def shell():
    home = (ROOT / "index.html").read_text()
    about = (ROOT / "about" / "index.html").read_text()
    analytics = home[home.index("<!-- Google tag"):home.index("</head>")]
    header = about[about.index('<a class="skip-link"'):about.index('<main id="main">')]
    header = header.replace(' aria-current="page"', "")
    footer = about[about.index('<footer class="site-footer">'):]
    return analytics, header, footer


def jsonld(p, url):
    crumbs = [("Home", SITE + "/"), ("Best rooms", SITE + "/best-rooms/"), (p["hotel"], url)]
    graph = [
        {"@type": "Article", "headline": p["title"], "description": p["description"],
         "datePublished": p["checked"], "dateModified": p["checked"],
         "author": {"@type": "Organization", "name": "Noravelle Stays"},
         "publisher": {"@type": "Organization", "name": "Noravelle Stays", "url": SITE + "/"},
         "mainEntityOfPage": url,
         "about": {"@type": "Hotel", "name": p["hotel"], "url": p["official_url"]}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs)]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False)


def cra(block):
    """Render the fixed three part structure: Hotel confirms / Our recommendation / Ask the hotel."""
    out = []
    for key, label in (("confirms", "Hotel confirms"), ("recommend", "Our recommendation"), ("ask", "Ask the hotel")):
        if block.get(key):
            out.append(f'<p class="cra cra-{key}"><strong>{label}:</strong> {block[key]}</p>')
    return "\n        ".join(out)


def cra_items(items):
    return "\n".join(
        f'        <div class="cra-item">\n          <h3>{it["label"]}</h3>\n          {cra(it)}\n        </div>' for it in items)


def render(p):
    url = f"{SITE}/best-rooms/{p['slug']}/"
    analytics, header, footer = shell()
    e = html.escape
    rows = "\n".join(
        f"            <tr><th scope=\"row\"><a href=\"{e(r[5])}\" rel=\"noopener noreferrer\" target=\"_blank\">{e(r[0])}</a></th><td>{e(r[1])}</td><td>{e(r[2])}</td><td>{e(r[3])}</td><td>{r[4]}</td></tr>"
        for r in p["compare"])
    li = lambda items: "\n".join(f"          <li>{x}</li>" for x in items)
    faq = "\n".join(f"        <details open>\n          <summary>{e(q)}</summary>\n          <p>{e(a)}</p>\n        </details>" for q, a in p["faq"])
    src = "\n".join(f'          <li><a href="{e(u)}" rel="noopener noreferrer" target="_blank">{e(l)}</a></li>' for l, u in p["sources"])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(p['title'])} | Noravelle Stays</title>
  <meta name="description" content="{e(p['description'])}">
  <link rel="canonical" href="{url}">
  <meta name="robots" content="index,follow">
  <meta property="og:title" content="{e(p['title'])}">
  <meta property="og:description" content="{e(p['description'])}">
  <meta property="og:url" content="{url}">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Noravelle Stays">
  <meta property="article:modified_time" content="{p['checked']}">
  <link rel="stylesheet" href="/css/styles.css">
  <script type="application/ld+json">
{jsonld(p, url)}
  </script>
{analytics}</head>
<body>
  {header}<main id="main">
    <div class="wrap">
      <nav class="breadcrumbs" aria-label="Breadcrumb"><ol>
        <li><a href="/">Home</a></li><li><a href="/best-rooms/">Best rooms</a></li><li aria-current="page">{e(p['hotel'])}</li>
      </ol></nav>
      <h1 class="page-title">{e(p['title'])}</h1>
      <p class="lede">Which room to ask for at <a href="{e(p['official_url'])}" rel="noopener noreferrer" target="_blank">{e(p['hotel'])}</a> in {e(p['city'])}, based only on the hotel's own published room details. Sources were checked on {p['checked_human']}. See the <a href="{p['city_url']}">{e(p['city'])} hotel guide</a> for the wider area.</p>
      <aside class="disclaimer-box" role="note"><p><em>Editorial guidance only. Room requests are never guaranteed and the hotel decides room assignment. We do not sell lodging or collect payment, and the hotel does not endorse Noravelle Stays. Confirm room type, view and price on the official site before you book. See our <a href="/disclaimer/">Disclaimer</a> and <a href="/affiliate-disclosure/">Affiliate Disclosure</a>.</em></p></aside>

      <section class="content-block" id="quick-answer">
        <h2>Quick answer</h2>
        {cra(p['quick'])}
      </section>

      <section class="content-block" id="room-types">
        <h2>Room types compared</h2>
        <div class="table-wrap"><table>
          <thead><tr><th scope="col">Room type</th><th scope="col">Size</th><th scope="col">Beds</th><th scope="col">View or outlook</th><th scope="col">Worth knowing</th></tr></thead>
          <tbody>
{rows}
          </tbody>
        </table></div>
        <p>Sizes, beds and views are as the hotel describes them, with a link to the official page for each row. "Not stated" means the official page does not say. {p.get('coverage', '')}</p>
      </section>

      <section class="content-block" id="floors-views">
        <h2>Best floors and views</h2>
        {cra(p['floors'])}
      </section>

      <section class="content-block" id="request">
        <h2>Rooms and wings to request</h2>
{cra_items(p['request'])}
        <p>{p.get('no_numbers', 'The hotel does not publish specific room numbers or stacks, so we do not name any. Ask for the room type and outlook instead.')}</p>
      </section>

      <section class="content-block" id="avoid">
        <h2>Rooms to avoid and why</h2>
{cra_items(p['avoid'])}
      </section>

      <section class="content-block" id="how-to-ask">
        <h2>How to ask</h2>
        <ul>
{li(p['ask'])}
        </ul>
      </section>

      <section class="faq" id="faq">
        <h2>Questions about rooms at {e(p['hotel'])}</h2>
{faq}
      </section>

      <section class="content-block" id="sources">
        <h2>Sources</h2>
        <p>Checked on {p['checked_human']}. Room details can change, so confirm on the official site.</p>
        <ul>
{src}
        </ul>
      </section>

      <p>Related: <a href="/best-rooms/">all best rooms guides</a> · <a href="{p['city_url']}">{e(p['city'])} hotel guide</a> · <a href="{p['dest_url']}">{e(p['city'])} destination guide</a> · <a href="/guides/how-we-pick-luxury-hotels/">how we research and pick hotels</a></p>
    </div>
  </main>
  {footer}"""


def build(pages):
    for p in pages:
        out = ROOT / "best-rooms" / p["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(p))
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    from best_rooms_pages import PAGES
    build(PAGES)
