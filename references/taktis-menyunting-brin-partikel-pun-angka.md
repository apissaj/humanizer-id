# Taktis Menyunting (BRIN, 2019) - partikel pun dan penulisan angka

Sumber: Badan Riset dan Inovasi Nasional, *Taktis Menyunting: Panduan ...*,
2019. Bab V "Praktik Menyunting Bahasa", butir g dan i (hlm. 119-122).
Buku menyatakan "Buku ini tidak diperjualbelikan"; kutipan dipakai sebagai
rujukan kaidah, bukan salinan isi buku.

## g. Partikel pun (Tabel 5.21, hlm. 119)

> Ada partikel yang ditulis serangkai dan ada pula yang ditulis terpisah.

Pun yang tetap terpisah (contoh buku):

> Apa pun makanannya, minumnya teh manis.
> Terlambat pun ke rumahnya, kita masih mendapat uang.
> Sekali pun ia tidak pernah meminta upah.

Pun yang ditulis serangkai (14 bentuk pada Tabel 5.21):
adapun, jikapun, sekalipun, andaipun, kalaupun, sementangpun, ataupun,
kendatipun, sungguhpun, bagaimanapun, maupun, walaupun, biarpun, meskipun.

Dipasang sebagai kaidah **TMS-007** (12 pasang): ada pun, jika pun, andai pun,
kalau pun, atau pun, kendati pun, sungguh pun, bagaimana pun, walau pun,
biar pun, meski pun, sementang pun.
Tidak diaktifkan: `sekalipun` dan `maupun` sudah ada di data, sedangkan
`sekali pun` sengaja dilewati karena buku sendiri memakainya sebagai contoh
bentuk terpisah (kontradiksi internal buku dengan daftar Tabel 5.21).
Bentuk `apa pun`, `terlambat pun`, dan pun pada pemakaian biasa tidak pernah
dijadikan pola.

## g.3. Partikel per (hlm. 120, tidak dijadikan kaidah)

> Penulisan yang berarti 'demi', 'tiap', 'mulai', atau 'melalui' ditulis
> terpisah dari kata yang mengikutinya.

Contoh buku: satu per satu, Rp1 juta per meter, Per 1 Januari 2023,
per panggilan video. Tidak dijadikan regex karena kata "per" juga muncul
sebagai preposition biasa dan singkatan satuan, sehingga rawan false-positive.

## h. Singkatan dan akronim (Tabel 5.22, hlm. 120-121, belum dijadikan kaidah)

| Tepat | Tidak tepat |
|---|---|
| A.H. Nasution | A. H. Nasution |
| Suman Hs. | Suman HS. |
| dr. Indra (dokter) | Dr. Indra |
| Dr. Pratiwi (doktor) | DR. Pratiwi |
| Dr. (H.C.) Sri Mulia | Dr. H.C. Sri Mulia |
| Anton, S.H. | Anton S.H. |
| R.M. Said | R. M. Said |
| A.K.B.P. Pratikno | AKBP Pratikno |
| STA (Sutan Takdir Alisjahbana) | S.T.A. |
| PT | P.T.; PT. |
| CV | C.V.; CV. |
| PAUD | Paud |
| hlm. | hlm; hal |
| a.n. | an; a/n |
| s.d. | sd; s/d |
| Gg. Kelinci | Gg Kelinci; GG Kelinci |
| 2 km | 2 Km |
| 10 kg | 10 Kg; 10 kg. |
| Rp2.000,00 | Rp.2.000,00 |
| Ikapi | IKAPI |
| UNESCO | Unesco |
| Ikatan Penerbit Indonesia (Ikapi) | Ikapi (Ikatan Penerbit Indonesia) |

Belum dijadikan regex: banyak bentuk bergantung konteks (gelar vs singkatan
nama, badan hukum vs singkatan lain) dan berisiko mengubah kutipan langsung
atau nama resmi.

## i. Angka dan bilangan (Tabel 5.23, hlm. 121-122)

Angka dipakai untuk ukuran dan nilai: sawah seluas 10 hektare, pukul 4 sore,
1 jam 30 menit, Rp10.000,00, sekira 8 persen, sebanyak 10%.
Bilangan yang dapat dinyatakan dengan satu kata ditulis dengan huruf kecuali
dalam perincian berurutan: "Ia sudah tiga kali tidak hadir", "Buku terjual
14 eksemplar", tetapi "1 laptop, 2 tablet, dan 10 smartphone".
Bilangan besar boleh ditulis sebagian dengan huruf: 500 ribu dosis,
kredit 50 juta.
Bilangan tingkat: Abad V Masehi, Perang Dunia II, Perang Dunia Kedua
(bukan Perang Dunia ke-II, Perang Dunia Dua, Perang Dunia Ke-2).

> Penulisan angka dan akhiran -an dirangkaikan dengan tanda hubung (-).

| Tepat | Tidak tepat |
|---|---|
| seharga Rp2.000-an | seharga Rp2.000an |
| tahun 1980-an | tahun 1980an |

Dipasang sebagai kaidah **TMS-008** dengan pola angka empat digit yang
langsung diikuti `an` serta nominal rupiah diikuti `an`, sehingga bentuk
seperti `tahun 2024an` juga tertangkap meski tidak ada di tabel buku.
