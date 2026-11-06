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

---

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

## Kamus Terbuka Kalke & Verba Ringan (`data/`)

Repositori ini menyediakan dataset terbuka berupa leksikon dan pola sintaksis terstruktur di [**`data/kalke-indonesia.json`**](data/kalke-indonesia.json) yang dapat dimanfaatkan untuk riset pemrosesan bahasa alami (NLP), pembuatan pustaka linter, atau fine-tuning model bahasa Indonesia.

Setiap entri memuat:
- Pola frasa pemicu dan asal frasa bahasa Inggris (*calque translationese*).
- Alternatif saran pengganti baku dan luwes.
- Rujukan kaidah linguistik serta contoh perbandingan sebelum dan sesudah.

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
