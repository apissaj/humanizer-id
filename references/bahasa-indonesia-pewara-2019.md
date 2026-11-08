# Ringkasan Ekstraksi Rujukan: Bahasa Indonesia untuk Pewara (Kurniawan dkk., Badan Bahasa 2019)

## 1. Identitas Dokumen Sumber

- **Judul Buku:** *Bahasa Indonesia untuk Pewara: Seri Penyuluhan Bahasa Indonesia*
- **Penulis:** Dwi Widayati Kurniawan, Maman Suryaman, dkk. (Penyusun Pusat Pembinaan Bahasa dan Sastra)
- **Penerbit:** Badan Pengembangan Bahasa dan Perbukuan, Kementerian Pendidikan dan Kebudayaan
- **Tahun Terbit:** 2019
- **Tebal:** 119 halaman
- **Sifat:** Bahan penyuluhan khusus pewara (master of ceremony); mencakup ejaan, bentuk-pilihan kata, kalimat, wacana lisan, pelafalan, intonasi, ekspresi, dan gestur pewara.

## 2. Intisari Kaidah Preskriptif

### A. Frasa Pewara Tidak Bernalar (hlm. 10, 90)
Dua frasa salih pewara yang lazim tetapi salah nalar:
- **Waktu dan tempat kami persilakan** — yang dipersilakan seharusnya orang (yang bertindak/menyampaikan), bukan waktu dan tempat. Perbaikan: *Waktu dan tempat akan disampaikan oleh panitia* atau *Kepada Bapak/Ibu X kami persilakan menyampaikan laporan*.
- **mengambil tempat duduknya masing-masing** — keliru karena yang diambil ialah kursi yang telah disediakan; bentuk baku: *harap mengambil tempat duduk yang telah disediakan*.

### B. Penyapa Jabatan dengan Honorifik Ganda (hlm. 11, 88)
Kesalahan menyapa pejabat di acara formal: **Yang kami hormati Bapak Kepala Biro Keuangan** atau **Ibu Direktur Jenderal ...** salah karena kata penyapa *Bapak/Ibu* hanya layak menyertai **nama orang**, bukan jabatan.
Pola yang benar: sebut jabatan dulu, lalu nama pemegangnya:
- *Yang kami hormati Kepala Biro Keuangan, Bapak Muhamad Irsal*
- *Yang kami hormati Direktur Jenderal ..., Bapak Paramardhika*

### C. Penyapa Jamak Mubazir (hlm. 86–87)
Gabungan penanda jamak ganda dalam sapaan pewara dilarang: *Para Ibu-ibu, Bapak-Bapak sekalian, Saudara-saudara sekalian, Para hadirin sekalian* — semuanya mubazir karena *para*, *sekalian*, dan bentuk ulang masing-masing sudah menyatakan jamak.
Bentuk yang benar: *Ibu-ibu, Bapak-Bapak, Ibu dan Bapak sekalian, saudara-saudara, hadirin*. (Kaidah ganda jamak ini selaras dengan entri `SPB-001`.)

### D. Verba Baku Pewara (hlm. 89)
Pewara wajib memakai bentuk baku: *menaati* (bukan *mentaati*), *menyukseskan* (bukan *mensukseskan*), *mengoordinasikan* (bukan *mengkoordinir*), *mengubah* (bukan *merubah*).

## 3. Pemetaan ke Dataset `data/kalke-indonesia.json`

| ID | Kaidah | Kategori | Kode Regex Utama |
|---|---|---|---|
| `PWR-001` | Frasa pewara tidak bernalar: *Waktu dan tempat kami persilakan*; *mengambil tempat duduknya masing-masing* | `retorika_klise_ai` | `\bwaktu\s+dan\s+tempat\b[^.!?]*\b(dipersilakan\|kami\s+persilakan)\b` |
| `PWR-002` | Penyapa jabatan dengan honorifik ganda: *Bapak Kepala Biro*, *Ibu Direktur Jenderal* | `retorika_klise_ai` | `\b(Bapak\|Ibu)\s+(Kepala\|Direktur\|...)\s+(Biro\|Bagian\|...)\b` |
