# Ekstrak Kaidah: Kesalahan Sintaksis Pleonasme Verba Bertujuan & Pemenggalan Klausa Konsekutif Skripsi Mahasiswa (Jurnal ILEAL 2018 & Jurnal Kande 2021)

- **Sumber Karya 1:** *Kesalahan Sintaksis Pada Skripsi Mahasiswa IAIN Syekh Nurjati Cirebon* (*Indonesian Language Education and Literature / ILEAL*, Vol. 4, No. 1, Desember 2018, hlm. 1–10, SINTA 2, DOI: 10.24235/ileal.v4i1.1880).
  - Penulis: Tati Sri Uswati dan Tato Nuryanto.
  - Berkas PDF: `books/jurnal_ileal_kesalahan_sintaksis_skripsi.pdf`.
- **Sumber Karya 2:** *Analisis Keefektifan Kalimat dalam Skripsi Mahasiswa Prodi Pendidikan Universitas Malikussaleh* (*Jurnal Kande: Jurnal Ilmiah Pendidikan Bahasa dan Sastra Indonesia*, Vol. 2, No. 1, April 2021, hlm. 151–160, SINTA Terakreditasi, DOI: 10.29103/jk.v2i1.4687).
  - Penulis: Nurmaya Sari, Syahriandi, dan Rani Ardesi Pratiwi.
  - Berkas PDF: `books/jurnal_kande_keefektifan_kalimat_skripsi.pdf`.

---

## 1. Kaidah Preskriptif Temuan Riset

### 1. Pleonasme Frasa Verba Bertujuan 'bertujuan untuk' (Jurnal ILEAL 2018, hlm. 6)
- **Kutipan Jurnal (hlm. 6):**
  > "Penggunaan Unsur Berlebihan/Lewah. Kasus 1d. PGMI.1.P5.1: *Model pembelajaran inkuiri ini bertujuan untuk mengorganisasikan pengetahuan yang dimiliki siswa sebagai fondasi yang kuat berdasarkan konsep metode ilmiah.* Preposisi untuk dalam frasa *bertujuan untuk* kurang tepat karena memiliki makna yang sama dengan kata *bertujuan*, sebaiknya pilih salah satu, *bertujuan* atau *untuk*."
- **Analisis Tata Bahasa & AI/LLM:**
  - Verba intransitif berafiks *ber-* (*bertujuan*) secara semantis mengandung makna gramatikal 'mempunyai tujuan'. Menambahkan preposisi direktif penanda sasaran/tujuan *untuk* di depannya adalah pleonasme lewah (redundansi ganda penanda tujuan).
  - Pada teks luaran LLM dan terjemahan mesin, konstruksi ini muncul sangat masif sebagai hasil alih bahasa harafiah dari pola bahasa Inggris *"aims to [verb]"* atau *"is intended to [verb]"* (misalnya: *Penelitian ini bertujuan untuk menganalisis...*).
  - Ragam ilmiah preskriptif baku menghendaki verba transitif langsung mengikuti *bertujuan* (*bertujuan menganalisis*, *bertujuan menguji*), atau membuang kata *bertujuan* dan memakai verba pasif terarah jika mempertahankan *untuk* (*dirancang untuk*, *dilakukan untuk*).

### 2. Pemenggalan Klausa Subordinatif Konsekutif Mandiri 'Sehingga ...' di Awal Kalimat (Jurnal Kande 2021, hlm. 155)
- **Kutipan Jurnal (hlm. 155):**
  > "Ketepatan Bentukan Bagian Kalimat. Dalam pemakaian bahasa, sering ditemukan bagian kalimat majemuk yang ditulis terpisah dari bagian kalimatnya, hal tersebut biasanya terjadi karena kekeliruan ketika menggunakan konjungsi. Contoh: (1) *Kami datang terlambat. Sehingga kami tidak dapat mengikuti perkuliahan.* Perbaikan kalimat ini dapat dilakukan dengan dua cara. Pertama, mengubah kalimat menjadi kalimat majemuk dengan menggunakan penghubung (konjungtor) sehingga, dan cara yang kedua adalah mengganti ungkapan penghubung intrakalimat (sehingga) menjadi ungkapan penghubung antarkalimat (oleh karena itu), seperti pada kalimat (1a) dan (1b) berikut: (1a) *Kami datang terlambat. Oleh karena itu, kami tidak dapat mengikuti perkuliahan.* (1b) *Kami datang terlambat sehingga kami tidak dapat mengikuti perkuliahan.*"
- **Analisis Tata Bahasa & AI/LLM:**
  - Konjungsi *sehingga* adalah konjungsi subordinatif intrakalimat yang mengaitkan klausa anak penanda akibat dengan klausa induk. Konjungsi intrakalimat tidak dapat berfungsi sebagai konjungsi antarkalimat dan tidak boleh ditempatkan di posisi awal kalimat mandiri baru yang terpisah oleh tanda titik (pemenggalan klausa/kalimat buntung).
  - Model AI/LLM sering memecah rantai penalaran kausal secara serampangan dengan membubuhkan tanda titik sebelum klausa akibat dan mengawalinya dengan *Sehingga* berhuruf kapital (*Model ini memiliki miliaran parameter. Sehingga beban GPU meningkat.*).
  - Perbaikan preskriptif: (1) gabungkan klausa dengan tanda koma (*..., sehingga beban GPU meningkat*), atau (2) ganti dengan konjungsi antarkalimat semantis yang sah (*Oleh karena itu, ...* / *Akibatnya, ...* / *Dengan demikian, ...*).

---

## 2. Draf Kaidah Baru untuk Dataset

### Kaidah 1: JRN-013 (Pleonasme Verba Bertujuan: bertujuan untuk)
- **ID:** `JRN-013`
- **Pola:** `bertujuan untuk`
- **Saran Pengganti:** `bertujuan [verba] / untuk [verba] / dirancang untuk [verba]`
- **Penjelasan:** Merujuk kajian kesalahan sintaksis skripsi (Jurnal ILEAL, 2018, hlm. 6), kata 'bertujuan' sudah menyatakan 'mempunyai tujuan', sehingga penambahan preposisi 'untuk' merupakan pleonasme lewah; langsung pasangkan verba setelah 'bertujuan' (misal: 'bertujuan menganalisis') atau gunakan 'untuk' tanpa 'bertujuan'.
- **Contoh Salah:** Model pembelajaran inkuiri ini bertujuan untuk mengorganisasikan pengetahuan siswa.
- **Contoh Benar:** Model pembelajaran inkuiri ini bertujuan mengorganisasikan pengetahuan siswa.

### Kaidah 2: JRN-014 (Pemenggalan Klausa Subordinatif: Sehingga di Awal Kalimat Baru)
- **ID:** `JRN-014`
- **Pola:** `konjungsi sehingga di awal kalimat baru`
- **Saran Pengganti:** `Oleh karena itu, / Akibatnya, / [gabungkan dengan klausa sebelumnya menggunakan tanda koma]`
- **Penjelasan:** Merujuk kajian keefektifan kalimat skripsi (Jurnal Kande, 2021, hlm. 155), 'sehingga' adalah konjungsi intrakalimat penanda akibat, bukan konjungsi antarkalimat; pemakaiannya di awal kalimat mandiri setelah titik memenggal kalimat majemuk menjadi klausa buntung.
- **Contoh Salah:** Kami datang terlambat. Sehingga kami tidak dapat mengikuti perkuliahan.
- **Contoh Benar:** Kami datang terlambat sehingga kami tidak dapat mengikuti perkuliahan.
