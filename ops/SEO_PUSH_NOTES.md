# SEO push notes — foundation batch (10 Sep 2026)

**Owner:** Joshua Israel / Joshua Israel Ventures LLC · **Site:** noravellestays.com  
**Mode:** Steady compounding. Quality over volume. No bought links, directory spam, or shady schemes.

## What shipped today (foundation only)

### New linkable assets (2 HTML routes)
1. `/resources/` — Resources hub with original luxury trip planning checklist + cards into guides/trends.
2. `/resources/us-luxury-hotel-trends/` — Original 2026 trends brief with:
   - Illustrative bar chart (Figure 1) paraphrasing U.S. Travel Association spending categories
   - Original planner table (trip personality → base type → Noravelle pages)
   - FAQ block
   - Methodology & limitations note
   - Sources list with outbound citations
   - Soft Compare CTA only (`NORAVELLE_AFFILIATES` remains `#`)

### Schema upgrades
- **Homepage:** richer `Organization` (`@id`, email, `ContactPoint`) + `WebSite` (`@id`, `inLanguage`).
- **Trends brief:** `Article` + `BreadcrumbList` + `FAQPage`.
- **Resources hub:** `CollectionPage` + `BreadcrumbList`.
- **Guides (Miami, Nashville, Charleston where-to-stay):** `Article` + `BreadcrumbList` + `FAQPage` + `TouristDestination` as `about` (not fake Hotel entities).
- **Hotels (Miami, Nashville):** `Article` + `BreadcrumbList`.

### Internal linking + citations (top pages)
Updated ~8 existing pages with denser links to resources, flights, contact, how-pricing-works, and 2–4 authoritative outbound citations where fitting:
- `/` (homepage)
- `/guides/where-to-stay-in-miami/`
- `/guides/where-to-stay-in-nashville/`
- `/guides/where-to-stay-in-charleston/`
- `/hotels/miami/`
- `/hotels/nashville/`
- `/how-pricing-works/`
- `/destinations/us/miami/`

Nav/footer: Resources entry added on patched pages; Explore footer lists resources + trends.

### Meta / docs
- `sitemap.xml` — added `/resources/` and `/resources/us-luxury-hotel-trends/`
- `PAGE_LIST.md` — routes updated
- `README.md` — SEO foundation section
- `css/styles.css` — sources/methodology/chart/checklist styles

## Sources cited (verified via WebSearch/WebFetch; omit if unverifiable)

| Source | URL |
|--------|-----|
| U.S. Travel Association — Travel Forecast (Spring 2026) | https://www.ustravel.org/research/travel-forecasts |
| CoStar / STR — U.S. Hotel Forecast Assumptions (Aug 2026) | https://www.costar.com/products/str-benchmark/resources/data-insights-blog/us-hotel-forecast-assumptions-august-2026 |
| BEA Travel & Tourism Satellite Account (Feb 2025 PDF) | https://apps.bea.gov/scb/issues/2025/02-february/pdf/0225-travel-tourism-satellite-account.pdf |
| NTTO | https://www.trade.gov/national-travel-and-tourism-office |
| NTTO Travel & Tourism Research | https://www.trade.gov/travel-and-tourism-research |
| UN Tourism / UNWTO statistics | https://www.e-unwto.org/toc/unwtotfb/current |
| Greater Miami CVB | https://www.miamiandbeaches.com/ |
| Visit Nashville | https://www.visitmusiccity.com/ |
| Charleston Area CVB | https://www.charlestoncvb.com/ |
| Visit Austin | https://www.austintexas.org/ |
| VISIT DENVER | https://www.visitdenver.com/ |
| New Orleans & Company | https://www.neworleans.com/ |

**Not used:** inventing citations; Resonance “$544B” secondary press was noted in research but not required for this brief — prefer primary .gov/.org/industry pages above.

## Guardrails still in force
- Contact: `[Contact: Noravelle Stays]` → joshuaofisrael@gmail.com
- Soft Compare CTAs only; affiliates stay `#`
- No false Expedia undercut claims
- Original content only; no plagiarism / scraped OTA copy
- Do not invent live prices or falsely mark specific hotels as Schema `Hotel`

## Suggested weekly cadence (compounding)

Aim **3–5 quality actions per week**, not dozens of thin URLs:

| Week focus | Examples |
|------------|----------|
| **Mon – deepen 1 guide** | Add 2–4 verified outbound citations + FAQ schema + internal links to resources/flights/pricing/contact |
| **Wed – deepen 1 hotel or destination** | Same pattern; optional TouristDestination `about`, never fake Hotel inventory |
| **Fri – linkable asset OR upgrade** | Extend checklist, add one original table/figure on resources, or refresh trends methodology with a newly verified source |
| **Ongoing** | Fix breadcrumbs/nav consistency; update sitemap `lastmod` when content meaningfully changes; re-verify citation URLs quarterly |

### Backlog ideas (do later, one at a time)
- `/guides/luxury-travel-planning-checklist/` standalone downloadable-style HTML (expand checklist from resources hub)
- Austin / New Orleans where-to-stay citation + FAQ upgrades
- Denver / Tampa destination pages with Visit Denver / local CVB links
- Breadcrumb hub URLs: consider adding real `/guides/` and `/hotels/` index pages before pointing breadcrumbs at Nashville placeholders
- Organization `sameAs` only after real public profiles exist

## Explicitly deferred (by design)
- Mass page generation
- Directory submissions / link buying
- Sitewide mechanical schema spam on every thin hotel stub in one day
