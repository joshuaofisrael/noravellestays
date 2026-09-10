/**
 * Noravelle Stays — optional affiliate URL slots
 * ---------------------------------------------
 * PRIMARY CTAs on hotel pages are official hotel websites (not this file).
 * These slots are OPTIONAL secondary “compare rates / flights” links for
 * when affiliate programs are approved. Keep "#" until then.
 *
 * Recommended networks (examples — not endorsements):
 *   flights: Travelpayouts / Aviasales, Kayak affiliate, similar flight metasearch
 *            (Avoid relying on Expedia Creator for flights — often $0 flight commission.)
 *   hotels:  OTA / hotel affiliate programs when live
 *   cars:    optional future car-rental affiliate
 *
 * Pages may use: <a data-affiliate="flights|hotels|cars" href="#">…</a>
 * Label those clearly as affiliate / “not live yet” — never as the only hotel action.
 * main.js rewrites href from this config on DOMContentLoaded.
 */
window.NORAVELLE_AFFILIATES = {
  hotels: "#",
  flights: "#",
  cars: "#"
};
