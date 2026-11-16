"""Test modul report: nomor urut, prioritas, render, dan tulis laporan."""
import os
import sys
import unittest
import tempfile
import shutil

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from humanizer_id.report import (
    klasifikasi_prioritas,
    nomor_laporan_berikutnya,
    render_laporan,
    tulis_laporan,
)


def buat_temuan(kategori="kalke_terjemahan_mesin", baris=1, pola="in order to",
                saran="untuk / guna", kalimat="Dalam rangka untuk menguji sistem."):
    return {
        "baris": baris, "kategori": kategori, "id": "KLK-001",
        "pola": pola, "saran": saran if isinstance(saran, list) else [saran],
        "penjelasan": "Kalke terjemahan mesin.",
        "kalimat": kalimat,
    }


class TestPrioritas(unittest.TestCase):
    def test_high(self):
        self.assertEqual(klasifikasi_prioritas("kalke_terjemahan_mesin"), "HIGH")
        self.assertEqual(klasifikasi_prioritas("verba_ringan"), "HIGH")
        self.assertEqual(klasifikasi_prioritas("retorika_klise_ai"), "HIGH")

    def test_medium_glosarium(self):
        self.assertEqual(klasifikasi_prioritas("glosarium_teknologi"), "MEDIUM")
        self.assertEqual(klasifikasi_prioritas("glosarium_hukum"), "MEDIUM")

    def test_low(self):
        self.assertEqual(klasifikasi_prioritas("jurnalistik_ekonomi_kata"), "LOW")
        self.assertEqual(klasifikasi_prioritas("pedoman_kampus_ipb"), "LOW")

    def test_unknown_dianggap_low(self):
        self.assertEqual(klasifikasi_prioritas("kategori_baru_apa_saja"), "LOW")


class TestNomorUrut(unittest.TestCase):
    def test_folder_kosong(self):
        d = tempfile.mkdtemp()
        try:
            self.assertEqual(nomor_laporan_berikutnya(d), 1)
        finally:
            shutil.rmtree(d)

    def test_melanjutkan_nomor_tertinggi(self):
        d = tempfile.mkdtemp()
        try:
            for n in (1, 3):
                open(os.path.join(d, f"audit-{n:03d}-2026-11-16.md"), "w").close()
            self.assertEqual(nomor_laporan_berikutnya(d), 4)
        finally:
            shutil.rmtree(d)

    def test_folder_tidak_ada(self):
        self.assertEqual(nomor_laporan_berikutnya("path/tidak/ada/x"), 1)


class TestRender(unittest.TestCase):
    def test_kosong_nol_temuan(self):
        out = render_laporan([], "naskah.md")
        self.assertIn("Nol temuan", out)

    def test_nomor_dan_prioritas_muncul(self):
        temuan = [buat_temuan(), buat_temuan(kategori="glosarium_teknologi", pola="cache", baris=2)]
        out = render_laporan(temuan, "naskah.md", tanggal="2026-11-16")
        self.assertIn("[1] HIGH", out)
        self.assertIn("[2] MEDIUM", out)
        self.assertIn("2 temuan", out)
        self.assertIn("Mode AFTER", out)
        self.assertIn("2026-11-16", out)

    def test_high_selalu_di_atas(self):
        temuan = [
            buat_temuan(kategori="jurnalistik_ekonomi_kata", pola="ditemukan", baris=1),
            buat_temuan(kategori="verba_ringan", pola="melakukan", baris=2),
        ]
        out = render_laporan(temuan, "naskah.md")
        self.assertLess(out.index("[1] HIGH"), out.index("[2] LOW"))


class TestTulis(unittest.TestCase):
    def test_tulis_dan_nomor_naik(self):
        d = tempfile.mkdtemp()
        try:
            p1 = tulis_laporan([buat_temuan()], "a.md", d, tanggal="2026-11-16")
            p2 = tulis_laporan([buat_temuan()], "a.md", d, tanggal="2026-11-17")
            self.assertTrue(p1.endswith("audit-001-2026-11-16.md"))
            self.assertTrue(p2.endswith("audit-002-2026-11-17.md"))
            self.assertTrue(os.path.exists(p1) and os.path.exists(p2))
        finally:
            shutil.rmtree(d)


if __name__ == "__main__":
    unittest.main()
