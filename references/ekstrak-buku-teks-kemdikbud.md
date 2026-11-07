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
