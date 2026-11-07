# Ringkasan Ekstraksi Rujukan: Tata Istilah Indonesia (Pusat Bahasa, 1978)

## 1. Identitas Dokumen Sumber

- **Judul Buku:** *Tata Istilah Indonesia*
- **Penyusun:** Dra. S.S. Adiwimarta, Dr. Harimurti Kridalaksana, Dr. Anton M. Moeliono, dkk.
- **Penerbit:** Pusat Pembinaan dan Pengembangan Bahasa, Departemen Pendidikan dan Kebudayaan
- **Tahun Terbit:** 1978
- **Tebal:** iv + 67 halaman
- **Sifat:** Buku materi penyuluhan kebahasaan terbatas untuk pelengkap *Pedoman Umum Pembentukan Istilah* (PUPI).

---

## 2. Intisari Kaidah Preskriptif Peristilahan

### A. Ejaan Fonemik Istilah Asing: Gugur Konsonan Akhir Tak Berfungsi (hlm. 51–52)
Hanya satuan bunyi yang berfungsi dalam fonologi bahasa Indonesia yang dilambangkan huruf. Konsonan penutup ganda atau gugus mati asing yang tidak dilafalkan dalam bahasa Indonesia digugurkan pada akhir kata:
- `dominant` → **dominan** (bukan *dominant*)
- `informant` → **informan** (bukan *informant*)
- `tolerant` → **toleran** (bukan *tolerant*)
- `relevant` → **relevan** (bukan *relevant*)
- `latent` → **laten** (bukan *latent*)
- `optimist` → **optimis** (bukan *optimist*)
- `realist` → **realis** (bukan *realist*)
- `nationalist` → **nasionalis** (bukan *nationalist*)
- `manifest` → **manifes** (bukan *manifest*)

### B. Istilah yang Dijauhkan / Kolot Menyalahi Asas (hlm. 49–50, Seksi 6.3.4)
Istilah sinonim lama yang menyalahi asas penamaan dan pembentukan istilah wajib ditinggalkan demi istilah baku modern:
- *zat lemas* → **nitrogen**
- *zat air* → **hidrogen**
- *zat asam* → **oksigen**
- *ilmu pasti* → **matematika**
- *ilmu pisah* → **kimia**
- *saran diri* → **autosugesti**
- *martabat* (kimia) → **valensi**

### C. Penanganan Awalan Non- Menurut Makna (hlm. 56–57)
Awalan asing *non-* tidak boleh diserap mentah secara serampangan (*non-X*); padanannya mengikuti tiga kategori makna:
1. Makna **'tidak'** → awalan **tak-** terangkai (*non-linear* → *taklinear*; *non-formal* → *takformal/nonformal*).
2. Makna **'bukan'** → kata lepas **bukan** (*non-metal* → *bukan logam*; *non-blok* → *bukan blok / nonblok*).
3. Makna **'tanpa / bebas dari'** (*-less / non-*) → awalan **nir-** (*motionless* → *nirgerak*; *non-laba* → *nirlaba*).

### D. Bentuk Serapan Jamak vs Tunggal (hlm. 38)
Pengambilan istilah serapan asing mengutamakan bentuk yang sudah lazim masuk ke bahasa Indonesia tanpa menghidupkan kembali paradigma morfologi inflektif bahasa asalnya:
- Bentuk baku: **fokus** (bukan jamak Latin *foki*); **laboratorium** (bukan jamak Latin *laboratoria*); **kriteria** (dari *criteria*); **fenomena** (dari *phenomena*).
- Menghidupkan kembali infleksi jamak Latin dianggap hiperkorek tak baku.

### E. Pembatasan Akhiran Keahlian -wan (hlm. 55)
Akhiran *-wan* (dari Sanskerta) yang menandai orang berkeahlian hanya sah dilekatkan pada kata berakhiran vokal /-a/:
- Sah: *matematikawan, fisikawan, statistikawan, sastrawan, ilmuwan, olahragawan*.
- Tidak sah: *\*geologiwan, \*kosmologiwan, \*teknikwan, \*hukumwan, \*ekonomiwan* → wajib diungkapkan secara analitis: **ahli geologi, ahli kosmologi, ahli teknik, pakar hukum, ekonom / ahli ekonomi**.

---

## 3. Pemetaan ke Dataset `data/kalke-indonesia.json`

| ID | Kaidah | Kategori | Kode Regex Utama |
|---|---|---|---|
| `TII-001` | Ejaan fonemik serapan -ant/-ent/-ist (gugur konsonan akhir tak berfonem) | `kata_baku_dan_morfologi` | `\b(dominant\|informant\|tolerant\|relevant\|optimist\|realist\|manifest)\b` |
| `TII-002` | Istilah klasik yang dijauhkan (zat lemas/air/asam, ilmu pasti/pisah) | `kata_baku_dan_morfologi` | `\b(zat\s+lemas\|zat\s+air\|zat\s+asam\|ilmu\s+pasti\|ilmu\s+pisah)\b` |
| `TII-003` | Awalan non- tanpa padanan tak-/bukan-/nir- | `kata_baku_dan_morfologi` | `\bnon-\s?\w+\b` |
| `TII-004` | Bentuk jamak Latin dihidupkan (foki, laboratoria) | `kata_baku_dan_morfologi` | `\b(foki\|laboratoria\|criteria\|phenomena)\b` |
| `TII-005` | Akhiran keahlian -wan pada akar nir-a (*geologiwan*) | `kata_baku_dan_morfologi` | `\b(\w+logiwan\|teknikwan\|sainswan\|hukumwan)\b` |
