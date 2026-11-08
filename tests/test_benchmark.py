"""Benchmark end-to-end humanizer-id atas pasangan draf mentah vs hasil suntingan.

Mengukur efektivitas ruleset pada teks multi-kalimat nyata:
- Jumlah temuan audit pada draf mentah AI vs versi hasil suntingan
- Persentase reduksi temuan
- Kerapatan temuan per 100 kata
- Laporan rinci per kategori kaidah

Dijalankan via: python tests/test_benchmark.py  (atau pytest)
"""

import sys
import os
import re
import json
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from audit import audit_text


def extract_blockquotes(md_text):
    """Ambil pasangan (draf_mentah, hasil_suntingan) dari file contoh markdown.

    Struktur file: bagian 'Draf Mentah' dan 'Hasil Suntingan' masing-masing
    memuat blok kutipan (baris diawali '>').
    """
    sections = re.split(r"^##\s+", md_text, flags=re.MULTILINE)
    raw, edited = [], []
    for sec in sections:
        title = sec.splitlines()[0].lower() if sec.splitlines() else ""
        quotes = []
        buf = []
        for line in sec.splitlines()[1:]:
            if line.startswith(">"):
                buf.append(line.lstrip("> ").strip())
            elif buf:
                quotes.append(" ".join(buf))
                buf = []
        if buf:
            quotes.append(" ".join(buf))
        if "draf mentah" in title:
            raw = quotes
        elif "hasil suntingan" in title:
            edited = quotes
    return " ".join(raw), " ".join(edited)


def count_words(text):
    return len(re.findall(r"\S+", text))


def summarize(findings, text):
    """Ringkas temuan: total, per kategori, kerapatan per 100 kata."""
    per_cat = {}
    for m in findings:
        per_cat[m["kategori"]] = per_cat.get(m["kategori"], 0) + 1
    n_words = count_words(text)
    density = (len(findings) / n_words * 100) if n_words else 0.0
    return {
        "total": len(findings),
        "per_kategori": per_cat,
        "kata": n_words,
        "per_100_kata": round(density, 2),
    }


class TestBenchmark(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(os.path.join(ROOT, "data", "kalke-indonesia.json"), encoding="utf-8") as f:
            cls.kalke = json.load(f)
        with open(os.path.join(ROOT, "data", "glosarium-lintas-bidang.json"), encoding="utf-8") as f:
            cls.glos = json.load(f)

        cls.examples_dir = os.path.join(ROOT, "examples")
        cls.docs = {}
        for fn in sorted(os.listdir(cls.examples_dir)):
            if fn.endswith(".md"):
                with open(os.path.join(cls.examples_dir, fn), encoding="utf-8") as f:
                    raw, edited = extract_blockquotes(f.read())
                if raw and edited:
                    cls.docs[fn] = (raw, edited)
        cls.results = {fn: (summarize(audit_text(raw, cls.kalke, cls.glos), raw),
                            summarize(audit_text(ed, cls.kalke, cls.glos), ed))
                       for fn, (raw, ed) in cls.docs.items()}

    def test_all_examples_parsed(self):
        """Minimal 5 dokumen benchmark ter-parse dengan pasangan lengkap."""
        self.assertGreaterEqual(len(self.docs), 5, f"Hanya {len(self.docs)} dokumen ter-parse")

    def test_edited_version_reduces_findings_significantly(self):
        """Versi suntingan wajib mereduksi temuan minimal 60% per dokumen."""
        for fn, (before, after) in self.results.items():
            if before["total"] == 0:
                continue
            reduction = 1 - (after["total"] / before["total"])
            self.assertGreaterEqual(
                reduction, 0.6,
                f"{fn}: reduksi hanya {reduction:.0%} ({before['total']} -> {after['total']} temuan)")

    def test_edited_version_lower_density(self):
        """Kerapatan temuan per 100 kata pada versi suntingan lebih rendah dari draf mentah."""
        for fn, (before, after) in self.results.items():
            self.assertLess(
                after["per_100_kata"], before["per_100_kata"],
                f"{fn}: kerapatan suntingan ({after['per_100_kata']}) >= draf ({before['per_100_kata']})")


if __name__ == "__main__":
    # Mode laporan: cetak tabel markdown lalu jalankan test
    import unittest as ut
    loader = ut.TestLoader()
    suite = loader.loadTestsFromTestCase(TestBenchmark)
    runner = ut.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Setelah test, cetak laporan metrik
    inst = TestBenchmark("test_all_examples_parsed")
    inst.setUpClass()
    print("\n## Laporan Benchmark End-to-End\n")
    print("| Dokumen | Kata (Mentah) | Temuan Mentah | /100 kata | Temuan Suntingan | /100 kata | Reduksi |")
    print("|---|---|---|---|---|---|---|")
    for fn, (before, after) in inst.results.items():
        red = f"{1 - after['total']/before['total']:.0%}" if before["total"] else "n/a"
        print(f"| {fn} | {before['kata']} | {before['total']} | {before['per_100_kata']} | {after['total']} | {after['per_100_kata']} | {red} |")

    sys.exit(0 if result.wasSuccessful() else 1)
