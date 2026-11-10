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


    def test_kridalaksana_lanin_sugono_rules(self):
        """Memastikan kaidah Kridalaksana (afiksasi ganda), Lanin (kalke campur kode), dan Sugono (temporal) terdeteksi akurat."""
        samples = [
            ("Langkah ini bertujuan memperbesarkan ukuran sampel data.", "KRD-001"),
            ("Pemerintah berencana memperlebarkan jalan arteri di pesisir.", "KRD-002"),
            ("Pengembang wajib meng-update berkas konfigurasi sebelum rilis.", "LAN-001"),
            ("Sistem dirancang untuk meng-handle lonjakan lalu lintas data.", "LAN-003"),
            ("Model klasifikasi ini berhasil di-deploy ke peladen produksi.", "LAN-008"),
            ("Penelitian komparasi algoritma selesai di tahun 2024.", "DSG-001"),
            ("Pengambilan sampel survei lapangan dilakukan di bulan Mei.", "DSG-002"),
            ("Model AI bertransformasi sangat pesat di era modern saat ini.", "DSG-003"),
        ]
        for sentence, expected_id in samples:
            findings = audit_text(sentence, self.kalke, self.glos)
            ids = [f["id"] for f in findings]
            self.assertTrue(
                any(expected_id in id_str for id_str in ids),
                f"Kaidah {expected_id} gagal mendeteksi: '{sentence}', terdeteksi: {ids}"
            )

    def test_new_stylistic_and_syntactic_rules(self):
        """Memastikan aturan baru (Mustakim, Wisnu Sasangka, J.S. Badudu) tertangkap presisi."""
        samples = [
            ("Masing-masing peserta wajib mengisi kuesioner evaluasi.", "MST-001"),
            ("Dengan metode ini dapat meningkatkan akurasi klasifikasi.", "SAS-001"),
            ("Dalam hubungan ini, peneliti melakukan evaluasi menyeluruh.", "BDD-008"),
            ("Berkenaan dengan hal tersebut, sistem dihentikan sementara.", "TMP-003"),
            ("Model mengalami degradasi, di mana hal ini disebabkan oleh data kotor.", "BDD-009"),
        ]
        for sentence, expected_id in samples:
            findings = audit_text(sentence, self.kalke, self.glos)
            ids = [f["id"] for f in findings]
            self.assertTrue(
                any(expected_id in id_str for id_str in ids),
                f"Kaidah {expected_id} gagal mendeteksi: '{sentence}', terdeteksi: {ids}"
            )

    def test_reduplication_scientific_terms_zero_fp(self):
        """Istilah teknis/sains berakhiran 2 tidak boleh memicu EJ-004 atau EYD-025."""
        scientific_sentences = [
            "Emisi gas CO2 dan NO2 meningkat seiring pertumbuhan industri otomotif.",
            "Area konservasi ini memiliki luas sekitar 45 km2 dan mencakup 120 m2 fasilitas observasi.",
            "Protokol otentikasi menggunakan OAuth2 di atas koneksi HTTP2.",
            "Model evaluasi menghasilkan koefisien determinasi R2 sebesar 0,89 pada arsitektur Llama2 dan GPT2.",
        ]
        for s in scientific_sentences:
            fs = audit_text(s, self.kalke, self.glos)
            redup_fps = [f["id"] for f in fs if f["id"] in ("EJ-004", "EYD-025")]
            self.assertEqual(
                len(redup_fps), 0,
                f"False positive pada istilah sains: {s} -> {redup_fps}"
            )

    def test_reduplication_informal_triggers_correctly(self):
        """Reduplikasi informal angka 2 wajib memicu temuan."""
        informal_samples = [
            "Buku2 itu telah dikembalikan ke perpustakaan.",
            "Anak2 bermain di lapangan terbuka.",
        ]
        for s in informal_samples:
            fs = audit_text(s, self.kalke, self.glos)
            redup_hits = [f["id"] for f in fs if f["id"] in ("EJ-004", "EYD-025")]
            self.assertGreater(
                len(redup_hits), 0,
                f"Gagal mendeteksi reduplikasi angka 2: {s}"
            )

    def test_metadata_docs_count_integrity(self):
        """Angka entri kalke riil di JSON wajib konsisten dan tidak fiktif."""
        total_kalke = sum(len(cat["entri"]) for cat in self.kalke["kategori"].values())
        total_glos = sum(len(b.get("istilah", [])) for b in self.glos.get("bidang", {}).values())
        self.assertGreater(total_kalke, 300, "Total kalke riil minimal 300")
        self.assertGreater(total_glos, 80, "Total glosarium riil minimal 80")

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
