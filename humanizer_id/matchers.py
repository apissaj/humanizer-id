import functools
"""Tabel registrasi matcher data-driven untuk audit.py (Refactor Tahap 1 / P1).

Setiap aturan: (predicate_fn, [compiled_regex, ...]):
- predicate_fn: lambda p -> bool (kondisi field pola entri kaidah)
- daftar regex terkompilasi: baris dianggap memicu kaidah jika SALAH SATU cocok
  (menjaga semantik `re.search(...) or re.search(...)` dari kode asal).

Dikonversi otomatis dari rantai if-elif audit.py lama (126 cabang).
Kaidah baru cukup ditambah satu baris di sini tanpa menyentuh audit.py.
"""

import re

# --- Helper Reduplikasi Angka 2 (Aman dari false positive sains/teknologi) ---
TECH_OR_SCIENTIFIC_TERMS_ENDING_IN_2 = {
    # Satuan metrik luas & volume
    "m", "km", "cm", "mm", "dm", "ha", "in", "ft",
    # Senyawa kimia & rumus molekul
    "co", "o", "no", "so", "h", "n", "cl", "tio", "h2o", "f", "br", "i",
    # Metrik matematika, statistik, machine learning
    "r", "l", "p", "v", "z", "x", "y", "chi", "f1",
    # Standar komputasi, model AI, hardware, teknologi
    "oauth", "http", "tls", "ssl", "tcp", "udp", "ipv", "win", "ps", "usb", "pci",
    "gpt", "llama", "bert", "dalle", "gemini", "stable", "vue", "angular", "python",
    "layer", "web", "level", "act", "gen", "part", "stage", "step", "tier",
    "nd", "st", "rd", "th",
}


class Reduplication2Matcher:
    """Matcher reduplikasi informal angka 2 bahasa Indonesia (mis. anak2, buku2).
    
    Kebal terhadap:
    - Satuan metrik luas: km2, m2, cm2
    - Senyawa kimia: CO2, O2, SO2, NO2
    - Istilah teknologi & AI: OAuth2, HTTP2, Llama2, GPT2, PS2, Win32
    - Notasi matematika/statistika: R2, L2
    """
    def __init__(self):
        self.pattern = r"\b(?:[a-zA-Z]+-)?([a-zA-Z]+)2(-?[a-zA-Z]+)?\b"

    def search(self, text):
        for m in re.finditer(r"\b(?:[a-zA-Z]+-)?([a-zA-Z]+)2(-?[a-zA-Z]+)?\b", text):
            base = m.group(1)
            # Tolak jika all-caps (CO2, O2, SO2, PS2, HTTP2, R2)
            if base.isupper():
                continue
            # Tolak jika mixed-case / camelCase (OAuth2, Llama2, GPT2)
            if not (base.islower() or (base.istitle() and len(base) > 2)):
                continue
            base_lower = base.lower()
            if len(base_lower) < 3:
                continue
            if base_lower in TECH_OR_SCIENTIFIC_TERMS_ENDING_IN_2:
                continue
            if not re.search(r'[aeiou]', base_lower):
                continue
            return m
        return None


REDUPLICATION_2_MATCHER = Reduplication2Matcher()

CUSTOM_RULES = [
    (lambda p: 'masing-masing' in p and ('kata benda' in p or 'nomina' in p), [re.compile(r'\bmasing-masing\s+(?:peserta|individu|mahasiswa|siswa|responden|anggota|komponen|bagian|sampel|variabel|orang|pihak|daerah|kelompok|faktor|unsur|unit)\b', re.IGNORECASE)]),
    (lambda p: 'dengan' in p.lower() and 'dapat' in p.lower() and ('cacat subjek' in p.lower() or 'preposisi' in p.lower()), [re.compile(r'(?:^|[.!?]\s+)\bDengan\s+(?:adanya\s+)?[a-zA-Z0-9\s\-]{3,35}\s+dapat\s+(?:meningkatkan|mempercepat|menghasilkan|mengurangi|membantu|memberikan|memudahkan|mengatasi|menjelaskan|mempengaruhi|memengaruhi|mencapai|menunjukkan)\b', re.IGNORECASE)]),
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
    (lambda p: 'ungkapan idiomatis dihilangkan' in p, [re.compile('\\b(sesuai|berkaitan|sehubungan)\\s+(?!dengan\\b)(?=(tidak|kurang|konteks|hal|masalah|perkara|ketentuan|aturan))', re.IGNORECASE), re.compile('\\b(bergantung|tergantung)\\s+(?!pada\\b)(?=(hasil|kondisi|keputusan|situasi|tingkat|cuaca|anggaran|penilaian|kesepakatan|hasil survei|dukungan))', re.IGNORECASE)]),
    (lambda p: 'makna asal/sumber/penjelasan' in p, [re.compile('\\b(?:terbuat|berasal|terbentuk|tersusun)\\s+daripada\\b|\\btujuan\\s+daripada\\b|\\bmaksud\\s+daripada\\b|\\bterbuat\\s+\\w*\\s*daripada\\b', re.IGNORECASE)]),
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
    (lambda p: 'preposisi titik waktu tidak baku' in p, [re.compile('\\bdi\\s+(?:tahun|periode|era|dekade)\\s+\\d{4}\\b|\\bdi\\s+(?:awal|tengah|akhir)\\s+(?:tahun|bulan|pekan|minggu)\\s+\\d{4}\\b|\\bdi\\s+(?:saat|kala)\\b|\\bdi\\s+(?:Senin|Selasa|Rabu|Kamis|Jumat|Sabtu|Minggu|Januari|Februari|Maret|April|Mei|Juni|Juli|Agustus|September|Oktober|November|Desember)\\b|\\bdi\\s+hari\\s+(?:Senin|Selasa|Rabu|Kamis|Jumat|Sabtu|Minggu)\\b', re.IGNORECASE)]),
    (lambda p: 'pleonasme preposisi majemuk' in p, [re.compile('\\bselain\\s+daripada\\b|\\bselain\\s+dari\\s+(itu|pada|laporan|biaya|data|hal|aspek|faktor)\\b', re.IGNORECASE)]),
    (lambda p: 'preposisi arah/lokasi ditulis serangkai tanpa spasi' in p, [re.compile('\\b(didalam|kedalam|diatas|keatas|dibawah|kebawah|didepan|kedepan|dibelakang|kebelakang|disamping|kesamping)\\b', re.IGNORECASE)]),
    (lambda p: 'konjungsi syarat berkorelasi mubazir' in p, [re.compile('\\b(jika|kalau|apabila|bila)\\b[^.!?]*\\b,?\\s*maka\\b', re.IGNORECASE)]),
    (lambda p: 'objek verba transitif disisipi preposisi' in p, [re.compile('\\b(memerintahkan|menugaskan|menganjurkan|mempersilakan)\\s+kepada\\b', re.IGNORECASE)]),
    (lambda p: 'penghubung bertentangan rangkap tiga' in p, [re.compile('\\b(walaupun|meskipun|sungguhpun|sekalipun)\\b[^.!?]*\\b(namun|tetapi)\\b[^.!?]*\\b,?\\s*maka\\b', re.IGNORECASE)]),
    (lambda p: 'pemakaian jam alih-alih pukul' in p, [re.compile('\\b(pada|sejak|hingga|sampai)\\s+jam\\b|\\bjam\\s+\\d{1,2}[.:]\\d{2}\\b|\\bjam\\s*:\\s*\\d{1,2}[.:]\\d{2}', re.IGNORECASE)]),
    (lambda p: 'verba kopula predikat definisi' in p, [re.compile('\\b\\w+\\s+yaitu\\s+(suatu|sebuah|benda|alat|metode|metoda|algoritma|teknik|proses|istilah|model|sistem|bentuk|cara|konsep|sifat|fungsi|keadaan|aktivitas)\\b', re.IGNORECASE)]),
    (lambda p: 'kata bekas untuk mengacu pada manusia' in p, [re.compile('\\bbekas\\s+(rektor|camat|lurah|presiden|gubernur|wali|bupati|mayor|menteri|kepala|ketua|direk|anggota|dosen|guru|kades|pejabat|hakim|jaksa|sekretaris|duta|jenderal|komandan|panglima|wakil)\\w*\\b', re.IGNORECASE)]),
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
    (lambda p: 'angka 2 sebagai penanda' in p, [REDUPLICATION_2_MATCHER]),
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
     [re.compile(r'\b(?:NIK|No\.?\s*KTP)\s*[:=]?\s*\d{4,}\b', re.IGNORECASE)]),
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
     [re.compile(r'(?<![a-zA-Z\d.,])[,\.]\d{1,4}(?!\d)')]),
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


# --- Kaidah Preposisi & Frasa Berpreposisi (PFP-005..008) ---
CUSTOM_RULES.extend([
    # PFP-005: penumpukan preposisi temporal sejak pada (Effendi & Aritonang hlm. 26 & 52)
    (lambda p: 'sejak pada / semenjak pada' in p,
     [re.compile(r'\b(sejak|semenjak)\s+pada\b', re.IGNORECASE)]),
    # PFP-006: pasangan korelatif antara dengan selain 'dan' (Effendi & Aritonang hlm. 43)
    (lambda p: 'antara ... sampai / antara ... hingga' in p,
     [re.compile(r'\bantara\b[^,.!?]{2,60}?\b(?:sampai|hingga|ataupun|atau)\b', re.IGNORECASE)]),
    # PFP-007: kalk klausa relatif 'di dalam mana' (in which / wherein)
    (lambda p: 'di dalam mana / ke dalam mana' in p,
     [re.compile(r'\b(?:di|ke)\s+dalam\s+mana\b', re.IGNORECASE)]),
    # PFP-008: ingkar ganda tanpa tidak / tanpa bukan
    (lambda p: 'tanpa tidak / tanpa bukan' in p,
     [re.compile(r'\btanpa\s+(?:tidak|bukan)\b', re.IGNORECASE)]),
])


# --- Kaidah Naskah Dinas Resmi (DIN-001..004) ---
CUSTOM_RULES.extend([
    # DIN-001: pembuka verba mentah tanpa subjek pada naskah dinas (hlm. 72)
    (lambda p: 'Membalas surat Saudara / Merujuk surat' in p,
     [re.compile(r'(?:^|[.!?]\s+)(?:Membalas|Merujuk|Menunjuk|Menjawab|Menindaklanjuti)\s+(?:surat|permohonan|nota|undangan|laporan)\b')]),
    # DIN-002: sisipan adverbia pada klitika pasif (hlm. 48)
    (lambda p: 'Masalah itu kami sudah laporkan' in p,
     [re.compile(r'(?i)\b(?:kami|kita|mereka)\s+(?:sudah|belum|akan|telah|sedang)\s+(?:laporkan|terima|kirim|sampaikan|selesaikan|tangani|bahas)\b')]),
    # DIN-003: pronomina '-nya' pada komunikasi orang kedua (hlm. 75)
    (lambda p: 'Atas perhatiannya / Harap maklum adanya' in p,
     [re.compile(r'(?i)(?:^|[.!?]\s+)(?:Atas\s+perhatiannya|Harap\s+maklum\s+adanya|Demikian\s+atas\s+bantuan\s+Saudara)\b')]),
    # DIN-004: ganda konjungsi konsesif 'meskipun ... tetapi' (hlm. 50)
    (lambda p: 'Meskipun ..., tetapi' in p,
     [re.compile(r'(?i)\b(?:meskipun|walaupun|biarpun)\b[^,.!?]{3,120},\s*tetapi\b')]),
])


# --- Kaidah Penyerapan Imbuhan Asing TII (TII-006..009) ---
CUSTOM_RULES.extend([
    # TII-006: -wise tanpa struktur 'demi' (TII hlm. 56)
    (lambda p: 'pointwise / piecewise / timewise' in p,
     [re.compile(r'(?i)\b(?:pointwise|piecewise|timewise|pagewise|stepwise|linewise|rowwise|columnwise|keywordwise)\b')]),
    # TII-007: -ous tanpa prefiks ber- (TII hlm. 56)
    (lambda p: 'harmonious / analogous' in p,
     [re.compile(r'(?i)\b(?:harmonious|analogous|continuous|homogenous|anomalous)\b')]),
    # TII-008: -and/-end tanpa sisipan -in- (TII hlm. 56)
    (lambda p: 'addend / multiplicand' in p,
     [re.compile(r'(?i)\b(?:addend|addends|dividend|dividends|multiplicand|multiplicands|minuend)\b')]),
    # TII-009: -er/-or tanpa prefiks pe- (TII hlm. 56)
    (lambda p: 'absorber / mixer / analyzer' in p,
     [re.compile(r'(?i)\b(?:absorber|mixer|analyzer|analyser|divider|insulator|conductor\s+listrik)\b')]),
])


# --- Kaidah Istilah Wacana Kridalaksana (DIL-005..008) ---
CUSTOM_RULES.extend([
    # DIL-005: bentuk rancu koherensitas dan kohesifitas (hlm. 23)
    (lambda p: 'koherensitas / kohesifitas' in p,
     [re.compile(r'(?i)\b(?:koherensitas|kohesifitas)\b')]),
    # DIL-006: transkripsi mentah presuposisi wacana (hlm. 47)
    (lambda p: 'presuposisi teks / presuposisi wacana' in p,
     [re.compile(r'(?i)\bpresuposisi\s+(?:teks|wacana|semantik|kalimat|pragmatik)\b')]),
    # DIL-007: padanan harfiah referensi belakang (back-reference, hlm. 20)
    (lambda p: 'referensi belakang' in p,
     [re.compile(r'(?i)\breferensi\s+belakang\b')]),
])


# --- Kaidah Surat-Menyurat Resmi (SUR-001..004) ---
CUSTOM_RULES.extend([
    # SUR-001: penghubung klausa 'yang mana' (hlm. 37)
    (lambda p: 'yang mana' in p,
     [re.compile(r'(?i)(?:,|\s)\s*yang\s+mana\b')]),
    # SUR-002: penghubung klausa ', di mana' (hlm. 37)
    (lambda p: 'di mana ...' in p,
     [re.compile(r'(?i)\b,\s*di\s+mana\b')]),
    # SUR-003: kata 'bunyi' untuk surat (hlm. 36)
    (lambda p: "bunyi surat / bunyi edaran" in p,
     [re.compile(r'(?i)\bbunyi\s+(?:surat|edaran|nota|telegram|sk|undangan)\b')]),
    # SUR-004: homonim 'sangsi' vs 'sanksi' (hlm. 36)
    (lambda p: "sangsi hukum / sangsi pidana" in p,
     [re.compile(r'(?i)\bsangsi\s+(?:hukum|pidana|administratif|perdata|disiplin)\b')]),
])


# --- Kaidah Bentuk dan Pilihan Kata BPK (BPK-011..012) ---
CUSTOM_RULES.extend([
    # BPK-011: awalan ke- adversatif salah kaprah (hlm. 28-29)
    (lambda p: 'ketabrak / ketimpa / ketubruk' in p,
     [re.compile(r'(?i)\b(?:ketabrak|ketimpa|ketubruk|kesandung|ketinggal|ketangkap)\b')]),
    # BPK-012: peluluhan fonem gagal pada konfiks meN-...-kan (hlm. 21-23)
    (lambda p: 'mengetrapkan / mentrapkan' in p,
     [re.compile(r'(?i)\b(?:mengetrapkan|mentrapkan|menterapkan|pengetrapan|pentrapan|penterapan|menterjemahkan|mentaati|mengkaitkan|mengrusak|pengrajin|penglepasan|pengrusakan)\b')]),
])


# --- Kaidah Seri Penyuluhan 1: Ejaan (SPE-001..003) ---
CUSTOM_RULES.extend([
    # SPE-001: tanda koma terlarang sebelum anak kalimat kausal/final di belakang (hlm. 39)
    (lambda p: ', karena / , agar / , supaya' in p,
     [re.compile(r',\s*(?:karena|agar|supaya)\b', re.IGNORECASE)]),
    # SPE-002: gabungan kata berawalan saja ditulis serangkai (hlm. 19)
    (lambda p: 'berterimakasih / bertandatangan' in p,
     [re.compile(r'(?i)\b(?:berterimakasih|bertandatangan|bersepakbola|membabibuta|menyebarluas)\b')]),
    # SPE-003: konjungsi antarkalimat di awal kalimat tanpa tanda koma (hlm. 36-37)
    (lambda p: 'Namun ... / Bahkan ... / Kemudian ...' in p,
     [re.compile(r'(?i)(?:^|[.!?]\s+)(?:Namun|Bahkan|Kemudian|Lagi\s+pula|Sebenarnya)\s+[a-z]')]),
])


# --- Kaidah Tambahan Seri Penyuluhan 9 EYD (EYD-023, EYD-025) ---
CUSTOM_RULES.extend([
    # EYD-023: unsur terikat 'maha' ditulis terpisah dari kata dasar (hlm. 36)
    (lambda p: 'maha siswa / maha kuasa / maha esa' in p,
     [re.compile(r'(?i)\bmaha\s+(?:siswa|kuasa|esa|guru|pemimpin|karya|wisuda|dewa|raja)\b')]),
    # EYD-025: angka 2 sebagai penanda reduplikasi pada naskah resmi (hlm. 35)
    (lambda p: 'orang2 / anak2 / buku2' in p,
     [REDUPLICATION_2_MATCHER]),
])


# --- Kaidah Lanjutan J.S. Badudu (BDD-004..007) ---
CUSTOM_RULES.extend([
    # BDD-004: fonem /c/ tidak luluh saat diberi prefiks meN- (menyolok -> mencolok)
    (lambda p: 'menyolok / menyuci / menyubit' in p,
     [re.compile(r'(?i)\bme(?:nyolok|nyuci|nyubit|nyulik)\b')]),
    # BDD-005: tolok ukur bukan tolak ukur (kata dasar tolok = standar/tara)
    (lambda p: 'tolak ukur / tolak-ukur' in p,
     [re.compile(r'(?i)\btolak[-\s]ukur\b')]),
    # BDD-006: peluluhan fonem /s/ kata serapan berprefiks meN- (menyukseskan bukan mensukseskan)
    (lambda p: 'mensukseskan / mensuplai / mensurvei' in p,
     [re.compile(r'(?i)\bme(?:nsukseskan|nsuplai|nsurvei)\b')]),
    # BDD-007: kalk relatif lokatif 'di mana' tempat nyata diganti 'tempat'
    (lambda p: 'gedung di mana / laboratorium di mana' in p,
     [re.compile(r'(?i)\b(?:gedung|ruangan|laboratorium|kota|desa|wilayah|daerah)\s+di\s+mana\b')]),
])


# --- Kaidah Tabel Baku-Tidak Baku Seri Penyuluhan Bentuk & Pilihan Kata (BPK-015..018) ---
CUSTOM_RULES.extend([
    # BPK-015: gugus konsonan kw- diserap ku-, dan jadual -> jadwal (hlm. 68)
    (lambda p: 'kwalitas / kwantitas / kwitansi / jadual' in p,
     [re.compile(r'(?i)\b(?:kwalitas|kwantitas|kwitansi|jadual)\b')]),
    # BPK-016: kalk Belanda prosen/persentase/kuisioner (hlm. 68)
    (lambda p: 'prosen / prosentase / presentase / kuisioner / questioner' in p,
     [re.compile(r'(?i)\b(?:prosentase|presentase|prosen|kuisioner|questioner)\b')]),
    # BPK-017: serapan Yunani -is/-os baku sistem/metode/hipotesis/diagnosis (hlm. 68)
    (lambda p: 'sistim / metoda / methode / hipotesa / diagnosa' in p,
     [re.compile(r'(?i)\b(?:sistim|metoda|methode|hipotesa|diagnosa)\b')]),
    # BPK-018: konsonan /j/ baku objek/subjek (hlm. 68)
    (lambda p: 'obyek / subyek' in p,
     [re.compile(r'(?i)\b(?:obyek|subyek)\b')]),
])


# --- Kaidah Morfologi Kata Bentukan Seri Penyuluhan BPK (BPK-019..022) ---
CUSTOM_RULES.extend([
    # BPK-019: kata dasar ubah, bukan robah (hlm. 5-6)
    (lambda p: 'dirubah / dirobah / merobah / perobahan' in p,
     [re.compile(r'(?i)\b(?:di(?:rubah|robah)|merobah|perobahan)\b')]),
    # BPK-020: peN- -> pe- pada dasar berawal /l/ dan /r/ (hlm. 14)
    (lambda p: 'penglepasan / pengrusakan / pengrusak' in p,
     [re.compile(r'(?i)\b(?:penglepasan|pengrusakan|pengrusak)\b')]),
    # BPK-021: konfiks ganda pada gabungan kata ditulis serangkai (hlm. 33-34)
    (lambda p: 'menyebar luaskan / menyalah gunakan' in p,
     [re.compile(r'(?i)\b(?:me(?:nyebar\s+luaskan|nyalah\s+gunakan|ngikut\s+sertakan|lipat\s+gandakan)|di(?:sebar\s+luaskan|salah\s+gunakan|ikut\s+sertakan|lipat\s+gandakan)|pe(?:nyebar\s+luasan|nyalah\s+gunaan|ngikut\s+sertaan|lipat\s+gandaan))\b')]),
    # BPK-022: prefiks tunggal pada gabungan kata ditulis terpisah (hlm. 34)
    (lambda p: 'mengadudomba / bertandatangan / bertepuktangan' in p,
     [re.compile(r'(?i)\b(?:mengadudomba|bertandatangan|bertepuktangan)\b')]),
])


# --- Kaidah Analogi, Pertalian Bentuk, dan Distingsi Leksikal (BPK-023..025) ---
CUSTOM_RULES.extend([
    # BPK-023: nomina intransitif per-an diberi agen 'oleh' -> pakai peng-an (hlm. 22)
    (lambda p: 'perkembangan ... oleh peneliti/pemerintah' in p,
     [re.compile(r'(?i)\bperkembangan\s+[^.!?,\n]{1,40}\s+oleh\s+(?:pemerintah|peneliti|tim|lembaga|penulis)\b')]),
    # BPK-024: kebijaksanaan untuk ranah institusional/politik -> kebijakan (hlm. 76)
    (lambda p: 'kebijaksanaan pemerintah / kebijaksanaan moneter' in p,
     [re.compile(r'(?i)\bkebijaksanaan\s+(?:pemerintah|kampus|rektorat|direksi|moneter|fiskal|publik|nasional)\b')]),
    # BPK-025: perluasan daripada non-komparatif biaya/pangkal/bagian/hakikat (hlm. 79-80)
    (lambda p: 'biaya daripada / pangkal daripada' in p,
     [re.compile(r'(?i)\b(?:biaya|pangkal|bagian|hakikat|hakekat|inti)\s+daripada\b')]),
])


# --- Kaidah Tabel Baku-Tidak Baku Lanjutan (BPK-027..031) ---
CUSTOM_RULES.extend([
    # BPK-027: sufiks serapan -itas bukan -ifitas (hlm. 68)
    (lambda p: 'produktifitas / kreatifitas / efektifitas' in p,
     [re.compile(r'(?i)\b(?:produktifitas|kreatifitas|efektifitas|sensitifitas|kompetitifitas)\b')]),
    # BPK-028: nama bulan Masehi baku Februari/November (hlm. 68)
    (lambda p: 'Pebruari / Nopember' in p,
     [re.compile(r'(?i)\b(?:pebruari|nopember)\b')]),
    # BPK-029: nama hari baku Jumat/Rabu (hlm. 68)
    (lambda p: "Jum'at / Rabo / Rebo" in p,
     [re.compile(r'\b(?:Jum[\'\u2019]at|jum[\'\u2019]at|Rabo|rabo|Rebo|rebo)\b')]),
    # BPK-030: penyerapan teknik (hlm. 68)
    (lambda p: 'tehnik / technik' in p,
     [re.compile(r'(?i)\b(?:tehnik|technik)\b')]),
    # BPK-031: penyerapan grafem ph- menjadi f (hlm. 68)
    (lambda p: 'photo / photo copi / foto copy' in p,
     [re.compile(r'(?i)\b(?:photo(?:\s+copi)?|foto\s+copy)\b')]),
])


# --- Kaidah Kehematan & Kesejajaran Sasangka 2015 (SPK-006..008) ---
CUSTOM_RULES.extend([
    # SPK-006: predikat seakar subjek peN-an (hlm. 74-75)
    (lambda p: 'pemberian ... diberikan / pengangkatan ... diangkat' in p,
     [re.compile(r'(?i)\b(?:pemberian\s+[^.!?]{1,50}?\bdiberikan|pengangkatan\s+[^.!?]{1,50}?\bdiangkat|pelantikan\s+[^.!?]{1,50}?\bdilantik|penunjukan\s+[^.!?]{1,50}?\bditunjuk|penjelasan\s+[^.!?]{1,50}?\bdijelaskan|pengumuman\s+[^.!?]{1,50}?\bdiumumkan|pendaftaran\s+[^.!?]{1,50}?\bdidaftarkan|penetapan\s+[^.!?]{1,50}?\bditetapkan|pengumpulan\s+[^.!?]{1,50}?\bdikumpulkan|pembagian\s+[^.!?]{1,50}?\bdibagikan|\bgaji\s+[^.!?]{1,50}?\bdigaji)\b')]),
    # SPK-007: penanda jamak + reduplikasi ganda (hlm. 75)
    (lambda p: 'beberapa temuan-temuan / para tamu-tamu' in p,
     [re.compile(r'(?i)\b(?:beberapa|para|sejumlah|seluruh)\s+([a-z]+)-\1\b')]),
    # SPK-008: sinonim rangkap penunjuk (hlm. 74)
    (lambda p: 'sebagaimana tersebut di atas / seperti tersebut di atas' in p,
     [re.compile(r'(?i)\b(?:sebagaimana|seperti)\s+tersebut\s+di\s+atas\b')]),
])


# --- Kaidah Ejaan Serapan Sriyanto 2015 (SPE-005..008) ---
CUSTOM_RULES.extend([
    # SPE-005: apostrof Arab & huruf q pada serapan (hlm. 14)
    (lambda p: "da'wah / do'a / taqwa / qalbu" in p,
     [re.compile(r"(?i)\b(?:da['\u2019]wah|do['\u2019]a|taqwa|qalbu)\b")]),
    # SPE-006: digraf non-baku serapan Arab-Sanskerta (hlm. 17)
    (lambda p: 'bhakti / dharma / wudhu / bathin / shalat' in p,
     [re.compile(r'(?i)\b(?:wudhu|bathin|shalat|sholat|ashar|shubuh|ustadz|ustadzah|hadits|adzan|dhuha)\b'),
      re.compile(r'\b(?:[Bb]hakti|[Dd]harma)\b(?!\s+[A-Z])')]),
    # SPE-007: singkatan PT tanpa titik (hlm. 50)
    (lambda p: 'PT. [Nama Perusahaan]' in p,
     [re.compile(r'\bPT\.\s+[A-Z][a-zA-Z0-9]+')]),
    # SPE-008: tanggal nama bulan berhimpit tanda hubung (hlm. 91)
    (lambda p: '12-September-2024 / 01-Januari-2023' in p,
     [re.compile(r'\b\d{1,2}-(?:Januari|Februari|Maret|April|Mei|Juni|Juli|Agustus|September|Oktober|November|Desember)-\d{4}\b', re.IGNORECASE)]),
])


# --- Kaidah Pemadanan & Penyerapan Qodratillah 2016 (TIQ-006..009) ---
CUSTOM_RULES.extend([
    # TIQ-006: serapan Belanda -eel menjadi -el (hlm. 14, 17)
    (lambda p: 'materiil / moriil / prinsipiil' in p,
     [re.compile(r'(?i)\b(?:materiil|moriil|prinsipiil|esensiil|potensiil|finansiil|substansiil)\b')]),
    # TIQ-007: kalk harfiah istilah ekonomi (hlm. 20)
    (lambda p: 'pasar beruang / pasar banteng' in p,
     [re.compile(r'(?i)\bpasar\s+(?:beruang|banteng)\b')]),
    # TIQ-008: padanan toko serbaada/toserba (hlm. 20)
    (lambda p: 'depstor / departement store' in p,
     [re.compile(r'(?i)\b(?:depstor|departement\s+store)\b')]),
    # TIQ-009: kalk parsial swalayan tanpa nomina inti (hlm. 20)
    (lambda p: "ke swalayan / di swalayan / dari swalayan" in p,
     [re.compile(r'(?i)\b(?:ke|di|dari)\s+swalayan\b')]),
])


# --- Kaidah PUEBI 2021 SK 321 (PUE-001..004) ---
CUSTOM_RULES.extend([
    # PUE-001: kapitalisasi kata turunan nama bangsa/bahasa (hlm. 7)
    (lambda p: 'peng-Indonesia-an / pengIndonesiaan / ke-Barat-baratan' in p,
     [re.compile(r'\b(?:peng-(?:Indonesia|Arab|Inggris|Jepang)-an|peng(?:Indonesia|Arab|Inggris|Jepang)an|ke-(?:Inggris|Barat|Arab|Jawa|Timur)-(?:inggrisan|baratan|araban|jawaan|timuran)|ke-(?:Inggris|Barat|Arab|Jawa|Timur)an)\b')]),
    # PUE-002: aksesoris -> aksesori (hlm. 47)
    (lambda p: 'aksesoris' in p,
     [re.compile(r'(?i)\baksesoris\b')]),
    # PUE-003: kharisma -> karisma (hlm. 47)
    (lambda p: 'kharisma / kharismatik' in p,
     [re.compile(r'(?i)\b(?:kharisma|kharismatik)\b')]),
    # PUE-004: eschelon -> eselon (hlm. 47)
    (lambda p: 'eschelon / esselon' in p,
     [re.compile(r'(?i)\b(?:eschelon|esselon)\b')]),
])


# --- Kaidah TBBBI Ed-4 Morfofonemik & Konjungsi Tetapi (TBB-027..029) ---
CUSTOM_RULES.extend([
    # TBB-027: verba dasar tunggal b/p salah asimilasi (hlm. 144)
    (lambda p: 'membom / mencek / mempel / mentik' in p,
     [re.compile(r'(?i)\b(?:membom|mencek(?!\w)|mempel|mentik)\b')]),
    # TBB-028: pangkal gugus konsonan tidak luluh (hlm. 144)
    (lambda p: 'memroduksi / memroses / memrogram' in p,
     [re.compile(r'(?i)\b(?:memroduksi|memroses|memrogram|menransfer|mengredit|menglaim)\b')]),
    # TBB-029: konjungsi tetapi di awal kalimat (hlm. 417)
    (lambda p: '"Tetapi" di awal kalimat' in p,
     [re.compile(r'(?:^|[.!?]\s+)(Tetapi\b(?:\s*,\s*|\s+))')]),
])


# --- Kaidah Ragam Cakapan Kamus BSE (RGM-001) ---
CUSTOM_RULES.extend([
    # RGM-001: kata ragam cakapan dalam tulisan formal (Kamus BSE 2008)
    (lambda p: 'nggak / gimana / cuman / banget / capek' in p,
     [re.compile(r'(?i)\b(?:nggak|nggaknya|gimana|cuman|banget|capek)\b')]),
])


# --- Kaidah Seri Penyuluhan Paragraf (PRG-001) ---
CUSTOM_RULES.extend([
    # PRG-001: konjungsi penumpu simpulan wajib diikuti koma (Suladi 2015, hlm. 55)
    (lambda p: 'Akhirnya / Akibatnya / Oleh karena itu' in p,
     [re.compile(r'(?:^|[.!?]\s+)(?:Berdasarkan uraian di atas\b(?!\s*,)|(?:Akhirnya|Akibatnya|Oleh karena itu|Maka dari itu|Dengan demikian)\b(?!\s*,))')]),
])


# --- Kaidah TBBBI Ed-4 Elatif & Verba Transitif Preposisional (TBB-030..031) ---
CUSTOM_RULES.extend([
    # TBB-030: penumpukan pewatas elatif (TBBBI hlm. 229)
    (lambda p: 'amat sangat / sangat amat' in p,
     [re.compile(r'(?i)\b(?:amat sangat|sangat amat|sungguh mahabesar|amat sangat sekali)\b')]),
    # TBB-031: verba transitif + preposisi tentang/mengenai/akan (TBBBI hlm. 129)
    (lambda p: 'membicarakan/mengetahui/membahas' in p,
     [re.compile(r'(?i)\b(?:membicarakan|mengetahui|membahas|menyebutkan|mengulas)\s+(?:tentang|akan|mengenai)\b')]),
])


# --- Kaidah Buku Ajar Perguruan Tinggi UNJA/UIN (UIN-007..008) ---
CUSTOM_RULES.extend([
    # UIN-007: kepemilikan kalke 'dari' (UNJA hlm. 98)
    (lambda p: 'kesimpulan/tujuan/hasil/dampak/manfaat/anak/ketua + dari' in p,
     [re.compile(r'(?i)\b(?:kesimpulan|tujuan|hasil|dampak|manfaat|fungsi|peran|pengaruh|anak|ketua|anggota|adik|kakak)\s+dari\s+(?:penelitian|studi|kajian|diskusi|kegiatan|program|rapat|seminar|[A-Z][a-z]+)\b')]),
    # UIN-008: verba benefaktif -kan + untuk (UNJA hlm. 108)
    (lambda p: 'membelikan/mengambilkan/membawakan/membuatkan' in p,
     [re.compile(r'(?i)\b(?:membelikan|mengambilkan|membawakan|membuatkan|mengirimkan|menuliskan|menyediakan|memasakkan|menjahitkan|menyumbangkan)\s+untuk\b')]),
])


# --- Kaidah Tanda Hubung EYD & PUEBI (EYD-026..027) ---
CUSTOM_RULES.extend([
    # EYD-026: se- + huruf kapital tanpa tanda hubung (EYD hlm. 61)
    (lambda p: 'se[Kapital] tanpa tanda hubung' in p,
     [re.compile(r'\bse[A-Z][a-z]+\b')]),
    # EYD-027: ke- + angka ordinal tanpa tanda hubung (EYD hlm. 61)
    (lambda p: 'ke[Angka] tanpa tanda hubung' in p,
     [re.compile(r'\bke\d+\b')]),
])


# --- Kaidah Buku PT UIN Alauddin Makassar (UIN-009..010) ---
CUSTOM_RULES.extend([
    # UIN-009: relatif lokatif tempat di mana (Halimah hlm. 125)
    (lambda p: 'tempat di mana / tempat dimana' in p,
     [re.compile(r'(?i)\btempat\s+di\s*mana\b')]),
    # UIN-010: pleonasme temporal zaman dahulu kala (Halimah hlm. 125)
    (lambda p: 'zaman dahulu kala' in p,
     [re.compile(r'(?i)\b(?:zaman|pada zaman)\s+dahulu\s+kala\b')]),
])


# --- Kaidah Seri Penyuluhan Bentuk dan Pilihan Kata 2019 (BPK-032..034) ---
CUSTOM_RULES.extend([
    # BPK-032: k tunggal pada sufiks -kan yang seharusnya kk (hlm. 41)
    (lambda p: 'menunjukan / ditunjukan' in p,
     [re.compile(r'(?i)\b(?:menunjukan|ditunjukan|mengontrakan|dikontrakan)\b')]),
    # BPK-033: kk ganda pada konfiks peng-...-an & ke-...-an yang seharusnya k tunggal (hlm. 42)
    (lambda p: 'penunjukkan / pendidikkan' in p,
     [re.compile(r'(?i)\b(?:penunjukkan|pendidikkan|kenaikkan|kebaikkan)\b')]),
    # BPK-034: pertanggungan jawab -> pertanggungjawaban (hlm. 43)
    (lambda p: 'pertanggungan jawab' in p,
     [re.compile(r'(?i)\bpertanggungan\s+jawab\b')]),
])


# --- Kaidah Pedoman Surat-Menyurat Resmi 1985 (SRT-007..008) ---
CUSTOM_RULES.extend([
    # SRT-007: kenapa -> mengapa (hlm. 55)
    (lambda p: p == 'kenapa',
     [re.compile(r'(?i)\bkenapa\b')]),
    # SRT-008: haturkan / menghaturkan terima kasih (hlm. 52)
    (lambda p: 'menghaturkan/haturkan' in p,
     [re.compile(r'(?i)\b(?:menghaturkan|haturkan)\s+(?:terima kasih|penghargaan|salam|permohonan|puji|syukur)\b')]),
])


# --- Kaidah Analisis Kesalahan Sintaksis Skripsi JSI UNNES & DE Journal (JRN-001..002) ---
CUSTOM_RULES.extend([
    # JRN-001: Selain itu juga (DE Journal 2023, hlm. 546)
    (lambda p: p == 'Selain itu juga',
     [re.compile(r'(?i)\bSelain\s+itu\s+juga\b')]),
    # JRN-002: banyak + verba + kata ulang jamak (JSI UNNES 2021, hlm. 7)
    (lambda p: 'banyak + verba + kata ulang jamak' in p,
     [re.compile(r'(?i)\bbanyak\s+(?:mengandung|memiliki|melibatkan|menghasilkan)\s+([a-zA-Z]+)-\1\b')]),
])


# --- Kaidah Analisis Diksi Skripsi Jurnal Genre UAD (JRN-003..004) ---
CUSTOM_RULES.extend([
    # JRN-003: baik ... ataupun -> baik ... maupun (Jurnal Genre UAD 2021, hlm. 100)
    (lambda p: p == 'baik ... ataupun',
     [re.compile(r'(?i)\bbaik\b(?:\s+[\w\-]+){1,6}\s+\bataupun\b')]),
    # JRN-004: pertama dan utama (Jurnal Genre UAD 2021, hlm. 99)
    (lambda p: p == 'pertama dan utama',
     [re.compile(r'(?i)\bpertama\s+dan\s+utama\b')]),
])


# --- Kaidah Kalimat Skripsi Unmuh Jember & Retorika Uniflor (JRN-005..006) ---
CUSTOM_RULES.extend([
    # JRN-005: dikarenakan -> disebabkan (Jurnal BB Unmuh Jember 2020, hlm. 58)
    (lambda p: p == 'dikarenakan',
     [re.compile(r'(?i)\bdikarenakan\b')]),
    # JRN-006: angka + orang + nomina insani (Jurnal Retorika Uniflor 2022, hlm. 56)
    (lambda p: 'bilangan + orang + nomina insani' in p,
     [re.compile(r'(?i)\b\d+\s+orang\s+(?:siswa|siswi|mahasiswa|mahasiswi|dosen|peserta|responden|guru)\b')]),
])


# --- Kaidah Ejaan Abstrak Skripsi Jurnal Jurribah / EBI V (JRN-007..008) ---
CUSTOM_RULES.extend([
    # JRN-007: simbol ampersand (&) dalam teks prosa (hlm. 479)
    (lambda p: 'simbol ampersand' in p,
     [re.compile(r'(?<=\w)\s+&\s+(?=\w)')]),
    # JRN-008: spasi sebelum tanda titik dua (hlm. 479)
    (lambda p: 'spasi sebelum tanda titik dua' in p,
     [re.compile(r'\b[a-zA-Z0-9]+\s+:(?:\s+|$)')]),
])


# --- Kaidah Sintaksis Skripsi Jurnal JPLED Unimal (JRN-009..010) ---
CUSTOM_RULES.extend([
    # JRN-009: konjungsi intrakalimat 'Dan' di awal kalimat mandiri (hlm. 807)
    (lambda p: p == 'konjungsi dan di awal kalimat baru',
     [re.compile(r'(?:^|[.!?]\s+)\bDan\b\s+')]),
    # JRN-010: kontaminasi kuantor 'sebagian banyak' (hlm. 809)
    (lambda p: p == 'sebagian banyak',
     [re.compile(r'(?i)\bsebagian\s+banyak\b')]),
])


# --- Kaidah Diksi, Korelatif & Sintaksis Skripsi (JRN-011..014) ---
CUSTOM_RULES.extend([
    # JRN-011: jumlah rata-rata (Ar-Rumman 2024, hlm. 548)
    (lambda p: p == 'jumlah rata-rata',
     [re.compile(r'(?i)\bjumlah\s+rata-rata\b')]),
    # JRN-012: hingga ... maupun -> baik ... maupun (Jurnal Lazuardi 2024, hlm. 58)
    (lambda p: p == 'hingga ... maupun',
     [re.compile(r'(?i)\b(?:hingga|sampai)\b(?:\s+[\w\-]+){1,6}\s+\bmaupun\b')]),
    # JRN-013: pleonasme frasa verba bertujuan 'bertujuan untuk' (ILEAL 2018 hlm. 6)
    (lambda p: p == 'bertujuan untuk',
     [re.compile(r'(?i)\bbertujuan\s+untuk\b')]),
    # JRN-014: pemenggalan klausa subordinatif konsekutif 'Sehingga' di awal kalimat (Kande 2021 hlm. 155)
    (lambda p: p == 'konjungsi sehingga di awal kalimat baru',
     [re.compile(r'(?:^|[.!?]\s+)\bSehingga\b\s+')]),
])


# --- Kaidah EYD V (2022) & Seri Penyuluhan / Tata Naskah Dinas (2025) ---
CUSTOM_RULES.extend([
    # SPE-011: bilangan tingkat Romawi didahului 'ke-' (ke-XI, ke-IX) -> hapus 'ke-' atau pakai angka Arab
    (lambda p: 'ke-Romawi bertingkat ganda' in p,
     [re.compile(r'\bke-(?=[IVXLCDM]+\b)(?:M{0,3}(?:CM|CD|D?C{0,3})(?:XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3}))\b')]),
    # SPE-012: jenjang pendidikan tanpa tanda hubung antara huruf dan angka (S1, S2, S3, D3, D4)
    (lambda p: 'jenjang pendidikan tanpa tanda hubung' in p,
     [re.compile(r'\b(?:S[1-3]|D[1-4])\b')]),
    # BPK-046: pleonasme resiprokal ganda 'saling' + ber-...-an
    (lambda p: 'saling + ber-...-an resiprokal ganda' in p,
     [re.compile(r'(?i)\bsaling\s+ber(?:pandang|gandeng|rangkul|papas|tabrak|peluk|jabat|sentuh|salam|tukar|hadap|temu|pegang)an\b')]),
    # DIN-006: singkatan NIP diikuti tanda titik sebelum nomor induk
    (lambda p: 'singkatan NIP bertitik sebelum nomor' in p,
     [re.compile(r'\bNIP\.(?=\s*\d)')]),
    # DIN-007: singkatan jabatan/atas nama surat dinas tanpa tanda titik (a.n, Plt, Plh)
    (lambda p: 'singkatan jabatan surat dinas tanpa titik' in p,
     [re.compile(r'(?:(?<!\w)a\.n(?!\.)\s+|\bPl[th](?!\.)\s+(?=[A-Z]))')]),
    # DIN-008: verba berakhiran -kan ('memberitahukan') disisipi preposisi 'kepada' + insani
    (lambda p: 'memberitahukan kepada [insani]' in p,
     [re.compile(r'(?i)\bmemberitahukan\s+kepada\s+(?:saudara|bapak|ibu|peserta|seluruh|semua|para)\b')]),
    # DIN-009: pembuka surat tanpa subjek diawali 'Bagi semua/seluruh/para ...' + verba aktif
    (lambda p: "subjek surat diawali preposisi 'Bagi semua/seluruh" in p,
     [re.compile(r'(?:^|[.!?]\s+)Bagi\s+(?:semua|seluruh|para)\s+[^.!?,]{3,60}\b(?:menyerahkan|mengirimkan|mengisi|melengkapi|membawa|mengikuti)\b')]),
    # SPK-010: konjungsi korelatif ganda 'walaupun/meskipun ... , namun'
    (lambda p: "konjungsi korelatif ganda 'walaupun/meskipun ... namun'" in p,
     [re.compile(r'(?i)\b(?:walaupun|meskipun|biarpun|kendatipun)\b[^,.!?]{3,120},\s*namun\b')]),
    # SPK-011: pertumpukan dua penanda kausal 'disebabkan terjadinya' / 'dikarenakan terjadinya'
    (lambda p: 'disebabkan terjadinya / dikarenakan terjadinya' in p,
     [re.compile(r'(?i)\b(?:disebabkan|dikarenakan)\s+terjadi(?:nya)?\b')]),
])


@functools.lru_cache(maxsize=1024)
def _find_custom_rule(pattern_str):
    for predicate, compiled_list in CUSTOM_RULES:
        if predicate(pattern_str):
            return compiled_list
    return None


def match_custom_rules(pattern_str, clean_line):
    """Cek satu entri kaidah terhadap satu baris teks.

    Return (is_handled, matched, span):
    - is_handled: True jika pola punya penanganan kustom di tabel
    - matched: True jika baris memicu kaidah (satu regex cukup)
    - span: tuple (start, end) dari karakter yang cocok atau None
    """
    compiled_list = _find_custom_rule(pattern_str)
    if compiled_list is not None:
        for rgx in compiled_list:
            m = rgx.search(clean_line)
            if m:
                return (True, True, m.span())
        return (True, False, None)
    return (False, False, None)

# Kaidah kapitalisasi EYD V (SK 0424/I/BS.00.01/2022) — butuh cek CASE-SENSITIVE:
# pola salah = huruf kecil / kapital salah; contoh benar harus TIDAK cocok.
CUSTOM_RULES.append((lambda p: p == "teori darwin", [re.compile(r"\bteori\s+darwin\b")]))
CUSTOM_RULES.append((lambda p: p == "hukum archimedes", [re.compile(r"\bhukum\s+archimedes\b")]))
CUSTOM_RULES.append((lambda p: p == "rumus phytagoras", [re.compile(r"\brumus\s+phytagoras\b")]))
CUSTOM_RULES.append((lambda p: p == "Binti", [re.compile(r"\bBinti\b")]))
CUSTOM_RULES.append((lambda p: p == "Proklamasi kemerdekaan", [re.compile(r"\bProklamasi\s+kemerdekaan\b")]))
CUSTOM_RULES.append((lambda p: p == "batik cirebon", [re.compile(r"\bbatik\s+cirebon\b")]))
CUSTOM_RULES.append((lambda p: p == "soto banjar", [re.compile(r"\bsoto\s+banjar\b")]))
CUSTOM_RULES.append((lambda p: p == "kopi gayo", [re.compile(r"\bkopi\s+gayo\b")]))
CUSTOM_RULES.append((lambda p: p == "bubur manado", [re.compile(r"\bbubur\s+manado\b")]))
CUSTOM_RULES.append((lambda p: p == "buku bahasa dan sastra", [re.compile(r"\bbuku\s+bahasa\s+dan\s+sastra\b")]))

# Lambang satuan salah kapital (PUPI III.9): "5 Newton" -> "5 newton", "3 Kg" -> "3 kg".
# Case-sensitive: kapitalisasi adalah inti kesalahannya. Bentuk baku SI yang benar
# (N, J, W, kg, km, MB, GB) tidak boleh tertangkap.
CUSTOM_RULES.append((
    lambda p: p == "5 Newton / 3 Kg / 10 KM (lambang satuan salah kapital)",
    [re.compile(
        r"\b\d+(?:[.,]\d+)?\s?(?:Kg|KM|Cm|Mm|ML|Mg|KW|KWh|KWH|Kkal|KKal"
        r"|Newton|Joule|Watt|Volt|Ampere|Kelvin|Hertz|Pascal|Coulomb|Farad|Tesla|Ohm)\b"
    )],
))

# Bentuk terikat PUPI II.4.2.2.a (Kepmendiknas 146/U/2004): prefiks asing yang
# diserap menempel langsung pada bentuk dasar, bukan berdiri sebagai kata terpisah.
CUSTOM_RULES.append((lambda p: p == "pra sekolah", [re.compile(r"\bpra\s+(?:sekolah|sejarah|kondisi|ujian|karya|sidang|kuliah|krisis)\b", re.IGNORECASE)]))
CUSTOM_RULES.append((lambda p: p == "ekstra kurikuler", [re.compile(r"\b(?:ekstra|extra)\s+(?:kurikuler|kulikuler|kampus)\b", re.IGNORECASE)]))
CUSTOM_RULES.append((lambda p: p == "anti korupsi", [re.compile(r"\banti\s+(?:korupsi|komunis|virus|oksidan|sosial|narkoba)\b", re.IGNORECASE)]))
CUSTOM_RULES.append((lambda p: p == "multi disiplin", [re.compile(r"\bmulti\s+(?:disiplin|disipliner|fungsi|media|nasional|kultural|budaya)\b", re.IGNORECASE)]))
# --- Kaidah Kata Baku-Tidak Baku Buku Praktis Bahasa Indonesia 1 (BPBI-001..002, Badan Bahasa) ---
# Sumber: Buku Praktis Bahasa Indonesia 1, Bab Kata (id.wikisource.org). Tabel 32 + 21 pasang.
# Catatan: baud->baut, sutra->sutera, lembab->lembap TIDAK diaktifkan (makna teknis/akademik/umum yang sah).
CUSTOM_RULES.append((
    lambda p: "erobik / akountan / arkhais" in p,
    [re.compile(r"(?i)\b(?:erobik|akountan|arkhais|gladi|hirarki|karir|kuatir|konggres|kurve|nahkoda|perangko|setasiun|sahdu|trampil|trotoir|wakap|wassalam)\b")],
))
CUSTOM_RULES.append((
    lambda p: "antri / atlit / ajimat" in p,
    [re.compile(r"(?i)\b(?:antri|atlit|ajimat|faksimil|filem|ijin|joang|khabar|kangker|kongkrit|tentram|jiarah)\b")],
))

CUSTOM_RULES.append((
    lambda p: "karenanya / makanya" in p,
    [re.compile(r"(?i)\b(?:karenanya|makanya)\b")],
))

# --- Kaidah Kata Baku-Tidak Baku Buku Praktis Bahasa Indonesia 2 (BPBI-004, Badan Bahasa) ---
# Sumber: Buku Praktis Bahasa Indonesia 2, bagian 1-30 & 31-60 (id.wikisource.org).
# hisap->isap dan himbau->imbau TIDAK diaktifkan (kontroversial dalam pemakaian modern).
CUSTOM_RULES.append((
    lambda p: "dekret / azas / hutang" in p,
    [re.compile(r"(?i)\b(?:dekret|azas|hutang|maghrib|atmosfir|eksim|apotik|kridit)\b")],
))

# --- Pleonasme penghubung contoh Buku Praktis Bahasa Indonesia 2 (BPBI-005, Badan Bahasa) ---
# Melengkapi RML-004 (seperti misalnya). Sumber: BPBI2 61-90.
CUSTOM_RULES.append((
    lambda p: "contohnya seperti / umpamanya seperti" in p,
    [re.compile(r"(?i)\b(?:contohnya seperti|umpamanya seperti)\b")],
))

# --- Kaidah Buku Praktis Bahasa Indonesia 1 / Lain-lain & Sastra (BPBI-006, Badan Bahasa) ---
# 'dilola' salah bentukan (di- + kelola -> dikelola); 'sanjak' dihindari, dipakai 'sajak'.
CUSTOM_RULES.append((
    lambda p: "dilola / sanjak" in p,
    [re.compile(r"(?i)\b(?:dilola|sanjak)\b")],
))


# --- Bentuk tidak lazim BPBI2 (BPBI-007, Badan Bahasa) ---
# 'pirsawan' -> 'pemirsa'; 'debet' -> 'debit'; 'voucher' -> 'voucer'.
CUSTOM_RULES.append((
    lambda p: "pirsawan / debet / voucher" in p,
    [re.compile(r"(?i)\b(?:pirsawan|debet|voucher)\b")],
))


# --- Ejaan serapan Taktis Menyunting (TMS-001, BRIN 2019) ---
# Tabel 5.1 & 5.16: bentuk serapan salah eja pada naskah.
CUSTOM_RULES.append((
    lambda p: p.startswith("frustasi / negoisasi"),
    [re.compile(r"(?i)\b(?:frustasi|negoisasi|interprestasi|konkrit|komoditi|horisontal|infantri|marjin|dirijen|otobiografi|pondasi|birahi|minimun|orisinil|quantum|malpraktik)\b")],
))


# --- Bentuk tidak baku Taktis Menyunting (TMS-002, BRIN 2019) ---
# telanjur->terlanjur, nampak->tampak, cindera mata->cendera mata.
CUSTOM_RULES.append((
    lambda p: p.startswith("telanjur / perduli"),
    [re.compile(r"(?i)\b(?:telanjur|perduli|autodidak|trend|goncang|inagurasi|rubuh|men?contek|nampak|juridis|propemerintah|cindera\s+mata|cenderamata)\b"), re.compile(r"(?i)\bqori'")],
))


# --- Kesalahan leksikal pada terbitan ilmiah Kaltim (TBI-001, Pusat Bahasa 2009) ---
# propesional->profesional, ketrampilan->keterampilan, tergantung dari->bergantung pada.
CUSTOM_RULES.append((
    lambda p: p.startswith("propesional / kerampilan"),
    [re.compile(r"(?i)\b(?:propesional|kerampilan|ketrampilan|mengkomunikasikan|mendiskritkan|tehnologi|mengasilkan|prosentasi|nampaknya)\b"), re.compile(r"(?i)\btergantung\s+dari\b")],
))


# --- TMS-003: bentuk terikat ditulis serangkai (Taktis Menyunting 2019, Tabel 5.18) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("antar golongan"),
    [re.compile(r"(?i)\b(?:antar\s+golongan|multi\s+lateral|purna\s+wirawan|nara\s+hubung|pra\s+jabatan|sapta\s+krida)\b")],
))

# --- TMS-004: gabungan kata padu ditulis serangkai (Taktis Menyunting 2019, Tabel 5.20) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("acap kali"),
    [re.compile(r"(?i)\b(?:acap\s+kali|sedia\s+kala|kaca\s+mata|karya\s+wisata|kasat\s+mata|suka\s+cita|kosa\s+kata|syah\s+bandar|mata\s+hari|olah\s+raga|peri\s+bahasa|duka\s+cita|puspa\s+warna)\b")],
))


# --- TMS-005: bentuk lewah (Taktis Menyunting 2019, Tabel 5.6, hlm. 102-103) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("sangat sempurna sekali"),
    [re.compile(r"(?i)\b(?:sangat\s+sempurna\s+sekali|sangat\s+jauh\s+sekali|banyak\s+buku\-buku|beberapa\s+pendapat\-pendapat|melakukan\s+penangkapan|melakukan\s+pembinaan|melakukan\s+perubahan|menyatakan\s+pendapat|menggabungkan\s+menjadi\s+satu|saling\s+salip\-menyalip|menanyakan\s+pertanyaan|berencana\s+akan|maka\s+daripada\s+itu|maju\s+ke\s+depan)\b")],
))

# --- TMS-006: ungkapan idiomatik (Taktis Menyunting 2019, Tabel 5.8, hlm. 105-106) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("berdasarkan atas"),
    [re.compile(r"(?i)\b(?:berdasarkan\s+atas|bergantung\s+kepada|terjadi\s+atas)\b")],
))


# --- TMS-007: partikel pun ditulis serangkai (Taktis Menyunting 2019, Tabel 5.21, hlm. 119) ---
# adapun, ataupun, walaupun, meskipun; 'apa pun' dan 'terlambat pun' tetap terpisah.
CUSTOM_RULES.append((
    lambda p: p.startswith("ada pun"),
    [re.compile(r"(?i)\b(?:ada|jika|andai|kalau|atau|kendati|sungguh|bagaimana|walau|biar|meski|sementang)\s+pun\b")],
))

# --- TMS-008: angka + akhiran -an wajib bertanda hubung (Tabel 5.23, hlm. 122) ---
# 1980an -> 1980-an, Rp2.000an -> Rp2.000-an.
CUSTOM_RULES.append((
    lambda p: p.startswith("tahun 1980an"),
    [re.compile(r"(?i)\b(?:19|20)\d{2}an\b"),
     re.compile(r"(?i)\bRp\s?\d[\d.]*an\b")],
))


# --- TMS-009: spasi keliru pada tanda baca (Taktis Menyunting 2019, hlm. 124) ---
# 'kata .', 'kata ,', '( kata', 'kata )', 'namun,mungkin'. Titik dua sudah di JRN-008.
CUSTOM_RULES.append((
    lambda p: p.startswith("kata . / kata ,"),
    [re.compile(r"(?<=\S)\s+[.,;!?](?!\.)"),
     re.compile(r"[\(“\u2018]\s+"),
     re.compile(r"\s+[)\)”\u2019]"),
     re.compile(r",(?=[A-Za-z])")],
))

# --- TMS-010: koma/tanya kalimat langsung harus di dalam tanda petik (Tabel 5.25, hlm. 125) ---
# '“ini”, kata' -> '“ini,” kata'; '“ini”? tanya' -> '“ini?” tanya'.
CUSTOM_RULES.append((
    lambda p: p.startswith("'ini', kata"),
    [re.compile(r"[\u201d\u201c\"]\s*,\s+(?=(?:kata|ujar|tanya|tutur|jelas|ujarnya|katanya|sambung|lanjut|jawab|tegas|tambah|imbuh|pinta|minta|tandas|sahut|ucap)\b)"),
     re.compile(r"[\u201d\u201c\"]\s*\?(?=[\s,.;:])")],
))

# --- TMS-011: elipsis wajib berspasi (Taktis Menyunting 2019, hlm. 126) ---
# 'sedang...buku' -> 'sedang ... buku'; 'mereka....' -> 'mereka ....'.
CUSTOM_RULES.append((
    lambda p: p.startswith("sedang...buku"),
    [re.compile(r"(?<=[A-Za-z])\.{3,}(?=[A-Za-z])"),
     re.compile(r"(?<=[A-Za-z])\.{3,}(?=\s+[A-Za-z])")],
))

# --- TMS-012: tanda pisah en dash untuk rentang waktu (hlm. 126) ---
# 'pukul 09:00-10:00' dan 'tanggal 10-11 November' -> en dash.
CUSTOM_RULES.append((
    lambda p: p.startswith("pukul 09:00-10:00"),
    [re.compile(r"\b\d{1,2}[:.]\d{2}\s*-\s*\d{1,2}[:.]\d{2}\b"),
     re.compile(r"\b\d{1,2}\s*-\s*\d{1,2}\s+(?:Januari|Februari|Maret|April|Mei|Juni|Juli|Agustus|September|Oktober|November|Desember)\b")],
))


# --- TMS-013: konjungsi korelatif berpasangan, tapi juga tidak baku (Tabel 5.29, hlm. 128) ---
# 'tidak hanya ... tapi juga' -> '..., tetapi juga'; 'bukan hanya ... tapi juga' -> '..., melainkan juga'.
CUSTOM_RULES.append((
    lambda p: p.startswith("tidak hanya ..., tapi juga"),
    [re.compile(r"(?i)\b(?:tidak|bukan)\s+hanya\b[^.!?\n]{0,120}?\btapi\s+juga\b")],
))

# --- TMS-014: kalimat tidak sepadan, subjek didahului preposisi (Tabel 5.32, hlm. 130) ---
# 'Kepada pengendara mobil diharap ...' -> 'Pengendara mobil diharap ...'.
CUSTOM_RULES.append((
    lambda p: p.startswith("Kepada pengendara mobil diharap"),
    [re.compile(r"(?i)\b(?:kepada|bagi)(?!\s+hasil\b)\s+[A-Za-z][^.,;:!?\n]{2,50}?\s+(?<!yang )(?:diharap|diharapkan|diminta|dipersilakan)\b")],
))


# --- TMS-015: bentuk padu keliru pada istilah media (Zaim 2018) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("media masa / nara blog"),
    [re.compile(r"(?i)\bmedia\s+masa\b"), re.compile(r"(?i)\bnara\s+blog\b")],
))

# --- TMS-016: kekeliruan bentuk kata naskah akademik (Sihombing dkk. 2024) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("impelementasi / pelaksaan"),
    [re.compile(r"(?i)\b(?:impelementasi|pelaksaan)\b"),
     re.compile(r"(?i)\binstrument\b(?=\s+(?:penelitian|peneliti)\b)")],
))

# --- TMS-017: kata depan di serangkai dengan nomina (Rahman, BRIN 2022) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("dimasa / diinternet"),
    [re.compile(r"(?i)\bdi(?:masa|internet|rumah|kantor|lapangan|sekolah|kampus)\b")],
))

# --- TMS-018: imbuhan terpisah spasi dari bentuk dasar (Rahman, BRIN 2022) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("memudah kan / menumbuh kembangkan"),
    [re.compile(r"(?i)\b(?:mem(?!ang\b)|men|meng|meny)[a-z]{2,}\s+(?:kan|lah|nya)\b"),
     re.compile(r"(?<![A-Za-z])(?:men|mem|meng|meny)\s+[a-z]{4,}\b"),
     re.compile(r"(?i)\bmenumbuh\s+kembangkan\b")],
))

# --- TMS-019: nama bahasa berhuruf kecil (EYD; contoh Rahman, BRIN 2022) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("bahasa inggris / bahasa indonesia"),
    [re.compile(r"\b(?:ber)?bahasa\s+(?:inggris|indonesia|arab|jepang|belanda|prancis|mandarin|jawa|sunda|korea)\b")],
))

# --- TMS-020: gabungan kata bentuk bebas diserangkai (BP2, Bahasa Indonesia untuk Pejabat Pemerintah) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("sumberdaya / tatausaha"),
    [re.compile(r"(?i)\b(?:sumberdaya|tatausaha|dayacipta|peranserta|jurutulis|serahterima)\b"),
     re.compile(r"(?i)\b(?:sumber|tata|daya|peran|juru|serah)-(?:daya|usaha|cipta|serta|tulis|terima)\b")],
))

# --- TMS-021: unsur terikat ditulis terpisah (BP2, Bahasa Indonesia untuk Pejabat Pemerintah) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("non migas / antar daerah"),
    [re.compile(r"(?i)\b(?:non[ -]migas|antar[ -]daerah|purna[ -]jual|pra[ -]sejarah|catur[ -]warga)\b"),
     re.compile(r"(?i)\b(?:tri[ -]tunggal|dwi[ -]fungsi|eka[ -]darma|sapta[ -]pesona|sub[ -]sistem)\b")],
))


# --- TMS-023: singkatan jalan dan telepon pada alamat surat ---
CUSTOM_RULES.append((
    lambda p: p.startswith("Jl. / Jln. / Telp. / Tip."),
    [re.compile(r"\bJl\.\s*(?=[A-Z0-9])"),
     re.compile(r"\bJln\.\s*"),
     re.compile(r"(?i)\bTelp\.\s*(?=[0-9(])"),
     re.compile(r"(?i)\bTip\.\s*(?=[0-9(])")],
))

# --- TMS-024: format tanggal surat dinas ---
CUSTOM_RULES.append((
    lambda p: p.startswith("Tanggal 25 Bulan Juni Tahun 2015"),
    [re.compile(r"(?i)\btanggal\s+\d{1,2}\s+bulan\s+[a-z]+\s+tahun\s+\d{4}\b"),
     re.compile(r"\b\d{1,2}\s+(?:Jan|Feb|Mar|Apr|Mei|Jun|Jul|Agu|Sep|Okt|Nov|Des)\s*'\d{2}\b"),
     re.compile(r"(?<![\d-])\d{1,2}-\d{2}-\d{4}(?![\d-])"),
     re.compile(r"\b0\d\s+(?:Januari|Februari|Maret|April|Mei|Juni|Juli|Agustus|September|Oktober|November|Desember)\b")],
))

# --- TMS-025: penulisan jumlah lampiran surat dinas ---
CUSTOM_RULES.append((
    lambda p: p.startswith("Lampiran: 5 (lima) lembar"),
    [re.compile(r"(?i)\blampiran\s*:\s*(?:\d+\s*\([a-z]+\)|[a-z]+\s*\(\d+\))"),
     re.compile(r"(?i)\blampiran\s*:\s*-\s*$"),
     re.compile(r"(?i)\blamp(?:iran)?\.\s*(?=\d)")],
))

# --- TMS-026: nomor surat dinas diakhiri titik atau titik-hubung ---
CUSTOM_RULES.append((
    lambda p: p.startswith("Nomor: 3546/F8/C.11/2015."),
    [re.compile(r"(?i)\bnomor\s*:\s*\S+\s*\.-?\s*$")],
))

# --- TMS-022: alamat surat "Kepada Yth." / "Kepada Yang terhormat" (BP2, 2016) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("Kepada Yth /"),
    [re.compile(r"(?i)\bkepada\s+(?:yth\.?(?!\s+(?:bapak|ibu|sdr|saudara)\b)|yang\s+terhormat)(?=\s|$)")],
))


# --- TMS-027: singkatan NIP berkapitalisasi campur atau diberi spasi kelompok (BP2, 2016, hlm. 71) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("Nip 195900071989031003"),
    [re.compile(r"\bNip(?=\s*\d)"),
     re.compile(r"\bNIP\s+\d{1,6}(?:\s+\d{1,6})+\b")],
))

# --- TMS-028: pihak pemberi tembusan didahului "Yth." atau diikuti "sebagai laporan" (BP2, 2016, hlm. 72) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("Tembusan: Yth."),
    [re.compile(r"(?i)\btembusan\s*:[^\n]{0,60}?\byth\."),
     re.compile(r"(?i)\btembusan\s*:[^\n]*\bsebagai\s+laporan\b")],
))




# --- TMS-029: adjektiva pembanding diikuti "dari" alih-alih "daripada" (Mustakim 2019, hlm. 79) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("lebih besar dari /"),
    [re.compile(r"(?i)\b(?:lebih|kurang)\s+(?:besar|tinggi|jauh|banyak|kecil|berat|panjang|pendek|cepat|"
                r"lambat|murah|mahal|baik|pandai|luas|sempit|dalam|dangkal|rendah|dekat|sedikit|kuat|lemah|"
                r"muda|tua|mahir|efisien|efektif|kompleks|rumit|sulit|mudah|produktif|signifikan)\s+dari\b"
                r"(?!\s+\d)")],
))

# --- BAK-002: me-/di- + rubah alih-alih ubah (Pusat Bahasa 2009, hlm. 49) ---
CUSTOM_RULES.append((
    lambda p: p == "merubah",
    [re.compile(r"(?i)\b(?:me|di)rubah\w*\b")],
))

# --- BAK-004: mentargetkan alih-alih menargetkan (Pusat Bahasa 2009, hlm. 47) ---
CUSTOM_RULES.append((
    lambda p: p == "mentargetkan",
    [re.compile(r"(?i)\bmentarget\w*\b")],
))

# --- BPK-044: penanggungjawab diserangkai (Seri Penyuluhan Ejaan 2025, hlm. 35) ---
CUSTOM_RULES.append((
    lambda p: p == "penanggungjawab",
    [re.compile(r"(?i)\bpenanggungjawab\w*\b")],
))

# --- BPK-045: bekerjabakti diserangkai (Seri Penyuluhan Ejaan 2025, hlm. 35) ---
CUSTOM_RULES.append((
    lambda p: p == "bekerjabakti",
    [re.compile(r"(?i)\bbekerjabakti\w*\b")],
))

# --- BDD-009: klise "di mana hal ini" (Badudu) ---
CUSTOM_RULES.append((
    lambda p: p == "di mana hal ini",
    [re.compile(r"(?i),\s*di\s*mana\s+hal\s+ini\b")],
))

# --- TMS-030: gabungan kata dan partikel salah rangkai (Pusat Bahasa 2009, hlm. 42-45) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("salahsatunya / tindaklanjuti"),
    [re.compile(r"(?i)\bsalahsatu(?:nya)?\b"),
     re.compile(r"(?i)\btindaklanjuti\b|\b(?:di|men|meng)?tindak\s+lanjuti\b"),
     re.compile(r"(?i)\bunjukrasa\b"),
     re.compile(r"(?i)\blagipula\b"),
     re.compile(r"(?i)\bnon\s+aktif\b")],
))

# --- TMS-031: kordinator dan mengkomentari (Pusat Bahasa 2009, hlm. 45-46) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("kordinator / kordinasi"),
    [re.compile(r"(?i)\bkordinas\w*\b|\bkordinator\b"),
     re.compile(r"(?i)\bmengkomentar\w*\b")],
))

# --- SPE-014: tandatangani alih-alih tanda tangani (ditandatangani tetap benar) ---
CUSTOM_RULES.append((
    lambda p: p == "tandatangani",
    [re.compile(r"\btandatangani\b")],
))

# --- TMS-032: akhiran serapan -ir tidak baku -> -asi/-isasi (Pusat Bahasa 2009, hlm. 38-40) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("legalisir / inventarisir"),
    [re.compile(r"(?i)\b\w*legalisir\w*\b"),
     re.compile(r"(?i)\b\w*inventarisir\w*\b"),
     re.compile(r"(?i)\b\w*akomodir\w*\b"),
     re.compile(r"(?i)\b\w*organisir\w*\b"),
     re.compile(r"(?i)\b\w*regionalisir\w*\b"),
     re.compile(r"(?i)\b\w*koordinir\w*\b")],
))

# --- TMS-033: ejaan serapan yang belum disesuaikan (Pusat Bahasa 2009, hlm. 40-41) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("tehknik / enerjik"),
    [re.compile(r"(?i)\btehknik\w*\b|\btehnik\w*\b"),
     re.compile(r"(?i)\b\w*enerjik\w*\b"),
     re.compile(r"(?i)\b\w*rejional\w*\b"),
     re.compile(r"(?i)\baktip\w*\b"),
     re.compile(r"(?i)\bperogram\w*\b")],
))

# --- BAK-005: analisa alih-alih analisis ---
CUSTOM_RULES.append((
    lambda p: p == "analisa",
    [re.compile(r"(?i)\banalisa\b|\banalisa\w*kan\b")],
))

# --- BAK-007: praktek alih-alih praktik ---
CUSTOM_RULES.append((
    lambda p: p == "praktek",
    [re.compile(r"(?i)\bpraktek\w*\b")],
))

# --- BPK-038: mengaktipkan alih-alih mengaktifkan (Tata Naskah Dinas 2025, hlm. 40) ---
CUSTOM_RULES.append((
    lambda p: p == "mengaktipkan",
    [re.compile(r"(?i)\b\w*aktipkan\b")],
))

# --- TMS-034: penghubung antarkalimat di awal kalimat tanpa koma (Pusat Bahasa 2009, hlm. 33) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("Sementara itu ... / Oleh karena itu"),
    [re.compile(r"(?m)(?:^|[.!?]\s+|\n)\s*(?:Sementara\s+itu|Oleh\s+karena\s+itu|Dengan\s+demikian|Selain\s+itu)\s+(?=[^\s,.;:])")],
))

# --- TMS-035: verba tanpa awalan ber- sebagai predikat (Mustakim 2019, hlm. 62) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("sudah kumpul / telah kumpul"),
    [re.compile(r"(?i)\b(?:sudah|telah|akan|baru)\s+(?:kumpul|jumpa)\b"),
     re.compile(r"(?i)\bsampai\s+jumpa\b")],
))

# --- TMS-036: bentuk tidak baku daftar Mustakim 2019 (hlm. 67-68) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("akte / beaya"),
    [re.compile(r"(?i)\bakte\b"),
     re.compile(r"(?i)\bbeaya\b"),
     re.compile(r"(?i)\befektip\w*\b"),
     re.compile(r"(?i)\beffektif\w*\b"),
     re.compile(r"(?i)\beffisien\w*\b")],
))

# --- TMS-037: perangkapan verba, penyerapan keliru, dan preposisi serangkai (Kaltim 2009, hlm. 8-11) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("menstimulir / panili"),
    [re.compile(r"(?i)\b\w*stimulir\w*\b"),
     re.compile(r"(?i)\bpanili\b"),
     re.compile(r"(?i)\b(?:di(?:sekitar|areal|area|ladang|kebun|kantor|dunia|pasar|rumah|atas|sekolah))\b(?!\w)")],
))

# --- TMS-038: preposisi gabungan tidak lengkap (Kaltim 2009, hlm. 11) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("mulai Maret sampai Mei"),
    [re.compile(r"\b(?:mulai|Mulai|MULAI)\s+(?:[A-Z][a-z]+\s+|\d)[^.!?;\n]{0,60}?\bsampai\b(?!\s+dengan\b)"),
     re.compile(r"\b(?:dari|Dari|DARI)\s+(?:[A-Z][a-z]+\s+|\d)[^.!?;\n]{0,60}?\bsampai\b(?!\s+dengan\b)"),
     re.compile(r"\b(?:sejak|Sejak|SEJAK)\s+(?:bulan\s+)?(?:[A-Z][a-z]+\s+|\d)[^.!?;,\n]{0,60}?\bsampai\b(?!\s+dengan\b)")],
))

# --- TMS-039: serapan memposisikan/marjinal/hektar (Kaltim 2009, hlm. 24-25) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("memposisikan / marjinal"),
    [re.compile(r"(?i)\b\w*posisikan\b|\bmemposisi\b"),
     re.compile(r"(?i)\bmarjinal\w*\b"),
     re.compile(r"(?i)\bhektar\b")],
))

# --- TMS-040: konfiks wajib pada prioritas/hasil (Kaltim 2009, hlm. 25-26) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("menghasil (awalan meng-"),
    [re.compile(r"(?i)\bmenghasil\b")],
))

# --- TMS-041: respon alih-alih respons (Kaltim 2009, hlm. 26) ---
CUSTOM_RULES.append((
    lambda p: p == "respon",
    [re.compile(r"(?i)\brespon\b")],
))

# --- TMS-042: teoritis/sekedar (Kaltim 2009, hlm. 33-34) ---
CUSTOM_RULES.append((
    lambda p: p.startswith("teoritis / sekedar"),
    [re.compile(r"(?i)\bteoritis\b"),
     re.compile(r"(?i)\bsekedar\b")],
))

# --- SPK-012: subjek didahului penghubung bahwa setelah keterangan Menurut X (Kaltim 2009, hlm. 11-12) ---
CUSTOM_RULES.append((
    lambda p: "penghubung bahwa" in p,
    [re.compile(r"(?i)\bmenurut\s+[^,]{3,60},\s*bahwa\b")],
))

# --- SPK-013: frasa Berdasarkan X menunjukkan tanpa subjek (Kaltim 2009, hlm. 19) ---
CUSTOM_RULES.append((
    lambda p: "menunjukkan bahwa" in p,
    [re.compile(r"(?i)\bberdasarkan\s+[^,.]{3,60}\s+menunjukkan\b")],
))

# --- Siklus 20-22: EYD V (2022), Ejaan v2, Winarti (2009) 2.3.3-2.11, BPBI 2, Sasangka & Suladi ---
# Penyempurnaan BAK-012: kecualikan kata dasar 'antar' bermakna bawa/kirim (antar jemput, antar barang)
CUSTOM_RULES.append((
    lambda p: p == "antar ",
    [re.compile(r"(?i)\bantar\s+(?!jemput\b|barang\b|makanan\b|paket\b|surat\b|dokumen\b|obat\b|tamu\b)\w+")],
))

# EYD-065: gabungan kata padu EYD V Bab II.B.3.e yang salah dipisah
CUSTOM_RULES.append((
    lambda p: p.startswith("darma bakti / suka rela"),
    [re.compile(r"(?i)\bdarma\s+bakti\b"),
     re.compile(r"(?i)\bsuka\s+rela\b"),
     re.compile(r"(?i)\bsapu\s+tangan\b"),
     re.compile(r"(?i)\bbelas?\s+sungkawa\b"),
     re.compile(r"(?i)\bmana\s+suka\b"),
     re.compile(r"(?i)\bada\s+kalanya\b")],
))

# EYD-066: gabungan kata bebas & berimbuhan sepihak salah dirangkai
CUSTOM_RULES.append((
    lambda p: p.startswith("tandamata / kakitangan"),
    [re.compile(r"(?i)\btandamata\b"),
     re.compile(r"(?i)\bkakitangan\b"),
     re.compile(r"(?i)\bkakilima\b"),
     re.compile(r"(?i)\borangtua\b"),
     re.compile(r"(?i)\bberpestapora\b"),
     re.compile(r"(?i)\bkerjabaktikan\b")],
))

# EYD-067: gabungan kata berkonfiks penuh salah dipisah
CUSTOM_RULES.append((
    lambda p: p.startswith("menyama ratakan / menganak tirikan"),
    [re.compile(r"(?i)\b(?:menyama|disama|penyama)\s+ratakan\b|\bpenyama\s+rataan\b"),
     re.compile(r"(?i)\b(?:menganak|dianak|penganak)\s+tirikan\b"),
     re.compile(r"(?i)\b(?:mengambing|dikambing|pengambing)\s+hitamkan\b"),
     re.compile(r"(?i)\b(?:menganak|dianak)\s+emaskan\b"),
     re.compile(r"(?i)\b(?:menyerah|diserah|penyerah)\s+terimakan\b|\bpenyerah\s+terimaan\b"),
     re.compile(r"(?i)\bketidak\s+(?:tahuan|nyamanan|sempurnaan|ramahan|jelasan|adilan|pastian|mampuan|cocokan|stabilan|seimbangan|puasan|sesuaian)\b"),
     re.compile(r"(?i)\bkeputus\s+asaan\b"),
     re.compile(r"(?i)\bpengambil\s+alihan\b")],
))

# EYD-068: bentuk terikat EYD V Bab II.B.1.b, e & antar bebas
CUSTOM_RULES.append((
    lambda p: p.startswith("Yang Mahakuasa / eka bahasa"),
    [re.compile(r"\bYang\s+Mahakuasa\b"),
     re.compile(r"(?i)\beka\s+bahasa\b"),
     re.compile(r"(?i)\bnir\s+gagasan\b"),
     re.compile(r"(?i)\bantarjemput\b")],
))

# EYD-069: singkatan garis miring & format rupiah salah
CUSTOM_RULES.append((
    lambda p: p.startswith("a/n / u/p / d/a"),
    [re.compile(r"(?i)(?<![a-z0-9])\b(?:a/n|u/p|u/b|d/a)\b"),
     re.compile(r"\bRp\.\s*\d|\bRp\s+\d")],
))

# EYD-070: kesalahan tanda baca EYD V
CUSTOM_RULES.append((
    lambda p: p.startswith("(a). / ?."),
    [re.compile(r"(?:^|\n)\s*\([a-z0-9]{1,2}\)\.\s+\S"),
     re.compile(r"[?!]\.(?:\s|$)"),
     re.compile(r"(?i)\bskor\s+\d+\s*:\s*\d+\b")],
))

# EYD-071: unsur serapan EYD V Bab IV (asing -> baku)
CUSTOM_RULES.append((
    lambda p: p.startswith("akommodasi / asesoris"),
    [re.compile(r"(?i)\bakommodasi\b"),
     re.compile(r"(?i)\basesoris\b"),
     re.compile(r"(?i)\bkonsekwen(?:si)?\b"),
     re.compile(r"(?i)\b(?:ekivalen|equivalen)\w*\b"),
     re.compile(r"(?i)\bsouvenir\b"),
     re.compile(r"(?i)\bdiskripsi\w*\b"),
     re.compile(r"(?i)\bstirio\b"),
     re.compile(r"(?i)\bespresso\b"),
     re.compile(r"(?i)\btentrem\b"),
     re.compile(r"(?i)\bgrebek\b"),
     re.compile(r"(?i)\bblusukan\b")],
))

# EYD-072: unsur serapan Arab EYD V Bab IV
CUSTOM_RULES.append((
    lambda p: p.startswith("tafakkur / ummat"),
    [re.compile(r"(?i)\btafakkur\b"),
     re.compile(r"(?i)\bummat\b"),
     re.compile(r"(?i)\bkaffah\b"),
     re.compile(r"(?i)\btammat\b"),
     re.compile(r"(?i)\bnasehat\w*\b"),
     re.compile(r"(?i)\bhakekat\b"),
     re.compile(r"(?i)\bmahluk\b"),
     re.compile(r"(?i)\bsh[oa]hih\b"),
     re.compile(r"(?i)\bitikad\b"),
     re.compile(r"(?i)\budzur\b"),
     re.compile(r"(?i)\b(?:dzalim|dholim|zhalim)\b"),
     re.compile(r"(?i)\bdzat\b"),
     re.compile(r"(?i)\b(?:fikir|berfikir|memfikirkan|pemfikiran)\b"),
     re.compile(r"(?i)\b(?:nafas|bernafas|pernafasan)\b"),
     re.compile(r"(?i)\bfaidah\b")],
))

# TMS-043: peluluhan KTSP & penyisipan /k/ keliru Kaltim 2009
CUSTOM_RULES.append((
    lambda p: p.startswith("mengkursuskan / mengsukseskan"),
    [re.compile(r"(?i)\bmengkursuskan\b"),
     re.compile(r"(?i)\bmengsukseskan\b"),
     re.compile(r"(?i)\bmensejahterakan\b"),
     re.compile(r"(?i)\bmempercayai\b"),
     re.compile(r"(?i)\b(?:ditelarkan(?:nya)?|mentelarkan)\b")],
))

# TMS-044: serapan tidak baku terbitan ilmiah Kaltim 2009
CUSTOM_RULES.append((
    lambda p: p.startswith("mendiskriditkan / sekertaris"),
    [re.compile(r"(?i)\bmendiskriditkan\b"),
     re.compile(r"(?i)\b(?:sekertaris|serketaris)\b"),
     re.compile(r"(?i)\bsejogyanya\b"),
     re.compile(r"(?i)\bperaktek\w*\b"),
     re.compile(r"(?i)\b(?:ditolerir|menolerir)\b"),
     re.compile(r"(?i)\bkonperensi\b")],
))

# TMS-045: gabungan kata & bentuk terikat terbitan ilmiah Kaltim 2009
CUSTOM_RULES.append((
    lambda p: p.startswith("tenagakerja / semi permeabel"),
    [re.compile(r"(?i)\btenagakerja\b"),
     re.compile(r"(?i)\bsemi\s+permeabel\b"),
     re.compile(r"(?i)\bmenitik\s+beratkan\b")],
))

# TMS-046: kerancuan diksi & preposisi Kaltim 2009
CUSTOM_RULES.append((
    lambda p: p.startswith("mengacuh pada / hidup-hidupan"),
    [re.compile(r"(?i)\bmengacuh\s+(?:pada|kepada)\b"),
     re.compile(r"(?i)\bhidup-hidupan\b"),
     re.compile(r"(?i)\bmembahas\s+dan\s+membicarakan\b"),
     re.compile(r"(?i)\blain\s+di\s+samping\s+itu\b"),
     re.compile(r"(?i)\bpada\s+antara\s+tahun\b")],
))

# SPK-014: kerancuan Menurut pada X & preposisi objek verba transitif
CUSTOM_RULES.append((
    lambda p: p.startswith("Menurut pada ... / mengamanatkan kepada"),
    [re.compile(r"(?i)\bmenurut\s+pada\b"),
     re.compile(r"(?i)\bmengamanatkan\s+kepada\b"),
     re.compile(r"(?i)\bmenyimpulkan\s+tentang\b")],
))

# BPBI-008: ungkapan Dirgahayu & BBWI (BPBI 2 Bahasa)
CUSTOM_RULES.append((
    lambda p: p.startswith("dirgahayu HUT / dirgahayu RI ke-"),
    [re.compile(r"(?i)\bdirgahayu\s+HUT\b"),
     re.compile(r"(?i)\bdirgahayu\s+RI\s+ke[-\s]?\d+\b"),
     re.compile(r"(?i)\bHUT\s+RI\s+ke[-\s]?\d+\b"),
     re.compile(r"\bBBWI\b")],
))

# BPBI-009: bahwa setelah verba harapan/anjuran (BPBI 2 Kalimat)
CUSTOM_RULES.append((
    lambda p: p.startswith("menganjurkan bahwa / mengharapkan bahwa"),
    [re.compile(r"(?i)\b(?:menganjurkan|mengharapkan|mengimbau|menghimbau|memohon)\s+bahwa\b")],
))

# SPK-015: konjungsi antarkalimat tanpa koma (Suladi 2015 & BPBI 2)
CUSTOM_RULES.append((
    lambda p: p.startswith("Oleh sebab itu / Meskipun demikian"),
    [re.compile(r"(?m)(?:^|[.!?]\s+|\n)\s*(?:Oleh\s+sebab\s+itu|Meskipun\s+demikian|Walaupun\s+demikian|Sehubungan\s+dengan\s+(?:hal\s+)?itu|Berkaitan\s+dengan\s+hal\s+itu)\s+(?=[^\s,.;:])")],
))

# --- Kaidah Baharman (UNM) & Jurnal Skripsi/BIPA (Siklus 23-24: TMS-047, JSK-007..010) ---
CUSTOM_RULES.extend([
    # TMS-047: kesalahan adaptasi serapan (Baharman hlm. 11-12, 15)
    (lambda p: p.startswith("misskoordinasi / volantilitas"),
     [re.compile(r"(?i)\b(?:misskoordinasi|volantilitas|investation|illegal)\b")]),
    # JSK-007: kesalahan ejaan leksikal proposal skripsi (Khair 2018, hlm. 47-48)
    (lambda p: p.startswith("pengetauan / cendrung"),
     [re.compile(r"(?i)\b(?:pengetauan|cendrung|defenisi|kesangupan)\b"),
      re.compile(r"\balternative\b")]),
    # JSK-008: kata depan penunjuk lokasi/arah serangkai (Khair 2018 hlm. 49; Saputra & Alber 2021; Yahya 2018 hlm. 63)
    (lambda p: p.startswith("dikelas / kejenjang"),
     [re.compile(r"(?i)\b(?:dikelas|kejenjang|disana|disini|disitu)\b")]),
    # JSK-009: bentuk leksikal tidak baku (Yahya dkk. 2018, hlm. 63-64)
    (lambda p: p.startswith("kaos / silahkan / membawah"),
     [re.compile(r"(?i)\b(?:kaos|silahkan|membawah)\b")]),
    # JSK-010: ragam lisan tidak baku dalam teks formal (Yahya dkk. 2018, hlm. 58, 63; TBBBI 4 hlm. 523)
    (lambda p: p.startswith("tapi / udah / cuma"),
     [re.compile(r"(?i)\b(?:tapi|udah|cuma(?!-cuma))\b")]),
])

# --- Kaidah TBBBI Edisi IV Lanjutan (Siklus 25: TBB-032..035) ---
CUSTOM_RULES.extend([
    # TBB-032: partikel -kah pada predikat tanya berpola S-P yang diawali yang (TBBBI 4 hlm. 346-348)
    (lambda p: p.startswith("Yang ... apakah?"),
     [re.compile(r"(?:^|[.!?]\s+)Yang\s+(?:[a-zA-Z-]+\s+){1,5}(?:apakah|siapakah)\b")]),
    # TBB-033: konjungsi tetapi mengawali kalimat baru (TBBBI 4 hlm. 397-398)
    (lambda p: p.startswith("Tetapi ... (konjungsi"),
     [re.compile(r"(?m)(?:^|[.!?]\s+)Tetapi,?\s+")]),
    # TBB-034: artikula para dengan nomina takspesifik (TBBBI 4 hlm. 401)
    (lambda p: p.startswith("para anak / para orang / para manusia"),
     [re.compile(r"(?i)\bpara\s+(?:anak|orang|manusia)\b(?!\s+(?:ilmu|hukum|ahli))")]),
    # TBB-035: penanda sebab lisan tidak baku gara-gara / mentang-mentang (TBBBI 4 hlm. ~437)
    (lambda p: p.startswith("gara-gara / mentang-mentang"),
     [re.compile(r"(?i)\b(?:gara-gara|mentang-mentang)\b")]),
])

# --- Kaidah Beberapa Permasalahan (Pusat Bahasa) & Mekanisasi JSK-012..017 (Siklus 26-28) ---
CUSTOM_RULES.extend([
    # TMS-049: peluluhan mempedomani, bentuk baku & -kan (Beberapa Permasalahan hlm. 81-82; BRIN 2022 hlm. 17; JURRIBAH 2026)
    (lambda p: p.startswith("mempedomani / febuari"),
     [re.compile(r"(?i)\b(?:mempedomani|febuari|transpotasi|himbauan|menghimbau|dihimbau|menimalisir|meminimalisir|minimalisir)\b")]),
    # TMS-050: preposisi serangkai & walikota (Beberapa Permasalahan hlm. 83-84, 123)
    (lambda p: p.startswith("kearah / didaerah"),
     [re.compile(r"(?i)\b(?:kearah|didaerah|diluar|disamping|walikota)\b")]),
    # TMS-051: gabungan kata berkonfiks tindak lanjut terpisah (Beberapa Permasalahan hlm. 82)
    (lambda p: p.startswith("menindak lanjuti"),
     [re.compile(r"(?i)\b(?:menindak|ditindak|penindak)\s+lanjut(?:i|kan)\b")]),
    # EYD-074: spasi menyisip pada tanda hubung kata ulang (Beberapa Permasalahan hlm. 83)
    (lambda p: p.startswith("kata ulang berspasi"),
     [re.compile(r"(?i)\b([a-z]{3,})(?:\s+-\s*|-\s+)\1\b")]),
    # EYD-075: singkatan gelar & lembaga huruf kecil (Beberapa Permasalahan hlm. 121-123)
    (lambda p: p.startswith("Ssos / Msi / Spd"),
     [re.compile(r"\b(?:Ssos|Msi|Spd|Amd|Skom|Mkom|Shum|Mhum|Mts)\b")]),
    # JSK-012: akhiran -nya terpisah spasi (KIBASP 2026, hlm. 529)
    (lambda p: p.startswith("akhiran -nya ditulis terpisah"),
     [re.compile(r"(?i)(?<=[a-z]{3})\s+nya\b")]),
    # JSK-013: tanda titik ganda .. (KIBASP 2026, hlm. 530)
    (lambda p: p.startswith("tanda titik ganda .."),
     [re.compile(r"(?<![.\s])\.\.(?!\.)(?=\s|$)")]),
    # JSK-014: titik koma setelah yaitu/yakni (KIBASP 2026, hlm. 531)
    (lambda p: p.startswith("yaitu; / yakni;"),
     [re.compile(r"(?i)\b(?:yaitu|yakni)\s*;")]),
    # JSK-015: typo abstrak & nama aplikasi (JURRIBAH 2026; DEIKTIS 2026; Unmuh Jember 2020)
    (lambda p: p.startswith("manjemen / sehinnga"),
     [re.compile(r"(?i)\b(?:manjemen|sehinnga|lingkukngan)\b"),
      re.compile(r"\bGoogle\s+From\b"),
      re.compile(r"\bWhatsapp\b")]),
    # JSK-016: pastinya ragam cakapan ilmiah (DiSastra 2021, hlm. 66)
    (lambda p: p.startswith("pastinya (ragam cakapan"),
     [re.compile(r"(?i)\bpastinya\b")]),
    # JSK-017: Menurut (Nama Tahun) menyatakan... (DiSastra 2021, Kasus 6)
    (lambda p: p.startswith("Menurut (Nama, Tahun) menyatakan"),
     [re.compile(r"(?i)\bmenurut\s+\([A-Z][a-zA-Z]+[^)]*\d{4}[^)]*\)\s+(?:menyatakan|mengungkapkan|menjelaskan)\b")]),
])

# --- Kaidah Seri Penyuluhan 9 EYD & Kalimat v2 (Siklus 29-30: E9L-026..027, EYD-076, SPK-017..019) ---
CUSTOM_RULES.extend([
    # E9L-026: kesalahan ejaan surat kabar & bahan latihan EYD (Seri Penyuluhan 9 EYD hlm. 38-44)
    (lambda p: p.startswith("azasi / muqaddimah"),
     [re.compile(r"(?i)\b(?:azasi|muqaddimah|akhlaq|centraal|romadhon|ramadhon|teknologie|kwota|extradiksi|effektiv|psikhologi|alkuran|ke-tuhan-an)\b"),
      re.compile(r"(?i)\b(?:ma['’]siat|sa['’]at)\b")]),
    # E9L-027: singkatan nama lembaga/istilah umum diberi titik per huruf (Seri Penyuluhan 9 EYD hlm. 41, 43)
    (lambda p: p.startswith("D.P.R. / U.U.D."),
     [re.compile(r"\b(?:D\.P\.R|U\.U\.D|K\.B|S\.M\.A|S\.M\.P)\.")]),
    # EYD-076: preposisi penunjuk lokasi/arah serangkai tambahan (EYD V Bab II.G)
    (lambda p: p.startswith("diseluruh / ditempat"),
     [re.compile(r"(?i)\b(?:diseluruh|ditempat|diantara|ketengah)\b")]),
    # SPK-017: preposisi menyisip sebelum objek langsung verba transitif (Kalimat v2 hlm. 25-26)
    (lambda p: p.startswith("mengharap atas / berharap atas"),
     [re.compile(r"(?i)\b(?:mengharap|berharap|membangun)\s+(?:atas|daripada)\b")]),
    # SPK-018: pemasifan takgramatikal verba intransitif/kopulatif (Kalimat v2 hlm. 30)
    (lambda p: p.startswith("dijadi / dirupakan"),
     [re.compile(r"(?i)\b(?:dijadi|dirupakan)\b")]),
    # SPK-019: kalke siaran berita Inggris (Kalimat v2 hlm. 28)
    (lambda p: p.startswith("Ini [Nama] melaporkan dari"),
     [re.compile(r"(?i)\bIni\s+[A-Z][a-z]+\s+melaporkan\s+dari\b")]),
])

# --- Kaidah LIPI Press & Media Luar Ruang Lanjutan (Siklus 31-32: BRN-005..007, PSB-035) ---
CUSTOM_RULES.extend([
    # BRN-005: ke luar + tempat dipisah (LIPI Press hlm. 67)
    (lambda p: p.startswith("keluar negeri / keluar kota"),
     [re.compile(r"(?i)\bkeluar\s+(?:negeri|kota|daerah)\b")]),
    # BRN-006: preposisi di untuk keterangan waktu harian (LIPI Press hlm. 67)
    (lambda p: p.startswith("di malam hari / di siang hari"),
     [re.compile(r"(?i)\bdi\s+(?:malam|siang|pagi|sore)\s+(?:hari|sunyi|ini|itu)\b")]),
    # BRN-007: ejaan baku bertaraf, skala, suvenir, musala, gaji (LIPI Press hlm. 60; Opini XII hlm. 31; Semiloka 2019)
    (lambda p: p.startswith("bertarap / sekala / sovenir"),
     [re.compile(r"(?i)\b(?:bertarap|sekala|sovenir|mushol?la|gajih)\b")]),
    # PSB-035: serapan baku ruang publik (Media Luar Ruang 2015, hlm. 22-89)
    (lambda p: p.startswith("contemporer / boutique"),
     [re.compile(r"(?i)\b(?:contemporer|boutique|photocopy|photo\s+copy|taxi|mall)\b")]),
])
