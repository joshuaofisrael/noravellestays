#!/usr/bin/env python3
"""Legal hold gate tests. The hold fixture is never placed in the published tree."""

from __future__ import annotations

import hashlib
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import legal_gate  # noqa: E402


def visible_text(html: str) -> str:
    text = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.I)
    text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    return text


class LegalGateTests(unittest.TestCase):
    def test_clean_page_passes(self) -> None:
        html = (ROOT / "tests/fixtures/clean-page/index.html").read_text(encoding="utf-8")
        findings, notes = legal_gate.analyze_html(html, "tests/fixtures/clean-page/index.html", {"images": []})
        self.assertEqual(findings, [], notes)
        self.assertEqual(notes, [])

    def test_hold_page_fails_when_moved_into_published_tree(self) -> None:
        src = ROOT / "drafts/test-hotel-example/index.html"
        html = src.read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dest = root / "news" / "test-hotel-example"
            dest.mkdir(parents=True)
            (dest / "index.html").write_text(html, encoding="utf-8")
            review = root / "content-review"
            review.mkdir()
            (review / "image-licences.json").write_text(json.dumps({"images": []}), encoding="utf-8")
            (review / "approvals.json").write_text(json.dumps({"approvals": []}), encoding="utf-8")
            (review / "legal-holds.json").write_text(json.dumps({"paths": []}), encoding="utf-8")
            (review / "baseline-allowlist.json").write_text(json.dumps({"pages": []}), encoding="utf-8")
            outcome = legal_gate.evaluate(root, write_queue=False)
            rules = sorted({item.rule for item in outcome.blocking})
            self.assertIn("1", rules)
            self.assertIn("4", rules)
            self.assertIn("HOLD_REVIEW", rules)
            self.assertTrue(all(item.path == "news/test-hotel-example/index.html" for item in outcome.blocking))

    def test_hold_draft_is_not_a_publish_blocker(self) -> None:
        outcome = legal_gate.evaluate(ROOT, write_queue=False)
        draft = [item for item in outcome.findings if item.path.startswith("drafts/")]
        self.assertTrue(draft)
        self.assertTrue(any(item.rule == "1" for item in draft))
        self.assertFalse(any(item.path.startswith("drafts/") for item in outcome.blocking))

    def test_joshua_approval_clears_only_the_hold_marker(self) -> None:
        html = (
            "<!DOCTYPE html><html><head>"
            '<meta name="review-status" content="HOLD_REVIEW">'
            "<title>TEST quiet hold</title></head>"
            "<body><p>TEST. A quiet note with no allegation and no image.</p></body></html>"
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "notes" / "index.html"
            page.parent.mkdir(parents=True)
            page.write_text(html, encoding="utf-8")
            digest = hashlib.sha256(html.encode("utf-8")).hexdigest()
            review = root / "content-review"
            review.mkdir()
            (review / "image-licences.json").write_text("{}", encoding="utf-8")
            (review / "legal-holds.json").write_text(json.dumps({"paths": []}), encoding="utf-8")
            (review / "baseline-allowlist.json").write_text(json.dumps({"pages": []}), encoding="utf-8")
            (review / "approvals.json").write_text(
                json.dumps({"approvals": [{"path": "notes/index.html", "sha256": digest, "approver": "Josh"}]}),
                encoding="utf-8",
            )
            blocked = legal_gate.evaluate(root, write_queue=False)
            self.assertTrue(any(item.rule == "HOLD_REVIEW" for item in blocked.blocking))
            (review / "approvals.json").write_text(
                json.dumps(
                    {
                        "approvals": [
                            {"path": "notes/index.html", "sha256": "0" * 64, "approver": "Joshua"},
                            {"path": "notes/index.html", "sha256": digest, "approver": "Joshua"},
                        ]
                    }
                ),
                encoding="utf-8",
            )
            cleared = legal_gate.evaluate(root, write_queue=False)
            self.assertFalse(any(item.rule == "HOLD_REVIEW" for item in cleared.blocking))
            self.assertEqual(cleared.blocking, [])

    def test_allegation_stays_blocked_even_with_joshua_approval(self) -> None:
        src = (ROOT / "drafts/test-hotel-example/index.html").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "news" / "index.html"
            page.parent.mkdir(parents=True)
            page.write_text(src, encoding="utf-8")
            digest = hashlib.sha256(src.encode("utf-8")).hexdigest()
            review = root / "content-review"
            review.mkdir()
            (review / "image-licences.json").write_text("{}", encoding="utf-8")
            (review / "legal-holds.json").write_text(json.dumps({"paths": []}), encoding="utf-8")
            (review / "baseline-allowlist.json").write_text(json.dumps({"pages": []}), encoding="utf-8")
            (review / "approvals.json").write_text(
                json.dumps(
                    {"approvals": [{"path": "news/index.html", "sha256": digest, "approver": "Joshua"}]}
                ),
                encoding="utf-8",
            )
            outcome = legal_gate.evaluate(root, write_queue=False)
            rules = {item.rule for item in outcome.blocking}
            self.assertNotIn("HOLD_REVIEW", rules)
            self.assertIn("1", rules)
            self.assertIn("4", rules)

    def test_rule_8_is_not_allowlisted(self) -> None:
        html = "<!DOCTYPE html><html><head><title>Plain</title></head><body><p>A plain page.</p></body></html>"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "secret" / "index.html"
            page.parent.mkdir(parents=True)
            page.write_text(html, encoding="utf-8")
            digest = hashlib.sha256(html.encode("utf-8")).hexdigest()
            review = root / "content-review"
            review.mkdir()
            (review / "image-licences.json").write_text("{}", encoding="utf-8")
            (review / "approvals.json").write_text(json.dumps({"approvals": []}), encoding="utf-8")
            (review / "legal-holds.json").write_text(
                json.dumps({"paths": ["secret/index.html"]}),
                encoding="utf-8",
            )
            (review / "baseline-allowlist.json").write_text(
                json.dumps(
                    {
                        "pages": [
                            {
                                "path": "secret/index.html",
                                "sha256": digest,
                                "exemptions": [{"rule": "8", "key": "secret/index.html"}],
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            outcome = legal_gate.evaluate(root, write_queue=False)
            self.assertTrue(any(item.rule == "8" for item in outcome.blocking))

    def test_image_rules_and_decorative_exception(self) -> None:
        manifest = {
            "images": [
                {"path": "photo.jpg", "status": "HOLD", "licence": None},
                {"path": "owned.jpg", "status": "documented", "licence": "Publisher retains the copyright."},
                {"path": "icons/mark.svg", "status": "documented", "licence": "Original icon."},
            ]
        }
        html = """
        <img src="/photo.jpg" alt="A lobby">
        <img src="/owned.jpg" alt="A desk">
        <img src="/blank.jpg" alt="">
        <img src="/icons/mark.svg" alt="" role="presentation">
        <img src="art.png" alt="AI generated portrait of a guest">
        """
        findings, _notes = legal_gate.analyze_html(html, "city/index.html", manifest)
        keys = {(item.rule, item.key) for item in findings}
        self.assertIn(("3", "photo.jpg"), keys)
        self.assertNotIn(("3", "owned.jpg"), keys)
        self.assertNotIn(("3", "blank.jpg"), keys)
        self.assertNotIn(("3", "icons/mark.svg"), keys)
        self.assertIn(("3", "city/art.png"), keys)
        self.assertIn(("7", "ai:city/art.png"), keys)

    def test_phrase_denials_are_not_hits(self) -> None:
        denied = (
            "<p>We do not give medical advice.</p>"
            "<p>These hotels do not endorse Noravelle Stays and are not “official partners.”</p>"
        )
        findings, notes = legal_gate.analyze_html(denied, "x/index.html", {"images": []})
        self.assertFalse(any(item.rule in {"5", "7"} for item in findings))
        phrases = {note.phrase for note in notes}
        self.assertIn("medical advice", phrases)
        self.assertIn("official partners", phrases)
        affirmed = "<p>You should invest now for a guaranteed return. We are the official partner of the resort.</p>"
        findings, _notes = legal_gate.analyze_html(affirmed, "x/index.html", {"images": []})
        rules = {item.key for item in findings if item.rule in {"5", "7"}}
        self.assertIn("you should invest", rules)
        self.assertIn("guaranteed return", rules)
        self.assertIn("official partner", rules)

    def test_election_terms_and_name_screen(self) -> None:
        html = "<p>The registration deadline passed and the polling place moved. This offer is a scam.</p>"
        findings, _notes = legal_gate.analyze_html(html, "x/index.html", {"images": []})
        keys = {item.key for item in findings}
        self.assertIn("registration deadline", keys)
        self.assertIn("polling", keys)
        self.assertFalse(any(item.rule == "1" for item in findings))
        alleged = "<p>Test Hotel Example was arrested in a fraud scam.</p>"
        findings, _notes = legal_gate.analyze_html(alleged, "x/index.html", {"images": []})
        self.assertTrue(any(item.rule == "1" and "Test Hotel Example" in item.key for item in findings))

    def test_article_without_source_fails_and_with_source_passes(self) -> None:
        bare = '<script type="application/ld+json">{"@type":"Article"}</script><p>A claim.</p>'
        findings, _notes = legal_gate.analyze_html(bare, "x/index.html", {"images": []})
        self.assertTrue(any(item.rule == "4" for item in findings))
        sourced = bare + '<p><a href="https://www.si.edu/visit">Smithsonian visit page</a></p>'
        findings, _notes = legal_gate.analyze_html(sourced, "x/index.html", {"images": []})
        self.assertFalse(any(item.rule == "4" for item in findings))

    def test_new_public_prose_has_no_hyphen_or_dash(self) -> None:
        pages = [
            ROOT / "drafts/test-hotel-example/index.html",
            ROOT / "tests/fixtures/clean-page/index.html",
        ]
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        section = readme.split("## Content review", 1)[1].split("## SEO", 1)[0]
        samples = [visible_text(path.read_text(encoding="utf-8")) for path in pages]
        samples.append(section)
        for sample in samples:
            self.assertNotIn("-", sample)
            self.assertNotIn("–", sample)
            self.assertNotIn("—", sample)

    def test_drafts_are_excluded_from_the_pages_config(self) -> None:
        config = (ROOT / "_config.yml").read_text(encoding="utf-8")
        for folder in ("drafts/", "content-review/", "scripts/", "tests/"):
            self.assertIn(f"- {folder}", config)
        workflow = (ROOT / ".github/workflows/legal-hold.yml").read_text(encoding="utf-8")
        self.assertIn("needs: legal-gate", workflow)
        self.assertIn("actions/deploy-pages", workflow)

    def test_manifest_does_not_guess_and_records_credit(self) -> None:
        manifest = json.loads((ROOT / "content-review/image-licences.json").read_text(encoding="utf-8"))
        paths = {item["path"] for item in manifest["images"]}
        for rel in legal_gate.image_files(ROOT):
            self.assertIn(rel, paths)
        for item in manifest["images"]:
            self.assertEqual(item["status"], "HOLD")
            self.assertFalse(item.get("licence"))
        by_path = {item["path"]: item for item in manifest["images"]}
        self.assertIn("Noravelle", by_path["images/hotels/tampa-hero.jpg"]["credit"])
        self.assertIn("Illustrative", by_path["assets/img/breakfast.webp"]["credit"])

    def test_live_site_gate_is_not_blocking(self) -> None:
        outcome = legal_gate.evaluate(ROOT, write_queue=False)
        self.assertEqual(outcome.missing_config, [])
        self.assertEqual(outcome.blocking, [])
        published_rules = {item.rule for item in outcome.findings if item.published}
        self.assertNotIn("1", published_rules)
        self.assertNotIn("5", published_rules)
        self.assertNotIn("7", published_rules)
        phrases = {note.phrase for note in outcome.notes}
        self.assertIn("official partners", phrases)
        self.assertIn("medical advice", phrases)

    def test_approvals_file_is_empty(self) -> None:
        data = json.loads((ROOT / "content-review/approvals.json").read_text(encoding="utf-8"))
        self.assertEqual(data["approvals"], [])

    def test_queue_lines_use_the_required_fields(self) -> None:
        raw = (ROOT / "content-review/queue.jsonl").read_text(encoding="utf-8").splitlines()
        rows = [json.loads(line) for line in raw if line.strip()]
        self.assertTrue(rows)
        draft = [row for row in rows if row["draft_path"].startswith("drafts/")]
        self.assertTrue(draft)
        for row in rows:
            self.assertEqual(list(row.keys()), list(legal_gate.QUEUE_FIELDS))
            self.assertEqual(row["site"], "noravellestays.com")
            self.assertEqual(row["bot"], "Travel site bot")
            self.assertEqual(row["status"], "HOLD_REVIEW")
            self.assertIsInstance(row["sources"], list)

    def test_queue_append_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "notes" / "index.html"
            page.parent.mkdir(parents=True)
            page.write_text(
                '<script type="application/ld+json">{"@type":"Event"}</script><p>No source here.</p>',
                encoding="utf-8",
            )
            review = root / "content-review"
            review.mkdir()
            (review / "image-licences.json").write_text("{}", encoding="utf-8")
            (review / "legal-holds.json").write_text(json.dumps({"paths": []}), encoding="utf-8")
            (review / "approvals.json").write_text(json.dumps({"approvals": []}), encoding="utf-8")
            legal_gate.evaluate(root, write_queue=True)
            first = (review / "queue.jsonl").read_text(encoding="utf-8")
            legal_gate.evaluate(root, write_queue=True)
            second = (review / "queue.jsonl").read_text(encoding="utf-8")
            self.assertEqual(first, second)
            self.assertIn('"rule": "4"', first)
            self.assertIn('"bot": "Travel site bot"', first)


if __name__ == "__main__":
    unittest.main()
