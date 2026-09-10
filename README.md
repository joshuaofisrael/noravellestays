# Noravelle Stays (`noravellestays.com`)

Static boutique / luxury-leaning US stay site for **Noravelle Stays**, owned by **Joshua Israel Ventures LLC**.

Affiliate-only MVP: editorial destination/hotel/flight guidance with soft **Compare rates / Compare flights** CTAs. **No payment collection, no checkout, not merchant of record.** Not positioned as cheap hotels.

> **Changelog:** Rebranded from ThinFee Stays (`thinfeestays.com` / `/workspace/thinfeestays-site` backup) to Noravelle Stays (`noravellestays.com` / `/workspace/noravellestays-site`).

## Stack

- Plain HTML (folder `index.html` URLs)
- `css/styles.css` — teal/navy travel aesthetic
- `js/affiliates.js` — swap live affiliate deep links (`hotels`, `flights`, `cars`)
- `js/main.js` — mobile nav + applies `data-affiliate` hrefs from config
- No required build step (`_generate.py` / `_patch_flights.py` are optional regenerate helpers)

## Affiliate config

Edit `/js/affiliates.js`:

```js
window.NORAVELLE_AFFILIATES = {
  hotels: "#",   // OTA / hotel program deep link
  flights: "#",  // Travelpayouts / Kayak-class (not Expedia Creator for flights — often $0)
  cars: "#"
};
```

Buttons use `data-affiliate="hotels|flights|cars"`. When a URL is not `#`, `main.js` adds `rel="nofollow sponsored noopener"` and `target="_blank"`.

**Do not invent live affiliate URLs** — keep `#` until programs are approved. Soft Compare CTAs only.

## Local preview

```bash
cd /workspace/noravellestays-site
python3 -m http.server 8080
```

Open `http://127.0.0.1:8080/` (root-absolute `/css/...` paths need a local server).

## Deploy

Netlify drag-and-drop or GitHub Pages from site root (where `index.html` lives). No build command. Canonical host: `https://noravellestays.com`.

## Legal / contact

- `/affiliate-disclosure/` — FTC, LLC, hotel + flight affiliates; boutique/luxury framing
- `/privacy/`, `/terms/`, `/disclaimer/`, `/how-pricing-works/`
- Contact form: FormSubmit → `joshuaofisrael@gmail.com`
  - Subject tag: `[Contact: Noravelle Stays]`
  - `_next` thanks URL: `https://noravellestays.com/contact/thanks/`

## Content rules

- Original en-US prose; no scraped OTA copy
- No fake live prices/star inventories
- Soft CTAs only; no “Book now on Noravelle”
- Boutique / high-ticket framing — not cheap hotels
- Do not claim we currently undercut Expedia’s hotel take
- Honest fee/affiliate claims on how-pricing-works and affiliate disclosure
