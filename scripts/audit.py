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

def load_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    kalke_path = os.path.join(base_dir, "data", "kalke-indonesia.json")
    glosarium_path = os.path.join(base_dir, "data", "glosarium-lintas-bidang.json")
    
    kalke_dict = {}
    glosarium_dict = {}
    
    if os.path.exists(kalke_path):
        with open(kalke_path, "r", encoding="utf-8") as f:
            kalke_dict = json.load(f)
    else:
        print(f"[!] Peringatan: {kalke_path} tidak ditemukan.", file=sys.stderr)

    if os.path.exists(glosarium_path):
        with open(glosarium_path, "r", encoding="utf-8") as f:
            glosarium_dict = json.load(f)
            
    return kalke_dict, glosarium_dict

def audit_text(text, kalke_dict, glosarium_dict):
    findings = []
    lines = text.splitlines()

    for line_idx, line in enumerate(lines, start=1):
        clean_line = line.strip()
        if not clean_line or clean_line.startswith("#") or clean_line.startswith("```"):
            continue

        # 1. Scan Kalke, Verba Ringan, Pola AI, Kata Baku
        for cat_key, cat_data in kalke_dict.get("kategori", {}).items():
            for entry in cat_data.get("entri", []):
                pattern_str = entry["pola"]
                # Deteksi pola template seperti "Meskipun X, bukan berarti Y", "antara A dengan B", "baik A ataupun B"
                if "..." in pattern_str or " X, " in pattern_str or " A " in pattern_str:
                    matched = False
                    if "bukan berarti" in pattern_str and "bukan berarti" in clean_line.lower():
                        matched = True
                    elif "antara" in pattern_str and "dengan" in pattern_str:
                        if re.search(r'\bantara\b.+?\bdengan\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "baik" in pattern_str and "ataupun" in pattern_str:
                        if re.search(r'\bbaik\b.+?\bataupun\b', clean_line, re.IGNORECASE):
                            matched = True
                    elif "bukan" in pattern_str and "tetapi" in pattern_str:
                        if re.search(r'\bbukan\b.+?\btetapi\b', clean_line, re.IGNORECASE):
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
        sys.exit(0)

    kalke_dict, glosarium_dict = load_data()

    if sys.argv[1] == "--demo":
        sample_text = """
Di era digital yang berkembang dengan sangat pesat saat ini, pemrosesan bahasa alami memegang peranan yang sangat krusial.
Dalam penelitian ini peneliti melakukan implementasi arsitektur Transformer dan menguji performa cache database.
Dapat disampaikan bahwa situasi force majeure menghalangi proses deployment ke server backend.
Meskipun akurat, bukan berarti arsitektur ini tanpa kompromi performa.
        """
        print("[*] Menjalankan demonstrasi pemindaian pada teks sampel lintas bidang...")
        findings = audit_text(sample_text, kalke_dict, glosarium_dict)
        print_report(findings, "Teks Demo Multi-Bidang")
        return

    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print(f"[!] Berkas tidak ditemukan: {filepath}", file=sys.stderr)
        sys.exit(1)

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    findings = audit_text(content, kalke_dict, glosarium_dict)
    print_report(findings, filepath)

if __name__ == "__main__":
    main()
