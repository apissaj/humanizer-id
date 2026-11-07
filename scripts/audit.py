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
                if "..." in pattern_str or " X, " in pattern_str or " A " in pattern_str or "sedangkan" in pattern_str or "sehingga" in pattern_str or "para tamu-tamu" in pattern_str or "karena ... maka" in pattern_str or "meskipun ... tetapi" in pattern_str or "ganda jamak" in pattern_str or "itu sendiri" in pattern_str or "mau tidak mau" in pattern_str or "konjungsi koordinatif" in pattern_str or "bertingkat" in pattern_str or "nomor NIK" in pattern_str or "kartu KIP" in pattern_str or "virus HIV" in pattern_str or "partai PPP" in pattern_str or "pronomina persona taksa" in pattern_str or "hiponimi-hipernim" in pattern_str or "akibat-sebab terbalik" in pattern_str or "nama diri geografi yang menjadi nama jenis" in pattern_str or "bentuk dasar turunan nama bangsa" in pattern_str or "jabatan/pangkat tanpa nama orang" in pattern_str:
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
                    elif "sehingga" in pattern_str:
                        if re.search(r'(?:^|[.!?]\s+)\bsehingga\b', clean_line, re.IGNORECASE):
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
                    elif "hiponimi-hipernim" in pattern_str:
                        if re.search(r'\bjangankan\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "akibat-sebab terbalik" in pattern_str or "sebab-akibat terbalik" in pattern_str:
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
        saran_str = " / ".join(['"' + s + '"' for s in item["saran"]])
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
