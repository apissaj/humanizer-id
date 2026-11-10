"""Unit test untuk mode perbaikan otomatis (autofix) leksikal deterministik."""

import unittest
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from audit import load_data
from humanizer_id.engine import fix_text


class TestAutofix(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.kalke, cls.glos, _ = load_data()

    def test_fix_bound_forms_eyd_v(self):
        """Bentuk terikat EYD V wajib diperbaiki serangkai tanpa merusak kata lain."""
        sample = "Penanganan pasca panen dan kegiatan non formal diselenggarakan oleh sub bagian humas."
        fixed, count, logs = fix_text(sample, self.kalke, self.glos)
        self.assertIn("pascapanen", fixed)
        self.assertIn("nonformal", fixed)
        self.assertIn("subbagian", fixed)
        self.assertEqual(count, 3)

    def test_fix_transitive_verbs_redundant_preposition(self):
        """Verba transitif dengan preposisi mubazir tentang/mengenai wajib dibersihkan."""
        sample = "Artikel ini membahas tentang optimasi sistem dan menjelaskan mengenai metrik performa."
        fixed, count, logs = fix_text(sample, self.kalke, self.glos)
        self.assertIn("membahas optimasi sistem", fixed)
        self.assertIn("menjelaskan metrik performa", fixed)
        self.assertNotIn("membahas tentang", fixed)
        self.assertNotIn("menjelaskan mengenai", fixed)
        self.assertEqual(count, 2)

    def test_fix_preserves_capitalization(self):
        """Huruf kapital di awal kalimat wajib dipertahankan setelah penggantian."""
        sample = "Pasca panen memerlukan fasilitas pengeringan yang memadai."
        fixed, count, logs = fix_text(sample, self.kalke, self.glos)
        self.assertTrue(fixed.startswith("Pascapanen"), f"Kapitalisasi gagal: {fixed}")

    def test_clean_text_remains_untouched(self):
        """Teks yang sudah baku tidak boleh mengalami perubahan apapun."""
        sample = "Pascapanen padi berlangsung tertib di bawah pengawasan subbagian logistik."
        fixed, count, logs = fix_text(sample, self.kalke, self.glos)
        self.assertEqual(fixed, sample)
        self.assertEqual(count, 0)


if __name__ == "__main__":
    unittest.main()
