# Humanizer ID

Panduan penyuntingan bahasa Indonesia akademik dan profesional untuk agen kecerdasan buatan dan platform LLM. Menghilangkan rasa kaku, membersihkan kalke terjemahan mesin, membenahi fragmentasi kalimat, dan menjaga integritas fakta ilmiah tanpa manipulasi detektor.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![CI](https://github.com/apissaj/humanizer-id/actions/workflows/ci.yml/badge.svg)](https://github.com/apissaj/humanizer-id/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/apissaj/humanizer-id)](https://github.com/apissaj/humanizer-id/releases)

---

## Mengapa Naskah AI Bahasa Indonesia Terasa Kaku?

Kekakuan tulisan AI bahasa Indonesia jarang disebabkan oleh kesalahan tata bahasa. Penyebab utamanya adalah:
1. **Nominalisasi menumpuk & verba ringan:** AI gemar menulis *“melakukan pengujian terhadap”* alih-alih *“menguji”*.
2. **Kalke (*Calque*) terjemahan mesin:** Model berpikir dalam bahasa Inggris lalu menerjemahkan klausa demi klausa (*“respecting boundaries”* diterjemahkan mentah menjadi *“menghormati batas”*).
3. **Penyangkalan antisipatif:** Pola khas AI seperti *“Meskipun X, bukan berarti Y...”* yang menyangkal hal yang tidak ditanyakan pembaca.
4. **Fragmentasi kalimat monoton:** Kalimat-kalimat pendek satu klausa yang berderet patah-patah (*staccato*).
5. **Monotoni pembuka antar-paragraf:** Konjungsi transisi mekanis berulang di awal tiap paragraf (*Selain itu,... Lebih lanjut,... Oleh karena itu,...*).
6. **Transisi kopong (ilusi keterhubungan):** Kata sambung kausalitas palsu (*"Dengan demikian, hal ini membuktikan..."*) tanpa premis data yang cukup.

---

## Sumber Data Resmi (Buku Teks & Pedoman Terdokumentasi)

Seluruh kaidah di dalam Humanizer ID **bukan karangan bebas** — setiap aturan ditelusuri dari dokumen resmi terbitan pemerintah dan pedoman akademik perguruan tinggi, lengkap dengan nomor halaman:

### Buku Teks Resmi Kemendikbudristek (Sumber Primer)
| Buku | Kontribusi Kaidah | Lokasi Ekstrak |
|---|---|---|
| *Cerdas Cergas Berbahasa dan Bersastra Indonesia* Kelas XI (Edisi Revisi, 2024, ISBN 978-634-00-0958-3) | Ragam bahasa karya ilmiah (denotatif, objektif, impersonal), sistematika karya ilmiah, contoh perbaikan kalimat efektif resmi (hlm. 210–215) | [references/ekstrak-buku-teks-kemdikbud.md](references/ekstrak-buku-teks-kemdikbud.md) |
| *Bahasa Indonesia untuk SMA/MA/SMK/MAK Kelas XII* (Edisi Revisi, 2024) | Lima ciri kalimat efektif (Sasangka, 2019), kaidah surat resmi (*agar menjadi*, *guna meningkatkan*), 9 kata tidak baku (hlm. 29–34) | [references/ekstrak-buku-teks-kemdikbud.md](references/ekstrak-buku-teks-kemdikbud.md) |
| *Bahasa Indonesia untuk Perguruan Tinggi* (Suyatno dkk., FITK UIN Jakarta) | Enam syarat keefektifan kalimat akademik (kesatuan ide, kepaduan/koherensi, keparalelan, ketepatan diksi, kehematan, kelogisan nalar) dan eliminasi frasa *namun demikian* (hlm. 100–107) | [references/buku-ajar-bahasa-indonesia-perguruan-tinggi.md](references/buku-ajar-bahasa-indonesia-perguruan-tinggi.md) |
| *Modul Keterampilan Berbahasa Indonesia untuk Perguruan Tinggi* (UNJA) | Tujuh ciri kalimat efektif, eliminasi konjungsi intrakalimat di awal kalimat (*sehingga, sedangkan*), pemangkasan superordinat pada hiponim (*warna merah*, *hari Selasa*), koreksi istilah populer *terkini* $\rightarrow$ *mutakhir*, larangan penjamakan ganda (*para dosen-dosen*) (hlm. 125–148) | [references/buku-modul-unja.md](references/buku-modul-unja.md) |
| *Bahasa Indonesia untuk Perguruan Tinggi* (Dr. Andi Halimah dkk., UIN Alauddin Makassar) | Enam pola padanan tidak serasi (*disebabkan karena*, *karena...maka*, *meskipun...tetapi*, *dan lain sebagainya*), peluluhan fonem /c/ (*menyuci* $\rightarrow$ *mencuci*), 9 bentuk penyengauan ragam lisan (*nulis* $\rightarrow$ *menulis*), teknik kutipan footnote/endnote/daftar pustaka, 5 ciri karya tulis ilmiah (hlm. 105–210) | [references/buku-ajar-uin-alauddin.md](references/buku-ajar-uin-alauddin.md) |
| *Bahasa Indonesia Untuk Perguruan Tinggi* (Dr. H. Ifnaldi, IAIN Curup) | Tujuh sifat ragam ilmiah (*cendekia, lugas, anti-fragmentaris, bertolak gagasan, formal-objektif, ringkas-padat, konsisten*), sistem perujukan note-bibliography vs parenthetical, tiga singkatan Latin catatan kaki (*ibid., op. cit., loc. cit.*), delapan bentuk plagiat (hlm. 22–30, 103–110) | [references/buku-ajar-iain-curup.md](references/buku-ajar-iain-curup.md) |

### Buku Bahasa & Linguistik Populer (Ivan Lanin)
- **Xenoglosofilia: Kenapa Harus Nginggris?** (Ivan Lanin, Kompas Gramedia, 2018) — telaah kritis kalke bahasa asing, pemadanan istilah berbasis kelaziman penutur.
- **Recehan Bahasa: Baku Tak Mesti Kaku** (Ivan Lanin, Mizan Qanita, 2020) — lima tingkatan ragam bahasa (beku, resmi, konsultatif, santai, akrab) dan prinsip keluwesan teks baku.

### Kajian Frekuensi Kosakata AI (Sains Internasional)
- **Kobak et al., *Science Advances* (2025, DOI: 10.1126/sciadv.adt3813)** — analisis korpus 15,1 juta abstrak PubMed membuktikan lonjakan kalke verba AI paling masif: *delve* (rasio kelebihan 28×), *underscore* (13,8×), *showcase* (10,7×). Di Indonesia, kata-kata ini mengalami alih-bahasa mentah menjadi penanda klise (*menyelami*, *menggarisbawahi berlebihan*, *hiruk pikuk*).

### Penyajian Data Visual, Teks Observasi, & Artikel Opini (Direktorat SMA Kemendikbud 2020)
- **Modul Pembelajaran SMA Bahasa Indonesia KD 3.1 & 4.1 (Teks Tanggapan Berbasis Visual/Tabel & Grafik):** Rujukan visual bernomor ilmiah (`TBG-001`), pembedaan grafik/bagan/diagram (`TBG-002`), konjungsi intrakalimat pertentangan komparasi data (`TBG-003`).
- **Modul Pembelajaran SMA Bahasa Indonesia KD 3.1 & 4.1 (Teks Laporan Hasil Observasi):** Definisi umum bebas pleonasme kopula-partitif (`LHO-001`), kolokasi taksonomi baku terbagi atas (`LHO-002`), eliminasi kontaminasi perincian dan lain sebagainya (`LHO-003`).
- **Modul Pembelajaran SMA Bahasa Indonesia KD 3.10 & 4.10 (Artikel Opini):** Modalitas probabilitas ilmiah vs spekulatif lisan (`OPN-002`), pemisahan klaim empiris vs prospektif (`OPN-003`), evidensialitas argumen rekomendasi normatif (`OPN-004`).

### Jurnal Ilmiah Kebahasaan Widyaparwa & Peristilahan Asesmen BSKAP 2022
- **Widyaparwa: Jurnal Ilmiah Kebahasaan dan Kesastraan Vol. 48 No. 1 (Balai Bahasa DIY, Juni 2020):** Pencegahan kebocoran pola tuturan lisan ke naskah ilmiah: pelesapan agen/kalimat buntung (`WDY-001`), inversi alur perhatian/distorsi subjek (`WDY-002`), ketaksaan enklitik indefinit -nya (`WDY-003`), penurunan transitivitas akibat pelesapan objek terdampak (`WDY-004`), eufemisme/slang santai (`WDY-005`), kalimat K-P-O tanpa subjek mandiri (`WDY-006`).
- **Panduan Pembelajaran dan Asesmen BSKAP Kemendikbudristek (2022):** 24 peristilahan resmi Kurikulum Merdeka (Capaian Pembelajaran, TP, ATP, KKTP, asesmen formatif/sumatif).

### Bahasa Pejabat Pemerintah & Surat Dinas (Badan Bahasa 2019 & Pusat Bahasa 1991)
- **Bahasa Indonesia untuk Pejabat Pemerintah** (Dadang Mullyana dkk., Badan Pengembangan dan Pembinaan Bahasa, 2019, 93 hlm.) — ekonomi bahasa verba nominal (*melakukan kunjungan → berkunjung*), pasif persona tersisip adverbia (*kami sudah laporkan* salah), nomina deverbal penderita verba pasif (*pelaksanaan ... dilaksanakan* salah), dan penghilangan preposisi perihal setelah verba transitif (*membahas tentang/mengenai*) → [references/bahasa-pejabat-pemerintah-2019.md](references/bahasa-pejabat-pemerintah-2019.md)
- **Pedoman Surat-Menyurat dalam Bahasa Indonesia** (Pusat Pembinaan dan Pengembangan Bahasa, 1991) — kaidah nalar frasa surat: *mengatasi ketinggalan* (bukan *mengejar*), kolokasi *isi surat* (bukan *bunyi surat*), konsistensi bilangan tingkat Romawi (*ke-45* atau *XLV*, bukan *ke-XLV*), dan paronim *berkenaan dengan* vs *berkenan* → [references/buku-surat-menyurat-pusat-bahasa.md](references/buku-surat-menyurat-pusat-bahasa.md)

### Bahasa Pewara (Badan Bahasa 2019)
- **Bahasa Indonesia untuk Pewara: Seri Penyuluhan Bahasa Indonesia** (Dwi Widayati Kurniawan, Maman Suryaman, dkk., Badan Pengembangan dan Pembinaan Bahasa, 2019, 119 hlm.) — kaidah naskah acara dan penyapaan formal: frasa pewara tidak bernalar (*Waktu dan tempat kami persilakan*), penyapa jabatan tanpa honorifik ganda (*Bapak Kepala Biro* salah; benar *Kepala Biro, Bapak X*), sapaan jamak non-ganda, dan verba baku pewara (*menaati, menyukseskan, mengoordinasikan, mengubah*) → [references/bahasa-indonesia-pewara-2019.md](references/bahasa-indonesia-pewara-2019.md)

### Paragraf & Kepaduan (Badan Bahasa 2019)
- **Paragraf: Seri Penyuluhan Bahasa Indonesia** (Drs. Suladi, M.Pd., Badan Pengembangan dan Pembinaan Bahasa, 2019, x+129 hlm.) — syarat paragraf yang baik (kesatuan, kepaduan, kelengkapan, keruntutan, konsistensi sudut pandang): referensi anaforis/kataforis yang berkoreferensi (pronomina persona/demonstratif wajib anteseden jelas), penomoran ordinal perincian yang runtut (*Pertama, Kedua, Ketiga* tanpa pengulangan), dan ketuntasan klasifikasi (bilangan pasti di kalimat topik = jumlah penjelas yang sama) → [references/paragraf-penyuluhan-suladi-2019.md](references/paragraf-penyuluhan-suladi-2019.md)

### Kalimat & Konjungsi (Badan Bahasa 2019)
- **Kalimat: Seri Penyuluhan Bahasa Indonesia** (Sry Satriya Tjatur Wisnu Sasangka, Badan Pengembangan dan Pembinaan Bahasa, 2019, x+107 hlm.) — kaidah struktur kalimat efektif: larangan korelatif *jika/kalau ... maka* (menghilangkan klausa utama), larangan menyisipkan preposisi pada objek verba transitif (*memerintahkan kepada X*), larangan menumpuk konjungsi pertentangan rangkap tiga (*walaupun + namun + maka*), serta ketaksaan penempatan adverbia *baru* → [references/kalimat-penyuluhan-sasangka-2019.md](references/kalimat-penyuluhan-sasangka-2019.md)

### Preposisi & Frase Berpreposisi (Pusat Bahasa 1992)
- **Preposisi dan Frase Berpreposisi** (Drs. S. Effendi dan Drs. Buha Aritonang, Pusat Pembinaan dan Pengembangan Bahasa, 1992, viii+74 hlm., ISBN 979-459-317-6) — kajian sintaktis-semantis preposisi Indonesia: titik waktu baku *pada tahun/hari/era* (bukan *di tahun/hari*), pleonasme *selain daripada*, dan penulisan preposisi ruang/arah wajib terpisah (*di dalam, ke atas, di bawah*) → [references/preposisi-dan-frase-berpreposisi-1992.md](references/preposisi-dan-frase-berpreposisi-1992.md)

### Istilah Linguistik (Pusat Bahasa 1978)
- **Daftar Istilah Linguistik Asing-Indonesia** (Harimurti Kridalaksana, Pusat Pembinaan dan Pengembangan Bahasa, 1978, xiv+59 hlm., ditelaah Amran Halim, A.M. Moeliono, J.S. Badudu dkk.) — prinsip pengistilahan resmi: penyederhanaan sinonim asing menjadi satu padanan, penolakan terjemahan harfiah (*atlas bahasa*, *keterampilan bahasa*), urutan unsur padanan (*predikat nominal*, *pinjam terjemah*), alih fonem klasik (*bahasa kentum*, *kenematika*), dan pemilahan makna proses vs hasil (*peminjaman* vs *pinjaman*) → [references/daftar-istilah-linguistik-kridalaksana-1978.md](references/daftar-istilah-linguistik-kridalaksana-1978.md)

### Bahasa Indonesia Perguruan Tinggi (UIN Jakarta 2017)
- **Bahasa Indonesia untuk Perguruan Tinggi: Membangun Karakter Mahasiswa melalui Bahasa** (Dr. Suyatno, M.Pd., Tri Pujiati, Didah Nurhamidah, Lutfi Syauki Faznur, Penerbit IN MEDIA, 2017, xii+150 hlm., ISBN 978-602-0969-90-9) — pasangan kata penghubung korelatif baku (*tidak ... tetapi ...* vs *bukan ... melainkan ...*), keparalelan bentuk imbuhan dalam perincian (*pembelian, pembuatan, pelabelan*), dan salah nalar pola frasa *bebas parkir → parkir gratis* → [references/bahasa-indonesia-pt-suyatno-2017.md](references/bahasa-indonesia-pt-suyatno-2017.md)

### Peristilahan (Badan Bahasa 2019)
- **Tata Istilah: Seri Penyuluhan Bahasa Indonesia** (Meity Taqdir Qodratillah, Badan Pengembangan dan Pembinaan Bahasa, 2019, xii+78 hlm.) — pemutakhiran Tata Istilah 1978 untuk era KBBI V: paradigma imbuhan *pemukiman/permukiman* dan *perubahan/pengubahan*, metanalisis palsu *-itas/-isasi* (*sinergitas, standarisasi*), penulisan gabungan bentuk bebas (*ibu kota, kerja sama*), peluluhan *peN-* baku (*penerjemah, perajin*), dan eufoni padanan (*efektif > mangkus*) → [references/tata-istilah-penyuluhan-2019.md](references/tata-istilah-penyuluhan-2019.md)

### Peristilahan (Pusat Bahasa 1978)
- **Tata Istilah Indonesia** (Adiwimarta, Kridalaksana, Moeliono dkk., Pusat Pembinaan dan Pengembangan Bahasa, 1978, iv+67 hlm.) — buku penyuluhan pelengkap PUPI: ejaan fonemik serapan (gugur konsonan akhir tak berfungsi), istilah yang dijauhkan (*zat lemas → nitrogen*), padanan awalan *non-* menurut makna (*tak-/bukan/nir-*), penolakan jamak Latin yang dihidupkan (*foki, laboratoria*), dan batasan akhiran keahlian *-wan* → [references/tata-istilah-indonesia-1978.md](references/tata-istilah-indonesia-1978.md)

- **Edisi 2019 (pemutakhiran):** kaidah diksi tambahan dari edisi pemutakhiran *Bentuk dan Pilihan Kata* (Mustakim, Badan Pengembangan Bahasa dan Perbukuan, 2019, x+95 hlm.): pembedaan *pukul* vs *jam* (titik waktu vs durasi), kopula definisi *adalah/ialah* alih-alih *yaitu/yakni*, *mantan* vs *bekas* untuk manusia vs benda, dan pemerinci tuntas (*yaitu/yakni*) vs parsial (*antara lain/misalnya*) sesuai bilangan → [references/bentuk-pilihan-kata-mustakim-2019.md](references/bentuk-pilihan-kata-mustakim-2019.md)

### Seri Penyuluhan: Bentuk dan Pilihan Kata (Badan Bahasa)
- **Bentuk dan Pilihan Kata** (Drs. Mustakim, M.Hum., Pusat Pembinaan Pemasyarakatan Bahasa, 2014, 110 hlm., ISBN 978-979-069-204-6) — tiga kriteria pemilihan kata (ketepatan, kecermatan, keserasian); kaidah anti-pleonasme pasangan sinonim, pembedaan *dll./dsb./dst.*, resiprokal ganda *saling + bentuk ulang*, keutuhan ungkapan idiomatis berpreposisi, dan pembatasan *daripada* khusus makna perbandingan → [references/buku-seri-penyuluhan-bentuk-pilihan-kata.md](references/buku-seri-penyuluhan-bentuk-pilihan-kata.md)

### Pedoman Ejaan & Tata Bahasa Resmi Pemerintah
- **EYD Edisi V** (Keputusan Kepala Badan Bahasa No. 0424/I/BS.00.01/2022) — peluluhan KTSP, bentuk terikat, partikel *pun* → [references/pedoman-kebahasaan-resmi.md](references/pedoman-kebahasaan-resmi.md)
- **TBBBI (Tata Bahasa Baku Bahasa Indonesia) Edisi IV** — kesejajaran predikat, kalimat efektif.
- **PUEBI Daring (Permendikbud 50/2015)** — gabungan kata konfiks (*menggarisbawahi*), bentuk ulang (*buku-buku*, bukan *buku2*), akronim nama diri → [references/](references/)
- **PASTI (Portal Pemadanan Istilah) Badan Bahasa Kemendikdasmen RI** (pasti.kemendikdasmen.go.id) — 172.931 istilah dari 59 ranah ilmu. Digunakan untuk membakukan padanan istilah teknologi (*machine learning* → **pemelajaran mesin**, *deep learning* → **pemelajaran mendalam**, *cloud computing* → **komputasi awan**, *data science* → **sains data**).

### Pedoman Penulisan Skripsi Perguruan Tinggi
- **Pedoman Tugas Akhir DIKE FMIPA UGM** — rujukan persamaan matematis bernomor: *“Berdasarkan Persamaan (3.1)...”*, pemisahan Simpulan vs Saran.
- **Pedoman Skripsi Universitas Indonesia (UI)** — kaidah sitasi dan format persamaan.

### Data Lexikon & Korpus (Komunitas Terbuka)
- Dataset distilasi EYD V (38 kategori aturan resmi), leksikon 238 kata baku↔nonbaku, glosarium istilah teknologi (115 entri) & hukum (25 entri).
- Statistik leksikon resmi KBBI: 112.538 entri (50.668 dasar + 26.835 turunan + 31.492 gabungan).

> Setiap entri di [`data/kalke-indonesia.json`](data/kalke-indonesia.json) yang bersumber dari buku mencantumkan rujukan halaman (contoh: *Buku Bahasa Indonesia Kelas XI Revisi 2024, hlm. 213*), sehingga bisa diverifikasi langsung ke dokumen aslinya.

## Perbandingan Sebelum & Sesudah

Berikut adalah contoh penyuntingan pada abstrak penelitian teknik (studi kasus lengkap tersedia di folder [**examples/**](examples/)):

| Draf Mentah AI / ChatGPT | Hasil Suntingan Humanizer ID |
|---|---|
| *Di era digital saat ini, optimasi basis data merupakan hal yang sangat krusial. Dalam penelitian ini melakukan analisis terhadap performa indeks B-Tree yang mengalami peningkatan kecepatan sebesar 35%. Meskipun cepat, bukan berarti indeks ini tanpa cela. Tulisan ini membahas bagaimana implementasi partisi tabel memberikan pengaruh terhadap throughput transaksi yang mana sangat penting untuk sistem.* | *Optimasi basis data menjadi penentu efisiensi sistem berskala besar. Penelitian ini menganalisis performa indeks B-Tree yang mencatatkan peningkatan kecepatan hingga 35%. Kendati demikian, karakteristik beban kerja tetap memunculkan tantangan komputasi tersendiri. Pada penelitian ini dibahas implementasi partisi tabel untuk meningkatkan throughput transaksi secara berkelanjutan.* |

---

## Lembar Sontekan (*Cheat Sheet*) Diksi & Kalke

Padanan cepat untuk membersihkan tulisan AI dan birokratis:

| Pola AI / Kaku | Bentuk Luwes & Lugas | Jenis Masalah |
|---|---|---|
| melakukan pengukuran terhadap | mengukur | Verba ringan |
| melakukan analisis terhadap | menganalisis | Verba ringan |
| memberikan pengaruh terhadap | memengaruhi | Verba ringan |
| mengalami peningkatan sebesar | meningkat / naik sebesar | Nominalisasi |
| menghormati batas sistem | selaras dengan batas sistem | Kalke (*respecting boundaries*) |
| menghapus limbah | meniadakan / meminimalkan limbah | Kalke (*eliminate waste*) |
| tidak datang tanpa harga | bukan tanpa konsekuensi / kendala | Kalke (*not without a price*) |
| Makalah ini membahas... | Pada makalah ini dibahas... | Personifikasi dokumen |
| ...yang mana sangat penting | ...yang penting / sehingga penting | Pronomina relatif salah |
| X, bukan berarti Y | Kendati X, tantangan Y tetap... | Penyangkalan antisipatif |

---

## Dukungan Preset Format Skripsi Kampus Indonesia

Humanizer ID mendukung konvensi dan pedoman tugas akhir/skripsi spesifik dari perguruan tinggi terkemuka di Indonesia (tersedia di [**`data/pedoman-kampus.json`**](data/pedoman-kampus.json) & panduan lengkap [**`references/panduan-preset-kampus.md`**](references/panduan-preset-kampus.md)):

| ID Kampus | Perguruan Tinggi | Sistem Sitasi Bawaan | Kaidah Khusus yang Diterapkan |
|---|---|---|---|
| `ui` | **Universitas Indonesia (UI)** | APA / IEEE | Abstrak dwibahasa presisi; penomoran tabel/gambar per bab (`Tabel 1.1`). |
| `itb` | **Institut Teknologi Bandung (ITB)** | IEEE / Harvard | Rujukan persamaan di dalam kurung `(1.1)`; sampul minimalis. |
| `ugm` | **Universitas Gadjah Mada (UGM)** | IEEE / APA | Format `Persamaan (nomor)`; pemisahan tegas bab Simpulan vs Saran. |
| `its` | **Institut Teknologi Sepuluh Nopember (ITS)** | IEEE | Tinjauan pustaka *state-of-the-art* 5 tahun terakhir; margin 3-2.5-3-2 cm. |
| `ipb` | **IPB University** | Name-Year | Sub-bab **tanpa titik di akhir** (`1.1 Latar Belakang`); indentasi paragraf 1 cm; nama ilmiah spesies miring berautoritas (*Oryza sativa* L.). |
| `undip` | **Universitas Diponegoro (UNDIP)** | IEEE / APA | Hierarki judul bab kapital tebal di tengah; kepatuhan pasif metodologi. |
| `unpad` | **Universitas Padjadjaran (UNPAD)** | APA / Chicago | Abstrak maksimal 250 kata dalam satu paragraf spasi tunggal. |
| `unair` | **Universitas Airlangga (UNAIR)** | Vancouver / APA | Pembedaan sitasi bernomor biomedis (Vancouver) vs sosial-humaniora (APA). |
| `ub` | **Universitas Brawijaya (UB)** | IEEE / APA | Larangan konjungsi di awal kalimat; paragraf minimal 2 kalimat efektif. |
| `telkom` | **Telkom University** | IEEE | Format naskah artikel IEEE; sitasi repositori GitHub & dataset publik. |
| `udinus` | **Universitas Dian Nuswantoro (UDINUS)** | IEEE / APA | Pengujian fungsionalitas *black-box* & pengujian pengguna pada rekayasa perangkat lunak; format kode monospace. |
| `uns` | **Universitas Sebelas Maret (UNS)** | APA / IEEE | Bab romawi, sub-bab desimal/alfanumerik, abstrak dwibahasa 200–250 kata. |
| `unnes` | **Universitas Negeri Semarang (UNNES)** | APA Style 7th | Desimal bertingkat tanpa titik akhir sub-bab; kutipan panjang (>40 kata) indent 1.2 cm spasi 1. |
| `upi` | **Universitas Pendidikan Indonesia (UPI)** | APA Style 7th | Pemisahan bab Analisis Data & Pembahasan dari Temuan; judul bab kapital di tengah tebal. |
| `unhas` | **Universitas Hasanuddin (UNHAS)** | Harvard / Vancouver / IEEE | Penomoran halaman bab di tengah bawah & lanjutan di kanan atas; wajib terjemahan kutipan asing. |
| `unand` | **Universitas Andalas (UNAND)** | APA / Harvard | Abstrak satu paragraf tunggal tanpa indent; rujukan persamaan bernomor di kanan `(1.1)`. |
| `jurnal-dikbud` | Jurnal Pendidikan & Kebudayaan Kemendikbud | 2.5 | 2.5 | 3.0 | 2.5 | Nama-tahun (Verdana 9, spasi 1) | Judul maks 14 kata, abstrak 150-200 kata tanpa acuan/singkatan, tanpa gelar, rujukan tahun a/b |
| `jurnal-jipp` | Jurnal Inovasi & Perekayasa Pendidikan (Balitbang Kemdiknas) | 3.0 | 3.0 | 3.5 | 3.0 | Alfabetis-Kronologis | Abstrak dwibahasa 100-150 kata, 5 kata kunci, proporsi 10-15-10-50-15, 15-20 hlm kuarto |

> **Cara Pakai:** Cukup sebutkan nama kampus Anda saat memberikan naskah, misalnya: *"Sunting abstrak skripsi ini dengan preset **ugm**"* atau *"Perbaiki Bab III metodologi dengan aturan **ipb**"*.

---

## Instalasi Paket Python (PyPI)

Mesin audit `humanizer-id` tersedia sebagai paket Python mandiri:

```bash
pip install humanizer-id
```

Setelah terpasang, gunakan lewat CLI:

```bash
# Audit naskah langsung
humanizer-id naskah.md

# Audit dengan preset domain spesifik
humanizer-id naskah.md --preset akademik
humanizer-id surat.md --preset dinas

# Jalankan teks demo bawaan
humanizer-id --demo
```

Atau sebagai modul Python:

```python
from humanizer_id.audit import load_default_data, audit_text

kalke, glos = load_default_data()
findings = audit_text("Naskah yang ingin diperiksa...", kalke, glos)
for f in findings:
    print(f["id"], "-", f["pola"])
```

---

## Cara Penggunaan

### 1. Salin Cepat untuk ChatGPT, Claude Web, & Gemini Gems
Jika Anda menggunakan antarmuka web (tanpa coding agent):
- Buka panduan siap pakai di [**PROMPT.md**](PROMPT.md).
- Salin teks instruksi ke kolom **Custom Instructions** (ChatGPT) atau **Project System Prompt** (Claude Projects).

### 2. Pemasangan pada AI Coding Agents

#### Hermes Agent
Simpan berkas `SKILL.md` ke folder skill Hermes Anda:
```bash
# Direktori skill aktif
mkdir -p ~/.hermes/skills/creative/humanizer-id
cp SKILL.md ~/.hermes/skills/creative/humanizer-id/
```

#### Claude Code
```bash
git clone https://github.com/apissaj/humanizer-id.git ~/.claude/skills/humanizer-id
```

#### Google Antigravity
```bash
# Global
git clone https://github.com/apissaj/humanizer-id.git ~/.gemini/config/skills/humanizer-id

# Per-Project Workspace
git clone https://github.com/apissaj/humanizer-id.git .agents/skills/humanizer-id
```

---

---

## Kamus Terbuka & Glosarium Lintas Bidang (`data/`)

Repositori ini menyediakan dataset terbuka berupa leksikon dan pola sintaksis terstruktur:
- [**`data/kalke-indonesia.json`**](data/kalke-indonesia.json): 314 entri leksikon kalke terjemahan mesin, verba ringan, pola antisipatif AI, dan kaidah morfologi peluluhan KTSP resmi EYD V.
- [**`data/glosarium-lintas-bidang.json`**](data/glosarium-lintas-bidang.json): 45+ padanan istilah baku dari berbagai kalangan profesional (Teknologi & Software, Hukum & Regulasi, Jurnalistik & Media Siber, serta Bisnis & Manajemen).

Panduan register dan gaya penulisan mendalam untuk tiap kalangan tersedia di dokumen [**`references/panduan-gaya-lintas-kalangan.md`**](references/panduan-gaya-lintas-kalangan.md).

---

## Alat Pemindai Mandiri (*CLI Auditor*)

Tersedia skrip audit cepat tanpa dependensi eksternal (100% pustaka standar Python) untuk memindai dokumen Markdown atau teks secara lokal:

```bash
# Uji coba dengan teks sampel demo
python scripts/audit.py --demo

# Pindai naskah skripsi atau artikel Anda
python scripts/audit.py path/ke/naskah.md

# Gunakan preset domain terfokus (akademik, dinas, jurnalistik, umum)
python scripts/audit.py naskah.md --preset akademik
python scripts/audit.py surat.md --preset dinas
python scripts/audit.py opini.md --preset jurnalistik
```
Skrip akan mencetak nomor baris, pola kalke atau verba ringan yang terdeteksi, saran perbaikan, dan catatan kaidah editorialnya secara seketika.

## Prinsip Integritas Ilmiah

- **Nol Fabrikasi Data:** Tidak menambahkan angka, parameter uji, atau sitasi baru yang tidak ada pada draf asli penulis demi membuat kalimat terkesan mendalam.
- **Safeguard Pasif Ilmiah:** Kalimat pasif pada bab Metodologi dan Hasil adalah konvensi resmi penulisan sains Indonesia dan tidak diubah secara agresif.
- **Zona Terlarang Disunting:** Dilarang mengubah instrumen penelitian tervalidasi (kuesioner/skala Likert), dokumen kontrak, dan paten hukum.
- **Bukan Alat Bypass Deteksi:** Panduan ini berfokus pada keterbacaan manusia. Kelancaran tata bahasa bukan jaminan skor pada alat deteksi AI statistik.


---

## 📚 Modul Jurnal Ilmiah Bereputasi (`jurnal/`)

Sub-skill khusus untuk menulis dan mengaudit naskah artikel jurnal bereputasi:
**Scopus Q1-Q4, Web of Science, SINTA 1-2, IEEE, Springer, Elsevier**. Modul ini
dipisah dari humanizer umum namun tetap memakai mesin audit dan dataset yang sama.

```
jurnal/
├── SKILL.md                       # prosedur 4 fase (pemetaan jurnal → drafting → audit → checklist)
├── checklist.md                   # 28 poin audit kualitas naskah
├── templates/
│   ├── abstract-template.md       # template abstrak 5 kalimat (150-250 kata)
│   ├── judul-template.md          # 3 formula judul, maksimal 14 kata
│   ├── cover-letter-template.md   # template surat pengantar submission
│   └── response-to-reviewer-template.md  # respons komentar reviewer
├── references/
│   ├── imrad-structure.md         # pedoman struktur IMRaD global
│   └── scopus-sinta-map.md        # peta strata Scopus/SINTA + red flags predator
├── scripts/
│   └── word_count_check.py        # pemeriksa batas kata per bagian
└── examples/
    └── sample-manuscript.md       # contoh naskah dummy yang lolos audit
```

### Cara Pakai Cepat
```bash
# 1. Audit kebahasaan naskah dengan preset jurnal
python scripts/audit.py <naskah.md> --kampus jurnal-dikbud

# 2. Cek batas kata per bagian
python jurnal/scripts/word_count_check.py <naskah.md>

# 3. Ikuti checklist.md sampai 28/28 ✅
```

### Prinsip Utama
1. Abstrak 150-250 kata tanpa sitasi dan akronim yang belum didefinisikan.
2. Judul maksimal 14 kata, spesifik, memuat kata kunci.
3. Nama penulis tanpa gelar/pangkat/jabatan (Pedoman Jurnal Dikbud).
4. Novelty dinyatakan eksplisit di akhir Introduction.
5. Semua kaidah kebahasaan humanizer-id (314 entri) berlaku juga di sini.

---

## Lisensi

Perangkat lunak dan panduan ini dilisensikan di bawah [Lisensi MIT](LICENSE) © 2026 Hafizh Muzani.
