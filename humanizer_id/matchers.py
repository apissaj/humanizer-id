"""Tabel registrasi matcher data-driven untuk audit.py (Refactor Tahap 1 / P1).

Setiap aturan: (predicate_fn, [compiled_regex, ...]):
- predicate_fn: lambda p -> bool (kondisi field pola entri kaidah)
- daftar regex terkompilasi: baris dianggap memicu kaidah jika SALAH SATU cocok
  (menjaga semantik `re.search(...) or re.search(...)` dari kode asal).

Dikonversi otomatis dari rantai if-elif audit.py lama (126 cabang).
Kaidah baru cukup ditambah satu baris di sini tanpa menyentuh audit.py.
"""

import re

CUSTOM_RULES = [
    (lambda p: 'bukan berarti' in p, [re.compile('\\bbukan\\s+berarti\\b', re.IGNORECASE)]),
    (lambda p: 'antara' in p and 'dengan' in p, [re.compile('\\bantara\\b.+?\\bdengan\\b', re.IGNORECASE)]),
    (lambda p: 'baik' in p and 'ataupun' in p, [re.compile('\\bbaik\\b.+?\\bataupun\\b', re.IGNORECASE)]),
    (lambda p: 'bukan' in p and ('tetapi' in p or 'namun' in p), [re.compile('\\bbukan\\b.+?\\b(tetapi|namun)\\b', re.IGNORECASE)]),
    (lambda p: 'sedangkan' in p, [re.compile('(?:^|[.!?]\\s+)\\bsedangkan\\b', re.IGNORECASE)]),
    (lambda p: 'para tamu-tamu' in p, [re.compile('\\b(para|beberapa|semua)\\s+([a-zA-Z]+)-\\2\\b', re.IGNORECASE)]),
    (lambda p: 'karena ... maka' in p, [re.compile('\\bkarena\\b.+?\\bmaka\\b', re.IGNORECASE)]),
    (lambda p: 'meskipun ... tetapi' in p, [re.compile('\\b(meskipun|walaupun|biarpun)\\b.+?\\b(tetapi|namun)\\b', re.IGNORECASE)]),
    (lambda p: 'ganda jamak' in p, [re.compile('\\b(para|beberapa|berbagai|semua)\\s+([a-zA-Z]+)-\\2\\b', re.IGNORECASE)]),
    (lambda p: 'itu sendiri' in p or 'mau tidak mau' in p, [re.compile('\\b(itu sendiri|mau tidak mau)\\b', re.IGNORECASE)]),
    (lambda p: 'konjungsi koordinatif' in p, [re.compile('\\boleh\\s+\\w+\\s+dan\\s+\\w+\\s+yang\\b', re.IGNORECASE)]),
    (lambda p: "'yang' bertingkat" in p, [re.compile('^\\s*[A-Z][^.!?]*\\byang\\b[^.!?]*\\byang\\b[^.!?]*\\byang\\b[^.!?]*\\.$')]),
    (lambda p: 'nomor NIK' in p, [re.compile('\\b(nomor\\s+NIK|nomor\\s+PIN)\\b', re.IGNORECASE)]),
    (lambda p: 'kartu KIP' in p, [re.compile('\\b(kartu\\s+KIP|kartu\\s+KTP|ATM\\s+card)\\b', re.IGNORECASE)]),
    (lambda p: 'virus HIV' in p, [re.compile('\\bvirus\\s+HIV\\b', re.IGNORECASE)]),
    (lambda p: 'partai PPP' in p, [re.compile('\\bpartai\\s+(PPP|PDIP|PAN)\\b', re.IGNORECASE)]),
    (lambda p: 'pronomina persona taksa' in p, [re.compile('\\b[A-Z][a-z]+\\s+dan\\s+\\w+\\b[^.!?]{2,80}\\b(ia|dia)\\b', re.IGNORECASE)]),
    (lambda p: 'hierarki kata umum-khusus' in p, [re.compile('\\bjangankan\\b[^.!?]{0,60}\\bpun\\b', re.IGNORECASE)]),
    (lambda p: 'urutan sebab-akibat' in p or 'akibat-sebab terbalik' in p, [re.compile('(?:^|[.!?]\\s+)\\b(oleh sebab itu|oleh karena itu|karena itu)\\b', re.IGNORECASE)]),
    (lambda p: 'nama diri geografi yang menjadi nama jenis' in p, [re.compile('\\b(Kunci\\s+Inggris|Pisang\\s+Ambon|Mesin\\s+Diesel|15\\s+Watt)\\b')]),
    (lambda p: 'bentuk dasar turunan nama bangsa' in p, [re.compile('\\b(Peng-Indonesia-an|Keinggris-Inggrisan|Pengindonesiaan)\\b')]),
    (lambda p: 'jabatan/pangkat tanpa nama orang' in p, [re.compile('\\b(Sejumlah\\s+Menteri|rapat\\s+Kabinet|para\\s+Gubernur|para\\s+Menteri)\\b')]),
    (lambda p: 'imbuhan di- ditulis terpisah' in p, [re.compile('\\bdi\\s+(analisis|teliti|observasi|kembangkan|temukan|gunakan|lakukan|tulis|baca|uji)\\b', re.IGNORECASE)]),
    (lambda p: 'sedangkan dipakai di awal kalimat' in p, [re.compile('(?:^|[.!?]\\s+)\\bSedangkan\\b')]),
    (lambda p: 'elipsis subjek melompati' in p, [re.compile('(?:^|[.!?]\\s+)\\b(Perlu|Harus|Dapat|Mungkin|Sebaiknya|Bisa)\\s+(dilakukan|diperhatikan|dipertimbangkan|ditinjau|disimpulkan|dicatat|diketahui|disebutkan|dilihat|dipahami)\\b', re.IGNORECASE)]),
    (lambda p: 'atas perhatiannya' in p, [re.compile('\\bAtas perhatiannya\\b|\\bkerja samanya\\b', re.IGNORECASE)]),
    (lambda p: 'Kepada Yth.' in p, [re.compile('\\bKepada\\s+Yth\\.\\s+Bapak\\s+[A-Z]')]),
    (lambda p: 'titik dua sebelum pelengkap' in p, [re.compile('\\b(memerlukan|membutuhkan|membeli|menyediakan|membawa|menggunakan|meliputi):\\s+\\w+', re.IGNORECASE)]),
    (lambda p: 'partikel pun ditulis serangkai' in p, [re.compile('\\b(apapun|siapapun|satupun|berapapun|dimanapun|kapanpun|bagaimanapun(?:\\s)?[^,])\\b', re.IGNORECASE)]),
    (lambda p: 'membahas tentang' in p, [re.compile('\\b(membahas|membicarakan|mempelajari|meneliti|mengkaji|menguraikan)\\s+(tentang|mengenai)\\b', re.IGNORECASE)]),
    (lambda p: 'kalimat tanpa subjek berawalan preposisi' in p, [re.compile('(?:^|[.!?]\\s+)\\b[Dd]alam\\s+\\w+\\s*(?:ini|tersebut)\\s+(?:akan\\s+)?(?:membahas|membicarakan|meneliti|menganalisis|mengkaji|menguraikan|menyajikan|mengevaluasi|mengungkap|memaparkan)\\b')]),
    (lambda p: 'Karena itu,' in p, [re.compile('(?:^|[.!?]\\s+)\\bKarena itu,\\s+')]),
    (lambda p: 'Selain itu (tanpa koma)' in p, [re.compile('(?:^|[.!?]\\s+)\\bSelain itu(?!,)\\s+\\S', re.IGNORECASE)]),
    (lambda p: 'namun intrakalimat tanpa koma' in p, [re.compile('(?<!,)\\s+\\bnamun\\b\\s+\\S', re.IGNORECASE)]),
    (lambda p: ', sehingga' in p, [re.compile(',\\s*sehingga\\b', re.IGNORECASE)]),
    (lambda p: ', karena' in p, [re.compile(',\\s*karena\\b', re.IGNORECASE)]),
    (lambda p: 'hanya ... saja' in p, [re.compile('\\bhanya\\b[^.!?]{1,40}\\bsaja\\b', re.IGNORECASE)]),
    (lambda p: 'pleonasme pasangan sinonim' in p, [re.compile('\\b(agar\\s+supaya|demi\\s+untuk|lalu\\s+kemudian|kalau\\s+seandainya|seperti\\s+misalnya|contohnya\\s+seperti)\\b', re.IGNORECASE)]),
    (lambda p: 'antara lain lalu ditutup' in p, [re.compile('\\b(misalnya|seperti|contohnya|umpamanya|antara lain)\\b[^.!?]{4,120}?\\b(dan\\s+lain-lain|dan\\s+sebagainya|dan\\s+seterusnya)\\b', re.IGNORECASE)]),
    (lambda p: 'bentuk ulang resiprokal' in p, [re.compile('\\bsaling\\s+(\\w+)-(\\w+)\\b', re.IGNORECASE), re.compile('\\bsaling\\s+ber\\w+an\\b', re.IGNORECASE)]),
    (lambda p: 'penyalahgunaan dan sebagainya' in p, [re.compile('\\b(sesi\\s+\\w+,\\s*sesi\\s+\\w+|pertama,\\s*\\w+,\\s*kedua)[^.!?]{0,60}\\bdan\\s+lain-lain\\b', re.IGNORECASE)]),
    (lambda p: 'ungkapan idiomatis dihilangkan' in p, [re.compile('\\b(sesuai|berkaitan|sehubungan)\\s+(?!dengan\\b)(?=(tidak|kurang|konteks|hal|masalah|perkara|ketentuan|aturan))', re.IGNORECASE), re.compile('\\b(bergantung|tergantung)\\s+(?!pada\\b)(?=(hasil|kondisi|keputusan|situasi|tingkat))', re.IGNORECASE)]),
    (lambda p: 'makna asal/sumber/penjelasan' in p, [re.compile('\\bterbuat\\s+daripada\\b|\\btujuan\\s+daripada\\b|\\bmaksud\\s+daripada\\b|\\bterbuat\\s+\\w*\\s*daripada\\b', re.IGNORECASE)]),
    (lambda p: 'menggugurkan konsonan akhir' in p, [re.compile('\\b(dominant|informant|tolerant|relevant|optimist|realist|nationalist|manifest|latent|konsultan?\\w*ant)\\b', re.IGNORECASE)]),
    (lambda p: 'istilah klasik/generik dijauhkan' in p, [re.compile('\\bzat\\s+lemas\\b|\\bzat\\s+air\\b|\\bzat\\s+asam\\b|\\billmu\\s+pasti\\b|\\billmu\\s+pisah\\b|\\bsaran\\s+diri\\b', re.IGNORECASE)]),
    (lambda p: 'awalan non- dipertahankan mentah' in p, [re.compile('\\bnon-\\s?\\w+|\\bnon\\s\\w+', re.IGNORECASE)]),
    (lambda p: 'bentuk jamak Latin/Inggris' in p, [re.compile('\\bfoki\\b|\\blaboratoria\\b|\\bcriteria\\b|\\bphenomena\\b', re.IGNORECASE)]),
    (lambda p: 'akhiran keahlian -wan' in p, [re.compile('\\b\\w+logiwan\\b|\\bteknikwan\\b|\\bsainswan\\b|\\bhukumwan\\b|\\bekonomiwan\\b|\\bmanajemenwan\\b', re.IGNORECASE)]),
    (lambda p: 'pemukiman dipakai untuk menyebut kawasan' in p, [re.compile('\\bpemukiman\\s+(padat|kumuh|liar|warga|penduduk|baru|transmigran|pedesaan|perkotaan)\\b|\\bkawasan\\s+pemukiman\\b|\\barea\\s+pemukiman\\b', re.IGNORECASE)]),
    (lambda p: 'pengubahan dipakai untuk keadaan' in p, [re.compile('\\bpengubahan\\s+(iklim|sosial|zaman|sikap|cuaca|pola)\\b', re.IGNORECASE)]),
    (lambda p: 'metanalisis palsu akhiran asing' in p, [re.compile('\\bsinergitas\\b|\\bstandarisasi\\b|\\befektifitas\\b|\\baktifitas\\b', re.IGNORECASE)]),
    (lambda p: 'gabungan bentuk bebas ditulis serangkai' in p, [re.compile('\\bibukota\\b|\\bkerjasama\\b|\\bbatubara\\b|\\banakperusahaan\\b|\\btokoserbaada\\b', re.IGNORECASE)]),
    (lambda p: 'peluluhan peN- keliru pada nomina pelaku' in p, [re.compile('\\bpengrajin\\b|\\bpenterjemah\\b|\\bpensurvei\\b|\\bpembom\\b', re.IGNORECASE)]),
    (lambda p: 'melainkan dipasangkan dengan tidak' in p, [re.compile('\\btidak\\s+[^.!?]{2,80}?\\bmelainkan\\b', re.IGNORECASE)]),
    (lambda p: 'perincian tidak sejajar bentuknya' in p, [re.compile('\\bmeliputi\\b[^.!?]*\\b(membuat|diberi|dilakukan|menambah|mengubah)\\b', re.IGNORECASE)]),
    (lambda p: 'salah nalar frasa bebas parkir' in p, [re.compile('\\bbebas\\s+parkir\\b', re.IGNORECASE)]),
    (lambda p: 'kerancuan sufiksasi proses vs hasil' in p, [re.compile('\\bproses\\s+pinjaman\\b|\\bproses\\s+pisahan\\b|\\b(menerima|mengambil|membayar)\\s+peminjaman\\s+(uang|buku|dana|modal)\\b', re.IGNORECASE)]),
    (lambda p: "penerjemahan harfiah kaku pada frasa 'linguistic'" in p, [re.compile('\\bketerampilan\\s+linguistik\\b|\\batlas\\s+linguisti[ks]\\b', re.IGNORECASE)]),
    (lambda p: 'struktur frasa padanan terbalik' in p, [re.compile('\\bnominatif\\s+predikat\\b|\\bterjemah\\s+pinjam\\b', re.IGNORECASE)]),
    (lambda p: 'penyerapan fonem klasik keliru' in p, [re.compile('\\bbahasa\\s+sentum\\b|\\bsenematika\\b|\\bapokop\\b', re.IGNORECASE)]),
    (lambda p: 'preposisi titik waktu tidak baku' in p, [re.compile('\\bdi\\s+(tahun|hari|saat|awal|akhir|tengah|minggu|bulan|jam|waktu|masa|periode|era|dekade)\\b', re.IGNORECASE)]),
    (lambda p: 'pleonasme preposisi majemuk' in p, [re.compile('\\bselain\\s+daripada\\b|\\bselain\\s+dari\\s+(itu|pada|laporan|biaya|data|hal|aspek|faktor)\\b', re.IGNORECASE)]),
    (lambda p: 'preposisi arah/lokasi ditulis serangkai tanpa spasi' in p, [re.compile('\\b(didalam|kedalam|diatas|keatas|dibawah|kebawah|didepan|kedepan|dibelakang|kebelakang|disamping|kesamping)\\b', re.IGNORECASE)]),
    (lambda p: 'konjungsi syarat berkorelasi mubazir' in p, [re.compile('\\b(jika|kalau|apabila)\\b[^.!?]*\\b,?\\s*maka\\b', re.IGNORECASE)]),
    (lambda p: 'objek verba transitif disisipi preposisi' in p, [re.compile('\\b(memerintahkan|menugaskan|menganjurkan|mempersilakan)\\s+kepada\\b', re.IGNORECASE)]),
    (lambda p: 'penghubung bertentangan rangkap tiga' in p, [re.compile('\\b(walaupun|meskipun|sungguhpun|sekalipun)\\b[^.!?]*\\b(namun|tetapi)\\b[^.!?]*\\b,?\\s*maka\\b', re.IGNORECASE)]),
    (lambda p: 'pemakaian jam alih-alih pukul' in p, [re.compile('\\b(pada|sejak|hingga|sampai)\\s+jam\\b|\\bjam\\s+\\d{1,2}[.:]\\d{2}\\b', re.IGNORECASE)]),
    (lambda p: 'verba kopula predikat definisi' in p, [re.compile('\\b\\w+\\s+yaitu\\s+(suatu|sebuah|metode|metoda|algoritma|teknik|proses|istilah|model|sistem|bentuk|cara|konsep|sifat|fungsi|keadaan|aktivitas)\\b', re.IGNORECASE)]),
    (lambda p: 'kata bekas untuk mengacu pada manusia' in p, [re.compile('\\bbekas\\s+(rektor|presiden|gubernur|wali|bupati|mayor|menteri|kepala|ketua|direk|anggota|dosen|guru|kades|pejabat|jenderal|komandan|panglima|wakil)\\w*\\b', re.IGNORECASE)]),
    (lambda p: 'perincian tuntas berbilangan pasti' in p, [re.compile('\\b(dua|tiga|empat|lima)\\s+\\w+\\b[^.!?]*\\b(misalnya|antara lain)\\b', re.IGNORECASE)]),
    (lambda p: 'referensi kataforis dengan pronomina persona' in p, [re.compile('^(Dengan begitu|Dengan demikian|Karena itu|Setelah menyelidikinya)\\b[^.!?]*\\b(itu|ini|ia|dia)\\b')]),
    (lambda p: 'penomoran ordinal perincian tidak berurutan' in p, [re.compile('\\bPertama\\b[^P]{0,80}?Kedua\\b[^K]{0,80}?Ketiga\\b[^P]{0,80}?Ketiga\\b')]),
    (lambda p: 'frasa pewara tidak bernalar' in p, [re.compile('\\bwaktu\\s+dan\\s+tempat\\b[^.!?]*\\b(dipersilakan|kami\\s+persilakan|saya\\s+persilakan)\\b|\\bmengambil\\s+tempat\\s+duduknya\\s+masing-masing\\b', re.IGNORECASE)]),
    (lambda p: 'penyapa jabatan dengan honorifik ganda' in p, [re.compile('\\b(Bapak|Ibu)\\s+(Kepala|Direktur|Dekan|Rektor|Gubernur|Bupati|Wali\\s+Kota|Menteri|Ketua)\\s+(Biro|Bagian|Dinas|Jenderal|Fakultas|Universitas|Daerah|Badan|Komisi|Lembaga)\\b', re.IGNORECASE)]),
    (lambda p: 'pengutip preposisional diikuti verba aktif transitif tanpa subjek' in p, [re.compile('\\b(Menurut|Dengan|Dalam)\\s+[^.!?]{2,60}?\\b(menyatakan|menuntut|memutuskan|mengungkapkan|mengingatkan|membuktikan|mengonfirmasi)\\s+(bahwa|adalah|tentang|para)\\b')]),
    (lambda p: "tanpa predikat: subjek beranak 'yang' panjang" in p, [re.compile('^[A-Z][^.!?]*\\byang\\b[^.!?]*\\byang\\b[^.!?]*\\bdengan\\s+berdasarkan\\s+pada\\b[^.!?]*\\.')]),
    (lambda p: 'konstruksi verba nominal mubazir' in p, [re.compile('\\b(melakukan\\s+kunjungan|mengajukan\\s+saran|mengeluarkan\\s+pemberitahuan|disebabkan\\s+oleh\\s+fakta|meninggalkan\\s+kesan)\\b', re.IGNORECASE)]),
    (lambda p: 'sisipan adverbia memisahkan kata ganti pasif' in p, [re.compile('\\b(kami|kita|saya)\\s+(sudah|belum|akan|sedang|telah)\\s+(laporkan|sampaikan|kirimkan|bicarakan|bahas|putuskan|rencanakan|umumkan)\\b', re.IGNORECASE)]),
    (lambda p: 'nomina deverbal salah predikat pasif' in p, [re.compile('\\b(Pelaksanaan|Perencanaan|Penyusunan|Pemberlakuan|Penggunaan|Pelatihan|Pembaruan)\\b[^.!?]*\\b(dilaksanakan|direncanakan|disusun|diberlakukan|digunakan|dilatih|dibarukan)\\b')]),
    (lambda p: 'predikat transitif diikuti frasa preposisional perihal' in p, [re.compile('\\b(membahas|membicarakan|mengupas|menguraikan|membangun|mendukung|menangani)\\s+(tentang|mengenai|daripada)\\b', re.IGNORECASE)]),
    (lambda p: 'salah nalar semantik verba mengejar' in p, [re.compile('\\bmengejar\\s+(ketinggalan|keterbelakangan|ketertinggalan)\\b', re.IGNORECASE)]),
    (lambda p: 'klise salah kolokasi teks resmi' in p, [re.compile('\\b(bunyi\\s+(surat|edaran|nota|naskah|laporan)|surat\\s+(?:itu\\s+)?berbunyi)\\b', re.IGNORECASE)]),
    (lambda p: 'awalan ordinal ke- ditempelkan pada angka Romawi' in p, [re.compile('\\bke-[IVXLCDM]+\\b')]),
    (lambda p: 'kerancuan paronim berkenan dengan' in p, [re.compile('\\b[Bb]erkenan\\s+dengan\\b')]),
    (lambda p: 'sangat ... sekali' in p, [re.compile('\\bsangat\\s+\\w+\\s+sekali\\b', re.IGNORECASE)]),
    (lambda p: 'bukan hanya' in p, [re.compile('\\bbukan hanya\\b[^.!?]{1,60}\\b(melainkan juga|tetapi juga)\\b', re.IGNORECASE)]),
    (lambda p: 'bales / dibales' in p, [re.compile('\\b(bales|dibales|ngirim|dingirim)\\b', re.IGNORECASE)]),
    (lambda p: 'kata ganti persona' in p, [re.compile('\\b(saya|aku|kamu)\\b', re.IGNORECASE)]),
    (lambda p: "konjungsi koordinatif 'dan' tidak sejajar" in p, [re.compile('\\boleh\\s+\\w+\\s+dan\\s+\\w+\\s+yang\\s+me', re.IGNORECASE)]),
    (lambda p: 'kata kerja mental aktif' in p, [re.compile('\\b(kami|kita|saya)\\s+(berasumsi|menduga|mengira|memahami|menyadari|merasa)\\b', re.IGNORECASE)]),
    (lambda p: 'sitasi tidak lengkap' in p, [re.compile('\\bmenurut\\s+ahli\\b', re.IGNORECASE)]),
    (lambda p: 'kendati demikian (konsesif tidak paralel)' in p, [re.compile('(?:^|[.!?]\\s+)\\bKendati demikian,')]),
    (lambda p: 'unsur terikat ditulis terpisah' in p, [re.compile('\\b(sub\\s+unit|sub\\s+bagian|maha\\s+guru|peri\\s+laku|antar\\s+kota)\\b', re.IGNORECASE)]),
    (lambda p: 'Di era digital' in p, [re.compile('\\bDi era digital yang berkembang\\b', re.IGNORECASE)]),
    (lambda p: 'dimana/diketika/disewaktu' in p, [re.compile('\\b\\w+\\s+(dimana|di mana|diketika|disewaktu)\\s+\\w+\\b', re.IGNORECASE)]),
    (lambda p: 'tanggungjawab' in p, [re.compile('\\b(tanggungjawab|kerjasama|tandatangan|terimakasih|ujicoba|kantorpos|dutabesar|cagaralam)\\b', re.IGNORECASE)]),
    (lambda p: 'dari pada' in p, [re.compile('\\b(dari\\s+pada|barang\\s+kali|pada\\s+hal|sekali\\s+gus|bila\\s+mana|apa\\s+bila|mata\\s+hari|bumi\\s+putra|segi\\s+tiga)\\b', re.IGNORECASE)]),
    (lambda p: 'rujukan deiksis spasial semu' in p, [re.compile('\\b(grafik|tabel|bagan|diagram)\\s+(di\\s+atas|di\\s+bawah(?:\\s+ini)?|berikut)\\b', re.IGNORECASE)]),
    (lambda p: 'istilah bagan untuk merepresentasikan' in p, [re.compile('\\bbagan\\s+(batang|garis|lingkaran)\\b', re.IGNORECASE)]),
    (lambda p: 'pleonasme penumpukan kopula' in p, [re.compile('\\b(merupakan|adalah)\\s+salah\\s+satu\\s+termasuk\\b|\\badalah\\s+merupakan\\s+salah\\s+satu\\b', re.IGNORECASE)]),
    (lambda p: 'inkonsistensi kolokasi verba taksonomi' in p, [re.compile('\\bterbagi\\s+(dari|dalam)\\b', re.IGNORECASE)]),
    (lambda p: 'kontaminasi frasa penutup deret perincian' in p, [re.compile('\\bdan\\s+lain\\s+sebagainya\\b', re.IGNORECASE)]),
    (lambda p: 'modalitas spekulatif ragam lisan' in p, [re.compile('\\b(bisa\\s+jadi|sepertinya|kayaknya)\\b', re.IGNORECASE)]),
    (lambda p: 'pelesapan agen tak berdasar anteseden' in p, [re.compile('(?:^|[.!?]\\s+)\\b(Menghitung|Membagi|Menganalisis|Mengamati|Merancang|Mengukur)\\s+[a-z]+')]),
    (lambda p: 'ketaksaan rujukan enklitik indefinit' in p, [re.compile('(?:^|[.!?]\\s+)\\bKatanya\\b|\\bhasilnya\\s+menunjukkan\\b', re.IGNORECASE)]),
    (lambda p: 'keajegan peristilahan kurikulum tercampur' in p, [re.compile('\\b(Kurikulum\\s+Merdeka|modul\\s+ajar|Fase\\s+[A-F])\\b[^.!?]{2,120}?\\b(Kompetensi\\s+Dasar|KKM\\s+\\d+|indikator\\s+pencapaian|Silabus)\\b', re.IGNORECASE)]),
    (lambda p: 'singkatan resmi kurikulum tanpa bentuk panjang' in p, [re.compile('(?:^|[.!?]\\s+)\\b(ATP|KKTP|CP|TP)\\s+(disusun|diukur|ditetapkan|dirumuskan|diturunkan)\\b')]),
    (lambda p: 'interferensi eufemisme bunyi' in p, [re.compile('\\b(kurang\\s+mantap|cukup\\s+oke|nge-blend)\\b', re.IGNORECASE)]),
    (lambda p: 'penumpukan keterangan spasial-temporal inisial' in p, [re.compile('(?:^|[.!?]\\s+)\\b(Pada\\s+saat\\s+melakukan|Di\\s+dalam\\s+analisis)\\s+[^,.!?]{5,90}\\b(menemukan|menunjukkan|menyimpulkan|ditemukan)\\b', re.IGNORECASE)]),
    (lambda p: 'penyamaran aspek prospektif' in p, [re.compile('\\b(membuktikan|terbukti|menunjukkan|menegaskan)(?:\\s+bahwa)?\\b[^,.!?]{2,100}?\\bakan\\s+\\w+', re.IGNORECASE)]),
    (lambda p: 'pernyataan opini normatif' in p, [re.compile('\\b(seharusnya|semestinya)\\b[^,.!?]{1,120}?\\b(langsung|seluruh(?:nya)?|sepihak|sekaligus|semuanya|sepenuhnya|tuntas)\\b', re.IGNORECASE)]),
    (lambda p: 'inversi attention flow' in p, [re.compile('(?:^|[.!?]\\s+)[A-Z][a-z]+(?:\\s+[a-z]+){0,4}\\s+ini,?\\s+[^,.!?]{2,40}?\\bme\\w+nya\\b')]),
    (lambda p: 'penurunan derajat transitivitas' in p, [re.compile('\\b(adalah|ialah|memungkinkan)\\s+(?:untuk\\s+)?me[a-z]+(?:kan|i)\\s*[.!?]', re.IGNORECASE)]),
    (lambda p: 'PSM Makassar / Persija Jakarta' in p, [re.compile('\\b(PSM\\s+Makassar|Persija\\s+Jakarta|Arema\\s+Malang|klub\\s+PSM\\s+Makassar)\\b', re.IGNORECASE)]),
    (lambda p: 'sistem SI / sistem satuan SI' in p, [re.compile('\\b(sistem\\s+SI|sistem\\s+satuan\\s+SI)\\b', re.IGNORECASE)]),
    (lambda p: 'nomor ISBN / nomor ISSN' in p, [re.compile('\\b(nomor\\s+(?:ISBN|ISSN|NPWP))\\b', re.IGNORECASE)]),
    (lambda p: 'dosen DPA / dosen-dosen DPA' in p, [re.compile('\\b(dosen(?:-dosen)?\\s+DPA|dosen\\s+pembimbing\\s+DPA)\\b', re.IGNORECASE)]),
    (lambda p: 'kode QR code / format PDF format' in p, [re.compile('\\b(kode\\s+QR\\s+code|format\\s+PDF\\s+format|monitor\\s+LCD\\s+display|layar\\s+LCD\\s+display|mesin\\s+ATM\\s+machine)\\b', re.IGNORECASE)]),
    (lambda p: 'konjungsi konsekuensi intrakalimat maka' in p, [re.compile('(?:^|[.!?]\\s+)\\s*Maka,?\\s+[^.!?]{2,}')]),
    (lambda p: 'penomoran hierarki angka desimal' in p, [re.compile('\\b\\d+\\.\\d+\\.\\d+\\.\\d+(?:\\.\\d+)*\\b')]),
    (lambda p: 'seting lokasi administratif' in p, [re.compile('\\bdi\\s+(?:SMA|SMK|SMP|SD|MI|MTs|MA|Kantor\\s+Dinas)[\\w\\s]{1,25}?(?:Tahun\\s+Ajaran|Tahun\\s+Anggaran)\\b', re.IGNORECASE)]),
    (lambda p: 'eufemisme birokratis penutup fakta negatif' in p, [re.compile('\\b(penyesuaian\\s+tarif|penyesuaian\\s+harga\\s+BBM|mengamankan\\s+tersangka|dirumahkan\\s+sementara)\\b', re.IGNORECASE)]),
    (lambda p: 'booking room / grand opening' in p, [re.compile('\\b(booking\\s+room|grand\\s+opening|meeting\\s+room|launching\\s+produk)\\b', re.IGNORECASE)]),
    (lambda p: 'mengacuhkan (diartikan mengabaikan)' in p, [re.compile('\\b(mengacuhkan\\s+(?:peringatan|nasihat|himbauan|aturan|larangan)|absensi\\s+(?:siswa|karyawan|peserta)\\s+meningkat|tidak\\s+bergeming\\s+menatap)\\b', re.IGNORECASE)]),
    (lambda p: 'sangat mutlak / kondisi prasyarat awal' in p, [re.compile('\\b(sangat\\s+mutlak|kondisi\\s+prasyarat\\s+awal|saling\\s+tolong-menolong\\s+satu\\s+sama\\s+lain)\\b', re.IGNORECASE)]),
    (lambda p: 'angka 2 sebagai penanda' in p, [re.compile('\\b[a-zA-Z]+2\\b')]),
]



# --- Kaidah Tambahan (P3: GLS-003, KBI-004, MBI-004) ---
CUSTOM_RULES.extend([
    # GLS-003: kolokasi verba-nomina metaforis janggal (Glosarium Linguistik 2002)
    (lambda p: 'kolokasi leksikal baku' in p or 'melahirkan solusi' in p,
     [re.compile(r'\b(melahirkan\s+solusi|menghidangkan\s+musik|mencanangkan\s+pemecahan)\b', re.IGNORECASE)]),
    # KBI-004: leksikon percakapan santai di naskah resmi (Kongres Bahasa VII 1998)
    (lambda p: 'ragam percakapan lisan atau dialek daerah' in p,
     [re.compile(r'\b(bikin\s+bingung|banget\b)|(\s+kok\s*(?=[.!?]))|(\s+sih\s*(?=[.!?]))', re.IGNORECASE)]),
    # MBI-004: identitas responden berdigit tanpa anonimisasi (Istiqomah 2020)
    (lambda p: 'data mentah identitas subjek' in p,
     [re.compile(r'\b(?:NIK|NIP|No\.?\s*KTP)\s*[:=]?\s*\d{4,}\b', re.IGNORECASE)]),
])



# --- Kaidah Penerbit BRIN (BRN-001, BRN-002) ---
CUSTOM_RULES.extend([
    # BRN-001: klise kerendahan hati palsu prakata (Penerbit BRIN 2024, Preface)
    (lambda p: 'klise permohonan maaf prakata' in p,
     [re.compile(r'\b(penulis\s+(?:menyadari|sadar)\s+bahwa(?:\s+buku|\s+karya|\s+naskah|\s+penelitian)?\s+(?:ini|ini\s+masih)|masih\s+jauh\s+dari\s+sempurna|memiliki\s+banyak\s+kekurangan|tak\s+luput\s+dari\s+(?:berbagai\s+)?kekurangan)\b', re.IGNORECASE)]),
    # BRN-002: judul subbab generik laporan riset pada monograf (Penerbit BRIN 2024, Text Matter)
    (lambda p: 'judul subbab generik laporan riset' in p,
     [re.compile(r'(?:^|\b[Bb]ab\s+|[Ss]ubbab\s+|[Bb]agian\s+|#+\s*)(?:[IVX]+\.?\s+)?(?:Tinjauan\s+Pustaka|Metodologi\s+Penelitian|Rumusan\s+Masalah|Hasil\s+dan\s+Pembahasan|Manfaat\s+Penelitian|Landasan\s+Teori|Kajian\s+Pustaka|Metode\s+Penelitian)\b', re.IGNORECASE)]),
])


# --- Kaidah Buku Babon: Gorys Keraf, J.S. Badudu, Bahasa Tempo ---
CUSTOM_RULES.extend([
    # KRF-001: kontaminasi bentuk leksikal (Keraf, Diksi dan Gaya Bahasa)
    (lambda p: 'mengenyampingkan / mempersering' in p,
     [re.compile(r'\b(mengenyampingkan|mempersering)\b', re.IGNORECASE)]),
    # KRF-002: penumpukan nomina abstrak berkabut (Keraf)
    (lambda p: 'penumpukan nomina abstrak' in p,
     [re.compile(r'\b(melakukan\s+upaya\s+(?:peningkatan|pengembangan|pemaksimalan)|upaya\s+peningkatan\s+(?:dan\s+pengembangan|mutu|kualitas)\s+(?:di\s+dalam|dalam|terhadap)?)\b', re.IGNORECASE)]),
    # BDD-001: pleonasme sebab-akibat disebabkan karena (Badudu)
    (lambda p: 'disebabkan karena' in p,
     [re.compile(r'\b(disebabkan\s+(?:oleh\s+)?karena)\b', re.IGNORECASE)]),
    # BDD-002: daripada non-komparatif (Badudu)
    (lambda p: 'daripada' in p and ('tujuan' in p or 'dampak' in p or 'hasil' in p or 'fungsi' in p),
     [re.compile(r'\b((?:tujuan|dampak|hasil|fungsi|manfaat|peranan|pengaruh)\s+daripada)\b', re.IGNORECASE)]),
    # TMP-001: basa-basi dinas penunda fakta (Tempo)
    (lambda p: 'basa-basi dinas penunda fakta' in p,
     [re.compile(r'\b(Sehubungan\s+dengan\s+hal\s+(?:tersebut(?:\s+di\s+atas)?\s*,?\s*maka|itu)|Dalam\s+rangka\s+untuk\s+dapat|Dengan\s+ini\s+diberitahukan\s+bahwa)\b', re.IGNORECASE)]),
])


# --- Kaidah TBBBI Bab X: Pelesapan & Koordinasi Verba Transitif ---
CUSTOM_RULES.extend([
    # TBB-009: pelesapan subjek asimetris pada anak kalimat pasif awal (TBBBI hlm. 355)
    (lambda p: 'pelesapan subjek asimetris' in p,
     [re.compile(r'(?:^|[.!?]\s+)Setelah\s+di\w+(?:kan|i)?\s+[^,.!?]{2,40},\s+(?:mereka|peneliti|pemerintah|tim|kita)\s+\w+', re.IGNORECASE)]),
    # TBB-010: posisi objek terbalik pada koordinasi verba transitif (TBBBI hlm. 356)
    (lambda p: 'posisi objek mendahului verba kedua' in p,
     [re.compile(r'\b(menguji|menganalisis|mencari|mencuri|menangkap|memburu|mengumpulkan|mengolah)\s+[^,.;!?]{2,30}(?:tersebut|itu)\s+(?:atau|dan)\s+(?:meng|me)\w+\s*[.?]', re.IGNORECASE)]),
])


# --- Kaidah TBBBI Pronomina & Adjektiva (TBB-012..015) ---
CUSTOM_RULES.extend([
    # TBB-012: pronomina 'mereka' untuk benda/konsep tak bernyawa (TBBBI hlm. 201)
    (lambda p: "pronomina 'mereka' mengacu pada benda" in p,
     [re.compile(r'(?i)\b(?:algoritma|model|dokumen|buku|data|berkas|file|server|fitur|metode|perangkat|komputer|sampel|variabel|kebijakan|produk|sistem|instrumen|temuan|ide|gagasan|langkah|saran|rekomendasi)[a-z]*\b[^.!?]{2,50}\.\s+Mereka\s+(?:ada|merupakan|memproses|berfungsi|menyimpan|bekerja|memiliki|mengandung|terdiri|memuat|dipakai|digunakan|harus|akan|dapat|dapat\s+di|bisa)'), re.compile(r'(?i)\bmereka\s+(?:memproses|menghitung|mengolah|menyimpan)\b')]),
    # TBB-013: 'ia' pascapreposisi (TBBBI hlm. 200)
    (lambda p: "ia' pascapreposisi" in p or 'kepada ia' in p,
     [re.compile(r'(?i)\b(?:kepada|untuk|bersama|tentang|dengan|terhadap|bagi|oleh|dari)\s+ia\b')]),
    # TBB-014: kontaminasi ekuatif 'sama ... seperti' (TBBBI hlm. 237)
    (lambda p: 'sama pentingnya seperti' in p,
     [re.compile(r'(?i)\bsama\s+\w+nya\s+seperti\b')]),
    # TBB-015: pleonasme superlatif 'paling ter-' (TBBBI hlm. 239-240)
    (lambda p: 'paling terbaik' in p,
     [re.compile(r'(?i)\bpaling\s+ter(?:baik|penting|besar|tinggi|rendah|kaya|mahal|murah|panjang|cepat|lambat|aman|dalam)\b')]),
])


# --- Kaidah TBBBI Kata Tugas, Verba ke--an, dan PUPI Desimal (TBB-016..018, PUPI-001) ---
CUSTOM_RULES.extend([
    # TBB-016: penumpukan preposisi ganda (TBBBI Bab VIII hlm. 230)
    (lambda p: 'guna untuk / bagi untuk' in p,
     [re.compile(r'(?i)\b(?:guna\s+untuk|bagi\s+untuk|tentang\s+daripada|di\s+dalam\s+rangka\s+untuk)\b')]),
    # TBB-017: kuantifikasi partitif 'daripada' (TBBBI hlm. 230-231)
    (lambda p: 'sebagian daripada / separuh daripada' in p,
     [re.compile(r'(?i)\b(?:sebagian|seperempat|setengah|separuh|sebilangan|\d+)\s+daripada\s+(?:mereka|para|seluruh|responden|penduduk|pengguna|siswa|mahasiswa|karyawan|peserta|sampel|data|\d+)\b')]),
    # TBB-018: verba semitransitif ke--an disisipi preposisi (TBBBI hlm. 140)
    (lambda p: 'kejatuhan oleh / kehabisan akan' in p,
     [re.compile(r'(?i)\b(?:kejatuhan|kehabisan|kemasukan|kedatangan|kebanjiran|kehujanan|kecopetan|kelaparan|kepanasan)\s+(?:oleh|akan|dengan)\b')]),
    # PUPI-001: notasi desimal tanpa nol di depan (PUPI 5.8, TBBBI hlm. 438)
    (lambda p: 'notasi desimal tanpa angka nol' in p,
     [re.compile(r'(?<![\d.,])[,\.]\d{1,4}(?!\d)')]),
])


# --- Kaidah TBBBI Keserasian & EYD Lambang Bilangan (TBB-019..020, EYD-020..022) ---
CUSTOM_RULES.extend([
    # TBB-019: penggandaan 'yang' pada kalimat emfatik (TBBBI hlm. 316)
    (lambda p: "penggandaan kata 'yang'" in p,
     [re.compile(r'(?i)\b(\w+lah)\s+yang\s+yang\b')]),
    # TBB-020: pleonasme kesalingan ganda (TBBBI hlm. 328)
    (lambda p: 'saling tolong-menolong satu sama lain' in p,
     [re.compile(r'(?i)\bsaling\s+(?:[a-z]+(?:-[a-z]+)?\s+)?satu\s+sama\s+lain\b')]),
    # EYD-020: angka Arab pembuka kalimat (EYD hlm. 418)
    (lambda p: 'angka Arab pada awal kalimat' in p,
     [re.compile(r'(?m)(?:^|[.!?]\s+)\d+\s+[a-z]')]),
    # EYD-021: bilangan -an tanpa tanda hubung (EYD hlm. 418)
    (lambda p: '50an / 90an / 2000-an' in p,
     [re.compile(r'(?i)\b\d{2,4}an\b')]),
])


# --- Kaidah TBBBI Morfologi Verba (TBB-021..024) ---
CUSTOM_RULES.extend([
    # TBB-021: konsonan /k/ tunggal keliru pada verba berakhiran -kan (TBBBI hlm. 116)
    (lambda p: 'letakan / tunjukan' in p,
     [re.compile(r'(?i)\b(?:wajib|harus|perlu|hendaknya|silakan|tolong|mohon)?\s*(letakan|tunjukan|masukan\s+data|masukan\s+sampel|masukan\s+ke)\b')]),
    # TBB-022: sufiks -i ganda pada dasar berakhiran /i/ (TBBBI hlm. 116)
    (lambda p: 'mengisii / menelitii' in p,
     [re.compile(r'(?i)\b[a-z]{3,}ii\b')]),
    # TBB-023: reduplikasi verba berafiks menggandakan sufiks (TBBBI hlm. 113)
    (lambda p: 'menyulitkan-nyulitkan' in p,
     [re.compile(r'\b(?:me|di)\w+(?:kan|i)-(?:me|di)?\w+(?:kan|i)\b', re.IGNORECASE)]),
    # TBB-024: klitika pasif ku- dan kau- dipisah spasi (TBBBI hlm. 117 & 412)
    (lambda p: 'ku miliki / kau ambil' in p,
     [re.compile(r'(?i)\b(?:ku|kau)\s+(?:ambil|miliki|baca|tulis|ketahui|pelajari|buat|susun|kirim|temukan|dapati|kumpulkan|teliti|uji)\b')]),
])


def match_custom_rules(pattern_str, clean_line):
    """Cek satu entri kaidah terhadap satu baris teks.

    Return (is_handled, matched):
    - is_handled: True jika pola punya penanganan kustom di tabel
    - matched: True jika baris memicu kaidah (satu regex cukup)
    """
    for predicate, compiled_list in CUSTOM_RULES:
        if predicate(pattern_str):
            for rgx in compiled_list:
                if rgx.search(clean_line):
                    return (True, True)
            return (True, False)
    return (False, False)
