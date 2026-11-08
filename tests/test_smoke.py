"""
Smoke-test menyeluruh untuk ruleset Humanizer ID (302 kaidah).
Memastikan:
1. Setiap kaidah aktif memicu ID-nya sendiri 100% pada contoh salah (0 miss).
2. Setiap contoh benar bebas dari false positive (0 FP across 302 rules).
3. Korpus campuran lintas ragam (ilmiah, dinas, naratif, teknis) bersih 0 FP.
4. Throughput di atas 2.000 kata/detik.
"""

import unittest
import os
import sys
import json
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from audit import audit_text, load_data


class TestComprehensiveSmoke(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.kalke, cls.glos, _ = load_data()

    def test_all_active_rules_catch_own_false_example(self):
        """276 kaidah regex aktif wajib memicu ID-nya sendiri pada contoh salah."""
        miss_active = []
        for cat in self.kalke["kategori"].values():
            for e in cat["entri"]:
                if e["pola"].startswith("[telaah]"):
                    continue
                fs = audit_text(e["contoh_salah"], self.kalke, self.glos)
                fired = {f["id"] for f in fs}
                if e["id"] not in fired:
                    miss_active.append((e["id"], e["pola"]))
        self.assertEqual(
            len(miss_active), 0,
            f"Kaidah aktif gagal memicu dirinya sendiri: {miss_active}"
        )

    def test_zero_false_positives_across_all_correct_examples(self):
        """Seluruh 302 contoh benar wajib 100% bebas dari false positive."""
        fp_list = []
        for cat in self.kalke["kategori"].values():
            for e in cat["entri"]:
                fs = audit_text(e["contoh_benar"], self.kalke, self.glos)
                if fs:
                    fp_list.append((e["id"], [f["id"] for f in fs], e["contoh_benar"]))
        self.assertEqual(
            len(fp_list), 0,
            f"False positive pada contoh benar: {fp_list}"
        )

    def test_mixed_genre_corpus_clean_texts_zero_findings(self):
        """Teks ragam ilmiah, dinas, naratif, teknis yang baku wajib 0 temuan."""
        clean_samples = [
            "Penelitian ini menguji stabilitas termal material komposit berbasis serat nanokarbon.",
            "Sehubungan dengan surat Kepala Biro tertanggal 15 Oktober 2024 perihal evaluasi tahunan, kami sampaikan laporan kinerja.",
            "Infrastruktur komputasi awan menggunakan klaster Kubernetes terkelola pada tiga zona ketersediaan.",
            "Ketika menyeberang rel kereta api, warga diimbau untuk selalu berhati-hati.",
        ]
        for text in clean_samples:
            fs = audit_text(text, self.kalke, self.glos)
            self.assertEqual(
                len(fs), 0,
                f"False positive pada sampel bersih: {text} -> {[f['id'] for f in fs]}"
            )

    def test_performance_throughput_above_2000_wps(self):
        """Mesin audit wajib memproses minimal 2.000 kata/detik."""
        sample = "Penelitian ini mengkaji penerapan arsitektur sistem informasi terintegrasi untuk meningkatkan efisiensi operasional.\n" * 50
        words = len(sample.split())
        t0 = time.time()
        audit_text(sample, self.kalke, self.glos)
        dur = time.time() - t0
        wps = words / dur if dur > 0 else 99999
        self.assertGreater(wps, 2000, f"Throughput terlalu lambat: {wps:.0f} wps")


if __name__ == "__main__":
    unittest.main()
