---
name: humanizer-id-wacana-retorika
description: Use when fixing kohesi paragraf & retorika naskah.
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

# Humanizer ID — Wacana Retorika

Sub-kaidah Humanizer ID. Muat berkas ini setelah `humanizer-id` (induk) menentukan mode kerja. Aturan integritas ilmiah pada induk tetap mengikat penuh.

---

### A. Eliminasi Monotoni Pembuka Antar-Paragraf (*Connector Addiction*)
AI memiliki kecenderungan adiktif menaruh kata penghubung mekanis di kata pertama setiap awal paragraf (*Selain itu,*, *Lebih lanjut,*, *Oleh karena itu,*, *Di sisi lain,*).
- **Aturan:** Maksimal satu konjungsi transisi di awal paragraf per halaman teks.
- **Solusi:** Buka paragraf baru dengan subjek tematis langsung, frasa nomina fokus, atau kalimat simpulan data terdahulu.

### B. Eliminasi Transisi Kopong & Ilusi Keterhubungan (*Illusory Cohesion*)
AI gemar menyisipkan kata sambung kausalitas (*“Dengan demikian, hal ini membuktikan bahwa...”*, *“Konsekuensinya, algoritma ini...”*) padahal kalimat sebelumnya belum memuat data premis yang cukup untuk menarik kesimpulan tersebut.
- **Aturan:** Evaluasi apakah kalimat sebelumnya benar-benar memuat premis pembukti. Bila bukti belum memadai, hapus transisi kausalitas tiruan dan tampilkan relasi sebagai hubungan koordinatif wajar.

### C. Penertiban Sudut Pandang Aktor (*Agent Drift Consistency*)
Cegah pergeseran pelaku tindakan yang bercampur baur dalam satu bab:
- **Salah:** *“Sistem dirancang oleh kami, lalu pengujian dilakukan oleh peneliti, dan laporan disusun oleh penulis.”*
- **Baku:** Tetapkan satu sudut pandang konsisten: pasif objektif murni (*“Sistem dirancang..., pengujian dilakukan..., dan laporan disusun...”*) atau konsisten menggunakan sebutan *peneliti*.

### D. Perajutan Sitasi Ilmiah Alami (*Citation Weaving*)
Hentikan pola kutipan nama berulang di awal kalimat (*“Menurut Pratama (2021)... Senada dengan itu, Wijaya (2022) menyatakan...”*):
- Fokuskan kalimat pada **sintesis temuan**, bukan nama penelitinya. Tempatkan nama dan tahun di kurung penutup:
  *“Peningkatan akurasi arsitektur berbasis atensi terbukti konsisten pada dataset teks informal (Pratama, 2021; Wijaya, 2022).”*
- Gabungkan rujukan yang memiliki kesimpulan seirama dalam satu kurung.

### E. Kalibrasi Derajat Kepastian Epistemik (*Epistemic Hedging*)
- **Fakta Empiris:** Gunakan verba deklaratif teruji: *menunjukkan, menghasilkan, membuktikan, mencatatkan*.
- **Inferensi & Korelasi:** Gunakan verba terukur: *mengindikasikan, berkorelasi dengan, mencerminkan*.
- **Hipotesis / Prakiraan:** Gunakan penanda probabilitas tunggal: *diduga, diproyeksikan, berpotensi*.
- **Larangan Tumpukan Hedging:** Dilarang menumpuk modalitas ganda dalam satu klausa (*“data ini mungkin berpotensi dapat diindikasikan bahwa...”* → *“data ini mengindikasikan bahwa...”*).

### F. Rujukan Tabel, Gambar, Persamaan Matematis, & Tipografi Teknis
- **Hindari Penunjuk Spasial Semu:**
  - Tabel & Gambar: Ubah *“tabel di bawah ini”* atau *“grafik di atas”* menjadi penunjuk bernomor ilmiah (*“Tabel 4.2”*, *“Gambar 3.1”*). Jangan merekayasa nomor bila belum tersedia.
  - Persamaan Matematis: Ganti rujukan informal *“rumus di atas”* atau *“persamaan berikut”* menjadi format baku: *“Berdasarkan Persamaan (3.1)...”* atau *“...sebagaimana dirumuskan pada Persamaan (2.4)”* (Pedoman Skripsi UGM & UI).
- **Tipografi Teknis:**
  - `monospace`: Perintah terminal (`npm run dev`), nama berkas (`config.json`), nama fungsi (`calculateStreaks()`), blok kode.
  - *Italic* (Cetak Miring): Istilah asing yang belum diserap resmi ke KBBI (*overfitting*, *zero-shot*, *loss function*).
  - Tegak: Istilah berpadanan baku (*basis data*, *tembolok*, *antarmuka*).

### O. Singkatan Latin Catatan Kaki & Sifat Ragam Ilmiah (Rujukan Buku Bahasa Indonesia IAIN Curup, 2021)

1. **Singkatan Latin wajib lengkap dengan titik dan dicetak miring:**
   - *Salah:* *“op cit 45”*, *“loc cit”*, *“ibidem halaman 23”*.
   - *Baku:* *“op. cit., hlm. 45”*; *“loc. cit., hlm. 12”*; *“ibid., hlm. 23”*.
   - *Ibid.* = karya sama dengan catatan sebelumnya; *Op. cit.* = karya yang pernah dikutip (tidak berurutan); *Loc. cit.* = halaman sama yang sudah dikutip.
2. **Tujuh sifat ragam ilmiah:** cendekia, lugas-jelas, anti-kalimat fragmentaris, bertolak dari gagasan (bukan penulis → didominasi kalimat pasif), formal-objektif, ringkas-padat, konsisten (istilah & tanda baca seragam sepanjang naskah).
3. **Nama pengarang:** di footnote urutan normal (nama diri → nama keluarga); di daftar pustaka dibalik (nama keluarga dulu). Nomor halaman wajib di footnote, opsional di daftar pustaka.

---

### P. Identitas Penulis Ilmiah & Singkatan Halaman (Rujukan Buku Siswa Kelas XI Kemendikbudristek, 2024)

1. **Nama penulis artikel ilmiah ditulis TANPA gelar akademik:** *“Dr. Ahmad Hidayat, M.Si.”* → *Baku:* *“Ahmad Hidayat”*.
2. **Nama belakang dilarang disingkat:** *“Ahmad H”* → *Baku:* *“Ahmad Hidayat”* — nama belakang menjadi kunci rujukan sitasi.
3. **Singkatan halaman baku:** `h.` untuk satu maupun banyak halaman (*h. 55–67*), bukan `hh.` (konvensi Indonesia tidak mengenal pluralisasi singkatan halaman).
4. **Ragam bahasa ilmiah tiga syarat:** objektif (berbasis data/fakta), reproduktif (makna pembaca = maksud penulis), denotatif murni (bebas konotasi/metafora).

---

### R. Kesatuan Ide Pokok & Pola Pengembangan Paragraf (Rujukan Buku Siswa Kelas XI Kemendikbudristek, 2024)

1. **Satu Paragraf Satu Ide Pokok:**
   - Setiap paragraf wajib memiliki satu kalimat topik (ide pokok) yang dikawal oleh kalimat-kalimat penjelas yang koheren.
   - Jangan mencampur dua topik berbeda (misal: membahas latensi model sekaligus membahas struktur dataset) dalam satu paragraf tunggal. Pecah menjadi dua paragraf tersendiri.
2. **Konsistensi Pola Deduksi / Induksi:**
   - **Deduksi (paling disukai ragam ilmiah):** Mulai dengan kalimat pernyataan umum/tesis di awal paragraf, kemudian diuraikan bukti empiris, metrik, atau elaborasinya di kalimat-kalimat berikutnya.
   - **Induksi:** Sajikan rentetan data pengujian/fakta terperinci, lalu akhiri dengan penarikan simpulan umum pada kalimat pamungkas paragraf.
   - Dilarang mencampuradukkan posisi kalimat topik secara acak yang membuat pembaca kebingungan menangkap gagasan sentral.

---

### U. Sindrom Akronim Redundan (RAS) & Keserasian Kohesi Wacana (Rujukan TBBBI Moeliono dkk. 1988/1998 & Haslinda-Thaba 2018)

1. **Larangan Sindrom RAS — Akronim Redundan:**
   - Unsur kepanjangan dalam akronim TIDAK boleh disebut ulang:
     - *nomor NIK* → *NIK* (N = Nomor)
     - *kartu KIP / kartu KTP* → *KIP / KTP* (K = Kartu)
     - *nomor PIN* → *PIN* (N = Number)
     - *virus HIV* → *HIV* (V = Virus)
     - *partai PPP / PDIP / PAN* → *PPP / PDI Perjuangan / PAN* (P = Partai)
     - *ATM card* → *kartu ATM* (M = Machine; 'card' redundan)
2. **Pronomina Anaforis Tunggal:**
   - Pronomina (*ia, dia, mereka, -nya*) wajib punya anteseden tunggal.
   - *Salah:* *"Ratna dan kawannya pergi karena ia harus mendaftar."* (taksa: siapa yang mendaftar?)
   - *Baku:* *"Ratna dan kawannya pergi karena Ratna harus mendaftar."*
3. **Urutan Hiponimi–Hipernim:**
   - Kata umum mencakup kata khusus, tidak boleh dibalik.
   - *Salah:* *"Jangankan membeli kursi, satu mebel pun kami tidak punya."*
   - *Baku:* *"Jangankan membeli aneka mebel, satu kursi pun kami tidak punya."*
4. **Pelesapan Subjek yang Sah:**
   - Subjek identik antarklausa dalam kalimat majemuk sebaiknya dilesapkan (elipsis); pengulangan subjek di setiap klausa melanggar asas ekonomi wacana (TBBBI, hlm. 330–333).

---

### AJ. Kepaduan & Keruntutan Paragraf (Rujukan Suladi, *Paragraf: Seri Penyuluhan Bahasa Indonesia*, Badan Bahasa, 2019)

1. **Arah Referensi & Koreferensi:** pronomina persona dan demonstratif (*itu, ini, ia, dia, -nya*) wajib memiliki anteseden anaforis yang jelas; hindari konstruksi kataforis rancu yang memunculkan pronomina sebelum maujud acuannya (hlm. 33–34).
2. **Keruntutan Ordinal:** penanda perincian berurutan wajib runtut dan konsisten (*Pertama, Kedua, Ketiga, Keempat*) — pengulangan (*Ketiga, Ketiga*) atau lompatan nomor merusak pernalaran paragraf (hlm. 55–56).
3. **Ketuntasan Klasifikasi:** jika kalimat topik memuat bilangan pasti (*tiga faktor*), kalimat penjelas wajib mengembangkan ketiga faktor secara lengkap tanpa meninggalkan sisa (hlm. 55).

### AM. Kaidah Penyajian Data Visual & Struktur Observasi (Rujukan Modul Pembelajaran SMA: Teks Tanggapan Tabel-Grafik & Laporan Hasil Observasi, Indri Anatya Permatasari, M.Pd., Direktorat SMA Kemendikbud 2020)

1. **Rujukan Visual Bernomor (TBG-001):** Deiksis spasial relatif (*grafik di atas, tabel di bawah ini, bagan berikut*) dilarang pada naskah ilmiah; wajib rujukan bernomor eksplisit (*Grafik 2, Tabel 4.1*) karena tata letak halaman dapat bergeser saat cetak/responsif (KD 3.1, hlm. 12-14).
2. **Terminologi Media Visual (TBG-002):** *grafik* untuk data numerik kuantitatif/fluktuasi deret waktu; *bagan* untuk hierarki/komponen struktural; *diagram* untuk prosedur/skema. Menyebut grafik batang sebagai "bagan batang" adalah kerancuan terminologi (KD 3.1, hlm. 9-11).
3. **Konjungsi Pertentangan Komparasi Data (TBG-003):** *Sedangkan* adalah konjungsi intrakalimat — dilarang membuka kalimat mandiri; ganti *Sementara itu, / Di sisi lain,* atau gabung klausa dengan koma (KD 3.1, hlm. 16-17; Alwi dkk. 2017).
4. **Definisi Umum LHO (LHO-001):** Dilarang menumpuk kopula + partitif + verba inklusi (*merupakan salah satu termasuk*); pilih satu konstruksi definisi lugas (KD 3.1/4.1, hlm. 27).
5. **Kolokasi Taksonomi (LHO-002):** *terbagi atas ...* (bukan *terbagi dari/dalam*); *dibagi menjadi ...* (KD 3.1/4.1, hlm. 24-25).
6. **Penutup Perincian (LHO-003):** Kontaminasi *dan lain sebagainya* dilarang — pilih *dan lain-lain* (rincian heterogen) atau *dan sebagainya* (rincian homogen) (KD 3.1/4.1, hlm. 28).

### AN. Ragam Opini Epistemik & Pencegahan Interferensi Tuturan Lisan (Rujukan Modul Pembelajaran SMA Artikel Opini KD 3.10, Direktorat SMA Kemendikbud 2020; Widyaparwa Vol. 48 No. 1, Balai Bahasa DIY 2020)

1. **Modalitas Spekulatif Lisan (OPN-002):** *bisa jadi, sepertinya, kayaknya* dilarang di teks formal; ganti *diduga, berpotensi, diindikasikan* (KD 3.10, hlm. 12).
2. **Fakta vs Proyeksi (OPN-003):** Pisahkan klausa verifikasi empiris (*terbukti mereduksi 4,2%*) dari proyeksi masa depan (*diproyeksikan dalam penelitian lanjutan*) — klaim "eksperimen membuktikan X akan mengeliminasi seluruh Y" rancu epistemik [telaah] (KD 3.10, hlm. 12-14).
3. **Opini Berevidensial (OPN-004):** Anjuran normatif (*seharusnya*) wajib disertai klausa evidensial berbasis regulasi/parameter/buji data; opini tanpa bukti adalah opini subjektif mentah [telaah] (KD 3.10, hlm. 16-18).
4. **Pelesapan Agen (WDY-001):** Kalimat ilmiah dilarang diawali langsung verba aktif transitif tanpa subjek (*Menghitung indeks bias...*); hadirkan subjek (*Peneliti menghitung...*) atau pasif (*dihitung...*) — 50% tuturan lisan mengalami agent deletion, ragam tulis tidak mentolerir (Kirana, hlm. 20-21, 25-26).
5. **Hierarki Topik (WDY-002):** Dilarang memajukan objek inanimat sebagai subjek semu lalu mengulang agen dengan pronomina (*Laporan ini bendahara telah menyelesaikannya*); selaraskan agen-subjek atau gunakan pasif baku [telaah] (Kirana, hlm. 20-21; Givon 1976; DeLancey 1981).
6. **Enklitik Indefinit (WDY-003):** *Katanya...* / *hasilnya menunjukkan...* tanpa anteseden eksplisit ditolak; ganti *Menurut Hidayat dkk. (2019)...* / *hasil pengujian menunjukkan...* (Kirana, hlm. 22-23).
7. **Transitivitas Tuntas (WDY-004):** Verba transitif tidak boleh menggantung tanpa objek penderita (*langkah berikutnya adalah memurnikan.*); lengkapi argumen objek (*memurnikan filtrat hasil maserasi*) [telaah] (Kirana, hlm. 24-26; Hopper & Thompson 1980).
8. **Leksikon Denotatif Formal (WDY-005):** Slang eufemistis tuturan (*kurang mantap, cukup oke, nge-blend*) dilarang di register ilmiah; ganti *kurang memadai, efektif, terintegrasi* (Permita, hlm. 41-48).
9. **Struktur K-P-O (WDY-006):** Kalimat diawali keterangan temporal/spasial lalu langsung verba tanpa subjek (*Pada saat melakukan pengambilan sampel darah di puskesmas menemukan...*) cacat struktur; sisipkan koma lalu subjek eksplisit (*...di puskesmas, petugas medis menemukan...*) (Kirana, hlm. 21).

### AP. Sindrom Akronim Redundantan, Kohesi Teks, Konversi Monograf, dan Peristilahan Ruang Publik (Rujukan Haslinda & Thaba 2018; Maharani/UI; Istiqomah 2020; Putusan Kongres Bahasa Indonesia VII 1998; Glosarium Linguistik 2002)

1. **Akronim-Toponimi Redundan (RAS-005):** Nama wilayah sudah terkandung dalam akronim (*M*akassar pada PSM, *Ja*karta pada Persija); tulis *Persija melawan PSM*, bukan *Persija Jakarta melawan PSM Makassar* (Haslinda & Thaba, hlm. 4-5).
2. **Akronim-Spesifikator Redundan (RAS-006..009):** Kata penjelas sudah termuat dalam akronim: *sistem SI*, *nomor ISBN/ISSN/NPWP*, *dosen DPA*, *kode QR code*, *monitor LCD display*, *mesin ATM machine* — gugurkan spesifikator duplikat (Haslinda & Thaba, hlm. 3-6).
3. **Konjungsi "Maka" Awal Kalimat (KOH-003):** *Maka* adalah konjungsi konsekuensi intrakalimat; dilarang membuka kalimat mandiri tanpa klausa syarat (*Jika X, maka Y*), ganti *Oleh karena itu* (Maharani, hlm. 17).
4. **Penomoran Subbab Monograf (MBI-002):** Penomoran desimal bertingkat dilarang melebihi tiga tingkat (*2.1.1.1*); gunakan judul bermakna atau tiga tingkat penuh (Istiqomah, hlm. 11).
5. **Judul Bebas Latar Administratif (MBI-003):** Judul buku ilmiah dilarang memuat seting administratif (*di SMA Negeri 1 Batu Tahun Ajaran 2011/2012*); lokasi dan tahun penelitian cukup pada bagian metodologi (Istiqomah, hlm. 10, 13).
6. **Eufemisme Birokratis (KBI-001):** Penutupan fakta negatif dengan pembalut halus (*penyesuaian tarif* = kenaikan harga; *mengamankan* = menangkap/menahan; *dirumahkan* = PHK) ditolak dalam ragam resmi; nyatakan kenyataannya lugas (Putusan Kongres VII, hlm. 6, Bagian Khusus B.2).
7. **Istilah Asing Mentah Ruang Publik (KBI-002):** *booking room, grand opening, meeting room, launching* di dokumen resmi digantikan padanannya: *ruang pemesanan, pembukaan resmi, ruang rapat, peluncuran* (Putusan Kongres VII, hlm. 3, Bagian Khusus A.a.2).
8. **Katakresis Paronim (GLS-002):** *Mengacuhkan* bukan *mengabaikan* (*mengacuhkan* = tidak menggubris dengan sengaja vs *mengabaikan* = tidak memedulikan); *absensi* bukan *kehadiran* melainkan daftar ketidakhadiran; *tidak bergeming* bukan berarti diam total (Lapoliwa & Nureni, hlm. 51).
9. **Tautologi Kehematan (GLS-004):** Gugurkan kelewahan tautologis: *sangat mutlak*, *kondisi prasyarat awal*, *saling tolong-menolong satu sama lain* → *mutlak*, *prasyarat*, *saling tolong-menolong* (Lapoliwa & Nureni, hlm. 50, 71).

### AP-Amandemen. Kolokasi Metaforis, Ragam Santai Naskah Resmi, dan Anonimisasi Subjek Penelitian

1. **Kolokasi Verba-Nomina Metaforis (GLS-003):** Pasangan verba-nomina wajib patuh kolokasi leksikal baku; *melahirkan* hanya untuk makhluk hidup (*melahirkan solusi* → *menghasilkan solusi*), *menghidangkan* untuk sajian konsumsi (*menghidangkan musik* → *menyajikan musik*), *mencanangkan* untuk program resmi (*mencanangkan pemecahan* → *merumuskan pemecahan*) (Lapoliwa & Nureni, hlm. 17).
2. **Leksikon Percakapan di Naskah Resmi (KBI-004):** Partikel dan verba ragam santai (*banget, bikin bingung, kok, sih*) dilarang pada buku teks dan naskah dinas; ganti *sangat/membingungkan*, hapus partikel (Putusan Kongres VII, hlm. 5-6, Bagian Khusus A.f.2 & B.4) [aspek kontekstual dinilai manual: *telaah* untuk pemakaian figuratif].
3. **Anonimisasi Subjek Penelitian (MBI-004):** Data identitas responden (*NIK, NIP, nomor KTP*) wajib disamarkan dengan inisial atau kode responden (*narasumber AD*); digit identitas pribadi mentah dalam naskah melanggar etika penelitian (Istiqomah, hlm. 5) [penilaian konteks naskah: *telaah* untuk kasus non-digit].
4. **Rancu Taksonomi Meronimi-Hiponimi (KOH-005):** Relasi "bagian dari" (*piston, busi* terhadap *mesin*) tidak boleh disebut "jenis" (*tiga jenis mesin*); gunakan *komponen/bagian* untuk meronimi dan *jenis* hanya untuk hiponimi (Maharani, hlm. 8-9, 14) [*telaah*].
5. **Pulau Anaforis (GLS-001):** Pronomina (*-nya, ini*) tidak boleh menggantikan nomina turunan utuh (*aromanya* untuk *aroma kopi* berbatas pulau anaforis); ulangi nomina lengkap atau bentuk padanannya (Lapoliwa & Nureni, hlm. 14) [*telaah*].
6. **Leksikon Sensasional Naskah Resmi (KBI-003):** Ungkapan berkonotasi vulgar atau sensasional untuk memicu viralitas dilarang dalam publikasi dinas; gunakan gaya lugas berbasis data (Putusan Kongres VII, hlm. 6, Bagian Khusus B.8) [*telaah*].

### BI. Koherensi & Kesatuan Paragraf (Seri Penyuluhan Paragraf, Suladi 2015)

1. **Koma Konjungsi Penumpu Simpulan (PRG-001):** Konjungsi penumpu simpulan yang berfungsi sebagai konjungsi antarkalimat wajib diikuti koma: *Akhirnya,* / *Akibatnya,* / *Oleh karena itu,* / *Maka dari itu,* / *Dengan demikian,* / *Berdasarkan uraian di atas,* (Suladi, 2015, hlm. 55).
2. **Kesatuan Paragraf & Kalimat Sumbang (PRG-002) `[telaah]`:** Tiap paragraf hanya boleh memuat satu gagasan utama; pisahkan topik baru ke paragraf terpisah dan hapus kalimat yang menyimpang dari kalimat topik (hlm. 13-14).

### BJ. Ragam Baku Bahasa Ilmiah Perguruan Tinggi (Kuntarto UNJA & Suyatno UIN Jakarta)

1. **Posesif Kalke Asing 'dari' (UIN-007):** Pola kepemilikan bahasa Indonesia langsung (*kesimpulan penelitian, tujuan program, anak Pak Lurah*), bukan lewat *dari* (*kesimpulan dari penelitian*) yang merupakan kalke struktur asing *van/of* (UNJA hlm. 98).
2. **Verba Benefaktif Akhiran -kan + 'untuk' (UIN-008):** Sufiks *-kan* sudah mengandung arti 'melakukan untuk orang lain'; dilarang menambahkan kata *untuk* di depan penyerta: *membelikan adik baju* (bukan *membelikan untuk adik baju*) (UNJA hlm. 108).

### BV. Kaidah Editorial Taktis Menyunting & Preskripsi Terbitan Ilmiah (Rujukan Bambang Trim Penerbit BRIN 2023 & Winarti dkk. Kantor Bahasa Kaltim 2005)
1. **Preservasi Makna Kata Spesifik (Penerbit BRIN):**
   - *acuh* bermakna peduli (jangan gunakan *acuh* untuk arti cuek tanpa kata ingkar *tidak*; gunakan *tidak acuh*).
   - *bergeming* bermakna diam/kukuh/tidak bergerak (jangan gunakan *bergeming* untuk arti goyah tanpa ingkar; gunakan *tidak bergeming*).
   - *senonoh* bermakna patut/sopan (larang pemakaian *senonoh* dalam arti asusila tanpa kata ingkar; gunakan *tidak senonoh*).
   - *tukas* bermakna menuduh (larang penggunaan *tukasnya* sebagai varian pewarta kata netral; gunakan *ujarnya* atau *tegasnya*).
2. **Diferensiasi Nomina Relasional & Waktu (Penerbit BRIN):**
   - Pembedaan *langganan* (pihak penyedia/toko) vs *pelanggan* (konsumen pembeli).
   - Pembedaan *jam* (rentang durasi, mis. *selama dua jam*) vs *pukul* (titik saat spesifik, mis. *pukul 14.00 WIB*).
   - Pembedaan *tiap-tiap* (posisi awal anteseden nomina) vs *masing-masing* (distributif posisi akhir).
   - Pembedaan *pemelajar* (orang yang belajar/siswa/mahasiswa) vs *pembelajar* (pengajar/instruktur yang membelajarkan).
   - Pembedaan *permukiman* (kawasan tempat tinggal) vs *pemukiman* (proses memukimkan).
   - Pembedaan *persebaran* (kondisi/peta tersebarnya objek) vs *penyebaran* (tindakan aktif menyebarkan).
3. **Pembersihan Pleonasme Leksikal Ekstrem & Kontaminasi Partitif (Penerbit BRIN):**
   - Larang *sangat sempurna sekali* / *luar biasa sempurna* (cukup *sempurna*).
   - Larang *kurang lebih sekitar* (pilih: *kurang lebih* atau *sekitar*).
   - Larang *semata-mata hanya* (pilih: *semata-mata* atau *hanya*).
   - Larang *misteri rahasia* (pilih: *misteri* atau *rahasia*).
   - Larang kontaminasi partitif dan enumeratif terbuka: frasa pembuka *seperti / di antaranya / misalnya* dilarang diakhiri dengan *dan lain-lain / dan sebagainya*.
4. **Kaidah Sintaksis & Pembentukan Kata Ilmiah (Kantor Bahasa Kaltim):**
   - Larang pleonasme kuantor jamak pada kata ulang: *semua lahan-lahan* / *semua faktor-faktor* -> pilih *semua lahan* atau *lahan-lahan*.
   - Pasangan preposisi rentang waktu preskriptif: bentuk *mulai Maret sampai Mei* tidak baku; gunakan *dari Maret sampai Mei*, *sejak Maret hingga Mei*, atau *mulai Maret hingga Mei*.
   - Pembentukan pasif berawalan *di-* wajib mempertahankan sufiks *-kan*: *memprioritaskan* -> pasif baku *diprioritaskan* (bukan *diprioritas*).
   - Penghilangan preposisi pemblokir subjek pada komplemen *bahwa*: kalimat *menunjukkan bahwa pada persentase N sangat rendah* wajib disunting menjadi *menunjukkan bahwa persentase N sangat rendah*.
   - Larangan tanda koma sebelum konjungsi komplementer *bahwa*: pola *menyatakan, bahwa* / *menemukan, bahwa* wajib ditertibkan menjadi *menyatakan bahwa* tanpa tanda koma.
