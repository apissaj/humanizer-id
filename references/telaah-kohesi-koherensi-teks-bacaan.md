# Telaah Preskriptif: Kohesi dan Koherensi Wacana Teks Bacaan (Universitas Indonesia 2018)

Dokumen ini memuat telaah kebahasaan preskriptif dan formulasi aturan audit operasional yang diekstraksi dari penelitian analisis wacana Widyantika Afiatna Maharani (Universitas Indonesia, 2018). Kajian ini ditujukan untuk melengkapi aturan audit Humanizer ID terkait kepaduan wacana teks, penataan konjungsi konsekuensi, batas variasi repetisi leksikal, dan konsistensi taksonomi meronimi–hiponimi.

---

## 1. Identitas Dokumen Sumber

- **Judul Dokumen:** *Kohesi dan Koherensi Teks Bacaan dalam Buku Bahasa Indonesia Kelas XII Semester 2*
- **Penulis:** Widyantika Afiatna Maharani
- **Afiliasi:** Program Studi Pascasarjana Linguistik / Ilmu Budaya, Universitas Indonesia
- **Publikasi:** Repositori Ilmiah Kemendikbudristek RI
- **Tebal Berkas:** 19 halaman (hlm. 1–19)
- **Repositori ID:** 10507
- **Fokus Kajian:** Analisis empiris piranti kohesi gramatikal (referensi, konjungsi, substitusi, elipsis), kohesi leksikal (repetisi, sinonimi, antonimi, hiponimi, meronimi, kolokasi), serta hubungan koherensi aditif dan kausal pada korpus teks bacaan buku ajar Kurikulum 2013 edisi 2015.

---

## 2. Analisis Substansi Kebahasaan Preskriptif

Penelitian Maharani (hlm. 6–18) menguji secara tekstual bagaimana wacana buku ajar kerap memuat kerancuan kohesi yang membingungkan siswa dan pembaca akademik:

1. **Pembedaan Ranah Referensi vs Elipsis/Substitusi (hlm. 6–7):**
   Referensi (anafora/katafora) memiliki daya jangkau bebas ke belakang (*long-range anaphora*). Namun, **elipsis dan substitusi terikat ketat pada batas klausa lokal (*immediate clause boundary*)**. Pelesapan subjek atau objek melintasi alinea membuat kalimat kehilangan subjek gramatikal secara permanen (telah diakomodasi sebagian dalam `KOH-002`).
2. **Penyalahgunaan Konjungsi Konsekuensi "Maka" di Awal Kalimat (hlm. 17, Wacana 21):**
   Peneliti mengidentifikasi cacat sintaksis wacana tajuk rencana (*Wacana 21*): *"Dengan demikian, bermula dari masalah kesehatan dalam keluarga akan dapat menimbulkan masalah lain... Maka, melalui tajuk rencana ini masyarakat diingatkan..."*. Konjungsi subordinatif intrakalimat *maka* dipakai mengawali kalimat mandiri baru tanpa adanya klausa syarat (*jika/kalau/apabila*).
3. **Monotoni Repetisi Leksikal Tanpa Substitusi (hlm. 13, 18, Wacana 9):**
   Peneliti mengkritik wacana yang mengulang leksem nomina inti yang sama secara beruntun (*Wacana 9*: kata *sastra* diulang 4 kali pada 4 kalimat berurutan). Hal ini memperlihatkan kemiskinan variasi diksi dan kegagalan memanfaatkan piranti substitusi atau sinonimi wacana.
4. **Pembedaan Taksonomis Hiponimi vs Meronimi (hlm. 8–9, 14, Wacana 13):**
   Glosarium wacana membedakan relasi *superordination* (hiponimi: relasi jenis/contoh, misal *sapi adalah jenis ternak*) dengan *composition* (meronimi: relasi bagian, misal *jantung adalah bagian organ tubuh*, bukan *jenis organ tubuh*). Perancuan kedua relasi ini dalam klausa perincian mengaburkan taksonomi ilmiah naskah.
5. **Kaidah Elipsis Nomina pada Deret Koordinatif Bertingkat (hlm. 12–13, Wacana 7):**
   Pelesapan nomina inti yang sah wajib mempertahankan anteseden lengkap pada konstituen kepala pertama deret perincian sebelum dilesapkan pada pewatas ordinal berikutnya.

---

## 3. Draf Kaidah Kebahasaan Baru (Integrasi Basis Aturan Audit)

Berikut adalah 4 usulan kaidah kebahasaan baru hasil telaah yang diverifikasi **tidak menduplikasi** entri yang sudah ada di `data/kalke-indonesia.json` (entri lama: `KOH-001` [konjungsi *sedangkan* di awal kalimat] dan `KOH-002` [elipsis subjek melompati batas paragraf]):

---

### Kaidah 1: KOH-003 (Penyalahgunaan Konjungsi Konsekuensi Intrakalimat "Maka" di Awal Kalimat)
- **ID:** `KOH-003`
- **Pola:** Konjungsi intrakalimat akibat/konsekuensi `Maka` diletakkan di posisi pertama awal kalimat mandiri (diawali huruf kapital setelah tanda titik) tanpa didahului klausa pengandaian/syarat (`Jika ..., maka ...`).
- **Saran Pengganti:** Ganti dengan konjungsi antarkalimat penanda kesimpulan atau konsekuensi baku: *"Oleh karena itu,"*, *"Oleh sebab itu,"*, atau satukan klausa tersebut ke dalam kalimat majemuk bertingkat pengandaian (Maharani, UI 2018, hlm. 17).
- **Penjelasan:** Maharani (hlm. 17, analisis Wacana 21) menemukan kekeliruan penempatan konjungsi subordinatif akibat *maka* di awal kalimat tunggal: *"Maka, melalui tajuk rencana ini masyarakat diingatkan..."*. Menurut tata bahasa baku, *maka* hanya berfungsi sebagai pengantar klausa utama yang berpasangan dengan anak kalimat bersyarat (*jika/bila/apabila/karena*). Menjadikan *maka* sebagai konjungsi antarkalimat melanggar aturan sintaksis subordinatif.
- **Contoh Salah:** "Perekonomian global diperkirakan menghadapi tantangan likuiditas yang berat. Maka, perbankan nasional wajib memperkuat cadangan modal."
- **Contoh Benar:** "Perekonomian global diperkirakan menghadapi tantangan likuiditas yang berat. Oleh karena itu, perbankan nasional wajib memperkuat cadangan modal."

---

### Kaidah 2: KOH-004 (Monotoni Leksikal akibat Repetisi Nomina Beruntun Tanpa Substitusi)
- **ID:** `KOH-004`
- **Pola:** Pengulangan kata benda/nomina leksikal yang sama persis lebih dari 3 kali berturut-turut pada posisi subjek atau objek dalam satu alinea tanpa memanfaatkan variasi pronomina persona, demonstratif rujukan, atau parafrasa sinonimik.
- **Saran Pengganti:** Variasikan kohesi teks dengan piranti substitusi (*"karya ini"*, *"perangkat tersebut"*), pronomina anaforis (*"-nya"*, *"ia"*), atau variasi leksikal ekuivalen (Maharani, UI 2018, hlm. 13, 18).
- **Penjelasan:** Maharani (hlm. 13 & 18, analisis Wacana 9) menyoroti paragraf yang mengulang leksem subjek secara mekanis: *"Sastra erat kaitannya... Sastra lahir... Sastra juga merupakan... Sastra yang telah dilahirkan..."*. Pengulangan mekanis ini mencirikan kemiskinan variasi leksikal yang sering kali dihasilkan oleh model bahasa AI generatif. Teks yang kohesif memanfaatkan anafora definit dan sinonimi gramatikal untuk menjaga dinamika wacana.
- **Contoh Salah:** "Kecerdasan buatan berkembang sangat cepat. Kecerdasan buatan dimanfaatkan dalam berbagai industri. Kecerdasan buatan mampu mengotomatisasi pekerjaan rutin. Kecerdasan buatan juga memicu tantangan etika baru."
- **Contoh Benar:** "Kecerdasan buatan berkembang sangat pesat dan mulai dimanfaatkan dalam beragam lini industri. Teknologi ini mampu mengotomatisasi pekerjaan rutin, meski penerapannya tetap memicu sejumlah tantangan etika baru."

---

### Kaidah 3: KOH-005 (Kerancuan Logika Taksonomis Relasi Bagian / Meronimi vs Jenis / Hiponimi)
- **ID:** `KOH-005`
- **Pola:** `[telaah] pencampuradukan pemarkah relasi bagian-keseluruhan (meronimi/composition) dengan pemarkah relasi jenis-subkelas (hiponimi/superordination) pada kalimat definisi atau perincian taksonomi`
- **Saran Pengganti:** Bedakan secara tegas antara *"merupakan bagian dari [entitas utuh]"* (meronimi: otak, ginjal adalah bagian tubuh) dengan *"merupakan jenis/ragam dari [kategori umum]"* (hiponimi: hipertensi adalah jenis penyakit) (Maharani, UI 2018, hlm. 8–9, 14).
- **Penjelasan:** Dalam telaah kohesi leksikal (Maharani, UI 2018, hlm. 8–9 & analisis Wacana 13), hiponimi merepresentasikan relasi inklusi hierarkis (*X adalah jenis dari Y*), sedangkan meronimi merepresentasikan relasi konstituen fisik (*A adalah bagian dari B*). Menyamakan penyebutan organ tubuh (*meronim*) sebagai varian atau ragam kelompok (*hiponim*) merusak ketepatan taksonomi klasifikasi ilmiah.
- **Contoh Salah:** "Penelitian ini mengklasifikasikan tiga jenis utama sistem komputer, yaitu CPU, memori RAM, dan papan induk."
- **Contoh Benar:** "Penelitian ini membedakan tiga komponen perangkat keras utama komputer, yaitu CPU, memori RAM, dan papan induk."

---

### Kaidah 4: KOH-006 (Kerancuan Posisi Elipsis Nomina pada Deret Koordinatif Pewatas Bertingkat)
- **ID:** `KOH-006`
- **Pola:** Pelesapan konstituen nomina inti di muka deret perincian bertingkat yang menyisakan hanya adjektiva/ordinal penjelas tanpa anteseden yang jelas di awal frasa (`memilih yang pertama, suku kata kedua, atau yang ketiga`).
- **Saran Pengganti:** Cantumkan nomina inti secara lengkap pada perincian pertama deret koordinatif, lalu lesapkan secara konsisten pada unsur perincian sesudahnya: *"memilih suku kata pertama, kedua, atau ketiga"* (Maharani, UI 2018, hlm. 12–13).
- **Penjelasan:** Maharani (hlm. 12–13, analisis Wacana 7) menganalisis kalimat: *"Huruf atau suku kata manakah dari sebuah kata yang mesti dicomot: [huruf atau suku kata] yang pertama, yang tengah, yang akhir..."*. Kaidah elipsis yang ekonomis menempatkan nomina kepala di awal deret sebelum pelepasan adjektival subordinatif. Inkonsistensi posisi pelesapan membuat pembaca kehilangan jangkar acuan gramatikal.
- **Contoh Salah:** "Peserta ujian dapat mengerjakan yang pertama, soal kedua, atau nomor ketiga secara bebas."
- **Contoh Benar:** "Peserta ujian dapat mengerjakan soal pertama, kedua, atau ketiga secara bebas."

---

## 4. Draf Entri JSON Siap Pakai (`data/kalke-indonesia.json`)

```json
[
  {
    "id": "KOH-003",
    "pola": "konjungsi konsekuensi intrakalimat maka di posisi awal kalimat baru",
    "saran_pengganti": [
      "Oleh karena itu,",
      "Oleh sebab itu,",
      "Dengan demikian,"
    ],
    "penjelasan": "Konjungsi intrakalimat 'maka' hanya berfungsi mengantar klausa utama setelah klausa syarat (jika/apabila); pemakaiannya sebagai perangkai awal kalimat mandiri melanggar kaidah subordinatif sintaksis (Maharani, UI 2018, hlm. 17).",
    "contoh_salah": "Krisis likuiditas mulai mengancam perbankan. Maka, otoritas moneter segera menaikkan suku bunga acuan.",
    "contoh_benar": "Krisis likuiditas mulai mengancam perbankan. Oleh karena itu, otoritas moneter segera menaikkan suku bunga acuan."
  },
  {
    "id": "KOH-004",
    "pola": "repetisi leksikal monoton subjek/objek lebih dari 3 kali berturut-turut dalam satu alinea tanpa substitusi",
    "saran_pengganti": [
      "gunakan pronomina persona atau demonstratif",
      "manfaatkan sinonimi leksikal konteks",
      "gabungkan beberapa klausa menjadi kalimat majemuk padu"
    ],
    "penjelasan": "Pengulangan leksem nomina yang sama secara beruntun tanpa variasi kohesi pronominal atau sinonimi mencerminkan gaya bahasa kaku khas keluaran draf mentah AI (Maharani, UI 2018, hlm. 13, 18).",
    "contoh_salah": "Vaksin telah diuji. Vaksin terbukti aman. Vaksin akan didistribusikan ke seluruh provinsi.",
    "contoh_benar": "Vaksin telah selesai diuji dan terbukti aman; produk imunisasi ini segera didistribusikan ke seluruh provinsi."
  },
  {
    "id": "KOH-005",
    "pola": "[telaah] kerancuan taksonomis relasi bagian (meronimi) dengan relasi jenis (hiponimi) pada klausa klasifikasi",
    "saran_pengganti": [
      "gunakan pemarkah bagian dari untuk relasi konstituen fisik",
      "gunakan pemarkah jenis/varian dari untuk relasi taksonomis inklusif"
    ],
    "penjelasan": "Pencampuradukan relasi bagian-keseluruhan (meronimi) dengan relasi jenis-subkelas (hiponimi) merusak ketepatan logika definisi ilmiah (Maharani, UI 2018, hlm. 8-9, 14).",
    "contoh_salah": "Laporan ini meneliti tiga jenis utama mesin mobil, yaitu piston, busi, dan karburator.",
    "contoh_benar": "Laporan ini meneliti tiga komponen utama mesin mobil, yaitu piston, busi, dan karburator."
  },
  {
    "id": "KOH-006",
    "pola": "inkonsistensi posisi pelesapan nomina inti pada deret perincian koordinatif berpewatas ordinal",
    "saran_pengganti": [
      "letakkan nomina inti di posisi pertama perincian lalu lesapkan pada ordinal berikutnya",
      "sebutkan: [Nomina] [Ordinal 1], [Ordinal 2], dan [Ordinal 3]"
    ],
    "penjelasan": "Kaidah elipsis nominal yang runtut mewajibkan penempatan nomina kepala pada awal perincian koordinatif sebelum dilesapkan pada penanda ordinal berikutnya (Maharani, UI 2018, hlm. 12-13).",
    "contoh_salah": "Siswa boleh memilih yang ganjil, paket genap, atau lembar remidi.",
    "contoh_benar": "Siswa boleh memilih paket ganjil, genap, atau remidi."
  }
]
```
