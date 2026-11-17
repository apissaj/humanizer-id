# Taktis Menyunting (BRIN, 2019) - tanda baca dan simbol

Sumber: Badan Riset dan Inovasi Nasional, *Taktis Menyunting: Panduan ...*,
2019. Bab V "Praktik Menyunting Bahasa", butir 3 dan 4 (hlm. 123-126).
Buku menyatakan "Buku ini tidak diperjualbelikan"; kutipan dipakai sebagai
rujukan kaidah, bukan salinan isi buku.

## 3. Pengelompokan tanda baca (Tabel 5.24, hlm. 123)

| Kelompok | Simbol | Contoh buku |
|---|---|---|
| Penyudah | . ! ? | Mereka bertemu di sini. / Tutup pintu, Mbang! / Siapa yang mengubahnya? |
| Penyela | , ; : | Jika malam tiba, mereka mulai bertebaran. / Adik asyik membaca buku; kakak asyik menulis. |
| Pembatas | / - \u2013 | Mereka mengundang pengurus se-Indonesia. / Pukul 13.00\u201314.00 kalian boleh beristirahat. |
| Peringkas | ' ... | Libur t'lah tiba. / Siapa yang tidak tahu si ...? |
| Pengapit | \u201c...\u201d '...' (...) | "Mintalah sama ibumu," ujar Ayah. / Proofreading 'koreksi cetak coba'. |

## 3.1. Spasi pada tanda baca (hlm. 124)

> Tanda baca selalu ditulis serangkai (tanpa spasi) dengan kata yang
> mengikutinya atau mendahuluinya.

Contoh keliru yang dikutip buku:

> Dunia tulis \u2013 menulis memang mengasyikkan . Namun , mungkin tidak bagi
> kalangan akademis yang menganggap menulis justru seperti \u2018 monster \u2018 yang
> menakutkan . Mereka merasa menulis adalah beban sehingga terkadang tersirat
> jalan pintas untuk menjiplak ( plagiat ) .

> Namun,mungkin tidak bagi kalangan akademis yang menganggap menulis justru
> seperti \u201cmonster\u201d.Mereka merasa menulis adalah beban [...] untuk menjiplak
> (plagiat).

Dipasang sebagai kaidah **TMS-009**, empat kekeliruan: spasi sebelum tanda
penyudah/penyela, spasi sesudah tanda buka kurung atau petik, spasi sebelum
tanda tutup, dan koma tanpa spasi sesudahnya.
Tidak diperiksa: titik dua (sudah `JRN-008`), serta spasi sesudah titik yang
hilang (rawan bentrok dengan singkatan bergelar seperti `S.H.` dan `op. cit.`).

## 3.2. Penulisan tanda baca yang tepat (hlm. 125)

> \u201cPergi sana!\u201d seru Intan kepada Randi.
> \u201cMereka belum juga pulang,\u201d ujar Ibu sangat khawatir.
> Pelatihan diselenggarakan tanggal 10\u201311 November 2022.
> \u201cMaaf ... maaf apa bisa diulang lagi?\u201d tanya Kinan.
> Gotong royong dalam Pancasila melambangkan sila ke-....
> Adiknya senang menulis; kakaknya senang menari.

## 4. Kekeliruan penggunaan tanda baca (Tabel 5.25, hlm. 125-126)

| Tidak tepat | Tepat |
|---|---|
| Mereka tidak paham bagaimana duduk persoalan yang membelit Rani? | Mereka tidak paham bagaimana duduk persoalan yang membelit Rani. |
| \u201cBesok kita mulai perburuan ini\u201d, kata Pak Mintarjo. | \u201cBesok kita mulai perburuan ini,\u201d kata Pak Mintarjo. |
| \u201cApa sih yang belum kamu pahami\u201d? tanya Tantri. | \u201cApa sih yang belum kamu pahami?\u201d tanya Tantri. |
| Ia membaca artikel berjudul \u201cPenyuntingan Naskah Pendek.\u201d | Ia membaca artikel berjudul \u201cPenyuntingan Naskah Pendek\u201d. |
| Ia baru saja menerima \u2018amplop\u2019 sebagai uang muka. | Ia baru saja menerima \u201camplop\u201d sebagai uang muka. |
| Social distancing \u201cpembatasan sosial\u201d sudah dilonggarkan. | Social distancing \u2018pembatasan sosial\u2019 sudah dilonggarkan. |
| Ia sedang... buku. | Ia sedang ... buku. |
| Jangan pedulikan mereka.... | Jangan pedulikan mereka .... |
| Rapat berlangsung pukul 09:00-10:00. | Rapat berlangsung pukul 09:00\u201310:00. |
| Mereka bersepakat damai-pertikaian telah berlangsung satu tahun. | Mereka bersepakat damai\u2014pertikaian telah berlangsung satu tahun. |

> Kata tanya, seperti apa, bagaimana, dan mengapa dapat digunakan pada
> kalimat berita sehingga kalimat tersebut seharusnya diakhiri dengan tanda
> titik.

> Tanda petik pada kalimat langsung diletakkan setelah tanda baca penyudah
> atau penyela.

> Tanda pisah digunakan untuk mengganti keterangan \u2018sampai dengan\u2019 atau
> menyisipkan keterangan di luar kalimat inti.

Dipasang sebagai kaidah:
- **TMS-010** - koma dan tanda tanya pada kalimat langsung harus di dalam
  tanda petik, diperiksa hanya bila diikuti verba pengiring (kata, ujar,
  tanya, jawab, dan sejenisnya).
- **TMS-011** - elipsis wajib berspasi sebelum dan sesudah. Pemeriksaan
  dibatasi pada elipsis di tengah kalimat (`sedang... buku`, `sedang...buku`);
  elipsis di ujung kalimat tidak dipakai karena pada teks contoh dan korpus
  mesin bentuk itu lazim menjadi penanda pemotongan kutipan, sehingga
  penerapannya menghasilkan positif palsu (terbukti pada uji regresi
  `tests/test_smoke.py`).
- **TMS-012** - rentang waktu (pukul 09:00-10:00, tanggal 10-11 November)
  memakai tanda pisah en dash.

Tidak dijadikan pola: kalimat berita yang diakhiri tanda tanya (butuh
penilaian makna), petik tunggal untuk istilah pinjaman (butuh konteks istilah),
dan tanda pisah penyela (\u2014) di tengah kalimat karena rawan bentrok dengan
tanda hubung pada kata ulang dan kata majemuk.
