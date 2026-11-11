"""Test suite regresi humanizer-id.

Bisa dijalankan lewat:
  pytest
atau tanpa dependensi pihak ketiga via:
  python tests/test_regression.py
"""

import sys
import os
import json
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from audit import audit_text


class TestHumanizerRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        kalke_path = os.path.join(ROOT, "data", "kalke-indonesia.json")
        glos_path = os.path.join(ROOT, "data", "glosarium-lintas-bidang.json")
        with open(kalke_path, encoding="utf-8") as f:
            cls.kalke = json.load(f)
        with open(glos_path, encoding="utf-8") as f:
            cls.glos = json.load(f)

        cls.entries = []
        def walk(x):
            if isinstance(x, dict):
                if "id" in x and "pola" in x:
                    cls.entries.append(x)
                for v in x.values():
                    walk(v)
            elif isinstance(x, list):
                for v in x:
                    walk(v)
        walk(cls.kalke)

        cls.aktif = [e for e in cls.entries if not e["pola"].startswith("[telaah]")]
        cls.telaah = [e for e in cls.entries if e["pola"].startswith("[telaah]")]

    def test_dataset_integrity(self):
        """Memastikan semua ID unik dan skema field esensial lengkap."""
        self.assertGreaterEqual(len(self.entries), 200)
        ids = [e["id"] for e in self.entries]
        self.assertEqual(len(ids), len(set(ids)), "Terdapat ID ganda dalam dataset!")
        for e in self.entries:
            self.assertTrue(e["contoh_salah"].strip(), f"ID {e['id']} tanpa contoh_salah")
            self.assertTrue(e["contoh_benar"].strip(), f"ID {e['id']} tanpa contoh_benar")

    def test_all_wrong_examples_caught(self):
        """100% contoh salah entri aktif WAJIB terdeteksi."""
        missed = []
        for e in self.aktif:
            detected = [m["id"] for m in audit_text(e["contoh_salah"], self.kalke, self.glos)]
            if e["id"] not in detected:
                missed.append((e["id"], e["pola"]))
        self.assertEqual(missed, [], f"Ada contoh_salah yang tidak terdeteksi: {missed}")

    def test_zero_false_positives_on_correct_examples(self):
        """0% False Positive pada contoh benar untuk kaidah dirinya sendiri."""
        fp = []
        for e in self.aktif:
            detected = [m["id"] for m in audit_text(e["contoh_benar"], self.kalke, self.glos)]
            if e["id"] in detected:
                fp.append((e["id"], e["pola"]))
        self.assertEqual(fp, [], f"False Positive terdeteksi pada contoh_benar: {fp}")

    def test_negative_corpus_zero_findings(self):
        """Korpus negatif (prosa baku lintas domain) wajib 0 temuan."""
        corpus_path = os.path.join(ROOT, "tests", "corpus_negative.json")
        with open(corpus_path, encoding="utf-8") as f:
            corpus = json.load(f)

        offending = []
        for sentence in corpus["kalimat"]:
            findings = audit_text(sentence, self.kalke, self.glos)
            if findings:
                offending.append((sentence[:50], [m["id"] for m in findings]))
        self.assertEqual(offending, [], f"FP korpus negatif: {offending}")

    def test_manual_review_entries_excluded_from_regex(self):
        """Entri [telaah] tidak boleh menembak contoh_benar dirinya via regex otomatis."""
        accidental = []
        for e in self.telaah:
            detected = [m["id"] for m in audit_text(e["contoh_benar"], self.kalke, self.glos)]
            if e["id"] in detected:
                accidental.append(e["id"])
        self.assertEqual(accidental, [], f"Entri [telaah] memicu FP pada teks benar: {accidental}")


    def test_eyd_v_dan_naskah_dinas_2025(self):
        """Memastikan kaidah EYD V, Seri Penyuluhan 2025, dan Tata Naskah Dinas terdeteksi akurat."""
        cases = [
            ("Penyelenggaraan kongres angkatan ke-XI berjalan lancar.", "SPE-011"),
            ("Pelamar minimal lulusan S1 dari perguruan tinggi terakreditasi.", "SPE-012"),
            ("Pejabat berwenang dengan NIP. 198204xxxxxxxxxxxx menandatangani berkas.", "DIN-006"),
            ("Surat edaran diteken oleh Plt Kepala Biro Hukum.", "DIN-007"),
            ("Panitia memberitahukan kepada peserta bahwa jadwal ujian diubah.", "DIN-008"),
            ("Bagi semua pegawai menyerahkan laporan kinerja sebelum Jumat.", "DIN-009"),
            ("Walaupun anggaran terbatas, namun riset tetap rampung tepat waktu.", "SPK-010"),
            ("Keterlambatan pengiriman disebabkan terjadinya cuaca buruk.", "SPK-011"),
            ("Kedua delegasi saling berpandangan sebelum menandatangani perjanjian.", "BPK-046"),
        ]
        for text, expected_id in cases:
            ids = [m["id"] for m in audit_text(text, self.kalke, self.glos)]
            self.assertIn(expected_id, ids, f"{expected_id} gagal terdeteksi pada: {text}")

        clean = "Meskipun anggaran terbatas, Plt. Kepala Biro berbekal NIP 198204xxxxxxxxxxxx dan ijazah S-1 menyelesaikan rapat."
        self.assertEqual(audit_text(clean, self.kalke, self.glos), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
