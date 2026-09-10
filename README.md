# Noravelle Stays (`noravellestays.com`)

Static **luxury / boutique US stay guides + day plans** for **Noravelle Stays**, owned and operated by **Joshua Israel Ventures LLC**.

We recommend **specific hotels** and link to their **official websites** (and trusted city lodging lists). Optional affiliate rate comparison may be added later and will stay disclosed. **No payment collection, no checkout, not merchant of record.** Hotels do not endorse Noravelle Stays.

## Stack

- Plain HTML (folder `index.html` URLs)
- `css/styles.css` — teal/navy travel aesthetic
- `js/affiliates.js` — optional affiliate deep links (`hotels`, `flights`, `cars`); primary CTAs are official hotel sites
- `js/main.js` — mobile nav + applies `data-affiliate` hrefs from config
- Original day-plan art under `images/dayplans/`
- No required build step

## Nav

Destinations · Hotels · Day plans · Guides · Resources · About · Contact  

“How we recommend” (`/how-pricing-works/`) lives in the footer (not primary nav).

## Affiliate config

Edit `/js/affiliates.js` only when programs are approved. Until then keep `#` and label secondary CTAs as “not live yet”. Do **not** invent live affiliate URLs. Do **not** use `#` as the only hotel action — use Official website links on hotel picks.

## Local preview

```bash
cd /workspace/noravellestays-site
python3 -m http.server 8080
```

Open `http://127.0.0.1:8080/`.

## Legal / contact

- `/affiliate-disclosure/`, `/privacy/`, `/terms/`, `/disclaimer/`, `/how-pricing-works/`
- Contact: FormSubmit → `joshuaofisrael@gmail.com`, subject `[Contact: Noravelle Stays]`
- Checklist: `ops/LEGAL_CONTENT_NOTES.md`

## Content rules

- Original en-US prose; no scraped OTA copy; no hotel brand photo scraping
- Named hotels: nominative fair use; verify official URLs before publishing
- Soft commerce only; no “Book now on Noravelle”
- No false Expedia / OTA undercut claims
- Independent editorial picks — not “official partners”

## SEO

- Organization + WebSite on homepage; Article / BreadcrumbList on guides, hotel pages, day plans
- Internal links across destinations, hotels, day plans, guides, resources
- White-hat only — see `ops/SEO_PUSH_NOTES.md`
