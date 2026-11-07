# Ekstrak Kaidah Buku Teks Resmi Kemendikbudristek

Rujukan utama dokumen ini adalah buku teks resmi berikut:
- **Judul:** *Cerdas Cergas Berbahasa dan Bersastra Indonesia untuk SMA/MA/SMK/MAK Kelas XI* (Edisi Revisi)
- **Penulis:** Heny Marwati & K. Waskitaningtyas
- **Penerbit:** Pusat Kurikulum dan Perbukuan, Kemendikbudristek RI, 2024
- **ISBN:** 978-623-388-439-6
- **Bab Relevan:** Bab VI — *Berperan dalam Konservasi Alam Indonesia Melalui Karya Ilmiah* (hlm. 188–234)

Ekstrak di bawah ini adalah **poin kaidah dan contoh terpilih** (bukan salinan bab utuh), disajikan untuk mendukung aturan editorial Humanizer ID.

---

## 1. Ragam Bahasa Karya Ilmiah (hlm. 210–213)

Tiga komponen penggunaan bahasa baku karya ilmiah versi rubrik resmi buku (Tabel 6.2):

1. **Bahasa baku** — mematuhi kaidah EYD dan leksikon KBBI.
2. **Kalimat bermakna denotasi** — kata dipakai sesuai makna kamarnya, bukan konotasi/kiasan. Contoh buku:
   - *Denotatif:* "Rendahnya indeks tersebut dipengaruhi oleh letak hutan yang **berdampingan** dengan perkebunan kelapa sawit." (berdampingan = bersebelahan)
   - *Konotatif:* "Penduduk desa bersembunyi saat **raja hutan** memasuki desa." (raja hutan = harimau, kiasan)
3. **Objektif & impersonal** — tanpa kata ganti orang pertama/kedua (*aku, kami, kamu*).

Rubrik buku (hlm. 216) menurunkan nilai jika terdapat kalimat dengan kata ganti orang pertama — padanan langsung dengan aturan *Mode Akademik Ketat* di SKILL.md.

---

## 2. Contoh Perbaikan Kalimat Efektif Resmi Buku (hlm. 213–215)

### Contoh 1: Paphiopedilum violascens
- **Sebelum (buku, hlm. 213):** *"Paphiopedilum violascens adalah anggrek berkantung cantik tanpa bintik hitam, merupakan spesies anggrek endemik Papua yang banyak ditemukan di hutan hujan, mulai dari dataran rendah hingga pegunungan bagian bawah."*
- **Sesudah (kunci jawaban buku, hlm. 214):** *"Paphiopedilum violascens merupakan spesies anggrek endemik Papua yang kantung bunganya tidak berbintik hitam dan hanya ditemukan di hutan hujan di bagian dataran rendah hingga pegunungan bagian bawah."*
- **Kaidah:** Kopula ganda *"adalah ... merupakan"* dipadatkan; struktur predikat tunggal.

### Contoh 2: Paragraf Maleo Senkawor (hlm. 214–215)
- **Sebelum (buku):** *"Di desa Saluki Sulawesi Tengah dapat ditemukan burung maleo senkawor. Burung maleo yang jambulnya berwarna hitam ini sudah mulai langka. ... Saat hendak bertelur, induk maleo dan pasangannya menggali lubang-lubang galian sedalam 50cm atau lebih. Telur burung maleo dipendam di dalam tanah dan ditinggalkan."*
- **Sesudah (kunci jawaban buku, hlm. 215):** *"Di desa Saluki, Sulawesi Tengah, dapat ditemukan burung maleo Senkawor yang mulai langka. Burung maleo berkembang biak dengan bertelur yang dikubur di dalam tanah sedalam 50 cm atau lebih. Telur ini biasanya dipendam di pantai berpasir panas atau pegunungan yang memiliki sumber panas bumi."*
- **Kaidah yang terlihat dari revisi resmi:**
  1. Rangkaian kalimat pendek monoton digabung (fusi kalimat).
  2. Satuan ukur ditulis baku: *50cm* → *50 cm* (spasi antara angka dan satuan).
  3. Informasi ganda ("dipendam di dalam tanah dan ditinggalkan") dipadatkan.

### Contoh 3: Sifat objektif karya ilmiah (hlm. 210)
- **Kalimat telaah buku:** *"Perjumpaan dengan sarang orang utan cukup menarik, di mana orang utan terlihat memanfaatkan jenis pohon yang sama sebagai sumber pakan dan tempat bersarang."*
- **Penilaian buku:** objektif karena tidak memakai kata ganti "aku/kami" — tetapi klausula *"di mana"* tetap termasuk pola yang dibersihkan Humanizer ID (BSE-002).

---

## 3. Ejaan Satuan Ukur

Dari revisi resmi buku: **angka dan satuan dipisahkan spasi** (*50 cm*, *5 kg*, *240 MHz*), kecuali lambang satuan yang melekat pada notasi khusus.

---

## 4. Integrasi dengan Dataset Humanizer ID

Empat entri baru telah ditambahkan ke `data/kalke-indonesia.json` bersumber dari buku ini:
- `BSE-001`: *adalah merupakan* → *merupakan/adalah* (hlm. 213)
- `BSE-002`: *di mana* sebagai kata sambung → konjungsi tepat (hlm. 210)
- `BSE-003`: *menggaris bawahi* → *menggarisbawahi* (konfiks, PUEBI)
- `BSE-004`: *mempertanggung jawabkan* → *mempertanggungjawabkan* (konfiks, PUEBI)

Skrip `scripts/audit.py` memuat dataset ini otomatis, sehingga keempat pola langsung terdeteksi saat pemindaian.

---

## 5. Kaidah Kalimat Efektif & Surat Resmi (Buku Siswa Kelas XII, 2024)

### Data Buku:
- **Judul:** *Bahasa Indonesia untuk SMA/MA/SMK/MAK Kelas XII* (Edisi Revisi)
- **Penerbit:** Pusat Kurikulum dan Perbukuan, Kemendikbudristek RI, 2024
- **Bab Relevan:** Bab I — *Mengomunikasikan Informasi Penting tentang Pendidikan dan/atau Pekerjaan* (hlm. 29–34)

### Lima Ciri Kalimat Efektif Resmi (Sasangka, 2019 dalam Buku Siswa XII, hlm. 30):
1. **Lugas:** Hanya informasi penting yang dipakai; mengandung makna yang padat tanpa basa-basi pengantar klise.
2. **Tepat:** Kalimat sesuai dengan maksud yang ingin disampaikan sehingga tidak menimbulkan multitafsir atau celah ambiguitas.
3. **Jelas:** Sesuai dengan struktur gramatikal baku dan lengkap unsur-unsurnya (Subjek dan Predikat jelas, tidak diawali preposisi perusak subjek).
4. **Hemat:** Kalimat ditampilkan cermat dan tidak boros atau berlebihan (anti-pleonasme kopula, pemangkasan verba ringan).
5. **Sejajar (Paralelisme):** Memiliki bentuk dan struktur yang paralel, sama, atau sederajat (keseragaman imbuhan morfemis pada perincian).

### Perbaikan Kalimat Surat Resmi (Aktivitas 1.11, hlm. 33):
1. **Pola Konjungsi Guna + Nomina yang Salah:**
   - *Salah (Buku hlm. 33):* *"Maksud dan tujuan melaksanakan kegiatan itu adalah guna peningkatan kinerja para karyawan."*
   - *Baku:* *"Tujuan kegiatan ini adalah untuk meningkatkan kinerja karyawan."* (Ganti nomina 'peningkatan' menjadi verba aktif 'meningkatkan').
2. **Pola Agar + Menjadikan yang Salah:**
   - *Salah (Buku hlm. 33):* *"Demikian surat ini kami sampaikan agar menjadikan perhatian dan kerja samanya..."*
   - *Baku:* *"Demikian surat ini kami sampaikan untuk menjadi perhatian Bapak/Ibu..."* (Penyelarasan verba intransitif).

---

## 6. Sistematika Karya Ilmiah Resmi (Buku Siswa Kelas XI, 2024, hlm. 213)

Buku Siswa Kelas XI (ISBN 978-634-00-0958-3) menetapkan sistematika karya ilmiah baku dalam tiga bagian:

### A. Bagian Awal:
1. Judul
2. Nama penulis dan afiliasinya
3. Abstrak
4. Kata kunci

### B. Bagian Inti:
1. Pendahuluan
2. Metode penelitian
3. Analisis data
4. Hasil
5. Pembahasan

### C. Bagian Akhir:
1. Simpulan dan saran
2. Daftar pustaka
3. Lampiran

### Ketentuan Ilmiah (Jones, 1960 dalam Laba & Rinayanthi, 2018: 15):
- Fakta disajikan berdasarkan hasil pengamatan, eksperimen, atau kajian pustaka.
- Karya ilmiah tidak terbatas pada sains dan teknologi.

### Ketentuan Artikel Ilmiah (Tanjung, 2015: 7):
- Artikel ilmiah ditulis dengan tata cara ilmiah dan pedoman ilmiah yang telah disepakati.
- Dikelompokkan sebagai artikel hasil penelitian dan artikel non-penelitian.

### Contoh Kalimat Pasif Objektif dari Artikel Resmi dalam Buku (hlm. 215):
*"Penelitian ini bertujuan untuk melihat kondisi terumbu karang di Teluk Ambon yang akan dibandingkan dengan penelitian sebelumnya. Metode yang digunakan adalah Line Intercept Transect (LIT) di delapan stasiun pengamatan."*
- Analisis: pasif baku (*bertujuan, digunakan*), tanpa kata ganti orang pertama, satuan & istilah asing miring.

### Sumber Karya Ilmiah Asli dalam Buku:
- Indrabudi, T., & Alik, R. — *"Status Kondisi Terumbu Karang di Teluk Ambon"* (Widyariset – LIPI). Dipakai buku sebagai contoh telaah ragam bahasa ilmiah.
---

## 3. Ekstrak Buku Siswa Kelas XI Edisi Revisi (Kemendikbudristek, 2024)

- **Judul:** *Cerdas Cergas Berbahasa dan Bersastra Indonesia untuk SMA/MA/SMK/MAK Kelas XI (Edisi Revisi)*
- **Penulis:** K. Waskitaningtyas & Heny Marwati
- **Bab Relevan:** Bab VI Berperan dalam Konservasi Alam Indonesia Melalui Karya Ilmiah (hlm. 209–265)

### A. Kaidah Ragam Bahasa Ilmiah (hlm. 257–258)
1. **Objektif:** Berdasarkan data dan fakta empiris, bebas sudut pandang pribadi/emosi.
2. **Reproduktif:** Informasi yang disampaikan penulis harus dapat dipahami oleh pembaca dengan makna yang persis sama.
3. **Denotatif murni:** Bebas dari penambahan makna konotatif/metaforis.

### B. Aturan Penulisan Identitas Penulis (hlm. 253)
1. **Nama penulis artikel ilmiah ditulis TANPA gelar akademik** (bukan *Dr. Ahmad Hidayat, M.Si*, melainkan *Ahmad Hidayat*).
2. **Nama belakang TIDAK BOLEH disingkat** (bukan *Ahmad H*, melainkan *Ahmad Hidayat*) karena nama belakang menjadi pengenal rujukan/sitasi.

### C. Sistematika Artikel Ilmiah Baku (hlm. 253–256)
1. **Bagian Awal:** Judul (lugas, tanpa singkatan tidak baku), Nama Penulis (tanpa gelar), Afiliasi, Abstrak (ringkasan masalah-metode-hasil-simpulan), Kata Kunci (3–5 istilah representatif).
2. **Bagian Inti:**
   - **Pendahuluan:** Latar belakang masalah, rumusan masalah (pertanyaan terukur), tujuan penelitian, manfaat penelitian.
   - **Kerangka Teoretis:** Kajian pustaka penelitian terdahulu dan hipotesis.
   - **Metodologi Penelitian:** Prosedur, data, teknik pengumpulan, dan analisis.
   - **Hasil & Pembahasan:** Interpretasi data dan temuan.
   - **Simpulan & Saran:** Jawaban rumusan masalah dan rekomendasi kebijakan/lanjutan.
3. **Bagian Akhir:** Daftar Pustaka (Harvard / APA) dan Lampiran (data pendukung).
### D. Konjungsi Intrakalimat vs Antarkalimat (Buku Kelas XII Kurikulum Merdeka, 2024, Bab IV hlm. 167–172)

Berdasar Alwi dkk. (2017), buku Kelas XII merinci dua kategori konjungsi:

#### 1. Konjungsi Intrakalimat — WAJIB Diawali Tanda Koma (Tabel 4.11, hlm. 168):
- `..., kecuali`, `..., kemudian`, `..., lalu`, `..., lantas`, `..., padahal`, `..., tetapi`, `..., namun`, `..., sedangkan`, `..., melainkan`, `..., bahkan`.
- Contoh: *"Adiknya rajin, sedangkan kakaknya malas."* / *"Mobil itu baru, tetapi sudah mogok."*

#### 2. Konjungsi Intrakalimat — TANPA Tanda Koma (Tabel 4.12, hlm. 168):
- `dan`, `atau`, `bahwa`, `karena`, `sehingga`, `agar`, `apabila`, `jika`, `maka`.
- Contoh: *"Jalan utama ditutup sehingga terjadi kemacetan."* / *"Ia tidak hadir karena sakit."*

#### 3. Larangan Konjungsi Intrakalimat di Awal Kalimat (hlm. 169):
- *Salah:* *"Ia kerap berolahraga. Sehingga wajar badannya sehat."*
- *Baku:* *"Ia kerap berolahraga sehingga wajar badannya sehat."* ATAU *"Ia kerap berolahraga. Oleh karena itu, wajar badannya sehat."*
- *Salah:* *"Kakak memilih sains. Sedangkan adik memilih sastra."*
- *Baku:* *"Kakak memilih sains, sedangkan adik memilih sastra."* ATAU *"Kakak memilih sains. Sementara itu, adik memilih sastra."*

#### 4. Konjungsi Antarkalimat (Tabel 4.13, hlm. 170):
Ditulis di awal kalimat baru dan diikuti tanda koma: *Adapun, Akan tetapi, Biarpun begitu, Contohnya, Dalam hal ini, Dengan demikian, Dengan kata lain, Di samping itu, Jadi, Karena itu, Kendatipun demikian, Maka dari itu, Meskipun begitu, Pada dasarnya, Pada hakikatnya, Pendeknya, Sebagai kesimpulan, Sebaiknya, Sebelumnya, Sebenarnya, Sehubungan dengan itu, Selain itu, Selanjutnya, Sementara itu, Sesungguhnya, Sungguhpun demikian, Untuk itu, Walaupun demikian*.
### E. Ide Pokok & Pola Pengembangan Paragraf (Buku Siswa Kelas XI 2024, Bab I hlm. 8–13)

1. **Kesatuan paragraf:** Setiap paragraf hanya memuat **satu ide pokok** yang tertuang dalam kalimat utama (*kalimat topik*). Dua gagasan dalam satu paragraf melanggar kaidah kesatuan.
2. **Pola pengembangan paragraf:**
   - **Deduksi:** kalimat utama di awal, diikuti kalimat-kalimat penjelas (umum → khusus).
   - **Induksi:** kalimat-kalimat penjelas di awal, kalimat utama di akhir (khusus → umum).
   - Pola harus konsisten; campuran kedua pola dalam satu paragraf membuat alur gagasan tidak runtut.
3. **Struktur teks argumentasi:** Ide pokok (kalimat topik) → ide-ide pendukung (kalimat penjelas) → simpulan/tuduhan penutup.
---

## 4. Ekstrak Modul Pembelajaran SMA Bahasa Indonesia Kelas XI (Direktorat SMA Kemendikbud, 2020)

- **Judul:** *Merancang Karya Ilmiah Sesuai dengan Unsur-Unsur dan Isi Karya Ilmiah (KD 3.14 & 3.15)*
- **Penerbit:** Direktorat SMA, Ditjen PAUD, DIKDAS, dan DIKMEN, Kemendikbud RI, 2020
- **Bagian Relevan:** Kegiatan Pembelajaran 3: Kebahasaan Karya Ilmiah (hlm. 17–19)

### A. Sembilan Ciri Kebahasaan Karya Ilmiah Baku (hlm. 17–18):
1. **Pilihan Kata Impersonal:** Dilarang menggunakan kata ganti persona pertama atau kedua (*aku, saya, kamu, dia*). Jika subjek perlu disebut, gunakan bentuk impersonal umum (*penulis, peneliti*) atau utamakan kalimat pasif.
2. **Kelugasan:** Pembahasan langsung pada inti masalah tanpa basa-basi verbal atau ornamen retoris.
3. **Pemberantasan Makna Ganda:** Menghindari kata dan konstruksi kalimat ambigu yang multitafsir.
4. **Keajegan & Kepastian Makna:** Penggunaan istilah yang konsisten dari awal hingga akhir naskah.
5. **Denotatif Murni:** Makna kata tidak mengalami pergeseran emosional atau penambahan asosiatif.
6. **Eksplisitas:** Hubungan antarunsur kalimat diungkapkan secara jelas dan tegas.
7. **Penggunaan Kata Baku:** Kepatuhan mutlak terhadap ejaan dan kaidah KBBI/EYD.
8. **Penggunaan Istilah Bidang Ilmu:** Ketepatan istilah teknis sesuai disiplin kajian.
9. **Kata Kerja Mental Pasif:** Pemanfaatan verba mental ilmiah (*diduga, dianalisis, dipahami, teridentifikasi*).
---

## 5. Ekstrak Modul Pembelajaran SMA Bahasa Indonesia Kelas XII (Direktorat SMA Kemendikbud, 2020)

- **Judul:** *Menganalisis Kebahasaan dan Menulis Artikel Opini (KD 3.11)*
- **Penerbit:** Direktorat SMA, Ditjen PAUD, DIKDAS, dan DIKMEN, Kemendikbud RI, 2020
- **Bagian Relevan:** Kegiatan Pembelajaran 2: Kepaduan Isi & Penalaran (hlm. 21–23)

### A. Kaidah Kepaduan Isi & Kelogisan Penalaran (hlm. 21)
1. **Ketaklogisan Sebab-Akibat Konjungsi Antarkalimat:**
   - *Salah:* *"Pak Amat mengidap kanker paru-paru. Oleh sebab itu, ia banyak merokok."*
   - *Analisis:* Penggunaan *oleh sebab itu* menyiratkan kanker adalah penyebab seseorang merokok. Penalaran terbalik ini merusak koherensi wacana.
   - *Baku:* *"Pak Amat banyak merokok. Oleh sebab itu, ia mengidap kanker paru-paru."*
2. **Karakteristik Artikel Opini Populer vs Karya Ilmiah Murni (hlm. 14):**
   - Artikel ilmiah: impersonal, pasif, istilah teknis disiplin ilmu, struktur kaku.
   - Artikel opini populer: komunikatif, lugas, adverbial frekuentatif (*sering, biasanya, kadang-kadang*), konjungsi penata argumentasi (*pertama, kedua, selain itu*), dan kalimat tanya retoris terarah tanpa multitafsir.
---

## 6. Ekstrak Modul Pembelajaran SMA Bahasa Indonesia Kelas XI (Direktorat SMA Kemendikbud, 2020)

- **Judul:** *Teks Proposal Karya Ilmiah (KD 3.12)*
- **Penerbit:** Direktorat SMA, Ditjen PAUD, DIKDAS, dan DIKMEN, Kemendikbud RI, 2020 (66 hlm.)
- **Bagian Relevan:** Unsur Kebahasaan Proposal — Penulisan Huruf (hlm. 24–34)

### A. Tiga Puluh Sembilan Aturan Huruf Kapital (hlm. 24–34)
Kaidah kunci yang paling sering dilanggar model bahasa:
1. **Nama jenis dari nama diri geografi/orang:** huruf kecil semua. (*kunci inggris, pisang ambon, mesin diesel, 15 watt* — bukan *Kunci Inggris, Mesin Diesel*).
2. **Bentuk dasar turunan nama bangsa/bahasa:** huruf kecil. (*pengindonesiaan, keinggris-inggrisan*).
3. **Jabatan/pangkat tanpa nama spesifik:** huruf kecil (*sejumlah menteri, rapat kabinet*), tetapi kapital bila merujuk nama spesifik (*Menteri Keuangan Republik Indonesia, Gubernur Jawa Barat*).
4. **Kekerabatan sapaan vs relasi:** kapital pada sapaan langsung (*"Kapan Bapak berangkat?"*, *Surat Saudara sudah saya terima*), huruf kecil pada relasi keluarga umum (*rumah paman dan bibi*).
5. **Nama dokumen resmi/lembaga:** kapital semua unsur, kecuali kata tugas (*Republik Indonesia, Badan Kesejahteraan Ibu dan Anak*), termasuk bentuk ulang sempurna (*Perserikatan Bangsa-Bangsa, Dasar-Dasar Ilmu Hukum*).
6. **Afiksasi nama diri Belanda/Jerman/Portugal:** huruf kecil untuk partikel (*Robin van Persie*).
7. **Nama orang yang menjadi nama jenis/satuan ukuran:** huruf kecil (*mesin diesel, 15 watt, ampere*), kecuali tetap kapital bila tetap disebut sebagai nama ilmuwan (*joule per Kelvin, Newton*).
8. **Nama peristiwa sejarah:** kapital bila nama resmi (*Perang Teluk, Konferensi Meja Bundar*); huruf kecil bila umum (*para pahlawan berjuang demi kemerdekaan Indonesia*).

### B. Huruf Miring (hlm. 34+)
- Nama buku, majalah, surat kabar yang dikutip dalam tulisan (*...berita di surat kabar Pos Kota*).
- Kata/ungkapan asing yang belum terserap.
---

## 7. Ekstrak Buku Siswa Kelas X Kurikulum Merdeka Edisi Revisi (Kemendikbudristek 2022)

- **Judul:** *Cerdas Cergas Berbahasa dan Bersastra Indonesia untuk SMA/MA/SMK/MAK Kelas X (Edisi Revisi)*
- **Penerbit:** Pusat Kurikulum dan Pembelajaran, Badan Pengembangan dan Pembinaan Bahasa, Kemendikbudristek, 2022 (320 hlm.)
- **Bagian Relevan:** Bab I — Mengungkap Fakta Alam secara Objektif (hlm. 18–26)

### A. Kaidah Kalimat Definisi: adalah vs merupakan (hlm. 19)
1. **Kata `adalah`:** Dipakai untuk menjelaskan pengertian yang MUTLAK (ekuivalensi A = B).
   - Contoh: *Belalang anggrek (Hymenopus Coronatus) adalah salah satu jenis belalang sentadu.*
2. **Kata `merupakan`:** Dipakai untuk menjelaskan pengertian yang TIDAK MUTLAK (penempatan objek dalam kategori yang bisa mencakup satu pengertian atau lebih).
   - Contoh: *Belalang anggrek merupakan predator polifagus.*

### B. Perbedaan Imbuhan di- dan Kata Depan di (Tabel 1.6, hlm. 20)
| Aspek | Imbuhan di- | Kata Depan di |
|---|---|---|
| Fungsi | Membentuk kata kerja pasif | Menunjukkan keterangan tempat/waktu |
| Penulisan | Serangkai dengan kata dasar | Terpisah dari kata yang diikuti |

- *Salah:* *"Data di analisis menggunakan SPSS."*
- *Baku:* *"Data dianalisis menggunakan SPSS."*

### C. Kutipan Tidak Langsung & Sumber Rujukan (hlm. 21–22)
- Dua format CMS edisi 17:
  - **Format dalam kurung:** *...ditemukan di daerah lembap (Borror & White, 1970: 37).*
  - **Format naratif:** *Essig (1958: 78) menyatakan bahwa...*
- **Tanggal akses wajib** untuk sumber daring karena konten internet bersifat dinamis.
- Format daftar pustaka skripsi: Nama. Tahun. "Judul". Jenis karya pada Prodi, Universitas. URL. Diakses tanggal.
- Alternatif format internasional: APA, MLA.

### D. Daftar Periksa LHO (Tabel 1.8, hlm. 26)
- Judul diawali huruf kapital kecuali kata depan; judul tanpa tanda baca akhir.
- Struktur wajib: definisi umum → deskripsi per bagian → deskripsi manfaat.
- Objektivitas: hanya informasi hasil pengamatan indrawi (lihat, dengar, cium, sentuh, rasa).
---

## 8. Ekstrak Buku Siswa Kelas XI Kurikulum Merdeka (Kemendikbudristek 2021)

- **Judul:** *Cerdas Cergas Berbahasa dan Bersastra Indonesia untuk SMA/SMK Kelas XI*
- **Penerbit:** Pusat Kurikulum dan Pembelajaran, Badan Pengembangan dan Pembinaan Bahasa, Kemendikbudristek, 2021 (240 hlm.)
- **Bagian Relevan:** Bab 6 — Berperan dalam Konservasi Alam Indonesia lewat Karya Ilmiah (hlm. 199–203)

### A. Ragam Bahasa Ilmiah & Evaluasi Objektivitas (hlm. 199–201)
1. **Pemberantasan Residu Kata Penghubung `dimana` (hlm. 200):**
   - Buku menyorot kalimat salah: *"Perjumpaan dengan sarang orang utan cukup menarik dimana orang utan terlihat..."*
   - Kata `dimana` bukan kata hubung subordinatif dalam ragam ilmiah baku; `dimana` hanya kata tanya tempat.
   - Perbaikan: ganti dengan konjungsi semantik yang tepat (*karena, tempat, sehingga*) atau restrukturisasi klausa.
2. **Karakteristik Karya Ilmiah Menurut Chaer (2011) & Laba-Rinayanthi (2018):**
   - **Objektif:** Pernyataan didukung data empiris/lapangan terukur, bukan perasaan penulis.
   - **Reproduktif:** Informasi yang disampaikan penulis dipahami sama persis oleh pembaca tanpa interpretasi ganda.
   - **Denotatif Murni:** Bebas dari makna konotatif yang mengandung penambahan rasa/emosi pembaca (*buah yang manis* = denotatif; *duduk dengan manis* = konotatif).
3. **Format Rujukan:**
   - Standar penulisan daftar pustaka: susunan nama pengarang pertama dibalik; tahun terbit; judul pustaka (miring); kota terbit: nama penerbit.
---

## 9. Ekstrak Buku Seri Penyuluhan 1: Ejaan dalam Bahasa Indonesia (Pusat Bahasa Depdikbud)

- **Judul:** *Seri Penyuluhan 1: Ejaan dalam Bahasa Indonesia*
- **Penyunting:** Lukman Hakim, Zainul Arifin, Yayah B. Lumintaintang
- **Penerbit:** Pusat Pembinaan dan Pengembangan Bahasa, Depdikbud (ISBN 979-459-154-8, 64 hlm.)
- **Bagian Relevan:** Bab III Penulisan Kata (hlm. 7–18)

### A. Kaidah Kata Ulang Baku (hlm. 13)
- Larangan mutlak penggunaan angka 2 dalam ragam resmi (*anak2, sekolah2, ber-kejar2-an*).
- Kata ulang ditulis lengkap dengan tanda hubung: *anak-anak, sekolah-sekolah, berkejar-kejaran, didorong-dorong*.
- Reduplikasi kata ulang berubah bunyi: konsonan (*sayur-mayur, lauk-pauk, ramah-tamah*), vokal (*huru-hara, gerak-gerik, bolak-balik*).

### B. Gabungan Kata: Terpisah vs Senyawa Serangkai (hlm. 15–17)
1. **Wajib Terpisah (unsur masih bebas):**
   - *tanggung jawab, kerja sama, tanda tangan, terima kasih, uji coba, kantor pos, duta besar, cagar alam, tata surya, bima sakti, serah terima*.
2. **Wajib Serangkai (senyawa padu):**
   - *daripada, barangkali, padahal, sekaligus, bilamana, apabila, matahari, saputangan, bumiputra, segitiga, hulubalang*.

### C. Unsur Terikat (hlm. 17–18)
- Bentuk terikat (*sub-, maha-, peri-, antar-, tuna-, catur-*) ditulis serangkai dengan kata dasar: *subunit, subbagian, mahaguru, mahatahu, perilaku, antarkota*.
- Pengecualian 1: Diikuti huruf kapital $ightarrow$ wajib diberi tanda hubung (*non-RRC, non-Indonesia, pan-Afrikanisme, antar-SMA*).
- Pengecualian 2: *maha* dan *peri* diikuti kata berimbuhan $ightarrow$ ditulis terpisah (*maha pengasih, maha pemurah*); diikuti kata dasar $ightarrow$ serangkai (*mahakasih, mahamurah*).
