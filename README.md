# Humanizer ID

Panduan penyuntingan bahasa Indonesia akademik dan profesional untuk agen kecerdasan buatan dan platform LLM. Menghilangkan rasa kaku, membersihkan kalke terjemahan mesin, membenahi fragmentasi kalimat, dan menjaga integritas fakta ilmiah tanpa manipulasi detektor.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/apissaj/humanizer-id)](https://github.com/apissaj/humanizer-id/releases)

---

## Mengapa Naskah AI Bahasa Indonesia Terasa Kaku?

Kekakuan tulisan AI bahasa Indonesia jarang disebabkan oleh kesalahan tata bahasa. Penyebab utamanya adalah:
1. **Nominalisasi menumpuk & verba ringan:** AI gemar menulis *“melakukan pengujian terhadap”* alih-alih *“menguji”*.
2. **Kalke (*Calque*) terjemahan mesin:** Model berpikir dalam bahasa Inggris lalu menerjemahkan klausa demi klausa (*“respecting boundaries”* diterjemahkan mentah menjadi *“menghormati batas”*).
3. **Penyangkalan antisipatif:** Pola khas AI seperti *“Meskipun X, bukan berarti Y...”* yang menyangkal hal yang tidak ditanyakan pembaca.
4. **Fragmentasi kalimat monoton:** Kalimat-kalimat pendek satu klausa yang berderet patah-patah (*staccato*).
5. **Monotoni pembuka antar-paragraf:** Konjungsi transisi mekanis berulang di awal tiap paragraf (*Selain itu,... Lebih lanjut,... Oleh karena itu,...*).
6. **Transisi kopong (ilusi keterhubungan):** Kata sambung kausalitas palsu (*"Dengan demikian, hal ini membuktikan..."*) tanpa premis data yang cukup.

---

## Sumber Data Resmi (Buku Teks & Pedoman Terdokumentasi)

Seluruh kaidah di dalam Humanizer ID **bukan karangan bebas** — setiap aturan ditelusuri dari dokumen resmi terbitan pemerintah dan pedoman akademik perguruan tinggi, lengkap dengan nomor halaman:

### Buku Teks Resmi Kemendikbudristek (Sumber Primer)
| Buku | Kontribusi Kaidah | Lokasi Ekstrak |
|---|---|---|
| *Cerdas Cergas Berbahasa dan Bersastra Indonesia* Kelas XI (Edisi Revisi, 2024, ISBN 978-634-00-0958-3) | Ragam bahasa karya ilmiah (denotatif, objektif, impersonal), sistematika karya ilmiah, contoh perbaikan kalimat efektif resmi (hlm. 210–215) | [references/ekstrak-buku-teks-kemdikbud.md](references/ekstrak-buku-teks-kemdikbud.md) |
| *Bahasa Indonesia untuk SMA/MA/SMK/MAK Kelas XII* (Edisi Revisi, 2024) | Lima ciri kalimat efektif (Sasangka, 2019), kaidah surat resmi (*agar menjadi*, *guna meningkatkan*), 9 kata tidak baku (hlm. 29–34) | [references/ekstrak-buku-teks-kemdikbud.md](references/ekstrak-buku-teks-kemdikbud.md) |

### Buku Bahasa & Linguistik Populer (Ivan Lanin)
- **Xenoglosofilia: Kenapa Harus Nginggris?** (Ivan Lanin, Kompas Gramedia, 2018) — telaah kritis kalke bahasa asing, pemadanan istilah berbasis kelaziman penutur.
- **Recehan Bahasa: Baku Tak Mesti Kaku** (Ivan Lanin, Mizan Qanita, 2020) — lima tingkatan ragam bahasa (beku, resmi, konsultatif, santai, akrab) dan prinsip keluwesan teks baku.

### Kajian Frekuensi Kosakata AI (Sains Internasional)
- **Kobak et al., *Science Advances* (2025, DOI: 10.1126/sciadv.adt3813)** — analisis korpus 15,1 juta abstrak PubMed membuktikan lonjakan kalke verba AI paling masif: *delve* (rasio kelebihan 28×), *underscore* (13,8×), *showcase* (10,7×). Di Indonesia, kata-kata ini mengalami alih-bahasa mentah menjadi penanda klise (*menyelami*, *menggarisbawahi berlebihan*, *hiruk pikuk*).

### Pedoman Ejaan & Tata Bahasa Resmi Pemerintah
- **EYD Edisi V** (Keputusan Kepala Badan Bahasa No. 0424/I/BS.00.01/2022) — peluluhan KTSP, bentuk terikat, partikel *pun* → [references/pedoman-kebahasaan-resmi.md](references/pedoman-kebahasaan-resmi.md)
- **TBBBI (Tata Bahasa Baku Bahasa Indonesia) Edisi IV** — kesejajaran predikat, kalimat efektif.
- **PUEBI Daring (Permendikbud 50/2015)** — gabungan kata konfiks (*menggarisbawahi*), bentuk ulang (*buku-buku*, bukan *buku2*), akronim nama diri → [references/](references/)
- **PASTI (Portal Pemadanan Istilah) Badan Bahasa Kemendikdasmen RI** (pasti.kemendikdasmen.go.id) — 172.931 istilah dari 59 ranah ilmu. Digunakan untuk membakukan padanan istilah teknologi (*machine learning* → **pemelajaran mesin**, *deep learning* → **pemelajaran mendalam**, *cloud computing* → **komputasi awan**, *data science* → **sains data**).

### Pedoman Penulisan Skripsi Perguruan Tinggi
- **Pedoman Tugas Akhir DIKE FMIPA UGM** — rujukan persamaan matematis bernomor: *“Berdasarkan Persamaan (3.1)...”*, pemisahan Simpulan vs Saran.
- **Pedoman Skripsi Universitas Indonesia (UI)** — kaidah sitasi dan format persamaan.

### Data Lexikon & Korpus (Komunitas Terbuka)
- Dataset distilasi EYD V (38 kategori aturan resmi), leksikon 238 kata baku↔nonbaku, glosarium istilah teknologi (115 entri) & hukum (25 entri).
- Statistik leksikon resmi KBBI: 112.538 entri (50.668 dasar + 26.835 turunan + 31.492 gabungan).

> Setiap entri di [`data/kalke-indonesia.json`](data/kalke-indonesia.json) yang bersumber dari buku mencantumkan rujukan halaman (contoh: *Buku Bahasa Indonesia Kelas XI Revisi 2024, hlm. 213*), sehingga bisa diverifikasi langsung ke dokumen aslinya.

## Perbandingan Sebelum & Sesudah

Berikut adalah contoh penyuntingan pada abstrak penelitian teknik (studi kasus lengkap tersedia di folder [**examples/**](examples/)):

| Draf Mentah AI / ChatGPT | Hasil Suntingan Humanizer ID |
|---|---|
| *Di era digital saat ini, optimasi basis data merupakan hal yang sangat krusial. Dalam penelitian ini melakukan analisis terhadap performa indeks B-Tree yang mengalami peningkatan kecepatan sebesar 35%. Meskipun cepat, bukan berarti indeks ini tanpa cela. Tulisan ini membahas bagaimana implementasi partisi tabel memberikan pengaruh terhadap throughput transaksi yang mana sangat penting untuk sistem.* | *Optimasi basis data menjadi penentu efisiensi sistem berskala besar. Penelitian ini menganalisis performa indeks B-Tree yang mencatatkan peningkatan kecepatan hingga 35%. Kendati demikian, karakteristik beban kerja tetap memunculkan tantangan komputasi tersendiri. Pada penelitian ini dibahas implementasi partisi tabel untuk meningkatkan throughput transaksi secara berkelanjutan.* |

---

## Lembar Sontekan (*Cheat Sheet*) Diksi & Kalke

Padanan cepat untuk membersihkan tulisan AI dan birokratis:

| Pola AI / Kaku | Bentuk Luwes & Lugas | Jenis Masalah |
|---|---|---|
| melakukan pengukuran terhadap | mengukur | Verba ringan |
| melakukan analisis terhadap | menganalisis | Verba ringan |
| memberikan pengaruh terhadap | memengaruhi | Verba ringan |
| mengalami peningkatan sebesar | meningkat / naik sebesar | Nominalisasi |
| menghormati batas sistem | selaras dengan batas sistem | Kalke (*respecting boundaries*) |
| menghapus limbah | meniadakan / meminimalkan limbah | Kalke (*eliminate waste*) |
| tidak datang tanpa harga | bukan tanpa konsekuensi / kendala | Kalke (*not without a price*) |
| Makalah ini membahas... | Pada makalah ini dibahas... | Personifikasi dokumen |
| ...yang mana sangat penting | ...yang penting / sehingga penting | Pronomina relatif salah |
| X, bukan berarti Y | Kendati X, tantangan Y tetap... | Penyangkalan antisipatif |

---

## Cara Penggunaan

### 1. Salin Cepat untuk ChatGPT, Claude Web, & Gemini Gems
Jika Anda menggunakan antarmuka web (tanpa coding agent):
- Buka panduan siap pakai di [**PROMPT.md**](PROMPT.md).
- Salin teks instruksi ke kolom **Custom Instructions** (ChatGPT) atau **Project System Prompt** (Claude Projects).

### 2. Pemasangan pada AI Coding Agents

#### Hermes Agent
Simpan berkas `SKILL.md` ke folder skill Hermes Anda:
```bash
# Direktori skill aktif
mkdir -p ~/.hermes/skills/creative/humanizer-id
cp SKILL.md ~/.hermes/skills/creative/humanizer-id/
```

#### Claude Code
```bash
git clone https://github.com/apissaj/humanizer-id.git ~/.claude/skills/humanizer-id
```

#### Google Antigravity
```bash
# Global
git clone https://github.com/apissaj/humanizer-id.git ~/.gemini/config/skills/humanizer-id

# Per-Project Workspace
git clone https://github.com/apissaj/humanizer-id.git .agents/skills/humanizer-id
```

---

---

## Kamus Terbuka & Glosarium Lintas Bidang (`data/`)

Repositori ini menyediakan dataset terbuka berupa leksikon dan pola sintaksis terstruktur:
- [**`data/kalke-indonesia.json`**](data/kalke-indonesia.json): 40 entri leksikon kalke terjemahan mesin, verba ringan, pola antisipatif AI, dan kaidah morfologi peluluhan KTSP resmi EYD V.
- [**`data/glosarium-lintas-bidang.json`**](data/glosarium-lintas-bidang.json): 45+ padanan istilah baku dari berbagai kalangan profesional (Teknologi & Software, Hukum & Regulasi, Jurnalistik & Media Siber, serta Bisnis & Manajemen).

Panduan register dan gaya penulisan mendalam untuk tiap kalangan tersedia di dokumen [**`references/panduan-gaya-lintas-kalangan.md`**](references/panduan-gaya-lintas-kalangan.md).

---

## Alat Pemindai Mandiri (*CLI Auditor*)

Tersedia skrip audit cepat tanpa dependensi eksternal (100% pustaka standar Python) untuk memindai dokumen Markdown atau teks secara lokal:

```bash
# Uji coba dengan teks sampel demo
python scripts/audit.py --demo

# Pindai naskah skripsi atau artikel Anda
python scripts/audit.py path/ke/naskah.md
```
Skrip akan mencetak nomor baris, pola kalke atau verba ringan yang terdeteksi, saran perbaikan, dan catatan kaidah editorialnya secara seketika.

## Prinsip Integritas Ilmiah

- **Nol Fabrikasi Data:** Tidak menambahkan angka, parameter uji, atau sitasi baru yang tidak ada pada draf asli penulis demi membuat kalimat terkesan mendalam.
- **Safeguard Pasif Ilmiah:** Kalimat pasif pada bab Metodologi dan Hasil adalah konvensi resmi penulisan sains Indonesia dan tidak diubah secara agresif.
- **Zona Terlarang Disunting:** Dilarang mengubah instrumen penelitian tervalidasi (kuesioner/skala Likert), dokumen kontrak, dan paten hukum.
- **Bukan Alat Bypass Deteksi:** Panduan ini berfokus pada keterbacaan manusia. Kelancaran tata bahasa bukan jaminan skor pada alat deteksi AI statistik.

---

## Lisensi

Perangkat lunak dan panduan ini dilisensikan di bawah [Lisensi MIT](LICENSE) © 2026 Hafizh Muzani.
