# Ringkasan Ekstraksi Rujukan: Preposisi dan Frase Berpreposisi (Effendi & Aritonang, Pusat Bahasa 1992)

## 1. Identitas Dokumen Sumber

- **Judul Buku:** *Preposisi dan Frase Berpreposisi*
- **Penulis:** Drs. S. Effendi dan Drs. Buha Aritonang
- **Penyunting:** Drs. Sriyanto
- **Pengantar:** Hasan Alwi (Kepala Pusat Pembinaan dan Pengembangan Bahasa)
- **Penerbit:** Pusat Pembinaan dan Pengembangan Bahasa, Departemen Pendidikan dan Kebudayaan
- **Tahun Terbit:** 1992
- **Tebal:** viii + 74 halaman (total 82 hlm. PDF)
- **ISBN:** 979-459-317-6
- **Sifat:** Laporan penelitian komprehensif tata bahasa Indonesia mengenai sintaksis dan semantik preposisi.

---

## 2. Intisari Kaidah Preskriptif

### A. Preposisi Titik Waktu Baku: *pada*, Bukan *di* (hlm. 49–50)
Preposisi yang berfungsi menandai titik waktu tertentu dalam bahasa Indonesia baku adalah **pada** (*pada tahun 1938, pada hari Kamis, pada keesokan harinya, pada awal bulan, pada era digital*).
Pemakaian preposisi *di* untuk nomina waktu (*di tahun 2020, di hari Senin, di saat itu, di era modern*) merupakan interferensi ragam lisan/cakapan yang tidak baku dalam tulisan formal.

### B. Pleonasme Preposisi Majemuk: *selain daripada* (hlm. 21–22)
Kata *selain* sudah berfungsi penuh sebagai penanda pengecualian. Penambahan preposisi kedua menjadi *selain daripada* atau *selain dari [nomina umum]* menghasilkan penumpukan preposisi mubazir; bentuk yang lugas ialah **selain ...** atau **di samping ...**.

### C. Penulisan Preposisi Ruang/Arah Wajib Terpisah (hlm. 21–22)
Preposisi majemuk yang dibentuk dari preposisi tunggal (*di/ke*) + nomina ruang/arah (*dalam, atas, bawah, depan, belakang, samping*) wajib ditulis terpisah dua kata karena masing-masing unsurnya masih dapat diperkecil:
- **di dalam** bukan *didalam*
- **ke dalam** bukan *kedalam*
- **di atas** bukan *diatas*
- **ke atas** bukan *keatas*
- **di bawah** bukan *dibawah*
- **ke bawah** bukan *kebawah*
- **di depan** bukan *didepan*
- **di samping** bukan *disamping*

Bentuk serangkai hanya berlaku bagi preposisi majemuk yang telah bersenyawa mutlak (*kepada*, *daripada*).

---

## 3. Pemetaan ke Dataset `data/kalke-indonesia.json`

| ID | Kaidah | Kategori | Kode Regex Utama |
|---|---|---|---|
| `PFP-001` | Preposisi titik waktu cakapan: *di tahun/hari/saat/era* (harusnya *pada*) | `kata_baku_dan_morfologi` | `\bdi\s+(tahun\|hari\|saat\|awal\|era\|dekade)\b` |
| `PFP-002` | Pleonasme preposisi majemuk: *selain daripada* (harusnya *selain / di samping*) | `kata_baku_dan_morfologi` | `\bselain\s+daripada\b` |
| `PFP-003` | Preposisi arah serangkai: *didalam, diatas, dibawah, kedalam* | `kata_baku_dan_morfologi` | `\b(didalam\|kedalam\|diatas\|keatas\|dibawah\|kebawah)\b` |
