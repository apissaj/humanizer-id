# Ringkasan Ekstraksi Rujukan: Bentuk dan Pilihan Kata (Mustakim, Badan Bahasa 2019)

## 1. Identitas Dokumen Sumber

- **Judul Buku:** *Bentuk dan Pilihan Kata: Seri Penyuluhan Bahasa Indonesia* (edisi pemutakhiran 2019)
- **Penulis:** Drs. Mustakim, M.Hum.
- **Penyunting:** Dra. Ebah Suhaebah, M.Hum.
- **Penerbit:** Badan Pengembangan Bahasa dan Perbukuan, Kementerian Pendidikan dan Kebudayaan
- **Tahun Terbit:** 2019
- **Tebal:** x + 95 halaman
- **Sifat:** Pemutakhiran edisi 2014 (Batch 7); struktur 3 bab: pendahuluan bentuk kata, pengimbuhan, dan pemilihan kata (kriteria ketepatan, kecermatan, keserasian).

## 2. Intisari Kaidah Preskriptif Baru (di luar BPK-001..006)

### A. Pembedaan Kata *jam* dan *pukul* (hlm. 78)
- **jam** = 'durasi atau jangka waktu' (dua jam perjalanan) atau 'arloji/alat penunjuk waktu' (jam dinding, jam tangan).
- **pukul** = 'waktu atau saat peristiwa' (titik waktu).
- Kekeliruan menahun: *pada jam 08.30* (harusnya *pada pukul 08.30*); acara dimulai *sejak jam 09.00* (harusnya *sejak pukul 09.00*).

### B. Verba Kopula Definisi: *adalah/ialah*, Bukan *yaitu/yakni* (hlm. 81)
Kata yang berfungsi predikatif definisi ialah **adalah** (mendefinisikan) dan **ialah** (menjelaskan), bukan *yaitu*. Konjungsi pemerinci *yaitu* dan *yakni* berstatus non-verba sehingga tidak bisa mengisi posisi predikat definisi setelah subjek: *\*Algoritma genetika yaitu metode...* → **Algoritma genetika adalah metode...**.

### C. Pembedaan Fungsi *yaitu/yakni* vs *misalnya/antara lain* (hlm. 81–82)
- **yaitu, yakni** = menyebutkan **seluruh** anggota (perincian tuntas, sesuai bilangan pasti di awal kalimat): *Ada dua hal, yaitu A dan B*.
- **misalnya, antara lain** = menyebutkan **sebagian** dari jumlah yang lebih banyak: *Ada banyak faktor, misalnya A dan B*.
- Kekeliruan: *\*Ada dua faktor utama ..., misalnya curah hujan dan serangan hama* → **yaitu**.

### D. Pembedaan Kata *mantan* dan *bekas* (hlm. 77)
- Kedua kata sama makna dasarnya ('tidak berfungsi lagi', padanan *ex*), tetapi **bekas** cenderung konotatif negatif (peyoratif) jika mengacu pada **orang**.
- Untuk menghapus konotasi peyoratif itu dalam ragam resmi, **mantan** dipilih bagi pemangku jabatan manusia: *mantan rektor, mantan presiden, mantan menteri*.
- **bekas** dibatasi pada benda/kondisi nonmanusia: *bekas kantor pos, bekas luka*.

### E. Kaidah Lain yang Terdokumentasi (sudah dicakup entri lama)
- Ekonomi bahasa: ganda jamak *sejumlah desa-desa, para guru-guru* (hlm. 49–50) — sudah dicakup `SPB-001`.
- Pasangan sinonim *agar supaya, lalu kemudian* (hlm. 60–61) — sudah dicakup `BPK-001`.
- Pembatas + penutup tak terbatas (hlm. 62) — sudah dicakup `BPK-002`.
- dll./dsb./dst. (hlm. 63–64) — sudah dicakup `BPK-004`.
- Resiprokal ganda *saling pukul-memukul* (hlm. 65–67) — sudah dicakup `BPK-003`.
- Ungkapan idiomatis berpreposisi (hlm. 74) — sudah dicakup `BPK-005`.
- Kekeliruan *di mana/yang mana* (hlm. 69–70) — sudah dicakup `KLK-008`.
- Kesalahan *daripada* (hlm. 68, 89–90) — sudah dicakup `BPK-006`.

## 3. Pemetaan ke Dataset `data/kalke-indonesia.json`

| ID | Kaidah | Kategori | Kode Regex Utama |
|---|---|---|---|
| `BPK-007` | *jam* untuk titik waktu (harusnya *pukul*) | `kata_baku_dan_morfologi` | `\b(pada\|sejak\|hingga\|sampai)\s+jam\b\|\bjam\s+\d{1,2}[.:]\d{2}\b` |
| `BPK-008` | *yaitu/yakni* sebagai kopula definisi (harusnya *adalah/ialah*) | `kata_baku_dan_morfologi` | `\b\w+\s+yaitu\s+(suatu\|metode\|...)\b` |
| `BPK-009` | *bekas* untuk manusia/pemangku jabatan (harusnya *mantan*) | `kata_baku_dan_morfologi` | `\bbekas\s+(rektor\|presiden\|...)\b` |
| `BPK-010` | Bilangan pasti + *misalnya/antara lain* (harusnya *yaitu/yakni*) | `kata_baku_dan_morfologi` | `\b(dua\|tiga\|empat\|lima)\s+\w+\b[^.!?]*\b(misalnya\|antara lain)\b` |
