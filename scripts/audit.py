#!/usr/bin/env python3
"""
Humanizer ID - Skrip Pemindai Kalke, Verba Ringan, & Istilah Lintas Bidang
Lisensi: MIT | Penulis: Hafizh Muzani (apissaj)
Repositori: https://github.com/apissaj/humanizer-id

Penggunaan:
    python scripts/audit.py <path_ke_file.md>
    python scripts/audit.py --demo
"""

import sys
import os
import json
import re

def load_data(kampus_id=None):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    kalke_path = os.path.join(base_dir, "data", "kalke-indonesia.json")
    glosarium_path = os.path.join(base_dir, "data", "glosarium-lintas-bidang.json")
    kampus_path = os.path.join(base_dir, "data", "pedoman-kampus.json")
    
    kalke_dict = {}
    glosarium_dict = {}
    kampus_dict = {}
    
    if os.path.exists(kalke_path):
        with open(kalke_path, "r", encoding="utf-8") as f:
            kalke_dict = json.load(f)
    else:
        print(f"[!] Peringatan: {kalke_path} tidak ditemukan.", file=sys.stderr)

    if os.path.exists(glosarium_path):
        with open(glosarium_path, "r", encoding="utf-8") as f:
            glosarium_dict = json.load(f)

    if kampus_id and os.path.exists(kampus_path):
        with open(kampus_path, "r", encoding="utf-8") as f:
            kampus_dict = json.load(f).get("kampus", {}).get(kampus_id.lower())
            if kampus_dict:
                print(f"[*] Preset kampus aktif: {kampus_dict.get('nama')} ({kampus_id})")
            else:
                print(f"[!] Preset kampus '{kampus_id}' tidak ditemukan di pedoman-kampus.json", file=sys.stderr)

    return kalke_dict, glosarium_dict, kampus_dict

def audit_text(text, kalke_dict, glosarium_dict, kampus_dict=None):
    findings = []
    lines = text.splitlines()

    for line_idx, line in enumerate(lines, start=1):
        clean_line = line.strip()
        if not clean_line or clean_line.startswith("```"):
            continue

        # Pemeriksaan Aturan Khusus Heading / Preset Kampus (bisa jalan pada baris markdown heading #)
        if kampus_dict and clean_line.startswith("#"):
            if "ipb" in str(kampus_dict.get("nama", "")).lower():
                m_subbab = re.search(r'^(?:#+\s*)(\d+\.\d+\.)\s+(.+)', clean_line)
                if m_subbab:
                    findings.append({
                        "baris": line_idx,
                        "kategori": "pedoman_kampus_ipb",
                        "id": "KAMPUS-IPB-01",
                        "pola": m_subbab.group(1),
                        "saran": [m_subbab.group(1)[:-1]],
                        "penjelasan": "Pedoman PPKI IPB Edisi Ke-4: Penomoran sub-bab tidak boleh diakhiri titik (gunakan '" + m_subbab.group(1)[:-1] + "').",
                        "kalimat": clean_line
                    })

        # Baris heading markdown murni dilewati untuk audit leksikal teks isi
        if clean_line.startswith("#"):
            continue

        # 1. Scan Kalke, Verba Ringan, Pola AI, Kata Baku
        for cat_key, cat_data in kalke_dict.get("kategori", {}).items():
            for entry in cat_data.get("entri", []):
                pattern_str = entry["pola"]
                # Deteksi pola template seperti "Meskipun X, bukan berarti Y", "antara A dengan B", "baik A ataupun B"
                if "..." in pattern_str or " X, " in pattern_str or " A " in pattern_str or "sedangkan" in pattern_str or "para tamu-tamu" in pattern_str or "karena ... maka" in pattern_str or "meskipun ... tetapi" in pattern_str or "ganda jamak" in pattern_str or "hanya ... saja" in pattern_str or "itu sendiri" in pattern_str or "mau tidak mau" in pattern_str or "konjungsi koordinatif" in pattern_str or "'yang' bertingkat" in pattern_str or "nomor NIK" in pattern_str or "kartu KIP" in pattern_str or "virus HIV" in pattern_str or "partai PPP" in pattern_str or "pronomina persona taksa" in pattern_str or "Karena itu," in pattern_str or "Selain itu (tanpa koma)" in pattern_str or "namun intrakalimat tanpa koma" in pattern_str or ", sehingga" in pattern_str or ", karena" in pattern_str or "sangat ... sekali" in pattern_str or "hanya ... saja" in pattern_str or "bukan hanya" in pattern_str or "bales / dibales" in pattern_str or "kata ganti persona" in pattern_str or "kata kerja mental aktif" in pattern_str or "konjungsi koordinatif 'dan' tidak sejajar" in pattern_str or "unsur terikat ditulis terpisah" in pattern_str or "Di era digital" in pattern_str or "sitasi tidak lengkap" in pattern_str or "kendati demikian" in pattern_str or "akibat-sebab terbalik" in pattern_str or "nama diri geografi yang menjadi nama jenis" in pattern_str or "bentuk dasar turunan nama bangsa" in pattern_str or "jabatan/pangkat tanpa nama orang" in pattern_str or "imbuhan di- ditulis terpisah" in pattern_str or "dimana/diketika/disewaktu" in pattern_str or "tanggungjawab" in pattern_str or "dari pada" in pattern_str or "angka 2 sebagai penanda" in pattern_str or "membahas tentang" in pattern_str or "kalimat tanpa subjek berawalan preposisi" in pattern_str or "atas perhatiannya" in pattern_str or "Kepada Yth." in pattern_str or "titik dua sebelum pelengkap" in pattern_str or "partikel pun ditulis serangkai" in pattern_str or "sedangkan dipakai di awal kalimat" in pattern_str or "elipsis subjek melompati" in pattern_str or "pleonasme pasangan sinonim" in pattern_str or "antara lain lalu ditutup" in pattern_str or "bentuk ulang resiprokal" in pattern_str or "penyalahgunaan dan sebagainya" in pattern_str or "ungkapan idiomatis dihilangkan" in pattern_str or "makna asal/sumber/penjelasan" in pattern_str or "menggugurkan konsonan akhir" in pattern_str or "istilah klasik/generik dijauhkan" in pattern_str or "awalan non- dipertahankan mentah" in pattern_str or "bentuk jamak Latin/Inggris" in pattern_str or "akhiran keahlian -wan" in pattern_str or "pemukiman dipakai untuk menyebut kawasan" in pattern_str or "pengubahan dipakai untuk keadaan" in pattern_str or "metanalisis palsu akhiran asing" in pattern_str or "gabungan bentuk bebas ditulis serangkai" in pattern_str or "peluluhan peN- keliru pada nomina pelaku" in pattern_str or "melainkan dipasangkan dengan tidak" in pattern_str or "perincian tidak sejajar bentuknya" in pattern_str or "salah nalar frasa bebas parkir" in pattern_str:
                    matched = False
                    if "bukan berarti" in pattern_str and "bukan berarti" in clean_line.lower():
                        matched = True
                    elif "antara" in pattern_str and "dengan" in pattern_str:
                        if re.search(r'\bantara\b.+?\bdengan\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "baik" in pattern_str and "ataupun" in pattern_str:
                        if re.search(r'\bbaik\b.+?\bataupun\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "bukan" in pattern_str and ("tetapi" in pattern_str or "namun" in pattern_str):
                        if re.search(r'\bbukan\b.+?\b(tetapi|namun)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "sedangkan" in pattern_str:
                        if re.search(r'(?:^|[.!?]\s+)\bsedangkan\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "para tamu-tamu" in pattern_str:
                        if re.search(r'\b(para|beberapa|semua)\s+([a-zA-Z]+)-\2\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "karena ... maka" in pattern_str:
                        if re.search(r'\bkarena\b.+?\bmaka\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "meskipun ... tetapi" in pattern_str:
                        if re.search(r'\b(meskipun|walaupun|biarpun)\b.+?\b(tetapi|namun)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "ganda jamak" in pattern_str:
                        if re.search(r'\b(para|beberapa|berbagai|semua)\s+([a-zA-Z]+)-\2\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "itu sendiri" in pattern_str or "mau tidak mau" in pattern_str:
                        if re.search(r'\b(itu sendiri|mau tidak mau)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "konjungsi koordinatif" in pattern_str:
                        # Kesejajaran: kalimat majemuk aktif pasif campuran via 'dan'
                        if re.search(r'\boleh\s+\w+\s+dan\s+\w+\s+yang\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "'yang' bertingkat" in pattern_str:
                        # Kalimat buntung yang bertingkat tanpa predikat utama
                        if re.search(r'^\s*[A-Z][^.!?]*\byang\b[^.!?]*\byang\b[^.!?]*\byang\b[^.!?]*\.$', clean_line):
                            matched = True
                    elif "nomor NIK" in pattern_str:
                        if re.search(r'\b(nomor\s+NIK|nomor\s+PIN)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "kartu KIP" in pattern_str:
                        if re.search(r'\b(kartu\s+KIP|kartu\s+KTP|ATM\s+card)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "virus HIV" in pattern_str:
                        if re.search(r'\bvirus\s+HIV\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "partai PPP" in pattern_str:
                        if re.search(r'\bpartai\s+(PPP|PDIP|PAN)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "pronomina persona taksa" in pattern_str:
                        if re.search(r'\b[A-Z][a-z]+\s+dan\s+\w+\b[^.!?]{2,80}\b(ia|dia)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "hierarki kata umum-khusus" in pattern_str:
                        # '[telaah]': tandai hanya kalimat pembatasan 'jangankan...pun'
                        if re.search(r'\bjangankan\b[^.!?]{0,60}\bpun\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "urutan sebab-akibat" in pattern_str or "akibat-sebab terbalik" in pattern_str:
                        # Konjungsi akibat ('oleh sebab itu', 'oleh karena itu', 'karena itu')
                        # di depan klausa yang bukan akibat — deteksi heuristic:
                        # konjungsi akibat muncul di awal kalimat setelah kalimat pendek sebelumnya
                        if re.search(r'(?:^|[.!?]\s+)\b(oleh sebab itu|oleh karena itu|karena itu)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "nama diri geografi yang menjadi nama jenis" in pattern_str:
                        # Kapitalisasi salah pada nama jenis: Kunci Inggris, Pisang Ambon, Mesin Diesel, 15 Watt
                        if re.search(r'\b(Kunci\s+Inggris|Pisang\s+Ambon|Mesin\s+Diesel|15\s+Watt)\b', clean_line):
                            matched = True
                    elif "bentuk dasar turunan nama bangsa" in pattern_str:
                        # Kapitalisasi atau pemenggalan salah pada turunan bangsa
                        if re.search(r'\b(Peng-Indonesia-an|Keinggris-Inggrisan|Pengindonesiaan)\b', clean_line):
                            matched = True
                    elif "jabatan/pangkat tanpa nama orang" in pattern_str:
                        # Kapital jabatan umum: Sejumlah Menteri, rapat Kabinet
                        if re.search(r'\b(Sejumlah\s+Menteri|rapat\s+Kabinet|para\s+Gubernur|para\s+Menteri)\b', clean_line):
                            matched = True
                    elif "imbuhan di- ditulis terpisah" in pattern_str:
                        # Salah tulis imbuhan pasif di-: 'di analisis', 'di teliti', 'di observasi', 'di kembangkan'
                        if re.search(r'\bdi\s+(analisis|teliti|observasi|kembangkan|temukan|gunakan|lakukan|tulis|baca|uji)\b', clean_line, re.IGNORECASE):
                            matched = True
                    # --- Matcher presisi KJK (Alwi dkk. 2017) ---
                    elif "sedangkan dipakai di awal kalimat" in pattern_str:
                        # 'Sedangkan' di awal kalimat setelah titik
                        if re.search(r'(?:^|[.!?]\s+)\bSedangkan\b', clean_line):
                            matched = True
                    elif "elipsis subjek melompati" in pattern_str:
                        # Kalimat diawali modalitas + pasif tanpa subjek: 'Perlu dilakukan...', 'Harus diperhatikan...'
                        if re.search(r'(?:^|[.!?]\s+)\b(Perlu|Harus|Dapat|Mungkin|Sebaiknya|Bisa)\s+(dilakukan|diperhatikan|dipertimbangkan|ditinjau|disimpulkan|dicatat|diketahui|disebutkan|dilihat|dipahami)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "atas perhatiannya" in pattern_str:
                        # Frasa penutup surat salah sasaran persona
                        if re.search(r'\bAtas perhatiannya\b|\bkerja samanya\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "Kepada Yth." in pattern_str:
                        # Alamat surat berawalan 'Kepada Yth.'
                        if re.search(r'\bKepada\s+Yth\.\s+Bapak\s+[A-Z]', clean_line):
                            matched = True
                    elif "titik dua sebelum pelengkap" in pattern_str:
                        # Verba transitif/predikat diikuti langsung tanda titik dua
                        if re.search(r'\b(memerlukan|membutuhkan|membeli|menyediakan|membawa|menggunakan|meliputi):\s+\w+', clean_line, re.IGNORECASE):
                            matched = True
                    elif "partikel pun ditulis serangkai" in pattern_str:
                        # Serangkai keliru: apapun, siapapun, satupun, berapapun (di luar 12 konjungsi padu)
                        if re.search(r'\b(apapun|siapapun|satupun|berapapun|dimanapun|kapanpun|bagaimanapun(?:\s)?[^,])\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "membahas tentang" in pattern_str:
                        # Verba transitif + preposisi mubazir: membahas tentang, membicarakan mengenai, mempelajari tentang
                        if re.search(r'\b(membahas|membicarakan|mempelajari|meneliti|mengkaji|menguraikan)\s+(tentang|mengenai)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "kalimat tanpa subjek berawalan preposisi" in pattern_str:
                        # 'Dalam X ini akan membahas...' / 'Pada penelitian ini akan meneliti...'
                        if re.search(r'(?:^|[.!?]\s+)\b[Dd]alam\s+\w+\s*(?:ini|tersebut)\s+(?:akan\s+)?(?:membahas|membicarakan|meneliti|menganalisis|mengkaji|menguraikan|menyajikan|mengevaluasi|mengungkap|memaparkan)\b', clean_line):
                            matched = True
                    elif "Karena itu," in pattern_str:
                        # Kausalitas informal tanpa 'Oleh': 'Karena itu,' di awal kalimat
                        if re.search(r'(?:^|[.!?]\s+)\bKarena itu,\s+', clean_line):
                            matched = True
                    elif "Selain itu (tanpa koma)" in pattern_str:
                        # 'Selain itu' di awal kalimat TIDAK diikuti koma
                        if re.search(r'(?:^|[.!?]\s+)\bSelain itu(?!,)\s+\S', clean_line, re.IGNORECASE):
                            matched = True
                    elif "namun intrakalimat tanpa koma" in pattern_str:
                        # 'namun' di tengah kalimat TANPA tanda koma sebelumnya
                        if re.search(r'(?<!,)\s+\bnamun\b\s+\S', clean_line, re.IGNORECASE):
                            matched = True
                    elif ", sehingga" in pattern_str:
                        # ', sehingga' keliru — konjungsi subordinatif tidak boleh didahului koma
                        if re.search(r',\s*sehingga\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif ", karena" in pattern_str:
                        # ', karena' keliru — klausa subordinatif tidak boleh didahului koma
                        if re.search(r',\s*karena\b', clean_line, re.IGNORECASE):
                            matched = True

                    # --- Matcher kehematan & gaya (UNJA, Sasangka, Moeliono) ---
                    elif "hanya ... saja" in pattern_str:
                        # Redundansi adverbia pembatas: 'hanya ... saja'
                        if re.search(r'\bhanya\b[^.!?]{1,40}\bsaja\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "pleonasme pasangan sinonim" in pattern_str:
                        if re.search(r'\b(agar\s+supaya|demi\s+untuk|lalu\s+kemudian|kalau\s+seandainya|seperti\s+misalnya|contohnya\s+seperti)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "antara lain lalu ditutup" in pattern_str:
                        if re.search(r'\b(misalnya|seperti|contohnya|umpamanya|antara lain)\b[^.!?]{4,120}?\b(dan\s+lain-lain|dan\s+sebagainya|dan\s+seterusnya)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "bentuk ulang resiprokal" in pattern_str:
                        if re.search(r'\bsaling\s+(\w+)-(\w+)\b', clean_line, re.IGNORECASE) or re.search(r'\bsaling\s+ber\w+an\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "penyalahgunaan dan sebagainya" in pattern_str:
                        if re.search(r'\b(sesi\s+\w+,\s*sesi\s+\w+|pertama,\s*\w+,\s*kedua)[^.!?]{0,60}\bdan\s+lain-lain\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "ungkapan idiomatis dihilangkan" in pattern_str:
                        if re.search(r'\b(sesuai|berkaitan|sehubungan)\s+(?!dengan\b)(?=(tidak|kurang|konteks|hal|masalah|perkara|ketentuan|aturan))', clean_line, re.IGNORECASE) or re.search(r'\b(bergantung|tergantung)\s+(?!pada\b)(?=(hasil|kondisi|keputusan|situasi|tingkat))', clean_line, re.IGNORECASE):
                            matched = True
                    elif "makna asal/sumber/penjelasan" in pattern_str:
                        if re.search(r'\bterbuat\s+daripada\b|\btujuan\s+daripada\b|\bmaksud\s+daripada\b|\bterbuat\s+\w*\s*daripada\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "menggugurkan konsonan akhir" in pattern_str:
                        # TII-001: ejaan fonemik - gugur konsonan akhir tak berfungsi
                        if re.search(r'\b(dominant|informant|tolerant|relevant|optimist|realist|nationalist|manifest|latent|konsultan?\w*ant)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "istilah klasik/generik dijauhkan" in pattern_str:
                        # TII-002: istilah dijauhkan
                        if re.search(r'\bzat\s+lemas\b|\bzat\s+air\b|\bzat\s+asam\b|\billmu\s+pasti\b|\billmu\s+pisah\b|\bsaran\s+diri\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "awalan non- dipertahankan mentah" in pattern_str:
                        # TII-003: non- tanpa padanan tak-/bukan-/nir-
                        if re.search(r'\bnon-\s?\w+|\bnon\s\w+', clean_line, re.IGNORECASE):
                            matched = True
                    elif "bentuk jamak Latin/Inggris" in pattern_str:
                        # TII-004: jamak Latin yang dihidupkan
                        if re.search(r'\bfoki\b|\blaboratoria\b|\bcriteria\b|\bphenomena\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "akhiran keahlian -wan" in pattern_str:
                        # TII-005: -wan pada akar tidak berakhir -a
                        if re.search(r'\b\w+logiwan\b|\bteknikwan\b|\bsainswan\b|\bhukumwan\b|\bekonomiwan\b|\bmanajemenwan\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "pemukiman dipakai untuk menyebut kawasan" in pattern_str:
                        # TIQ-001: pemukiman vs permukiman
                        if re.search(r'\bpemukiman\s+(padat|kumuh|liar|warga|penduduk|baru|transmigran|pedesaan|perkotaan)\b|\bkawasan\s+pemukiman\b|\barea\s+pemukiman\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "pengubahan dipakai untuk keadaan" in pattern_str:
                        # TIQ-002: pengubahan vs perubahan
                        if re.search(r'\bpengubahan\s+(iklim|sosial|zaman|sikap|cuaca|pola)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "metanalisis palsu akhiran asing" in pattern_str:
                        # TIQ-003: metanalisis sinergitas / standarisasi
                        if re.search(r'\bsinergitas\b|\bstandarisasi\b|\befektifitas\b|\baktifitas\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "gabungan bentuk bebas ditulis serangkai" in pattern_str:
                        # TIQ-004: gabungan bentuk bebas tanpa spasi
                        if re.search(r'\bibukota\b|\bkerjasama\b|\bbatubara\b|\banakperusahaan\b|\btokoserbaada\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "peluluhan peN- keliru pada nomina pelaku" in pattern_str:
                        # TIQ-005: peN- salah luluh
                        if re.search(r'\bpengrajin\b|\bpenterjemah\b|\bpensurvei\b|\bpembom\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "melainkan dipasangkan dengan tidak" in pattern_str:
                        # SYT-001: korelatif tidak ... melainkan
                        if re.search(r'\btidak\s+[^.!?]{2,80}?\bmelainkan\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "perincian tidak sejajar bentuknya" in pattern_str:
                        # SYT-002: perincian campur nomina/verba me-/pasif
                        if re.search(r'\bmeliputi\b[^.!?]*\b(membuat|diberi|dilakukan|menambah|mengubah)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "salah nalar frasa bebas parkir" in pattern_str:
                        # SYT-003: bebas parkir
                        if re.search(r'\bbebas\s+parkir\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "sangat ... sekali" in pattern_str:
                        # Pleonasme adverbia: 'sangat [kata] sekali'
                        if re.search(r'\bsangat\s+\w+\s+sekali\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "bukan hanya" in pattern_str:
                        # Klise AI: 'bukan hanya ..., melainkan juga ...'
                        if re.search(r'\bbukan hanya\b[^.!?]{1,60}\b(melainkan juga|tetapi juga)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "bales / dibales" in pattern_str:
                        # Ragam lisan percakapan: bales, dibales, ngirim, bilang
                        if re.search(r'\b(bales|dibales|ngirim|dingirim)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "kata ganti persona" in pattern_str:
                        # Persona pertama/kedua dalam karya ilmiah: saya, aku, kamu
                        if re.search(r'\b(saya|aku|kamu)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "konjungsi koordinatif 'dan' tidak sejajar" in pattern_str:
                        # Pasif di klausa pertama, aktif di klausa kedua: 'oleh X dan Y yang me-...'
                        if re.search(r'\boleh\s+\w+\s+dan\s+\w+\s+yang\s+me', clean_line, re.IGNORECASE):
                            matched = True
                    elif "kata kerja mental aktif" in pattern_str:
                        # Verba mental aktif persona: kami berasumsi/kita menduga/kami mengira
                        if re.search(r'\b(kami|kita|saya)\s+(berasumsi|menduga|mengira|memahami|menyadari|merasa)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "sitasi tidak lengkap" in pattern_str:
                        # 'Menurut ahli,' tanpa nama belakang dan tahun
                        if re.search(r'\bmenurut\s+ahli\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "kendati demikian (konsesif tidak paralel)" in pattern_str:
                        # 'Kendati demikian,' di awal kalimat
                        if re.search(r'(?:^|[.!?]\s+)\bKendati demikian,', clean_line):
                            matched = True
                    elif "unsur terikat ditulis terpisah" in pattern_str:
                        # 'sub unit', 'maha guru', 'peri laku', 'antar kota'
                        if re.search(r'\b(sub\s+unit|sub\s+bagian|maha\s+guru|peri\s+laku|antar\s+kota)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "Di era digital" in pattern_str:
                        # Pembuka klise AI fleksibel
                        if re.search(r'\bDi era digital yang berkembang\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "dimana/diketika/disewaktu" in pattern_str:
                        # Penggunaan 'dimana' sebagai kata hubung tengah kalimat
                        if re.search(r'\b\w+\s+(dimana|di mana|diketika|disewaktu)\s+\w+\b', clean_line, re.IGNORECASE) and not clean_line.strip().endswith("?"):
                            matched = True
                    elif "tanggungjawab" in pattern_str:
                        # Gabungan kata salah serangkai
                        if re.search(r'\b(tanggungjawab|kerjasama|tandatangan|terimakasih|ujicoba|kantorpos|dutabesar|cagaralam)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "dari pada" in pattern_str:
                        # Kata senyawa salah dipisah
                        if re.search(r'\b(dari\s+pada|barang\s+kali|pada\s+hal|sekali\s+gus|bila\s+mana|apa\s+bila|mata\s+hari|bumi\s+putra|segi\s+tiga)\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "angka 2 sebagai penanda" in pattern_str:
                        # Angka 2 pada kata ulang
                        if re.search(r'\b[a-zA-Z]+2\b', clean_line):
                            matched = True
                    
                    if matched:
                        findings.append({
                            "baris": line_idx,
                            "kategori": cat_key,
                            "id": entry["id"],
                            "pola": pattern_str,
                            "saran": entry["saran_pengganti"],
                            "penjelasan": entry["penjelasan"],
                            "kalimat": clean_line
                        })
                else:
                    regex = re.compile(r'\b' + re.escape(pattern_str.strip()) + r'\b', re.IGNORECASE)
                    if regex.search(clean_line):
                        findings.append({
                            "baris": line_idx,
                            "kategori": cat_key,
                            "id": entry["id"],
                            "pola": pattern_str,
                            "saran": entry["saran_pengganti"],
                            "penjelasan": entry["penjelasan"],
                            "kalimat": clean_line
                        })

        # 2. Scan Glosarium Lintas Bidang (Istilah Asing Belum Dibakukan & Ungkapan Jenuh)
        for domain_key, domain_data in glosarium_dict.get("bidang", {}).items():
            # Cek istilah asing
            for item in domain_data.get("istilah", []):
                term_raw = item["asing"].split("(")[0].strip()
                if len(term_raw) >= 3:
                    regex = re.compile(r'\b' + re.escape(term_raw) + r'\b', re.IGNORECASE)
                    if regex.search(clean_line):
                        findings.append({
                            "baris": line_idx,
                            "kategori": f"glosarium_{domain_key}",
                            "id": f"GLOS-{domain_key[:3].upper()}",
                            "pola": item["asing"],
                            "saran": [item["baku"]],
                            "penjelasan": item.get("catatan", "Padanan istilah resmi bahasa Indonesia."),
                            "kalimat": clean_line
                        })
            # Cek kaidah ekonomi kata jurnalistik
            for item in domain_data.get("kaidah_ekonomi_kata", []):
                jenuh_str = item["jenuh"]
                if jenuh_str.lower() in clean_line.lower():
                    findings.append({
                        "baris": line_idx,
                        "kategori": "jurnalistik_ekonomi_kata",
                        "id": "JURNAL-EKONOMI",
                        "pola": jenuh_str,
                        "saran": [item["lugas"]],
                        "penjelasan": item["alasan"],
                        "kalimat": clean_line
                    })



    return findings

def print_report(findings, filename=""):
    print("=" * 72)
    print("  HUMANIZER ID - LAPORAN PEMERIKSAAN GAYA, KALKE, & ISTILAH BAKU")
    if filename:
        print(f"  Berkas: {filename}")
    print("=" * 72)

    if not findings:
        print("[✓] Tidak ditemukan penanda kalke, verba ringan, atau istilah asing tak baku.")
        print("    Naskah terbaca lugas dan memenuhi kaidah bahasa Indonesia terpadu.")
        print("=" * 72)
        return

    print(f"Ditemukan {len(findings)} pemicu editorial terdeteksi:\n")
    for idx, item in enumerate(findings, start=1):
        cat_label = item["kategori"].replace("_", " ").upper()
        saran_val = item["saran"] if isinstance(item["saran"], str) else " / ".join(item["saran"]) if not (len(item["saran"]) == 1) else item["saran"][0]
        saran_str = '"' + saran_val + '"' 
        pola_val = item["pola"]
        print(f"[{idx}] Baris {item['baris']} [{item['id']} - {cat_label}]")
        print(f'    Pola terdeteksi : "{pola_val}"')
        print(f"    Saran perbaikan : {saran_str}")
        print(f"    Catatan kaidah  : {item['penjelasan']}")
        snippet = item['kalimat'][:80] + "..." if len(item['kalimat']) > 80 else item['kalimat']
        print(f"    Kutipan teks    : {snippet}")
        print("-" * 72)

    print(f"Total temuan: {len(findings)} indikasi pola yang perlu ditinjau.")
    print("=" * 72)

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        print("Pilihan tambahan:")
        print("    --kampus <id>    Gunakan aturan format spesifik kampus (ui, itb, ugm, its, ipb, undip, unpad, unair, ub, telkom, udinus)")
        sys.exit(0)

    # Parse --kampus flag
    kampus_id = None
    args = sys.argv[1:]
    if "--kampus" in args:
        idx = args.index("--kampus")
        if idx + 1 < len(args):
            kampus_id = args[idx + 1]
            args.pop(idx + 1)
            args.pop(idx)

    kalke_dict, glosarium_dict, kampus_dict = load_data(kampus_id)

    if args and args[0] == "--demo":
        sample_text = """
Di era digital yang berkembang dengan sangat pesat saat ini, pemrosesan bahasa alami memegang peranan yang sangat krusial.
Dalam penelitian ini peneliti melakukan implementasi arsitektur Transformer dan menguji performa cache database.
Dapat disampaikan bahwa situasi force majeure menghalangi proses deployment ke server backend.
Meskipun akurat, bukan berarti arsitektur ini tanpa kompromi performa.
## 1.1. Latar Belakang Penelitian
        """
        print("[*] Menjalankan demonstrasi pemindaian pada teks sampel lintas bidang...")
        findings = audit_text(sample_text, kalke_dict, glosarium_dict, kampus_dict)
        print_report(findings, f"Teks Demo (Preset Kampus: {kampus_id or 'Umum'})")
        return

    if not args:
        print("[!] Tentukan berkas yang ingin diperiksa.", file=sys.stderr)
        sys.exit(1)

    filepath = args[0]
    if not os.path.exists(filepath):
        print(f"[!] Berkas tidak ditemukan: {filepath}", file=sys.stderr)
        sys.exit(1)

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    findings = audit_text(content, kalke_dict, glosarium_dict, kampus_dict)
    print_report(findings, filepath)

if __name__ == "__main__":
    main()
