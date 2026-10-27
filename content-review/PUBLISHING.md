# Publishing gate for noravellestays.com

This folder is excluded from the Jekyll build. It is not part of the public site.

## What blocks a deploy

Workflow: `.github/workflows/legal-hold.yml`

- Job `legal-gate` runs on every pull request and on every push to `main`.
- Job `pages` has `needs: legal-gate` and runs only for a push to `main`. It builds the Jekyll site, refuses the artifact if `drafts/` or the hold test page is present, uploads the artifact, and deploys with `actions/deploy-pages`.
- A failing `legal-gate` job skips `pages`. No Actions deploy runs.

The Actions job `pages` waits on `legal-gate`. The repository Pages setting can still be a legacy branch deploy, which does not wait. See Confirmed publisher below for which mode was live after the gate shipped.

`drafts/`, `content-review/`, `scripts/`, and `tests/` are in `_config.yml` `exclude`, and the deploy job checks that `drafts/` did not reach `_site`.

## Files

- `RULE.md`: owner rule, copied as given.
- `image-licences.json`: one row per image file. `status: HOLD` and `licence: null` means there is no documented licence. Credit text is copied from existing pages. It is not a guessed licence.
- `legal-holds.json`: path blocklist (rule 8). Empty until a person adds a path.
- `approvals.json`: exact `sha256` plus `approver` `Joshua` for a `HOLD_REVIEW` page. Automated runs must not add rows.
- `baseline-allowlist.json`: existing live pages whose current sha256 still matches. Each entry exempts only the listed rule keys. It is not an approval. Rule 8 and `HOLD_REVIEW` are never exempted. Editing the HTML drops the exemption and the page is checked again. A page that still uses a HOLD image will then fail, even when the edit was not about the image. Record a real licence or remove the image before changing that page.
- `queue.jsonl`: one JSON object per line. Fields are `ts`, `site`, `bot` (`Travel site bot`), `title`, `flagged`, `rule`, `sources`, `suggestion`, `draft_path`, `status` (`HOLD_REVIEW`).

## Code enforced checks

1. Keyword screen only. The words fraud, lawsuit, arrested, scam, abuse, corruption, and misconduct are flagged when they sit within 400 characters of a multi word proper name or a Hotel name. Whether the sentence is an allegation, a denial, or a fair report is judgement.
2. Not enforced in code. Sensitive personal information is judgement only.
3. Every `img` must match a manifest row that is not `HOLD` and that has a non empty `licence`. Decorative images that are not SVG are excepted (empty alt, `role=presentation`, `aria-hidden=true`, or class `decorative`). SVG images are always checked. A missing row fails closed. Licences are not guessed.
4. A page with Article, NewsArticle, BlogPosting, Report, Event, or Review schema, or an element whose class or id marks sources, claims, or facts, needs at least one off site `http` link in an anchor. Whether that link supports the claim is judgement.
5. The phrases `guaranteed return`, `you should invest`, and `medical advice` are flagged. A denial in the 80 characters before the phrase, inside the same sentence, is not flagged.
6. The terms vote, polling, ballot, and `registration deadline` (plus simple variants such as voting or ballots) are flagged. Whether they are really about an election is judgement. A hit still fails the gate unless the current file hash is allowlisted.
7. The phrases `official partner`, `official partners`, and `endorsed by` are flagged unless denied in that same short window. An image marked `synthetic: true`, or captioned as AI generated, must include the word `illustrative` in the alt or the nearby caption. Whether a headline is stronger than the evidence is judgement only.
8. A published path listed in `legal-holds.json` fails the gate. Choosing what to list is a human step. The allowlist cannot override it.

`HOLD_REVIEW` is separate from the eight rules. A published page with `<meta name="review-status" content="HOLD_REVIEW">` fails unless `approvals.json` contains that path, that file's sha256, and approver `Joshua`. A page under `drafts/` is unpublished. The gate records it and does not fail the build. Moving it into the published tree fails the gate. The unit test does that copy in a temp folder and never writes it into the site.

## Commands

```bash
python3 scripts/legal_gate.py --write-manifest
python3 scripts/legal_gate.py --write-baseline
python3 scripts/legal_gate.py --ci
python3 -m unittest -v tests/test_legal_gate.py
```

`--write-baseline` rewrites the allowlist from the current live findings. Do not run it to hide a new page.

## Confirmed publisher

Checked after merge commit `6a5c76b170063d5706cb7a154126fdc8e1d600bb` on 27 Oct 2026.

The Legal hold workflow on `main` succeeded. Job `legal-gate` passed, then job `pages` built the site with Jekyll, rejected the artifact if drafts had leaked, uploaded it, and `deploy-pages` succeeded.

https://github.com/joshuaofisrael/noravellestays/actions/runs/40561644887

The Pages setting was still `build_type: legacy`, source branch `main`. A request to switch that setting to GitHub Actions returned 403. Branch protection could not be read or changed (403).

GitHub also ran its built in pages build and deployment for the same commit, and that run succeeded:

https://github.com/joshuaofisrael/noravellestays/actions/runs/40561643022

What actually blocks:

- In this workflow, `pages` needs `legal-gate`. A failing gate skips the Actions upload and the `deploy-pages` step. That order ran on `main`.
- The legacy branch publisher does not wait for `legal-gate`. A red gate does not stop that publisher. Stopping it needs the Pages source set to GitHub Actions, or a branch rule that requires the `legal-gate` check. This token cannot set either one.

After that deploy, `https://noravellestays.com/` and `/hotels/tampa/` returned 200. `/drafts/test-hotel-example/`, `/content-review/queue.jsonl`, and `/tests/fixtures/clean-page/` returned 404.
