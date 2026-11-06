# Panduan Gaya Penulisan Bahasa Indonesia Lintas Kalangan

Panduan ini memetakan karakteristik register bahasa, konvensi baku, dan jebakan gaya (*anti-patterns*) penulisan bahasa Indonesia di lima kalangan profesional: Akademik, Teknologi, Hukum, Jurnalistik, dan Bisnis.

---

## 1. Kalangan Akademik & Peneliti (Jurnal, Skripsi, Tesis)

### Karakteristik Utama:
- Mengedepankan objektivitas, presisi leksikal, dan keterukuran klaim.
- Kalimat pasif metodologi (*"Data dihimpun melalui pengamatan..."*) adalah konvensi baku untuk menjaga netralitas peneliti.

### Jebakan Khas AI & Solusinya:
- **Kutipan Nama Peneliti Formulaik:** Pola monoton *"Menurut Pratama (2021)... Senada dengan itu Wijaya (2022) berpendapat..."*.
  - *Solusi:* Rajut sitasi berbasis temuan/gagasan: *"Akurasi model Transformer terbukti stabil pada dataset informal (Pratama, 2021; Wijaya, 2022)"*.
- **Preposisi Pembunuh Subjek:** *"Dalam penelitian ini membuktikan..."* (klausa kehilangan subjek gramatikal).
  - *Solusi:* Hilangkan preposisi atau gunakan pasif baku: *"Penelitian ini membuktikan..."* atau *"Dalam penelitian ini dibuktikan..."*.
- **Pujian Tanpa Dasar Statistik:** Menyebut hasil *"luar biasa"*, *"sangat krusial"*, atau *"revolusioner"*.
  - *Solusi:* Sebutkan capaian kuantitatif langsung: *"meningkatkan akurasi sebesar 12,4%"*.

---

## 2. Kalangan Teknologi & Rekayasa Perangkat Lunak (Dokumentasi Teknis & Arsitektur)

### Karakteristik Utama:
- Kejelasan alur prosedur (*step-by-step*), konsistensi penamaan variabel/komponen, dan kepatuhan istilah serapan bidang komputer.

### Jebakan Khas AI & Solusinya:
- **Kalke Terjemahan Mesin Janggal:**
  - *"menghormati batas memori"* (*respecting boundaries*) → **"selaras dengan batas memori / berada dalam rentang memori"**.
  - *"menghapus limbah komputasi"* (*eliminate waste*) → **"meniadakan overhead komputasi"**.
- **Inkonsistensi Padanan Teknis:**
  - Gunakan leksikon baku terstruktur (lihat `data/glosarium-lintas-bidang.json`): *basis data* (database), *tembolok* (cache), *antarmuka pemrograman aplikasi* (API), *penyetelan halus* (fine-tuning).
  - Jangan memaksakan istilah janggal pada kata yang sudah lazim ditulis dalam format kode/monospace (misal: `npm run dev`, *docker container*).

---

## 3. Kalangan Hukum, Kontrak & Regulasi (Perjanjian, SOP, Kebijakan)

### Karakteristik Utama:
- Ketepatan makna tanpa celah multitafsir; kalimat panjang bertingkat dengan klausa syarat kondisional dipertahankan demi keabsahan yuridis.

### Pembedaan Derajat Kewajiban:
- **Wajib:** Mengikat secara imperatif hukum tanpa opsi alternatif (*"Pihak Pertama wajib membayar..."*).
- **Harus:** Mengindikasikan keharusan logis atau prosedural (*"Berkas permohonan harus diverifikasi terlebih dahulu"*).
- **Dapat:** Memberikan diskresi atau wewenang opsional (*"Pihak Kedua dapat menangguhkan pengiriman..."*).

### Padanan Istilah Hukum Baku:
- *force majeure* → **keadaan kahar**
- *legal standing* → **kedudukan hukum**
- *dissenting opinion* → **pendapat berbeda**
- *pro bono* → **bantuan hukum cuma-cuma**
- *due diligence* → **uji tuntas**

---

## 4. Kalangan Jurnalistik & Media Siber (Berita, Liputan, Siaran Pers)

### Karakteristik Utama:
- Menerapkan prinsip **ekonomi kata** (singkat, padat, lugas) dengan struktur piramida terbalik.

### Jebakan Verbositas & Penghilangan Ungkapan Jenuh:
| Ungkapan Jenuh / AI | Bentuk Lugas Jurnalistik | Alasan |
|---|---|---|
| dapat disampaikan bahwa | [langsung ke inti fakta] | Frasa basa-basi penunda kalimat |
| sementara itu di tempat berbeda | secara terpisah / di sisi lain | Klise formulaik penanda lokasi |
| mengembuskan napas terakhir | wafat / meninggal dunia | Eufemisme sastrawi berlebih |
| melakukan peninjauan secara langsung ke | meninjau lokasi | Pleonasme berlebihan |
| ditemukan dalam kondisi tidak bernyawa | ditemukan meninggal / tewas | Verbositas birokratis |

---

## 5. Kalangan Bisnis & Korporat (Proposal, Laporan Manajemen, Memo Eksekutif)

### Karakteristik Utama:
- Efisiensi komunikasi waktu (*executive brief*), orientasi pada hasil dan aksi konkret (*actionable items*).

### Pembersihan Jargon Korporat (*Corporate Buzzwords*):
- Ganti *"menciptakan sinergi antar bagian"* dengan **"mengintegrasikan proses kerja antarunit"**.
- Ganti *"mengungkit kapabilitas internal"* (*leverage*) dengan **"mendayagunakan kapasitas internal"**.
- Ganti *"melakukan transformasi holistik"* dengan **"merestrukturisasi sistem operasional secara menyeluruh"**.
- Ganti *"pembagian peran stakeholder"* dengan **"pembagian tugas pemangku kepentingan"**.
