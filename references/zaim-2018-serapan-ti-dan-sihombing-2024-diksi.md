# Dua sumber akademik: serapan TI (Zaim 2018) dan diksi skripsi (Sihombing dkk. 2024)

Dua artikel jurnal ini dipakai sebagai sumber kaidah `TMS-015` dan `TMS-016`.
Keduanya artikel jurnal terbuka, bukan buku berbayar. Kutipan di bawah verbatim
dari PDF yang tersimpan di `books/`; anotasi ditandai dengan "Catatan:".

## Sumber 1 - M. Zaim, "Keberterimaan dan Kebermanfaatan Serapan Kata Asing dalam Bidang Teknologi Informasi oleh Penutur Indonesia"

M. Zaim, Universitas Negeri Padang. Abstrak memuat kalimat pembuka:

> Kemunculan kata serapan bahasa asing dalam teknologi informasi yang ditulis
> dalam bahasa Indonesia telah memperkaya kosa kata Bahasa Indonesia sebagai
> bahasa yang digunakan dalam komunikasi formal dan informal.

### Temuan: frasa "media masa"

Frasa keliru itu muncul **lima kali** dalam artikel, antara lain:

> Hal ini dibuktikan dengan masih maraknya istilah asing itu muncul baik di
> media masa, media sosial, dan komunikasi lisan sehari-hari penutur bahasa
> Indonesia.

> Seringnya padanan kata ini digunakan oleh media masa dan pemuka masyarakat
> akan mempengaruhi penggunaannya dalam berkomunikasi oleh penutur Indonesia

Catatan: bentuk baku adalah *media massa*. *Masa* berarti 'waktu', *massa*
berarti 'kumpulan orang banyak'. Artikel ini sendiri memakai istilah *media
massa* pada bagian lain, jadi pemakaian *media masa* adalah ketidakkonsistenan
internal, bukan pilihan gaya.

### Temuan: padanan "narablog"

Tabel padanan istilah TI dalam artikel yang sama menulis bentuk padu:

> 1 bar code - kode batang
> 2 blogger - narablog
> 3 browser - peramban

Catatan: artikel ini menulis *narablog* (serangkai) di tabel, tetapi pada
bagian lain memakai *nara blog*. Bentuk baku mengikuti kaidah bentuk terikat
*nara-*: *narablog*, *narahubung*, *narasumber*, *narapidana*, semuanya
serangkai.

### Kaidah yang dipasang

`TMS-015` - pola `"media masa / nara blog"`, saran `media massa`, `narablog`.
Dua regex terpisah: `\bmedia\s+masa\b` dan `\bnara\s+blog\b`.

## Sumber 2 - Ovi Oktavia K. Sihombing dkk., "Analisis Pemilihan Diksi terhadap Penulisan Skripsi Mahasiswa PGSD Universitas Negeri Medan"

AR RUMMAN - Journal of Education and Learning Evaluation, Vol. 1 No. 2,
Desember 2024, hlm. 543 dst. E-ISSN 3047-0943, P-ISSN 3047-1141.

### Temuan 1: "impelementasi"

Kutipan naskah mahasiswa yang dianalisis (kolom kiri) dan perbaikan peneliti
(kolom kanan):

> Bagaimana persepsi guru SD terhadap impelementasi pembelajaran tematik
> kurikulum 2013, Kecamatan Sarudik kabupaten Tapanuli Tengah T.A. 2022/2023 ?

> Mengganti "impelementasi" dengan "implementasi."

Catatan: huruf *l* tertukar dengan *m*. Bentuk baku *implementasi*, bukan
*impelementasi*; turunannya *mengimplementasikan*, *terimplementasi*.

### Temuan 2: "pelaksaan"

> Pada tahap pelaksaan penelitian ini, peneliti memberikan kuesioner kepada
> responden untuk diisi.

Catatan: satu huruf *n* hilang. Bentuk baku *pelaksanaan*, dari *laksana* +
pe-an. Bandingkan *pelaksana*, *melaksanakan*.

### Temuan 3: "instrument penelitian"

> Sebelum kelapangan melaksanakan penelitian terlebih dahulu peneliti
> melaksanakan validasi pada instrument penelitian yang akan digunakan.

Catatan: bahasa Indonesia menyerap bentuk tunggal *instrumen*, bukan bentuk
Inggris *instrument*. Karena itu *instrumen penelitian*, *instrumen validasi*.

### Kaidah yang dipasang

`TMS-016` - pola `"impelementasi / pelaksaan / instrument penelitian"`, saran
`implementasi`, `pelaksanaan`, `instrumen penelitian`.

Bentuk pengecualian yang sengaja dijaga agar tidak false positive:

- `instrument` hanya ditandai bila diikuti `penelitian` atau `peneliti`
  (`\binstrument\b(?=\s+(?:penelitian|peneliti)\b)`), sebab teks berbahasa
  Inggris dan istilah teknis lain (mis. *instrument optik*) sah memakai
  *instrument*.
- `pelaksaan` tidak menyentuh `pelaksanaan`; `impelementasi` tidak menyentuh
  `implementasi`.

### Kesalahan yang sama tetapi tidak dipola

Dari tabel yang sama, artikel mencatat *"kosa kata"* (seharusnya *kosakata*),
*"di atas"* yang dipisah pada konteks keliru, dan *"kelapangan"* (seharusnya
*ke lapangan*).

- *kosa kata* sudah berkaidah pada `TMS-004` (gabungan kata), jadi tidak dibuat
  ID baru.
- *"di atas"* dan *"kelapangan"* sengaja belum dipola. Keduanya bergantung
  konteks: *di atas* sah pada *tabel di atas* maupun *di atas meja*, dan
  *kelapangan* hanya keliru bila bermakna arah (*ke lapangan*), sedangkan
  sebagai kata sifat (*sikap kelapangan hati*) bentuk itu tidak ada padanannya.
  Regex bentuk-tunggal akan menandai pemakaian yang benar, jadi keduanya
  dicatat sebagai bahan `[telaah]` manual, bukan kaidah otomatis.
