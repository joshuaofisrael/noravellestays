/**
 * Noravelle Stays — affiliate URL slots
 * ------------------------------------
 * Swap '#' for live deep links when programs are approved.
 * Recommended networks (examples — not endorsements):
 *   flights: Travelpayouts / Aviasales, Kayak affiliate, similar flight metasearch
 *            (Avoid relying on Expedia Creator for flights — often $0 flight commission.)
 *   hotels:  OTA / hotel affiliate programs when live
 *   cars:    optional future car-rental affiliate
 *
 * Pages use: <a data-affiliate="flights|hotels|cars" href="#">…</a>
 * main.js rewrites href from this config on DOMContentLoaded.
 */
window.NORAVELLE_AFFILIATES = {
  hotels: "#",
  flights: "#",
  cars: "#"
};
