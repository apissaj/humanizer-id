# Ringkasan Ekstraksi Rujukan: Daftar Istilah Linguistik Asing-Indonesia (Kridalaksana, Pusat Bahasa 1978)

## 1. Identitas Dokumen Sumber

- **Judul Buku:** *Daftar Istilah Linguistik Asing-Indonesia*
- **Penyusun:** Harimurti Kridalaksana
- **Penelaah:** Prof. Dr. Amran Halim, Anton M. Moeliono, Dr. J.S. Badudu, S. Effendi, Prof. Dr. Samsuri, Sjahrul Sjarif (Panitia Pengembangan Bahasa Indonesia) + Jawatankuasa Tetap Bahasa Malaysia (Prof. Dr. Asmah Haji Omar, Dr. Abdullah Hasan)
- **Penerbit:** Pusat Pembinaan dan Pengembangan Bahasa, Departemen Pendidikan dan Kebudayaan
- **Tahun Terbit:** 1978 (naskah proyek 1975/1976)
- **Tebal:** xiv + 59 halaman (dua kolom: istilah asing — padanan Indonesia)
- **Sifat:** Daftar padanan resmi istilah linguistik; bagian "Beberapa Penjelasan" (hlm. xiii–xiv) memuat prinsip preskriptif pengistilahan.

---

## 2. Intisari Prinsip Preskriptif Pengistilahan (hlm. xiii–xiv)

### A. Penyederhanaan Sinonim Asing Menjadi Satu Padanan (hlm. xiii)
Deret sinonim asing diindonesiakan dengan istilah tunggal:
- *incontiguous assimilation = noncontiguous assimilation = dilation = distant assimilation* → **asimilasi jauh**
- *iterative aspect = frequentative aspect = habitual aspect* → **aspek iteratif**

### B. Penolakan Penerjemahan Harfiah yang Menggeser Konsep (hlm. xiii)
Pengalihan tidak dilakukan membabi buta; padanan resmi:
- *linguistic atlas* → **atlas bahasa** (bukan *atlas linguistik/atlas linguistis*)
- *linguistic skill* → **keterampilan bahasa** (bukan *keterampilan linguistik*)
- *postvelar* → **velar belakang** (tetapi *postposision* tetap **postposisi**)
- *semantic component* → **komponen semantis**

### C. Urutan Unsur Padanan Mengikuti Struktur Frasa Indonesia (hlm. xiii)
Unsur kepala mendahului penjelasnya:
- *predicate nominative* → **predikat nominal** (bukan *nominatif predikat*)
- *predicate adjective* → **adjektiva predikatif**
- *loan translation* → **pinjam terjemah** (bukan *terjemah pinjam*)

### D. Alih Fonem Klasik: /k/ Latin Dipertahankan (hlm. xiii)
- *centum language* → **bahasa kentum** (bukan *bahasa sentum*)
- *cenematics* → **kenematika** (bukan *senematika*)
- *apocope* → **apokope** (bukan *apokop*)

### E. Nuansa Makna Proses vs Hasil (hlm. xiv)
Bahasa Indonesia membedakan hasil (*-an*) dan proses (*peN-...-an*) yang tak dibedakan bahasa sumber:
- *borrowing* → **pinjaman** (hasil) / **peminjaman** (proses)
- *split* → **pisahan** (hasil) / **pemisahan** (proses)

### F. Istilah Asing Usang Tidak Diindonesiakan (hlm. xiv)
*sematology, glossology* tidak diberi padanan; langsung pakai **semantik**. Jargon khusus tanpa padanan (*gapping, raising, hedge, freeze*) tetap ditulis sebagai bentuk asing.

---

## 3. Pemetaan ke Dataset `data/kalke-indonesia.json`

| ID | Kaidah | Kategori | Kode Regex Utama |
|---|---|---|---|
| `DIL-001` | Kerancuan proses vs hasil: *proses pinjaman/pisahan* | `kata_baku_dan_morfologi` | `\bproses\s+(pinjaman\|pisahan)\b` |
| `DIL-002` | Harfiah kaku: *keterampilan linguistik, atlas linguistik* | `kata_baku_dan_morfologi` | `\b(keterampilan\|atlas)\s+linguisti[ks]\b` |
| `DIL-003` | Urutan padanan terbalik: *nominatif predikat, terjemah pinjam* | `kata_baku_dan_morfologi` | `\b(nominatif\s+predikat\|terjemah\s+pinjam)\b` |
| `DIL-004` | Alih fonem klasik keliru: *bahasa sentum, senematika, apokop* | `kata_baku_dan_morfologi` | `\b(bahasa\s+sentum\|senematika\|apokop)\b` |
