# Telaah Preskriptif: Sindrom Akronim Redundan (RAS) dalam Pemakaian Bahasa Indonesia

Dokumen ini memuat telaah kebahasaan preskriptif dan formulasi aturan audit editorial yang diekstraksi dari penelitian ilmiah mengenai fenomena *Redundant Acronym Syndrome* (sindrom RAS) dalam bahasa Indonesia. Kajian ini ditujukan untuk melengkapi basis pengetahuan Humanizer ID dalam menyaring pleonasme akronim pada teks akademik, publikasi ilmiah, dan naskah administratif formal.

---

## 1. Identitas Dokumen Sumber

- **Judul Dokumen:** *Redundant Acronym Syndrome (RAS) Syndrome dalam Pemakaian Bahasa Indonesia*
- **Penulis:** Haslinda & Aziz Thaba
- **Afiliasi:** Program Studi Pendidikan Bahasa dan Sastra Indonesia, Universitas Muhammadiyah Makassar
- **Publikasi:** Jurnal / Prosiding Ilmiah Kebahasaan (Repositori Kemdikbud/Dikti)
- **Tebal:** 9 halaman (hlm. 1–9)
- **Fokus Kajian:** Identifikasi fenomena pleonasme akronim redundan, klasifikasi kesalahan berbahasa pada tataran sintaksis dan semantik (Corder, 1974: *Error / breaches of code*), serta pertentangan antara preskriptivisme dan deskriptivisme dalam ruang publik.

---

## 2. Analisis Substansi Kebahasaan Preskriptif

Penelitian Haslinda dan Thaba (hlm. 2–6) menegaskan bahwa sindrom RAS bukan sekadar variasi tuturan kolokial, melainkan bentuk **kesalahan berbahasa (*error*) pada tataran sintaksis dan semantik**. Kesalahan ini terjadi ketika kata penjelas yang mendahului atau mengikuti sebuah akronim/singkatan mengulang kembali unsur kata yang sudah terkandung di dalam kepanjangan akronim tersebut.

### Temuan Kritis Dokumen:
1. **Pelanggaran Preskriptivisme Bahasa Standar (hlm. 2–3):** Bahasa formal sangat bergantung pada ketepatan pola dan struktur hemat. Pengulangan unsur akronim melanggar asas ekonomi bahasa (*law of linguistic parsimony*) dan menciptakan tautologi semantik.
2. **Kategori Gejala Sindrom RAS di Ruang Publik (hlm. 4–5):**
   - **Kategori Numerik & Identitas:** *nomor NIK*, *nomor PIN* (N = Nomor / Number).
   - **Kategori Dokumen & Kartu:** *kartu KIP*, *kartu KTP*, *kartu ATM* (K = Kartu).
   - **Kategori Biologis/Medis:** *virus HIV* (V = Virus).
   - **Kategori Organisasi & Kepartaian:** *partai PPP*, *partai PDIP*, *partai PAN* (P = Partai).
   - **Kategori Toponimi Entitas / Klub Olahraga:** *PSM Makassar* (M = Makassar), *Persija Jakarta* (Ja = Jakarta), *Arema Malang* (Ma = Malang).
3. **Ekstensi ke Ranah Teknis & Akademik (hlm. 3, 5–6):**
   - *Sistem SI* (SI = Système International; pengulangan kata "sistem").
   - *Nomor ISBN / ISSN / NPWP* (N = Nomor / Number).
   - *Dosen DPA* (D = Dosen Pembimbing/Penasihat Akademik).
   - *Kode QR code / Format PDF format / Layar LCD display*.

---

## 3. Draf Kaidah Kebahasaan Baru (Integrasi Basis Aturan Audit)

Berikut adalah 5 draf kaidah baru hasil ekstraksi yang telah diverifikasi tidak menduplikasi entri yang sudah ada di `data/kalke-indonesia.json` (entri lama: `RAS-001` s.d. `RAS-004`):

---

### Kaidah 1: RAS-005 (Redundansi Toponimi pada Akronim Entitas/Organisasi)
- **ID:** `RAS-005`
- **Pola:** Pemakaian nama kota/daerah yang mendahului atau mengikuti akronim nama diri yang telah memuat toponimi tersebut (`PSM Makassar`, `Persija Jakarta`, `Arema Malang`, `klub PSM Makassar`).
- **Saran Pengganti:** Sebutkan akronimnya saja (*PSM*, *Persija*, *Arema*) atau uraikan kepanjangannya secara utuh (*Persatuan Sepak Bola Makassar*, *Persatuan Sepak Bola Indonesia Jakarta*, *Arek Malang*).
- **Penjelasan:** Haslinda & Aziz Thaba (hlm. 4–5, Tabel 1) menjelaskan bahwa penambahan nama wilayah di belakang akronim yang sudah berunsur toponimi merupakan bentuk redundansi semantik (*PSM Makassar* berarti *Persatuan Sepak Bola Makassar Makassar*). Dalam penulisan jurnalistik dan laporan formal, pengulangan toponimi nama diri harus dihindari.
- **Contoh Salah:** "Pertandingan babak final mempertemukan kesebelasan Persija Jakarta melawan PSM Makassar di Stadion Gelora Bung Karno."
- **Contoh Benar:** "Pertandingan babak final mempertemukan kesebelasan Persija melawan PSM di Stadion Gelora Bung Karno."

---

### Kaidah 2: RAS-006 (Redundansi Leksikal "Sistem" pada Akronim Satuan Internasional / SI)
- **ID:** `RAS-006`
- **Pola:** Pemakaian kata `sistem` atau frasa `sistem satuan` yang mendahului akronim `SI` (`sistem SI`, `sistem satuan SI`).
- **Saran Pengganti:** Gunakan `SI` saja, atau tuliskan bentuk panjangnya: `Sistem Internasional` / `Sistem Satuan Internasional`.
- **Penjelasan:** Huruf *S* dalam akronim *SI* berasal dari bahasa Prancis *Système International (d'unités)* yang berarti *Sistem Internasional*. Penulisan *sistem SI* menghasilkan pembacaan rancu *Sistem Sistem Internasional* yang melanggar asas kehematan istilah ilmiah baku (Haslinda & Thaba, hlm. 3, 5; selaras dengan Pedoman Pembentukan Istilah Pusat Bahasa).
- **Contoh Salah:** "Pengukuran massa jenis fluida dalam eksperimen laboratorium ini wajib mengikuti standarisasi sistem SI."
- **Contoh Benar:** "Pengukuran massa jenis fluida dalam eksperimen laboratorium ini wajib mengikuti standarisasi SI." (atau: "wajib mengikuti Sistem Satuan Internasional.")

---

### Kaidah 3: RAS-007 (Redundansi Kata "Nomor" pada Akronim Standar Terbitan dan Perpajakan)
- **ID:** `RAS-007`
- **Pola:** Pemakaian kata `nomor` yang mendahului akronim yang telah berunsur *N* (Nomor/Number) pada registrasi buku, serial, atau identitas pajak (`nomor ISBN`, `nomor ISSN`, `nomor NPWP`).
- **Saran Pengganti:** Cukup gunakan akronimnya secara mandiri: `ISBN`, `ISSN`, atau `NPWP`; atau ganti menjadi frasa kepanjangan baku (*nomor pokok wajib pajak*).
- **Penjelasan:** Haslinda & Thaba (hlm. 4–5) menggarisbawahi bahwa kata *nomor* di depan akronim yang berakhir atau diawali huruf bernilai *Nomor/Number* menghasilkan dwitautologi (*nomor International Standard Book Number* / *nomor Nomor Pokok Wajib Pajak*).
- **Contoh Salah:** "Buku monograf hasil konversi penelitian tersebut telah terdaftar dengan nomor ISBN resmi dari Perpustakaan Nasional."
- **Contoh Benar:** "Buku monograf hasil konversi penelitian tersebut telah terdaftar dengan ISBN resmi dari Perpustakaan Nasional."

---

### Kaidah 4: RAS-008 (Redundansi Nomina Jabatan/Civitas pada Akronim DPA / Dosen)
- **ID:** `RAS-008`
- **Pola:** Pemakaian kata `dosen` atau bentuk jamak `dosen-dosen` yang mendahului akronim pembimbing/penasihat akademik (`dosen DPA`, `dosen-dosen DPA`, `dosen pembimbing DPA`).
- **Saran Pengganti:** Gunakan `DPA` saja, atau uraikan menjadi `dosen pembimbing akademik` / `penasihat akademik`.
- **Penjelasan:** Huruf *D* dalam *DPA* sudah bermakna *Dosen* (Dosen Pembimbing Akademik / Dosen Penasihat Akademik). Konstruksi *dosen DPA* menghasilkan pengulangan leksikal mubazir *Dosen Dosen Pembimbing Akademik* yang kerap luput dari penyuntingan administrasi akademik perguruan tinggi (Haslinda & Thaba, hlm. 3, 5–6).
- **Contoh Salah:** "Mahasiswa wajib berkonsultasi dengan dosen DPA masing-masing sebelum mengisi kartu rencana studi."
- **Contoh Benar:** "Mahasiswa wajib berkonsultasi dengan DPA masing-masing sebelum mengisi kartu rencana studi." (atau: "berkonsultasi dengan dosen pembimbing akademik...")

---

### Kaidah 5: RAS-009 (Redundansi Spesifikator Media dan Perangkat Teknis)
- **ID:** `RAS-009`
- **Pola:** Pemakaian nomina pelengkap bahasa Inggris/Indonesia yang mengulang kata akhir akronim teknologi informasi (`kode QR code`, `format berkas PDF format`, `layar monitor LCD display`, `mesin ATM machine`).
- **Saran Pengganti:** Pangkas kata asing penjelas yang berulang: gunakan `kode QR`, `format PDF`, `layar LCD`, atau `mesin ATM`.
- **Penjelasan:** Dalam ranah teknologi digital, pengguna sering kali menyerap frasa asing secara serampangan (*code* pada *QR Code*, *format* pada *PDF [Portable Document Format]*, *display* pada *LCD [Liquid Crystal Display]*, *machine* pada *ATM [Automated Teller Machine]*), sehingga memicu sindrom RAS lintas-bahasa (Haslinda & Thaba, hlm. 3, 5).
- **Contoh Salah:** "Peserta seminar diminta memindai kode QR code yang tertera pada layar monitor LCD display di pintu masuk."
- **Contoh Benar:** "Peserta seminar diminta memindai kode QR yang tertera pada monitor LCD di pintu masuk."

---

## 4. Draf Entri JSON Siap Pakai (`data/kalke-indonesia.json`)

```json
[
  {
    "id": "RAS-005",
    "pola": "PSM Makassar / Persija Jakarta / Arema Malang / klub PSM Makassar",
    "saran_pengganti": [
      "PSM",
      "Persija",
      "Arema",
      "Persatuan Sepak Bola Makassar"
    ],
    "penjelasan": "Sindrom akronim redundan toponimi: nama wilayah sudah terkandung dalam akronim (M = Makassar, Ja = Jakarta, Ma = Malang) sehingga penambahan nama kota menghasilkan pengulangan semantis ganda (Haslinda & Thaba, 2018, hlm. 4-5).",
    "contoh_salah": "Pertandingan mempertemukan Persija Jakarta melawan PSM Makassar.",
    "contoh_benar": "Pertandingan mempertemukan Persija melawan PSM."
  },
  {
    "id": "RAS-006",
    "pola": "sistem SI / sistem satuan SI",
    "saran_pengganti": [
      "SI",
      "Sistem Internasional",
      "Sistem Satuan Internasional"
    ],
    "penjelasan": "Huruf S dalam akronim SI adalah 'Système' (Sistem Internasional). Frasa 'sistem SI' merupakan pleonasme lewah 'sistem sistem internasional' (Haslinda & Thaba, 2018, hlm. 3, 5).",
    "contoh_salah": "Pengukuran massa benda uji wajib berpedoman pada sistem SI.",
    "contoh_benar": "Pengukuran massa benda uji wajib berpedoman pada SI."
  },
  {
    "id": "RAS-007",
    "pola": "nomor ISBN / nomor ISSN / nomor NPWP",
    "saran_pengganti": [
      "ISBN",
      "ISSN",
      "NPWP",
      "nomor pokok wajib pajak"
    ],
    "penjelasan": "Huruf N pada ISBN/ISSN adalah 'Number' dan pada NPWP adalah 'Nomor'. Penyebutan 'nomor ISBN/NPWP' menimbulkan tautologi numerik (Haslinda & Thaba, 2018, hlm. 4-5).",
    "contoh_salah": "Naskah monograf telah memiliki nomor ISBN resmi.",
    "contoh_benar": "Naskah monograf telah memiliki ISBN resmi."
  },
  {
    "id": "RAS-008",
    "pola": "dosen DPA / dosen-dosen DPA / dosen pembimbing DPA",
    "saran_pengganti": [
      "DPA",
      "dosen pembimbing akademik",
      "penasihat akademik"
    ],
    "penjelasan": "Huruf D dalam singkatan DPA sudah berarti 'Dosen' (Dosen Pembimbing Akademik). Penggunaan 'dosen DPA' merupakan pleonasme jabatan fungsional (Haslinda & Thaba, 2018, hlm. 3-6).",
    "contoh_salah": "Mahasiswa berkonsultasi dengan dosen DPA sebelum registrasi mata kuliah.",
    "contoh_benar": "Mahasiswa berkonsultasi dengan DPA sebelum registrasi mata kuliah."
  },
  {
    "id": "RAS-009",
    "pola": "kode QR code / format PDF format / monitor LCD display / mesin ATM machine",
    "saran_pengganti": [
      "kode QR",
      "format PDF",
      "layar LCD",
      "ATM"
    ],
    "penjelasan": "Sindrom akronim redundan dwibahasa: kata asing pelengkap (code, format, display, machine) mengulang kembali kata pembentuk akhir akronim bahasa Inggris (Haslinda & Thaba, 2018, hlm. 3, 5).",
    "contoh_salah": "Silakan memindai kode QR code yang tertera pada selebaran.",
    "contoh_benar": "Silakan memindai kode QR yang tertera pada selebaran."
  }
]
```
