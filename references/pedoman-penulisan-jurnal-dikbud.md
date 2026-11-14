# Ekstrak Kaidah: Pedoman Penulisan Jurnal Pendidikan dan Kebudayaan (Balitbang Kemdikbud)

## 1. Identitas Dokumen Sumber

- **Judul Dokumen:** *Pedoman Penulisan Artikel Jurnal Pendidikan dan Kebudayaan*
- **Penerbit:** Badan Penelitian dan Pengembangan (Balitbang), Kementerian Pendidikan dan Kebudayaan RI, Jakarta
- **Tebal:** 5 hlm. Berkas dump: `work/text_dumps/pedoman_penulisan_jurnal_dikbud.txt` (`HAL 1` s.d. `HAL 5`).
- **Fokus Ekstraksi:** Standar baku artikel jurnal ilmiah nasional terakreditasi: pembatasan judul, anatomi abstrak mandiri, proporsi struktur IMRaD, eliminasi gelar akademik, dan sistem sitasi Turabian Reference List.

---

## 2. Peta Kaidah Preskriptif (PJK-001..015)

### A. Judul & Identitas Penulis

- **ID: PJK-001** (HAL 1, butir 4; HAL 3)
  - **Kaidah Batas Judul:** Judul artikel maksimal **14 kata** (tidak termasuk subjudul dan kata penghubung). Judul wajib spesifik, jelas, dan memuat kata kunci substantif.
  - **Verbatim:** *"Judul artikel maksimal 14 kata (tidak termasuk sub judul dan kata penghubung) ditulis dalam Bahasa Indonesia dan Bahasa Inggris."*

- **ID: PJK-002** (HAL 3, template)
  - **Kaidah Identitas Penulis:** Nama lengkap penulis ditulis **tanpa gelar akademik, tanpa pangkat, dan tanpa jabatan struktural**.
  - **Verbatim:** *"Nama lengkap penulis (tanpa gelar, pangkat atau jabatan)"*

### B. Struktur dan Komposisi Abstrak

- **ID: PJK-003** (HAL 1, butir 5; HAL 3)
  - **Kaidah Panjang & Bentuk Abstrak:** Abstrak wajib ditulis dalam **satu paragraf** dengan panjang **150–200 kata**, dwibahasa (Indonesia & Inggris).
  - **Verbatim:** *"Abstrak memuat tujuan penelitian, metode penelitian, hasil penelitian, dan kesimpulan. Abstrak ditulis dalam satu paragraf, 150-200 kata..."*

- **ID: PJK-004** (HAL 3, template)
  - **Kaidah Larangan dalam Abstrak:** Abstrak dilarang memuat: (1) acuan/sitasi, (2) catatan kaki (*footnote*), (3) kutipan pustaka, (4) singkatan/akronim yang belum dijabarkan, dan (5) informasi matematis/rumus teknis.
  - **Verbatim:** *"...tanpa acuan, catatan kaki, kutipan pustaka, singkatan/akronim, dan informasi matematis."*

- **ID: PJK-005** (HAL 1, butir 5; HAL 3)
  - **Kaidah Kata Kunci:** Berjumlah **3 sampai 5 kata atau frasa** yang penting, spesifik, dan mencerminkan konsep yang dikandung artikel.

### C. Proporsi Halaman Struktur IMRaD (Artikel Hasil Penelitian, HAL 1)

- **ID: PJK-006** (HAL 1, butir 7a) — **Pendahuluan (10%):** latar belakang alasan ilmiah, fenomena aktual, perumusan masalah, dan tujuan penelitian.
- **ID: PJK-007** (HAL 1, butir 7b) — **Kajian Literatur (15%):** kajian teori dan telaah hasil penelitian mutakhir yang relevan.
- **ID: PJK-008** (HAL 1, butir 7c) — **Metode (10%):** rancangan/model, populasi dan sampel, data, tempat/waktu, teknik pengumpulan, serta teknik analisis data.
- **ID: PJK-009** (HAL 1, butir 7d) — **Hasil dan Pembahasan (50%):** porsi terbesar artikel; wajib memuat interpretasi hasil, pembandingan dengan temuan terdahulu, nilai tambah, dan bukan sekadar memindahkan tabel angka.
- **ID: PJK-010** (HAL 1, butir 7e; HAL 4) — **Simpulan dan Saran (15%):** simpulan menjawab pertanyaan/tujuan penelitian; bukan rangkuman ulang, melainkan penegasan hasil temuan hakiki.

### D. Standar Pustaka Acuan (HAL 1, butir 7f; HAL 1, butir 8d)

- **ID: PJK-011** (HAL 1, butir 7f)
  - **Kaidah Kemutakhiran Pustaka:** Minimal berjumlah 10 (artikel penelitian) atau 25 (artikel konseptual); **80% wajib berasal dari sumber primer** (artikel jurnal, majalah ilmiah, disertasi, tesis) terbitan **10 tahun terakhir**.
  - **Verbatim:** *"Dari jumlah tersebut 80% berasal dari sumber primer yaitu artikel yang diterbitkan pada jurnal/majalah ilmiah, disertasi, dan tesis terbitan 10 tahun terakhir..."*

### E. Format Sitasi Turabian (HAL 2, butir 11)

- **ID: PJK-012** (HAL 2)
  - Penulis berulang di tahun sama dibedakan huruf: `1985a`, `1985b`.
  - Buku kumpulan artikel bereditor: bubuhkan `ed.` (satu editor) atau `eds.` (editor jamak).
  - Penulis lebih dari dua orang: pada daftar pustaka **tidak boleh disingkat et al. maupun dkk.**, seluruh nama penulis wajib dicantumkan lengkap.

---

## 3. Implikasi untuk Mesin Audit Kebahasaan & Modul Jurnal

1. **Aturan Panjang Judul:** Batas keras 14 kata — pemicu audit `jurnal/scripts/word_count_check.py`.
2. **Aturan Struktur Abstrak:** 1 paragraf, 150–200 kata, 0 sitasi, 0 akronim tanpa kepanjangan.
3. **Identitas Bebas Gelar:** Audit nama penulis mendeteksi dan menghapus gelar (*Dr., M.Si., Prof., Ph.D.*).
