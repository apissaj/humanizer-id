# Rusbiyantoro dkk. (2009), *Beberapa Permasalahan Pemakaian Bahasa Indonesia* - tanda baca dan unsur serapan

**Sumber primer:** Wenni Rusbiyantoro, Nur Bety, dan Mardi Nugroho. *Beberapa Permasalahan
Pemakaian Bahasa Indonesia*. Jakarta: Pusat Bahasa, Departemen Pendidikan Nasional, 2009.
Berkas: `books/beberapa_permasalahan_pemakaian_bahasa_indonesia.pdf`.

Catatan ini melanjutkan
`pusat-bahasa-2009-permasalahan-pemakaian-bahasa.md` (subbab 3.8.1-3.8.3) dan mencakup
subbab 3.6 (Pemakaian Tanda Baca, hlm. 27-37) serta 3.7 (Penulisan Unsur Serapan,
hlm. 38-41). Penanda `[OCR]` dan `[telaah]` mengikuti konvensi berkas saudaranya.

---

## 3.6.1 Tanda Titik - singkatan gelar `[hlm. 27-28]`

> singkatan nama orang, nama gelar, sapaan, jabatan, atau pangkat diikuti dengan tanda titik

Contoh: `dr HA Sofyan Hasdam SpS` -> `dr. H.A. Sofyan Hasdam, Sp.S`; `Drs H Syaukani HR MM` ->
`Drs. H. Syaukani, H.R., MM`.

`[telaah]` Singkatan gelar **tidak** dipola: EYD V memperbolehkan penulisan gelar tanpa titik
(kecenderungan baru), sehingga menandainya akan bertentangan dengan EYD-021 yang sudah
mengatur singkatan titik dua karakter. Kaidah ini tidak diaktifkan.

## 3.6.1 Tanda Titik - bilangan ribuan `[hlm. 28]`

> tanda titik digunakan untuk memisahkan bilangan ribuan atau kelipatannya

Contoh: `4253 calan jamaah` -> `4.253 calan jamaah`.

`[telaah]` Angka ribuan tanpa titik tidak dipola: penulisan `4253` masih lazim dan sering
dipakai dalam konteks teknis (kode, ID, tahun); penandaan otomatisnya berisiko tinggi
positif palsu. Tidak diaktifkan.

## 3.6.2.1 Tanda Koma dalam Perincian `[hlm. 29-30]`

> Pemakaian tanda koma dalam perincian yang terdiri atas tiga unsur atau lebih seharusnya
> diberi tanda koma sebelum kata dan.

Contoh: `Golkar, PPP, PBR dan PBB` -> `Golkar, PPP, PBR, dan PBB` (tiga unsur atau lebih).

> Jika penggabungan hanya terdiri atas dua unsur, sebelum kata penghubung dan tidak perlu
> dibubuhkan tanda koma.

Contoh salah sebaliknya: `menggandeng PT Citra Pamerindo, dan didukung oleh Kaltim Post` ->
koma dihapus.

`[telaah]` Koma serial sebelum `dan` pada perincian tiga unsur tidak dipola. Alasan: EYD V
tidak lagi mewajibkan koma serial (pilihan penulis), sehingga menandai teks yang memakai
`A, B dan C` akan menghasilkan tuduhan palsu pada naskah yang konsisten memilih gaya tanpa
koma serial. Tidak diaktifkan.

## 3.6.2.2 Koma Memisahkan Kalimat Setara `[hlm. 30-31]`

> Tanda koma harus digunakan untuk memisahkan kalimat setara yang satu dari kalimat setara
> berikutnya yang didahului oleh kata tetapi, melainkan, dan sedangkan.

Contoh: `... dipegang oleh orang yang memahami administrasi tetapi tidak paham tentang
perpustakaan` -> `... memahami administrasi, tetapi tidak paham ...`.

`[telaah]` Tidak dipola: kaidah koma sebelum `tetapi`/`sedangkan` antarklausa setara
bergantung struktur kalimat yang sulit dipastikan regex tanpa parser; risiko positif palsu
tinggi pada klausa pendek. Konjungsi `sedangkan` di posisi awal kalimat sudah dijaga
`TBG-003`. Tidak diaktifkan.

## 3.6.2.3 Koma Sebelum Anak Kalimat `[hlm. 31-32]`

> tanda koma tidak dipakai untuk memisahkan anak kalimat dari induk kalimat jika anak kalimat
> itu mengikuti induknya

Contoh: `... mengaku menjenguk Dicky, karena Dicky adalah teman ...` -> koma dihapus.

Kaidah ini **sudah aktif**: `KJK-005` (`, karena`) dan `SPE-001` (`, karena / , agar /
, supaya`) menangkap pola yang sama; contoh (91)-(93) buku terverifikasi tertangkap mesin
lama. Tidak ada entri baru.

## 3.6.2.4 Koma di Belakang Kata Penghubung pada Awal Kalimat `[hlm. 32-33]`

> penulisan kata atau ungkapan penghubung antarkalimat ... harus diikuti tanda koma

Contoh: `Namun biayanya ditanggung ...` -> `Namun, biayanya ditanggung ...`;
`Sementara itu perkembangan waduk ...` -> `Sementara itu, perkembangan waduk ...`.

Kaidah aktif:

| Kaidah | Cakupan |
|---|---|
| `SPE-003` | `Namun`, `Bahkan`, `Kemudian`, `Lagi pula` di awal kalimat tanpa koma (sudah ada) |
| `TMS-034` | `Sementara itu`, `Oleh karena itu`, `Dengan demikian`, `Selain itu` di awal kalimat tanpa koma (baru) |

Regex `TMS-034` mensyaratkan posisi awal kalimat (`(?m)(?:^|[.!?]\s+|\n)`) dan menolak bila
koma sudah ada (`(?=[^\s,.;:])`), sehingga kalimat tengah paragraf dan bentuk bersahaja
`..., sementara itu keputusan dituangkan ...` tidak tertandai.

## 3.6.3 Tanda Petik - kalimat langsung `[hlm. 34-36]`

> Tanda petik dipakai untuk mengapit petikan langsung yang berasal dari pembicaraan

Contoh: kutipan narasumber tanpa tanda petik setelah `kata Rachmad`, `tegas Lilik`, dan
sejenisnya.

`[telaah]` Tidak dipola: mendeteksi kutipan langsung yang hilang tanda petik menuntut
pemahaman batas kalimat dan atribusi; regex murni akan menandai hampir semua kalimat setelah
`kata X`. Tidak diaktifkan.

## 3.6.4 Tanda Hubung `[hlm. 36-37]`

> tanda hubung dipakai untuk menyambung unsur-unsur kata ulang

Contoh: `putra putri` -> `putra-putri`; `lain lain` -> `lain-lain`.

> jika ingin merangkaikan ke- dengan angka, di antara keduanya harus ada tanda hubung

Contoh: `Hut ke 58` -> `Hut ke-58`.

Kaidah aktif: `EYD-027` sudah menangani `ke 58` -> `ke-58` lewat pola `ke[Angka]` tanpa
tanda hubung; contoh (107) buku terverifikasi tertangkap mesin lama.

`[telaah]` Kata ulang `putra putri` / `lain lain` tanpa tanda hubung tidak dipola baru:
`BPK-004` sudah mengatur penggunaan `lain-lain` sebagai ungkapan, dan menandai setiap
pasangan kata yang berpotensi ulang tanpa konteks berisiko salah (bandingkan `putra putri`
vs frasa koordinatif `ayah putra`). Tidak diaktifkan.

> tanda hubung boleh dipakai untuk memperjelas hubungan bagian-bagian kata atau ungkapan

Contoh: `hubungan AS China` -> `hubungan AS-China`.

`[telaah]` Tidak dipola: tanda hubung pada pasangan sigla hanya dianjurkan ("boleh"), bukan
wajib; kaidah faktatif tidak layak jadi aturan audit. Tidak diaktifkan.

## 3.7 Penulisan Unsur Serapan `[hlm. 38-41]`

### Akhiran -ir `[hlm. 38-40]`

> akhiran -ir dan -ing sering digunakan. Padahal, akhiran tersebut tidak baku. Dalam bahasa
> Indonesia padanan yang tepat untuk akhiran -ir adalah -asi atau -isasi

Contoh aktif:

| Kaidah | Bentuk | Perbaikan |
|---|---|---|
| `TMS-032` | `dilegalisir`, `menginventarisir`, `terakomodir`, `terorganisir`, `mengkoordinir`, `diregionalisir` | `dilegalisasi`, `menginventarisasi`, `terakomodasi`, `terorganisasi`, `mengkoordinasi`, `diregionalisasi` |

> Kata organisir berasal dari bahasa Inggris organization yang penyerapannya ke dalam bahasa
> Indonesia dengan cara mengganti bunyi -tion dengan bunyi -si.

`[telaah]` Akhiran `-ing` (contoh buku: *shuttle cock*) tidak dipola: bentuk campuran
Inggris-Indonesia sudah dijaga kaidah kata asing lain dan polanya terlalu kabur untuk regex.

### Ejaan serapan lain `[hlm. 40-41]`

> penulisan yang benar adalah analisis, diagnosis, teknik, praktik, energik, regional, aktif,
> dan program

Kaidah aktif:

| Kaidah | Bentuk | Status matcher |
|---|---|---|
| `BAK-005` | `analisa` -> `analisis` | baru dipasang (siklus ini) |
| `BPK-017` | `sistim`, `metoda`, `hipotesa`, `diagnosa` | sudah ada |
| `BAK-007` | `praktek` -> `praktik` | baru dipasang |
| `BPK-038` | `mengaktipkan` -> `mengaktifkan` | baru dipasang |
| `TMS-033` | `tehknik`, `enerjik`, `rejional`, `aktip`, `perogram` | baru |

Regex `BAK-007` sengaja tidak menandai `praktis` (adjektiva yang memang berakhiran -tis),
dan `BPK-038` menangkap semua turunan `*aktipkan` (`mengaktipkan`, `diaktipkan`).

---

## Catatan verifikasi matcher

`TMS-032` diuji 6 bentuk positif dan 4 negatif, `TMS-033` 4 positif dan 5 negatif, `TMS-034`
4 positif dan 4 negatif; total `work/test_tms32_33.py` 28/28 dan `work/test_tms34.py` 11/11.
Regex `dilegalisir` awalnya `legalisir` dan tidak menangkap prefiks `di-`; diperbaiki
menjadi `\w*legalisir\w*`. `mengkoordinir` awalnya tidak ada dalam daftar kaidah dan
ditambahkan setelah uji positif gagal. Uji nol positif palsu (`test_smoke.py`) tetap 0 hit.
