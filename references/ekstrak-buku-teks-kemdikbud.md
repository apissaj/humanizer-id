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
