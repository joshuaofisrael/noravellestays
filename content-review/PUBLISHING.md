# Publishing gate for noravellestays.com

This folder is excluded from the Jekyll build. It is not part of the public site.

## What blocks a deploy

Workflow: `.github/workflows/legal-hold.yml`

- Job `legal-gate` runs on every pull request and on every push to `main`.
- Job `pages` has `needs: legal-gate` and runs only for a push to `main`. It builds the Jekyll site, refuses the artifact if `drafts/` or the hold test page is present, uploads the artifact, and deploys with `actions/deploy-pages`.
- A failing `legal-gate` job skips `pages`. No Actions deploy runs.

GitHub Pages was previously a legacy branch deploy from `main` (`build_type: legacy`). That publisher starts from the branch itself and does not wait for Actions. Switching the repository Pages source to GitHub Actions is what makes `pages` the only publisher. The result of that switch is recorded at the bottom of this file after it is attempted. If the source is still legacy, this workflow can fail a pull request and can fail its own deploy job, but the legacy publisher can still update the live site from `main`.

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

Pending the Pages source change on this pull request. Until that change succeeds, treat the legacy branch publisher as still able to deploy `main` without this gate.
