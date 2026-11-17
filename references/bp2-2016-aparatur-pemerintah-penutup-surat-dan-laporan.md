# Bahasa Indonesia untuk Aparatur Pemerintah (Badan Bahasa, 2016) - penutup surat dan laporan

Sumber: Mustakim, *Seri Penyuluhan Bahasa Indonesia: Bahasa Indonesia untuk
Aparatur Pemerintah*, Pusat Pembinaan, Badan Pengembangan dan Pembinaan Bahasa,
Kemendikbud, Jakarta, 2016. Bagian yang dibedah: 3.5 (hlm. 66-68), 3.6
(hlm. 69-73), dan Bab IV (hlm. 73-80). Kutipan verbatim dari `pdftotext`;
salah baca OCR ditandai `[OCR]`.

## 1. Pukul dan jam (hlm. 67)

> Pada paragraf isi seperti yang dicontohkan di atas, penggunaan kata pukul dan
> jam hendaknya dibedakan. Untuk menunjukkan waktu seperti pada contoh tersebut,
> kata yang lebih tepat digunakan adalah pukul, bukan jam. Hal itu karena kata
> jam dalam komunikasi resmi tidak digunakan untuk menyatakan waktu, tetapi
> digunakan untuk menyatakan benda penunjuk waktu, misalnya jam tangan, atau
> lamanya waktu (durasi), misalnya Rapat itu berlangsung selama tiga jam.

> Setelah kata pukul harus diikuti angka yang menunjukkan waktu permulaan acara
> dan batas akhir acara, misalnya pukul 09.00-12.00.

Catatan: data sudah punya `BPK-007` (*Bentuk dan Pilihan Kata*, Mustakim 2019,
hlm. 78) dengan isi yang sama, tetapi **matchernya belum pernah ada** sehingga
kaidah itu tidak pernah menyala. Siklus ini memasang matcher untuk `BPK-007`
alih-alih membuat ID baru: `jam 08.30` dan label `Jam: 09.00` ditandai, sedangkan
`selama tiga jam` (durasi) dan `jam tangan` (arloji) tidak.

Bentuk `pukul 09.00-selesai` juga dicela buku, tetapi tidak dipola: penandanya
kata *selesai* yang lazim pada naskah lain (`Acara berlangsung sampai selesai`).

## 2. Paragraf penutup: pelaku dan pronomina (hlm. 67-69)

Contoh tidak tepat (verbatim): `Atas perhatiannya, diucapkan terima kasih.`,
`Demikian atas bantuan Saudara, kami ucapkan terima kasih.`, `Demikian harap
maklum, dan atas perhatian dan kerja samanya, diucapkan terima kasih.`, `Harap
maklum adanya.`

> Kalimat penutup yang pertama (1) tidak tepat karena menggunakan kata ganti -nya.
> Kata ganti -nya merupakan pengganti orang ketiga, sedangkan komunikasi dalam
> surat itu disampaikan kepada orang kedua ...

> kata ganti yang digunakan sebagai pengganti penanda tangan surat adalah kami,
> bukan saya. Meskipun penanda tangan surat itu hanya satu orang, dia mewakili
> instansi, bukan atas nama dirinya sendiri.

Catatan: tidak ada kaidah baru. Seluruh bentuk itu sudah tercakup `SRT-001`,
`DIN-003`, dan `SMD-002` (pronomina `-nya` pada komunikasi orang kedua). Saran
`DIN-003` sudah berbunyi "Atas perhatian Saudara ... kami ucapkan terima kasih",
yaitu perbaikan rangkap yang diminta buku ini (buang `-nya`, ganti pelaku
pasif `diucapkan` menjadi `kami ucapkan`). Menambah kaidah `diucapkan terima
kasih` hanya akan menandai kalimat yang sama dua kali.

Pembedaan sapaan bapak/ibu (atasan) dan saudara (setingkat atau bawahan)
bergantung konteks organisasi; dicatat `[telaah]`.

## 3. Salam penutup (hlm. 69-70)

> Salam penutup wajib ditulis jika surat yang bersangkutan diawali dengan salam
> pembuka. ... ditulis dengan huruf awal kapital dan diakhiri dengan tanda koma.

> Ungkapan salam kami digunakan jika jabatan penanda tangan surat lebih tinggi
> kedudukannya daripada jabatan pihak yang dikirimi surat. Adapun ungkapan hormat
> kami dan salam takzim digunakan jika jabatan penanda tangan surat lebih rendah
> daripada jabatan yang dikirimi surat.

Catatan: pemilihan *salam kami* / *hormat kami* bergantung kedudukan jabatan
yang tidak terbaca dari teks; `[telaah]`.

## 4. NIP (hlm. 71)

> Nomor induk pegawai, yang disingkat NIP, ditulis di bawah dan sejajar dengan
> nama pejabat penanda tangan surat, menggunakan huruf kapital tanpa diakhiri
> dengan tanda titik dan diikuti dengan nomor tanpa jarak.

> Singkatan NIP harus seluruhnya ditulis dengan huruf kapital karena seluruh
> huruf pada singkatan itu diambil dari huruf awal kata ... tidak dibenarkan
> singkatan itu hanya huruf awalnya yang ditulis dengan huruf capital. Misalnya:
> Nip 195900071989031003

> Angka yang digunakan sebagai nomor NIP juga tidak menunjukkan jumlah. Oleh
> karena itu, tidak dibenarkan diserta dengan titik ataupun spasi setiap tiga
> angka atau pada batas tertentu. ... Misalnya: NIP 197 101 031 991 032004
> NIP 197101 03 1991032004

Kaidah `TMS-027` menangkap dua bentuk: `Nip` berkapitalisasi campur dan `NIP`
yang angkanya dipisah spasi menjadi beberapa kelompok. Bentuk `NIP. 1959...`
sudah ditangani `DIN-006`, jadi tidak diduplikasi.

Temuan sampingan: matcher `MBI-004` (identitas responden tanpa anonimisasi)
memakai pola `(?:NIK|NIP|No. KTP)\s*[:=]?\s*\d{4,}` sehingga **setiap** NIP pada
blok tanda tangan surat resmi ikut ditandai sebagai pelanggaran privasi. `NIP`
dikeluarkan dari pola itu; contoh salah `MBI-004` sendiri memang memakai NIK
(`Ahmad Dani (NIK 3201...)`), bukan NIP. Pemformatan NIP tetap dijaga `DIN-006`
dan `TMS-027`.

## 5. Tembusan (hlm. 72)

> Kata tembusan ditulis dengan huruf awal kapital, diikuti tanda baca titik dua,
> tanpa garis bawah ... Pihak yang diberi tembusan ditulis di bawah kata tembusan
> dan, apabila pihak yang diberi tembusan lebih dari satu, diberi nomor urut
> dengan angka Arab. Pihak yang diberi tembusan tidak didahului singkatan Yth.
> dan tidak diikuti frasa sebagai laporan. Apabila tidak ada pihak yang diberi
> tembusan, kata tembusan tidak perlu ditulis.

> Pada bagian akhir pihak yang diberi tembusan tidak diikuti tanda titik koma.

Kaidah `TMS-028` menangkap `Tembusan: Yth. ...` dan `Tembusan: ... sebagai
laporan`. Larangan titik koma di akhir daftar tembusan tidak dipola: titik koma
juga tanda baca sah di tempat lain, dan posisinya hanya bisa dinilai dari tata
letak surat, bukan dari teks mentah.

## 6. Bab IV: penulisan laporan (hlm. 73-80)

Isi bab ini hampir seluruhnya berupa tata letak dan kelengkapan bagian laporan:
halaman sampul, halaman judul, kata pengantar, daftar isi, daftar lambang,
pendahuluan, pembahasan, simpulan dan saran, daftar pustaka. Tidak ada pasangan
bentuk-salah/bentuk-benar yang bisa dipola, dengan dua pengecualian yang keduanya
tetap `[telaah]`:

> Tahun penulisan laporan itu cukup dituliskan angkanya saja, tidak perlu
> disertai kata tahun. Angka tahun itu ditulis tahun ketika laporan itu
> diselesaikan, tidak ditulis seperti tahun ajaran. Misalnya: 2015, bukan
> 2015/2016.

Alasan tidak dipola: bentuk `2015/2016` juga sah untuk tahun anggaran, tahun
akademik, dan rentang dua tahun pada teks nonlaporan, sehingga penandanya akan
menghasilkan salah tuduh di luar konteks halaman sampul.

> Judul laporan ditulis seluruhnya dengan menggunakan huruf kapital. ... judul
> bab ditulis seluruhnya dengan menggunakan huruf kapital, sedangkan judul
> subbabnya hanya huruf awal setiap unsur yang ditulis dengan huruf kapital,
> kecuali yang berupa kata depan atau kata sambung.

Alasan tidak dipola: kapitalisasi judul bergantung posisi (judul bab, subbab,
awal kalimat, nama diri) sehingga satu pola akan menandai pemakaian yang benar.
