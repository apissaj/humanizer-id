# Changelog

Semua perubahan penting pada proyek ini dicatat di berkas ini. Format mengikuti [Keep a Changelog](https://keepachangelog.com/id/1.1.0/) dan versi mengikuti [SemVer](https://semver.org/lang/id/).

## [Belum dirilis]

### 688 kaidah + 150 istilah glosarium

Bedah menyeluruh lima rujukan resmi (Siklus 20–22):

- **EYD Edisi V (SK Kepala Badan Bahasa No. 0424/I/BS.00.01/2022) & Seri Penyuluhan Ejaan v2** (`books/eyd_edisi_5_2022.pdf`, `books/seri_penyuluhan_ejaan_badanbahasa_v2.pdf`):
  - `EYD-065`..`EYD-068` — gabungan kata padu (`darmabakti`, `sukarela`, `saputangan`, `belasungkawa`, `manasuka`, `adakalanya`), gabungan kata bebas/berimbuhan sepihak (`tanda mata`, `kaki tangan`, `kaki lima`, `orang tua`, `berpesta pora`, `kerja baktikan`), gabungan kata berkonfiks penuh (`menyamaratakan`, `menganaktirikan`, `mengambinghitamkan`, `ketidaktahuan`, `keputusasaan`), serta bentuk terikat (`Yang Maha Kuasa`, `ekabahasa`, `nirgagasan`, `antar jemput`).
  - `BAK-012` disempurnakan agar kata dasar `antar` bermakna 'bawa/kirim' (*antar jemput*, *antar barang*) tidak tertandai keliru.
  - `EYD-069`..`EYD-070` — singkatan surat-menyurat bergaris miring (`a/n`, `u/p`, `u/b`, `d/a`), format `Rp` bertitik/berspasi, tanda titik setelah perincian berkurung `(a).`, tanda baca akhir ganda `?.`/`!.`, serta skor pertandingan bertitik dua (`skor 3:1` -> `skor 3-1`).
  - `EYD-071`..`EYD-072` — unsur serapan EYD V Bab IV (asing: `akomodasi`, `aksesori`, `konsekuen`, `ekuivalen`, `suvenir`, `deskripsi`, `stereo`, `espreso`, `tenteram`; Arab: `tafakur`, `umat`, `kafah`, `tamat`, `nasihat`, `hakikat`, `makhluk`, `sahih`, `uzur`, `zalim`, `pikir`, `napas`, `faedah`).
  - `EYD-073` (`[telaah]`) — huruf miring istilah asing/daerah, huruf tebal penegas, dan tanda pisah (`—`) untuk rentang.
- **Winarti dkk. (2009), Subbab 2.3.3–2.11** (Jurnal Ekonomi Pertanian, Mahakam, Didaktika, Dedikasi, Prediksi, Sosial Politik, Forum Ekonomi, Dinamika Ilmu, Poltanesa, hlm. 38–137):
  - `TMS-043`..`TMS-046` — peluluhan KTSP (`mengursuskan`, `menyukseskan`, `menyejahterakan`, `memercayai`, `ditelurkannya`), serapan ilmiah (`mendiskreditkan`, `sekretaris`, `seyogianya`, `praktik`, `ditoleransi`, `konferensi`), gabungan kata (`tenaga kerja`, `semipermeabel`, `menitikberatkan`), kerancuan diksi (`mengacu pada`, `hidup-hidup`, `membahas`, `di samping itu`, `pada/antara tahun`), serta perluasan `TMS-038` untuk `sejak ... sampai`.
- **Buku Praktis Bahasa Indonesia 2 (Bahasa, Istilah, Kalimat), Sasangka (2015) Kalimat, & Suladi (2015) Paragraf**:
  - `BPBI-008`..`BPBI-009` — ungkapan `Dirgahayu RI` / `HUT ke-N RI` / `WIB` (bukan `BBWI`) serta konjungsi `agar/supaya` (bukan `bahwa`) sesudah verba harapan/anjuran (`menganjurkan`, `mengharapkan`, `mengimbau`, `memohon`).
  - `SPK-014`..`SPK-016` — kerancuan `Menurut pada X` & preposisi objek verba transitif (`mengamanatkan kepada`, `menyimpulkan tentang`), koma sesudah penghubung antarkalimat (`Oleh sebab itu,`, `Meskipun demikian,`, `Walaupun demikian,`, `Sehubungan dengan itu,`, `Berkaitan dengan hal itu,`), dan `[telaah]` kalimat partisipial awal verba (Sasangka 2015, hlm. 88–96).
  - Glosarium lintas bidang bertambah 13 padanan resmi Pusat Bahasa (137 -> 150 istilah).

Referensi baru: `references/eyd-v-2022-lengkap.md`, `references/seri-penyuluhan-ejaan-v2-badan-bahasa.md`, `references/kaltim-2009-jurnal-mahakam-sospol-ekonomi.md`, `references/bpbi-2-bahasa-istilah-kalimat.md`, dan `references/kalimat-efektif-sasangka-2015.md`; sub-skill `skills/humanizer-id-ejaan-morfologi/SKILL.md`, `skills/humanizer-id-sintaksis/SKILL.md`, `skills/humanizer-id-diksi-istilah/SKILL.md`, dan tabel rute `SKILL.md` diperbarui.

### 670 kaidah

Bedah lanjut Winarti dkk. (2009): subbab 2.1.3-2.1.4 Jurnal Budidaya Pertanian (hlm. 14-23)
dan 2.3.1-2.3.2 Jurnal Ekonomi Pertanian dan Pembangunan (hlm. 32-37).

- `TMS-042` - `teoritis` -> `teoretis` (penyerapan langsung dari *theoretical*, bukan
  teori + -tis) dan `sekedar` -> `sekadar` (kadar + se-).
- `SPK-012` - subjek didahului penghubung `bahwa` setelah keterangan `Menurut X,`:
  `Menurut Kim H. Tan (1991), bahwa Al ...` -> penghubung dihilangkan.
- `SPK-013` - frasa keterangan mengambil posisi subjek: `Berdasarkan hasil penelitian
  menunjukkan bahwa ...` -> `Hasil penelitian menunjukkan bahwa ...`. Varian berkoma tetap
  lolos karena frasa keterangan diikuti subjek sah.
- `SPK-001` diperluas: daftar konjungsi syarat `jika|kalau|apabila` ditambah `bila`, mengikuti
  contoh `bila melapuk maka tidak bisa diserap` pada hlm. 14. Kalimat `Pengujian dilakukan bila
  cuaca mendukung.` tetap bersih.

Sembilan bentuk lain pada bab yang sama sudah tertangkap mesin lama (`KK-001`, `TMS-001`,
`BPK-032`, `BAK-011`, `BAK-001`, `KK-003`, `BAK-005`, `TBB-004`, `TMS-029`). Kasus yang
menuntut analisis fungsi sintaksis - subjek berkata depan `Pada ...`, redundans
`pemanfaatan ... dimanfaatkan`, dan `memiliki/mempunyai` - dicatat `[telaah]` tanpa pola.

Referensi baru: `references/kaltim-2009-penyusunan-kalimat-dan-ekonomi.md`.

Verifikasi: `work/test_tms42_spk012_013.py` 18/18, `uv run pytest -q` 45 passed, uji nol
positif palsu tetap 0.

### 667 kaidah

Bedah lanjut Winarti dkk. (2009) subbab 2.2.1-2.2.3, Jurnal Agrifor (hlm. 24-32):

- `TMS-039` - serapan dan turunannya: `memposisikan` -> `memosisikan`, `marjinal` ->
  `marginal`, `hektar` -> `hektare`.
- `TMS-040` - nomina `hasil` hanya dapat menerima konfiks: `menghasil` -> `menghasilkan`.
  Pasangan `diprioritas` pada halaman yang sama sudah dijaga `KK-004`, sehingga tidak
  diduplikasi.
- `TMS-041` - `respon` -> `respons`; regex `respon` tanpa `\w*` di awal agar
  `responden` tidak tertandai.

Kaidah buku yang sudah tertangkap mesin lama: `dirubah` (`BAK-002`/`BPK-019`), `tehnik`
(`BPK-030`), `dianalisa` (`BAK-005`), `mempengaruhi` (`BAK-001`), `terdiri dari`
(`TBB-004`), dan pembanding `lebih ... dari` (`TMS-029`).

Empat kasus penyusunan kalimat sengaja tidak dipola dan dicatat `[telaah]`: kesejajaran
deret perincian, subjek preposisional `Oleh X + predikat aktif`, subjek berkata depan, dan
verba kedua tanpa penghubung.

Referensi baru: `references/kaltim-2009-terbitan-ilmiah-kalimat-jurnal-agrifor.md`.

Verifikasi: `work/test_tms39_41.py` 15/15, `uv run pytest -q` 45 passed, uji nol positif
palsu tetap 0.

### 664 kaidah

Bedah pindah ke Winarti dkk. (2009), *Kesalahan Berbahasa Indonesia dalam Terbitan Ilmiah
Perguruan Tinggi di Kalimantan Timur*, subbab 2.1.1-2.1.2 (hlm. 7-14):

- `TMS-037` - perangkapan verba, penyerapan keliru, dan preposisi serangkai:
  `menstimulir` -> `menstimulasi`, `panili` -> `vanili`, `disekitar`/`diareal`/`diladang`
  ditulis terpisah. `mensuplai`, `dianalisa`, dan `produktifitas` tidak dibuat kaidah baru
  karena sudah tertangkap `BDD-006`, `BAK-005`, dan `BPK-027`.
- `TMS-038` - preposisi gabungan tidak lengkap: `mulai Maret sampai Mei` dan
  `dari Senin sampai Kamis` -> `sampai dengan`. Regex memakai huruf kapital nama bulan atau
  angka sebagai penanda rentang waktu agar kalimat seperti "mulai naik setelah remedial
  sampai tuntas" tidak tertandai; versi pertama dengan `(?i)` gagal kasus negatif itu dan
  dipersempit.

Referensi baru: `references/kaltim-2009-terbitan-ilmiah-pembentukan-kata.md` (kutipan
verbatim hlm. 7-14 + penanda `[OCR]` + penjelasan penyerempitan regex).

Verifikasi: `work/test_tms37_38.py` 19/19, `uv run pytest -q` 45 passed, uji nol positif
palsu tetap 0.

### 662 kaidah

Bedah dilanjutkan ke Mustakim (2019), subbab 3.1.3 keserasian kata (hlm. 60-68):

- `TMS-035` - verba tanpa awalan ber- sebagai predikat ragam resmi: `sudah kumpul`,
  `telah kumpul`, `sampai jumpa` -> `berkumpul`, `berjumpa` (hlm. 62).
- `TMS-036` - bentuk tidak baku dari tabel baku-tidak baku hlm. 67-68 yang belum tercakup
  kaidah lain: `akte`, `beaya`, `efektip`, `effektif`, `effisien`. Bentuk baku tertangkap
  kaidah lama: `analisa` -> `BAK-005`, `aktifitas` -> `TIQ-003`, `resiko` -> `BAK-008`,
  `kwalitas`/`kwitansi`/`jadual` -> `BPK-015`, dan seterusnya.
- `BPK-005` - daftar nomina ungkapan idiomatis tanpa preposisi diperluas dari daftar tertutup
  menjadi terbuka: `tergantung cuaca`, `bergantung anggaran`, `tergantung penilaian` kini
  tertandai. Frasa pendek yang lazim pada naskah hukum (`sesuai undang-undang`,
  `sesuai jadwal`) sengaja tetap dibiarkan dan dicatat `[telaah]`.

Referensi baru: `references/mustakim-2019-keserasian-kata-dan-tabel-baku.md` (kutipan
verbatim hlm. 60-68 + tabel status mesin untuk seluruh lajur baku-tidak baku + anotasi
`[telaah]` untuk `BPK-013`/`BPK-014` dan pasangan `antara lain`/`misalnya`).

Verifikasi: `work/test_tms35_36.py` 16/16, `uv run pytest -q` 45 passed, uji nol positif
palsu tetap 0. Regex `sampai jumpa` awalnya case-sensitive dan telah diberi `(?i)`.

### 660 kaidah

Melanjutkan bedah Rusbiyantoro dkk. (2009), kali ini subbab 3.6 (tanda baca, hlm. 27-37) dan
3.7 (unsur serapan, hlm. 38-41):

- `TMS-032` - akhiran serapan `-ir` tidak baku: `dilegalisir`, `menginventarisir`,
  `terakomodir`, `terorganisir`, `mengkoordinir`, `diregionalisir` -> bentuk `-asi`/`-isasi`.
- `TMS-033` - ejaan serapan yang belum disesuaikan: `tehknik`, `enerjik`, `rejional`,
  `aktip`, `perogram`.
- `TMS-034` - penghubung antarkalimat berunsur dua kata di awal kalimat tanpa koma:
  `Sementara itu`, `Oleh karena itu`, `Dengan demikian`, `Selain itu`; melengkapi `SPE-003`
  yang hanya menangani bentuk satu kata (`Namun`, `Bahkan`, `Kemudian`, `Lagi pula`).

Tiga kaidah lama yang ada di data tanpa mesin kini punya matcher: `BAK-005` (`analisa`),
`BAK-007` (`praktek`, tanpa menandai `praktis`), dan `BPK-038` (`mengaktipkan`).
Contoh buku (91)-(93) tentang koma sebelum anak kalimat kausal terverifikasi sudah
tertangkap `KJK-005` dan `SPE-001`; contoh (107) `Hut ke 58` sudah tertangkap `EYD-027`.

Lima kaidah buku sengaja tidak diaktifkan dan dicatat `[telaah]` di referensi: singkatan
gelar tanpa titik (EYD V memperbolehkan), angka ribuan tanpa titik, koma serial sebelum
`dan` (EYD V menjadikannya pilihan penulis), koma sebelum `tetapi`/`sedangkan` antarklausa,
dan kutipan langsung tanpa tanda petik.

Referensi baru: `references/pusat-bahasa-2009-tanda-baca-dan-serapan.md` (kutipan verbatim
hlm. 27-41 + penanda `[OCR]` + anotasi `[telaah]`).

Verifikasi: `work/test_tms32_33.py` 28/28, `work/test_tms34.py` 11/11, `uv run pytest -q`
45 passed, uji nol positif palsu tetap 0.


### 657 kaidah

Wenni Rusbiyantoro, Nur Bety, dan Mardi Nugroho, *Beberapa Permasalahan Pemakaian Bahasa
Indonesia* (Pusat Bahasa, Departemen Pendidikan Nasional, 2009), subbab 3.8.1-3.8.3
(hlm. 42-53):

- `TMS-030` - gabungan kata dan partikel yang salah rangkai: `salahsatunya`, `tindaklanjuti`,
  `unjukrasa`, `lagipula`, `non aktif`. Bentuk berimbuhan yang benar (`ditindaklanjuti`,
  `menindaklanjuti`) sengaja dibiarkan lolos.
- `TMS-031` - `kordinator`/`kordinasi` (KBBI memakai dua vokal `/oo/`) dan `mengkomentari`
  (fonem awal `/k/` luluh menjadi `mengomentari`).

Empat kaidah lama yang ada di data tanpa mesin kini punya matcher: `BAK-002` (`merubah`,
`dirubah`), `BAK-004` (`mentargetkan`), `BPK-044` (`penanggungjawab`), `BPK-045`
(`bekerjabakti`). `SPE-014` (`tandatangani`) ikut dipasang dengan regex yang tidak menangkap
`ditandatangani`. `BDD-009` (klise `, di mana hal ini`) dipasang dengan syarat koma di depan
agar klausa relatif yang sah tidak tertandai. `KPT-009` (`kerjasama`) sengaja tetap tanpa
matcher `CUSTOM_RULES` karena `kerjasama` sudah dilaporkan mesin kata tidak baku di
`engine.py`; menambah blok baru hanya menggandakan laporan.

Referensi baru: `references/pusat-bahasa-2009-permasalahan-pemakaian-bahasa.md` (kutipan
verbatim hlm. 42-53, penanda `[OCR]` untuk salah baca `l`->`I` dan `rn`->`m`, plus anotasi
`[telaah]` untuk `ranking`, `beking`, `open race`, dan `dimana` di awal kalimat yang sengaja
belum dipola).

Verifikasi: `work/test_tms30_31.py` 29/29, `uv run pytest -q` 45 passed, uji nol positif
palsu tetap 0.


## [2.4.6] - 2026-11-17

### 655 kaidah

Mustakim, *Bentuk dan Pilihan Kata: Seri Penyuluhan Bahasa Indonesia* (Badan Pengembangan
Bahasa dan Perbukuan, 2019), subbab 3.3 c-h (hlm. 76-82):

- `TMS-029` - adjektiva pembanding (`lebih`/`kurang` + adjektiva) diikuti `dari`, seharusnya
  `daripada`. Kalimat (50) dan (51) buku dipakai sebagai pasangan salah-benar.
- Pemerluasan regex kaidah lama, tanpa entri baru:
  - `BPK-006` - tambah `berasal`, `terbentuk`, `tersusun` (asal/sumber bahan).
  - `BPK-007` - tambah bentuk label `Jam: 09.00`.
  - `BPK-008` - tambah nomina predikat `benda`, `alat`, sehingga kalimat (54)
    "Logam yaitu suatu benda ..." tertangkap.
  - `BPK-009` - tambah jabatan `camat`, `lurah`, `hakim`, `jaksa`, `sekretaris`, `duta`.

Referensi baru: `references/mustakim-2019-bentuk-pilihan-kata-mantan-bekas-dari-daripada.md`
(kutipan verbatim hlm. 76-82 + catatan `[telaah]` untuk kalimat (52), (53), (57), (58) yang
sengaja belum dipola).

Perbaikan proses: tiga blok matcher duplikat untuk `BPK-007/008/009` ditemukan dan dihapus -
kaidah itu sudah punya matcher di indeks 68-70 yang tidak menyebut ID pada komentarnya,
sehingga `grep` atas ID memberi kesan "tanpa matcher". Jumlah aturan `CUSTOM_RULES` kembali
313 -> 310, dan seluruh perilaku baru dicapai lewat pemerluasan regex lama.

### Ditambahkan
- **Lima entri kaidah Buku Praktis Bahasa Indonesia (Badan Bahasa)** — `BPBI-001` (17 pasang: erobik→aerobik, akountan→akuntan, arkhais→arkais, gladi→geladi, hirarki→hierarki, karir→karier, kuatir→khawatir, konggres→kongres, kurve→kurva, nahkoda→nakhoda, perangko→prangko, setasiun→stasiun, sahdu→syahdu, trampil→terampil, trotoir→trotoar, wakap→wakaf, wassalam→wasalam) dan `BPBI-002` (12 pasang: antri→antre, atlit→atlet, ajimat→azimat, faksimil→faksimile, filem→film, ijin→izin, joang→juang, khabar→kabar, kangker→kanker, kongkrit→konkret, tentram→tenteram, jiarah→ziarah) dari BPBI1/Kata; `BPBI-003` (`karenanya`/`makanya` → *oleh karena itu*/*oleh sebab itu*/*jadi*) dari BPBI1/Kalimat; `BPBI-004` (8 pasang: dekret→dekrit, azas→asas, hutang→utang, maghrib→magrib, atmosfir→atmosfer, eksim→eksem, apotik→apotek, kridit→kredit) dari BPBI2/1-30 & 31-60; `BPBI-005` (`contohnya seperti`/`umpamanya seperti` sebagai pleonasme) dari BPBI2/61-90; `BPBI-006` (`dilola`→`dikelola`, `sanjak`→`sajak`) dari BPBI1/Lain-lain & Sastra. `BPBI-007` (`pirsawan`->`pemirsa`, `debet`->`debit`, `voucher`->`voucer`) dari BPBI2 bagian 1-90. Total entri **618 -> 625**. Ditambah dua entri dari *Taktis Menyunting: Panduan Menyunting Naskah* (BRIN, 2019): `TMS-001` (16 pasang ejaan serapan: frustasi, negoisasi, interprestasi, konkrit, komoditi, horisontal, infantri, marjin, dirijen, otobiografi, pondasi, birahi, minimun, orisinil, quantum, malpraktik) dan `TMS-002` (14 bentuk tidak baku: telanjur, perduli, autodidak, trend, goncang, inagurasi, rubuh, contek, nampak, juridis, qori', propemerintah, cindera mata, cenderamata) dari Tabel 5.1 dan 5.16 buku tersebut, sehingga total entri **625 -> 627**. Ditambah `TBI-001` dari Winarti dkk., *Kesalahan Berbahasa Indonesia dalam Terbitan Ilmiah Perguruan Tinggi di Kalimantan Timur* (Pusat Bahasa, 2009): 10 bentuk keliru pada artikel jurnal ilmiah (propesional, kerampilan, ketrampilan, mengkomunikasikan, mendiskritkan, tehnologi, mengasilkan, prosentasi, nampaknya, tergantung dari) beserta halaman penilaian penulisnya, sehingga total menjadi **628**. Ditambah `TMS-003` dan `TMS-004` dari *Taktis Menyunting* (BRIN, 2019), Tabel 5.18 (hlm. 115) dan Tabel 5.20 (hlm. 117): 6 bentuk terikat yang dipisah spasi (antar golongan, multi lateral, purna wirawan, nara hubung, pra jabatan, sapta krida) dan 13 gabungan kata padu yang dipisah (acap kali, sedia kala, kaca mata, karya wisata, kasat mata, suka cita, kosa kata, syah bandar, mata hari, olah raga, peri bahasa, duka cita, puspa warna), sehingga total menjadi **630**. Ditambah `TMS-005` dan `TMS-006` dari *Taktis Menyunting* (BRIN, 2019), Tabel 5.6 (hlm. 102-103) dan Tabel 5.8 (hlm. 105-106): 14 bentuk lewah yang belum berkaidah (sangat sempurna sekali, sangat jauh sekali, banyak buku-buku, beberapa pendapat-pendapat, melakukan penangkapan, melakukan pembinaan, melakukan perubahan, menyatakan pendapat, menggabungkan menjadi satu, saling salip-menyalip, menanyakan pertanyaan, berencana akan, maka daripada itu, maju ke depan) dan 3 ungkapan idiomatik berpreposisi keliru (berdasarkan atas, bergantung kepada, terjadi atas), sehingga total menjadi **632**. Ditambah `TMS-007` (partikel pun yang wajib serangkai: ada pun, jika pun, andai pun, kalau pun, atau pun, kendati pun, sungguh pun, bagaimana pun, walau pun, biar pun, meski pun, sementang pun, dari Tabel 5.21 hlm. 119) dan `TMS-008` (angka berakhiran -an wajib bertanda hubung: tahun 1980an, Rp2.000an, dari Tabel 5.23 hlm. 122), sehingga total menjadi **634**. Ditambah empat kaidah tanda baca dari *Taktis Menyunting* (BRIN, 2019, hlm. 123-126): `TMS-009` spasi keliru pada tanda baca, `TMS-010` koma dan tanda tanya kalimat langsung yang jatuh di luar tanda petik, `TMS-011` elipsis tanpa spasi, dan `TMS-012` tanda hubung yang dipakai untuk rentang waktu alih-alih tanda pisah en dash, sehingga total menjadi **638**. Ditambah `TMS-013` (konjungsi korelatif yang memakai `tapi juga` alih-alih `tetapi juga` atau `melainkan juga`, Tabel 5.29 hlm. 128-129) dan `TMS-014` (kalimat tidak sepadan: subjek didahului preposisi pada pola `kepada`/`bagi` + `diharap(k)an`/`diminta`, Tabel 5.32 hlm. 130), sehingga total menjadi **640**. Ditambah `TMS-015` (`media masa` -> `media massa`, `nara blog` -> `narablog`; Zaim, 2018) dan `TMS-016` (`impelementasi`, `pelaksaan`, `instrument penelitian`; Sihombing dkk., 2024), sehingga total menjadi **642**. Ditambah `TMS-017` (kata depan `di` serangkai dengan nomina: `dimasa`, `diinternet`), `TMS-018` (imbuhan terpecah spasi: `memudah kan`, `menumbuh kembangkan`, `men translasi`), dan `TMS-019` (nama bahasa berhuruf kecil: `bahasa inggris`), ketiganya dari Kemas Ferri Rahman, *Komunikasi Perusahaan Melalui Tulisan* (BRIN, 2022, hlm. 34-35), sehingga total menjadi **645**. Ditambah `TMS-020` (gabungan kata bentuk bebas keliru diserangkai: `sumberdaya`, `tatausaha`, `jurutulis`, `serahterima`) dan `TMS-021` (unsur terikat keliru dipisah: `non migas`, `antar daerah`, `purna jual`, `pra sejarah`, `sub sistem`), keduanya dari Mustakim, *Bahasa Indonesia untuk Aparatur Pemerintah* (Badan Bahasa, 2016, hlm. 12-13), sehingga total menjadi **647**. Referensi: `references/bp2-2016-aparatur-pemerintah-gabungan-kata.md`. Ditambah lima kaidah surat dinas dari buku yang sama (hlm. 57-60): `TMS-022` (Kepada Yth. tanpa kata kepada), `TMS-023` (singkatan Jl./Jln./Telp./Tip.), `TMS-024` (format tanggal surat), `TMS-025` (jumlah lampiran), dan `TMS-026` (nomor surat diakhiri titik atau titik-hubung), sehingga total menjadi **652**. Referensi: `references/bp2-2016-aparatur-pemerintah-surat-dinas.md`. Dari bagian penutup surat dan Bab IV buku yang sama ditambah `TMS-027` (NIP berkapitalisasi campur atau berangka berspasi) dan `TMS-028` (pihak pemberi tembusan didahului Yth. atau diikuti *sebagai laporan*) menjadi **654**; `BPK-007` (*jam* alih-alih *pukul*) ternyata sudah bermesin — kesan "tanpa matcher" muncul karena blok lamanya tidak menyebut ID kaidah pada komentarnya — sehingga yang dilakukan adalah menambah bentuk label `Jam: 09.00` pada regex lama; dan `NIP` dikeluarkan dari pola `MBI-004` karena NIP pada blok tanda tangan surat resmi bukan data responden. Referensi: `references/bp2-2016-aparatur-pemerintah-penutup-surat-dan-laporan.md`. Referensi: `references/zaim-2018-serapan-ti-dan-sihombing-2024-diksi.md`. Referensi: `references/taktis-menyunting-brin-konjungsi-kalimat.md`. Referensi: `references/taktis-menyunting-brin-tanda-baca.md`. Referensi: `references/taktis-menyunting-brin-partikel-pun-angka.md`. Referensi: `references/taktis-menyunting-brin-lewah-idiomatik.md`. Referensi: `references/taktis-menyunting-brin-bentuk-terikat-gabungan-kata.md`. Referensi verbatim: `references/kesalahan-berbahasa-terbitan-ilmiah-kaltim-leksikal.md`; metadata referensi lama (2005, 170 hlm) dikoreksi menjadi cetakan 2009, xvi + 156 hlm. Referensi verbatim: `references/taktis-menyunting-brin-ejaan-kata.md`.
- **Matcher `BPBI-001`–`BPBI-005`** di `humanizer_id/matchers.py` — case-insensitive, `` word boundary; uji positif/negatif lolos tanpa false positive.
- **Ekstrak referensi verbatim + sitasi**: `references/bpbi-1-kata-badan-bahasa.md`, `references/bpbi-1-kalimat-badan-bahasa.md`, `references/bpbi-1-tanya-kebahasaan-badan-bahasa.md`, `references/bpbi-2-tanya-jawab-badan-bahasa.md`, `references/bpbi-1-lain-lain-badan-bahasa.md`, `references/bpbi-2-1-90-badan-bahasa.md`, `references/bpbi-1-sastra-badan-bahasa.md` (id.wikisource.org, domain publik UU No. 28/2014).

### Diperbaiki
- **Kontradiksi `CX11-002`**: entri sempat menyarankan `namun demikian` sebagai bentuk benar, padahal Buku Praktis 1 (`namun demikian` = *tetapi demikian* yang janggal) dan `PT-001` menyatakan salah. Saran diganti menjadi `meskipun demikian` / `(cukup 'namun')`.
- **`PT-001`** diperkaya sitasi Buku Praktis Bahasa Indonesia 1 sebagai sumber kedua.

### Dipertahankan
- `baud→baut`, `sutra→sutera`, `lembab→lembap` tercantum di buku namun **tidak diaktifkan** — `baud` sah sebagai satuan laju data, `sutra` sah dalam konteks akademik/keagamaan, `lembab` lazim dipakai (menunggu telaah semantik).
- `hisap→isap` dan `himbau→imbau` **tidak diaktifkan** — kontroversial dalam pemakaian modern.
- `mengetrapkan→menerapkan` dan `mengenyampingkan→mengesampingkan` dari BPBI1/Lain-lain **tidak diduplikasi** — sudah aktif di BPK-012 dan KRF-001.
- Pembahasan "majas vs gaya bahasa" (BPBI1/Sastra) hanya telaah terminologis — tidak dijadikan matcher.
- Pasangan BPBI2 **tidak diaktifkan**: `relawan->sukarelawan` (sumber merujuk KBBI 1996; KBBI V sudah memuat `relawan`), `para hadirin` (BPBI2 menilai tidak mubazir), `kurban/korban` (beda makna), `elit/elite` + `bonafid/bonafide` + `faksimil/faksimile` (pelafalan, false-positive tinggi).

## [2.4.5] — 2026-11-17

### Diperbaiki
- **Demote 6 kaidah sufiks asing ke `[telaah]`** (`TII-010`..`TII-014`, `TII-016`): pola *-ization, -logy, -ity, -ism, hyper-/poly-* rawan salah tangkap pada kata Indonesia (mis. *Laboratorium*), jadi dijadikan rujukan telaah, bukan aturan aktif.
- **Matcher `TII-015` lambang satuan salah kapital** — case-sensitive, menangkap *5 Newton*, *3 Kg*, *10 KM* tanpa salah tangkap lambang SI baku *N, J, W, kg, km, MB, GB*.
- **Konsol Windows UTF-8** — `main()` memaksa `stdout/stderr` ber-encoding UTF-8 agar panah/simbol laporan tidak membuat audit gagal di tengah jalan.
- Hapus `CUSTOM_RULES` mati milik kaidah yang di-demote.

### Diubah
- **`references/pupi-2004-kepmendiknas146.md`** — tulis ulang ekstrak verbatim.
- Blok `BW` sub-skill `ejaan-morfologi` kini 19 entri (menambah `TII-010`..`TII-016` sebagai butir 13–19).
- Angka kaidah terhitung ulang: **611 → 618** (582 aktif + 36 telaah).

## [2.4.4] — 2026-11-17

### Ditambahkan
- **12 kaidah penyerapan istilah dari PUPI** (Kepmendiknas 146/U/2004): `PUPI-002`..`PUPI-009` untuk bentuk serapan leksikal (*frekwensi, subyektif, propinsi, komplek, jaman, kaedah, managemen, ekstrim*) dan `PUPI-010`..`PUPI-013` untuk bentuk terikat (*pra-, ekstra-, anti-, multi-*).
- **`references/pupi-2004-kepmendiknas146.md`** — ekstrak verbatim 1.322 baris (Bab I–IV) termasuk tabel penyesuaian ejaan prefiks dan sufiks.
- **Blok `BW`** pada sub-skill `ejaan-morfologi` berisi 12 entri Pola → Perbaikan → Sebab plus tabel rujukan serapan sufiks/prefiks.

### Diperbaiki
- Blok `BV2` sub-skill `ejaan-morfologi`: butir 4–7 sebelumnya kehilangan **Perbaikan/Sebab** karena penggabungan baris.

### Catatan rilis
- Versi 2.4.1–2.4.3 tidak tercatat terpisah di berkas ini; ketiganya berisi integrasi EYD V, EYD 1987, dan PUEBI 2015 (kaidah `EYD-058`..`EYD-064`).

## [2.4.0] — 2026-11-17

### Ditambahkan
- **Installer `humanizer-id install`** — menyalin `SKILL.md`, `skills/`, `scripts/`, `humanizer_id/`, dan `data/` ke folder agen AI (Hermes Agent, Claude Code, Google Antigravity) secara otomatis. Deteksi target otomatis; `--target` memilih satu, `--with-references` menyertakan `references/`.
- **Test konsistensi versi** — pytest yang memastikan `pyproject.toml`, `__init__.py`, `SKILL.md` induk, 5 sub-skill, dan `uv.lock` selalu seversi.

## [2.3.1] — 2026-11-17

### Diperbaiki
- Deskripsi paket (README) di PyPI dan rujukan eksternal yang tidak relevan dihapus.
- 75 blok sub-skill dinormalisasi ke format entri **Pola → Perbaikan → Sebab** dengan sitasi halaman.

## [2.3.0] — 2026-11-17

### Ditambahkan
- **Mode AFTER — audit bernomor** (`--report`): temuan bernomor `humanizer/audit-NNN-YYYY-MM-DD.md` tanpa menyunting naskah; eksekusi hanya nomor yang disetujui.
- Generator laporan markdown `humanizer_id/report.py` dengan prioritas HIGH/MEDIUM/LOW.

## [2.2.0] — 2026-11-16

### Ditambahkan
- **Delivery Gate** PASS/FAIL dan Checklist Editorial pada `SKILL.md`.
- Konvensi entri kaidah Pola → Perbaikan → Sebab.

## [2.1.0] — 2026-11-16

### Diubah
- `SKILL.md` monolitik (~113 KB) dipecah menjadi induk ~195 baris + 5 sub-skill on-demand (ejaan-morfologi, sintaksis, diksi-istilah, wacana-retorika, naskah-resmi).

## [2.0.0] — 2026-11-15

### Ditambahkan
- 592 kaidah preskriptif total (integrasi pedoman jurnal Dikbud, surat-menyurat Pusat Bahasa, modul jurnalistik).

## Sebelum 2.0.0

Riwayat v1.x (mesin audit deterministik, autofix, glosarium lintas bidang) tersedia di [Releases](https://github.com/apissaj/humanizer-id/releases).
