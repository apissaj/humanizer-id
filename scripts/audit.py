#!/usr/bin/env python3
"""
Humanizer ID - Skrip Pemindai Kalke & Verba Ringan Mandiri
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

def load_dictionary():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dict_path = os.path.join(base_dir, "data", "kalke-indonesia.json")
    if not os.path.exists(dict_path):
        print(f"[!] Berkas kamus tidak ditemukan di: {dict_path}", file=sys.stderr)
        sys.exit(1)
    
    with open(dict_path, "r", encoding="utf-8") as f:
        return json.load(f)

def audit_text(text, dictionary):
    findings = []
    lines = text.splitlines()

    for line_idx, line in enumerate(lines, start=1):
        clean_line = line.strip()
        if not clean_line or clean_line.startswith("#") or clean_line.startswith("```"):
            continue
        
        for cat_key, cat_data in dictionary.get("kategori", {}).items():
            for entry in cat_data.get("entri", []):
                pattern_str = entry["pola"]
                if "..." in pattern_str or " X, " in pattern_str:
                    if "bukan berarti" in pattern_str and "bukan berarti" in clean_line.lower():
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
                    regex = re.compile(re.escape(pattern_str), re.IGNORECASE)
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
    return findings

def print_report(findings, filename=""):
    print("=" * 72)
    print("  HUMANIZER ID - LAPORAN PEMERIKSAAN GAYA & KALKE TULISAN")
    if filename:
        print(f"  Berkas: {filename}")
    print("=" * 72)

    if not findings:
        print("[✓] Tidak ditemukan penanda kalke atau verba ringan yang mencolok.")
        print("    Naskah terbaca lugas dan sesuai konvensi bahasa Indonesia baku.")
        print("=" * 72)
        return

    print(f"Ditemukan {len(findings)} indikasi pola AI / kalke:\n")
    for idx, item in enumerate(findings, start=1):
        cat_label = item["kategori"].replace("_", " ").upper()
        saran_str = " / ".join(['"' + s + '"' for s in item["saran"]])
        print(f"[{idx}] Baris {item['baris']} [{item['id']} - {cat_label}]")
        pola_val = item["pola"]
        print(f'    Pola terdeteksi : "{pola_val}"')
        print(f"    Saran perbaikan : {saran_str}")
        print(f"    Catatan kaidah  : {item['penjelasan']}")
        snippet = item['kalimat'][:80] + "..." if len(item['kalimat']) > 80 else item['kalimat']
        print(f"    Kutipan teks    : {snippet}")
        print("-" * 72)

    print(f"Total temuan: {len(findings)} pemicu editorial.")
    print("Gunakan saran di atas sebagai bahan telaah mandiri tanpa mengubah fakta teknis.")
    print("=" * 72)

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    dictionary = load_dictionary()

    if sys.argv[1] == "--demo":
        sample_text = (
            "Di era digital yang berkembang dengan sangat pesat saat ini, pemrosesan bahasa alami memegang peranan yang sangat krusial.\n"
            "Dalam penelitian ini peneliti melakukan implementasi terhadap arsitektur Transformer.\n"
            "Meskipun akurat, bukan berarti algoritma ini sempurna.\n"
            "Mekanisme ini menghormati batas representasi vektor yang mana hal tersebut sangat berguna.\n"
        )
        print("[*] Menjalankan demonstrasi pemindaian pada teks sampel...")
        findings = audit_text(sample_text, dictionary)
        print_report(findings, "Teks Sampel Demo")
        return

    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print(f"[!] Berkas tidak ditemukan: {filepath}", file=sys.stderr)
        sys.exit(1)

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    findings = audit_text(content, dictionary)
    print_report(findings, filepath)

if __name__ == "__main__":
    main()
