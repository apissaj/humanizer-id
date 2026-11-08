# Ringkasan Ekstraksi Rujukan: Kalimat — Seri Penyuluhan Bahasa Indonesia (Sasangka, Badan Bahasa 2019)

## 1. Identitas Dokumen Sumber

- **Judul Buku:** *Kalimat: Seri Penyuluhan Bahasa Indonesia*
- **Penulis:** Sry Satriya Tjatur Wisnu Sasangka
- **Penyunting:** Arie Andrasyah Isa
- **Penerbit:** Badan Pengembangan Bahasa dan Perbukuan, Kementerian Pendidikan dan Kebudayaan
- **Tahun Terbit:** 2019
- **Tebal:** x + 107 halaman
- **Sifat:** Bahan penguatan pemasyarakatan bahasa Indonesia; membahas frasa, jenis kalimat, dan kalimat efektif (kelugasan, ketepatan, kejelasan, kehematan, kesejajaran).

## 2. Intisari Kaidah Preskriptif

### A. Konjungsi Syarat Berkorelasi Mubazir: *jika/kalau/apabila ... maka ...* (hlm. 80–81)
Kombinasi konjungsi subordinatif syarat (*jika, kalau, apabila*) dengan korelatif *maka* membuat kedua klausa sama-sama subordinatif sehingga kalimat tidak memiliki klausa utama. Contoh analisis buku: *\*Jika keadaan semacam itu dibiarkan berlarut-larut, maka masyarakat di daerah itu bisa kehilangan kesabaran.* Perbaikan: gugurkan *maka* — *Jika keadaan semacam itu dibiarkan berlarut-larut, masyarakat di daerah itu bisa kehilangan kesabaran.*

### B. Objek Verba Transitif Disisipi Preposisi: *memerintahkan kepada X* (hlm. 78)
Contoh buku: *\*Pasal 52 ayat (2) UU SJSN memerintahkan kepada keempat badan tersebut untuk melakukan penyesuaian dengan UU SJSN* — struktur S-P-K-K yang rancu karena verba transitif *memerintahkan* kehilangan objek langsungnya. Perbaikan: *memerintahkan penyesuaian dengan UU SJSN kepada keempat badan tersebut* (S-P-O-K) atau *memerintah keempat badan tersebut untuk melakukan penyesuaian*.

### C. Penghubung Bertentangan Rangkap Tiga: *walaupun ... namun ... maka ...* (hlm. 82–84)
Penumpukan tiga konjungsi dalam satu kalimat majemuk (*walaupun/meskipun/sungguhpun + namun/tetapi + maka*) memotong klausa utama sehingga seluruh rangkaian berstatus anak kalimat. Buku menegaskan konjungsi *tetapi* mensyaratkan kedua klausa yang dihubungkan sejenis; perbaikannya memilih satu konjungsi dan mempertahankan satu klausa utama berpredikat mandiri.

### D. Ketidakefektifan Lain yang Terdokumentasi (hlm. 64–70)
- Pengisi mubazir *mau tidak mau* dan penegas semu *[nomina] itu sendiri* (hlm. 64–65) — sudah tercakup `SPB-002`.
- Kalimat beranak *yang* bertingkat tanpa predikat utama (hlm. 66) — sudah tercakup `SPB-004`.
- Ketaksaan penempatan adverbia *baru* (hlm. 74–75): *pelatihan karyawan baru dapat dilaksanakan* ambigu antara 'karyawan baru' dan 'baru dilaksanakan'.

### E. Pengutip Preposisional Merusak Subjek (hlm. 28–29)
Kalimat berstruktur **K-P-O** tidak ada dalam tipe kalimat dasar bahasa Indonesia. Frasa preposisional pengutip di awal kalimat (*menurut, dengan, dalam*) mengubah nomina berikutnya menjadi keterangan sehingga verba aktif transitif kehilangan subjek:
- *\*Menurut pakar lain di bidang pemasaran menyatakan bahwa ...*
- *\*Dengan perubahan zaman menuntut para pendidik ...*
- *\*Dalam debat calon presiden itu memutuskan bahwa ...*
Perbaikan: hapus preposisi (nomina menjadi subjek: *Pakar lain menyatakan bahwa ...*) atau pindahkan struktur ke K-S-P-Pel (*Menurut pakar lain, pemasaran adalah proses ...*).

### F. Kalimat Tanpa Predikat Berakhir Frasa Preposisional (hlm. 33–35)
Tuturan perundang-undangan dan laporan kerap berhenti pada keterangan: *\*Gaji guru yang diangkat oleh satuan pendidikan yang diselenggarakan oleh masyarakat dengan berdasarkan pada perjanjian kerja ...* — struktur S-K tanpa predikat sehingga belum menjadi kalimat (tidak mengungkapkan informasi utuh). Perbaikan: wajib memunculkan predikat (*... dibayar sesuai perjanjian kerja* / *... adalah setara dengan ...*). Catatan: frasa *dengan berdasarkan pada* itu sendiri juga tidak baku menurut TBBBI (lihat `TBB-005`), sehingga perbaikan terbaik menggantinya dengan *sesuai*.

---

## 3. Pemetaan ke Dataset `data/kalke-indonesia.json`

| ID | Kaidah | Kategori | Kode Regex Utama |
|---|---|---|---|
| `SPK-001` | *jika/kalau/apabila ... maka ...* | `retorika_klise_ai` | `\b(jika\|kalau\|apabila)\b[^.!?]*\b,?\s*maka\b` |
| `SPK-002` | *memerintahkan/menugaskan/menganjurkan/mempersilakan kepada X* | `retorika_klise_ai` | `\b(memerintahkan\|menugaskan\|menganjurkan\|mempersilakan)\s+kepada\b` |
| `SPK-003` | Rangkap tiga *walaupun ... namun/tetapi ... maka ...* | `retorika_klise_ai` | `\b(walaupun\|meskipun\|sungguhpun\|sekalipun)\b[^.!?]*\b(namun\|tetapi)\b[^.!?]*\b,?\s*maka\b` |
| `SPK-004` | Pengutip preposisional + verba transitif tanpa subjek (*Menurut X menyatakan bahwa ...*) | `retorika_klise_ai` | `\b(Menurut\|Dengan\|Dalam)\s+[^.!?]{2,60}?\b(menyatakan\|menuntut\|...)\s+(bahwa\|para\|...)\b` |
| `SPK-005` | Kalimat tanpa predikat berakhir *dengan berdasarkan pada ...* | `retorika_klise_ai` | `^[A-Z][^.!?]*\byang\b[^.!?]*\byang\b[^.!?]*\bdengan\s+berdasarkan\s+pada\b[^.!?]*\.` |
