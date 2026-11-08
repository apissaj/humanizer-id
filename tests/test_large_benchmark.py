"""Benchmark skala besar atas 20 dokumen keluaran AI lintas domain."""

import sys
import os
import json
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from audit import audit_text


class TestLargeBenchmark(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(os.path.join(ROOT, "data", "kalke-indonesia.json"), encoding="utf-8") as f:
            cls.kalke = json.load(f)
        with open(os.path.join(ROOT, "data", "glosarium-lintas-bidang.json"), encoding="utf-8") as f:
            cls.glos = json.load(f)

        cls.corpus_dir = os.path.join(ROOT, "tests", "benchmark_corpus")
        cls.files = sorted([f for f in os.listdir(cls.corpus_dir) if f.endswith(".md")])

    def test_corpus_count(self):
        """Memastikan minimal 20 dokumen AI uji tersedia."""
        self.assertGreaterEqual(len(self.files), 20)

    def test_overall_detection_rate(self):
        """Minimal 70% dokumen draf AI mentah terdeteksi memuat pola kebahasaan."""
        hit_docs = 0
        total_findings = 0
        for fn in self.files:
            with open(os.path.join(self.corpus_dir, fn), encoding="utf-8") as f:
                txt = f.read()
            findings = audit_text(txt, self.kalke, self.glos)
            if findings:
                hit_docs += 1
            total_findings += len(findings)

        hit_rate = hit_docs / len(self.files)
        self.assertGreaterEqual(
            hit_rate, 0.70,
            f"Tingkat deteksi hanya {hit_rate:.1%} ({hit_docs}/{len(self.files)} dokumen)")
        self.assertGreaterEqual(
            total_findings, 35,
            f"Total temuan terlalu sedikit ({total_findings} < 35)")


if __name__ == "__main__":
    unittest.main(verbosity=2)
