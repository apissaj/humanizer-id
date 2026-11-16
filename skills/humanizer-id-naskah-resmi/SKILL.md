---
name: humanizer-id-naskah-resmi
description: Use when fixing naskah dinas, pewara & metadata jurnal.
version: 2.1.0
author: Hafizh Muzani / Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [writing, editing, bahasa-indonesia, akademik, nlp]
    category: creative
    homepage: https://github.com/apissaj/humanizer-id
    parent: humanizer-id
---

# Humanizer ID — Naskah Resmi

Sub-kaidah Humanizer ID. Muat berkas ini setelah `humanizer-id` (induk) menentukan mode kerja. Aturan integritas ilmiah pada induk tetap mengikat penuh.

---

### AK. Bahasa Pewara & Salam Resmi (Rujukan Kurniawan dkk., *Bahasa Indonesia untuk Pewara*, Badan Bahasa, 2019)

1. **Frasa Pewara Bernalar:** *Waktu dan tempat kami persilakan* salah nalar — yang dipersilakan orang, bukan waktu-tempat; perbaikan: *Panitia akan menyampaikan waktu dan tempat* (hlm. 10, 90).
2. **Penyapa Jabatan Tanpa Honorifik Ganda:** *Yang kami hormati Kepala Biro, Bapak X* — kata penyapa *Bapak/Ibu* hanya menyertai nama orang, bukan jabatan (*Bapak Kepala Biro* salah) (hlm. 11, 88).
3. **Sapaan Jamak Non-Ganda:** *Ibu-ibu / Bapak dan Ibu sekalian / hadirin* — *para, sekalian,* dan bentuk ulang tidak boleh digabung (hlm. 86–87; selaras `SPB-001`).

### AL. Bahasa Dinas & Surat Resmi (Rujukan Mullyana dkk., *Bahasa Indonesia untuk Pejabat Pemerintah*, Badan Bahasa 2019; *Pedoman Surat-Menyurat dalam Bahasa Indonesia*, Pusat Bahasa 1991)

1. **Ekonomi Verba:** *melakukan kunjungan → berkunjung; mengajukan saran → menyarankan; mengeluarkan pemberitahuan → memberitahukan* (Mullyana 2019, hlm. 37).
2. **Pasif Diri Tanpa Sisipan:** *sudah kami laporkan*, bukan *kami sudah laporkan* — pronomina diri dan verba pangkal tidak boleh dipisah adverbia (Mullyana 2019, hlm. 48).
3. **Nomina Deverbal Bernalar:** *Pelaksanaan tugas itu dimulai* — nomina tindakan (*pelaksanaan/perencanaan*) tidak sah menjadi penderita verba pasifnya sendiri (Mullyana 2019, hlm. 49).
4. **Verba Transitif Langsung ke Objek:** *membahas usulan* — *tentang/mengenai/daripada* setelah verba transitif mubazir (Mullyana 2019, hlm. 39).
5. **Nalar Frasa Surat:** *mengatasi ketinggalan* (bukan *mengejar ketinggalan*); *isi surat* (bukan *bunyi surat*) (Pusat Bahasa 1991, hlm. 35–36).
6. **Ordinal Satu Sistem:** *ke-45* atau *XLV* — awalan *ke-* dilarang menempel angka Romawi (Pusat Bahasa 1991, hlm. 34).
7. **Berkenaan vs Berkenan:** 'sehubungan dengan' = *berkenaan dengan*; *berkenan* khusus makna 'bersedia dengan hormat' (Pusat Bahasa 1991, hlm. 39).

---

### AQ. Pedoman Penerbitan Buku Ilmiah Nasional (Rujukan Author Guidelines Penerbit BRIN, BRIN Publishing, 2024)

1. **Klise Kerendahan Hati Palsu (BRN-001):** Kalimat pembuka/prakata *penulis menyadari bahwa buku ini masih jauh dari sempurna*, *masih memiliki banyak kekurangan*, *tak luput dari kekurangan* dilarang; gantikan dengan pernyataan batasan ruang lingkup (*work limitations*) objektif — mis. *Buku ini berfokus pada X dan tidak mencakup Y karena...* (Penerbit BRIN, Bagian Preface).
2. **Judul Subbab Generik (BRN-002):** Pada monograf ilmiah, subbab bertitel *Tinjauan Pustaka*, *Metodologi Penelitian*, *Rumusan Masalah*, *Hasil dan Pembahasan*, *Manfaat Penelitian*, atau *Landasan Teori* dilarang; gunakan frasa topik substantif yang mencerminkan isi kajian secara langsung (Penerbit BRIN, Bagian Text Matter).
3. **Hierarki Penomoran Monograf (BRN-003):** Penjenjangan baku: *Bab I* (Romawi) → *A.* (Kapital) → *1.* (Arab) → *a.* (Kecil); penomoran desimal tak berbatas bergaya laporan teknis (*2.1.3.4.1*) ditolak [telaah] (Penerbit BRIN, Bagian Chapters).
4. **Catatan Kaki Konten (BRN-004):** Catatan kaki/endnote dilarang dipakai semata-mata untuk sitasi; wajib memuat penjelasan substantif, atau sitasi dialihkan ke sistem pengarang-tahun (APA) dalam badan teks [telaah] (Penerbit BRIN, Bagian Chapters & Citations).

### AY. Konvensi Naskah Dinas Resmi (Rujukan "Bahasa Indonesia untuk Pejabat Pemerintah", Seri Penyuluhan Badan Bahasa, Bab II hlm. 48-50 & Bab III hlm. 71-76)

1. **Pembuka Verba Mentah (DIN-001):* Naskah dinas dilarang dibuka dengan verba mentah tanpa subjek (*Membalas/Merujuk/Menunjuk/Menindaklanjuti surat...*); gunakan *Sehubungan dengan/Berdasarkan/Berkenaan dengan surat...* atau kalimat lengkap S-P-O.
2. **Sisipan Adverbia pada Klitika (DIN-002):* Pasif berklitika menolak sisipan adverbia (*Masalah itu kami sudah laporkan*); posisi tepat sebelum objek (*sudah kami laporkan*) atau ubah ke aktif.
3. **Pronomina Orang Kedua (DIN-003):* Penutup surat menggunakan acuan langsung *Saudara/Bapak/Ibu*; *Atas perhatiannya* / *Harap maklum adanya* menyalahi konvensi komunikasi resmi.
4. **Konsesif Tunggal (DIN-004):* *Meskipun ... tetapi* adalah ganda konjungsi mubazir; pilih *Meskipun X, Y* atau *X, tetapi Y*.

### BB. Bahasa Surat-Menyurat Resmi (Rujukan "Surat-Menyurat dalam Bahasa Indonesia", Pusat Bahasa Depdikbud, Bagian D hlm. 28-38)

1. **Eliminasi 'Yang Mana' (SUR-001):* Bentuk *yang mana* dalam kalimat surat tidak diperlukan; hilangkan *yang mana* atau ganti dengan *yang*.
2. **Kalk 'Di Mana' Non-Penanya (SUR-002):* *Di mana* bukan kata sambung klausa; ganti *tempat* atau hilangkan.
3. **Penghilangan Kata 'Bunyi' Surat (SUR-003):* Surat tidak dapat berbunyi; *sesuai dengan bunyi surat...* diganti langsung *sesuai dengan surat...*.
4. **Distingsi 'Sangsi' vs 'Sanksi' (SUR-004):* *Sangsi* bermakna 'ragu-ragu'; *sanksi* bermakna 'tindakan penegakan hukum/hukuman' (*sanksi administratif*, bukan *sangsi*).

### BN. Ragam Baku Bahasa Surat Dinas & Komunikasi Resmi (Pusat Bahasa 1985)

1. **Interogatif Informal 'kenapa' (SRT-007):** Di dalam teks formal, laporan resmi, dan karya ilmiah, kata tanya kausatif baku adalah *mengapa*, bukan *kenapa* yang merupakan ragam percakapan santai (hlm. 55).
2. **Diksi Takbaku Kedaerahan 'haturkan' (SRT-008):** Ungkapan santun surat penutup resmi menggunakan *ucapkan terima kasih* atau *sampaikan terima kasih*; bentuk *haturkan terima kasih* atau *menghaturkan puji syukur* tidak baku dalam bahasa Indonesia resmi (hlm. 52).
