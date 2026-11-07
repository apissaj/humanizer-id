# Ringkasan Ekstraksi Rujukan: Bahasa Indonesia untuk Perguruan Tinggi (Suyatno dkk., 2017)

## 1. Identitas Dokumen Sumber

- **Judul Buku:** *Bahasa Indonesia untuk Perguruan Tinggi (Membangun Karakter Mahasiswa melalui Bahasa)*
- **Penulis:** Dr. Suyatno, M.Pd., Tri Pujiati, M.Pd., Didah Nurhamidah, M.Pd., Lutfi Syauki Faznur, M.Pd. (Dosen UIN Syarif Hidayatullah Jakarta)
- **Penerbit:** Penerbit IN MEDIA, Jakarta
- **Tahun Terbit:** 2017
- **Tebal:** xii + 150 halaman
- **ISBN:** 978-602-0969-90-9
- **Sifat:** Buku ajar mata kuliah wajib universitas (MKWU) Bahasa Indonesia jenjang S-1.

---

## 2. Intisari Kaidah Preskriptif

### A. Pasangan Kata Penghubung / Korelatif Baku (hlm. 76)
Pasangan penghubung korelatif bersifat tetap dan tidak boleh disilang:
- **antara ... dan ...** (bukan *antara ... dengan ...*)
- **tidak ... tetapi ...** (bukan *tidak ... melainkan ...*)
- **bukan ... melainkan ...** (bukan *bukan ... tetapi ...*)
- **baik ... maupun ...** (bukan *baik ... ataupun ...*)

### B. Keparalelan / Kesejajaran Perincian (hlm. 103)
Unsur-unsur yang sama derajat dalam sebuah perincian wajib berpola gramatikal sama.
- Salah (campur bentuk): *Kegiatan perpustakaan meliputi pembelian buku, membuat katalog, dan buku-buku diberi label.*
- Benar (nomina semua): *Kegiatan perpustakaan meliputi pembelian buku, pembuatan katalog, dan pelabelan buku.*
- Benar (verba aktif semua): *Kegiatan perpustakaan meliputi membeli buku, membuat katalog, dan melabeli buku.*

### C. Salah Nalar Pola Frasa: Kasus 'Bebas Parkir' (hlm. 108)
Pola konstruksi *bebas + nomina* secara semantik bermakna **'tanpa ada / bersih dari X'**:
- *bebas buta huruf* = tanpa orang buta huruf
- *bebas becak* = kawasan tanpa becak
- *bebas asap rokok* = kawasan tanpa asap rokok
- *bebas bea* = tanpa pengenaan bea

Oleh sebab itu, frasa *bebas parkir* secara nalar berarti **'kawasan tanpa parkir / dilarang parkir'**. Mengartikannya sebagai boleh parkir atau parkir cuma-cuma adalah salah nalar menahun. Bentuk yang tepat ialah **parkir gratis** atau **bebas biaya parkir**.

---

## 3. Pemetaan ke Dataset `data/kalke-indonesia.json`

| ID | Kaidah | Kategori | Kode Regex Utama |
|---|---|---|---|
| `SYT-001` | Pasangan korelatif salah: *tidak ... melainkan ...* (harusnya *tidak ... tetapi ...*) | `retorika_klise_ai` | `\btidak\s+[^.!?]{2,80}?\bmelainkan\b` |
| `SYT-002` | Perincian tidak sejajar: nomina campur verba me-/pasif (*meliputi pembelian..., membuat...*) | `retorika_klise_ai` | `\bmeliputi\b[^.!?]*\b(membuat\|diberi\|dilakukan)\b` |
| `SYT-003` | Salah nalar frasa *bebas parkir* (harusnya *parkir gratis*) | `retorika_klise_ai` | `\bbebas\s+parkir\b` |
