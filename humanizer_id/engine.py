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
import functools
from .matchers import match_custom_rules

# Pengecualian kaidah per preset domain (audit terfokus)
# 'umum' = tanpa pengecualian (backward-compatible, seluruh kaidah aktif)
PRESET_EXCLUSIONS = {
    "umum": set(),
    "akademik": {
        # Konvensi naskah dinas tidak relevan untuk naskah akademik/jurnal
        "DIN-001", "DIN-003", "SUR-003",
    },
    "dinas": {
        # Kaidah monograf/kurikulum tidak relevan untuk surat dinas
        "BRN-002", "BRN-003", "BRN-004", "BSK-001", "BSK-002", "DIL-008",
    },
    "jurnalistik": {
        # Kaidah monograf & naskah dinas tidak relevan untuk artikel berita/opini
        "BRN-002", "BRN-003", "DIN-001", "DIN-003", "BSK-001", "BSK-002",
        "MBI-002", "MBI-003",
    },
}

PRESET_LABELS = {
    "umum": "Audit Umum (seluruh kaidah)",
    "akademik": "Preset Akademik (skripsi/tesis/jurnal)",
    "dinas": "Preset Dinas (surat/nota/pengumuman instansi)",
    "jurnalistik": "Preset Jurnalistik (berita/opini/rilis pers)",
}


def _resolve_data_dir():
    """Direktori dataset: paket (terpasang via pip) didahulukan, lalu root repo."""
    pkg_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    if os.path.isdir(pkg_dir):
        return pkg_dir
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


def load_data(kampus_id=None):
    base_dir = _resolve_data_dir()
    kalke_path = os.path.join(base_dir, "kalke-indonesia.json")
    glosarium_path = os.path.join(base_dir, "glosarium-lintas-bidang.json")
    kampus_path = os.path.join(base_dir, "pedoman-kampus.json")
    
    kalke_dict = {}
    glosarium_dict = {}
    kampus_dict = {}
    
    if os.path.exists(kalke_path):
        with open(kalke_path, "r", encoding="utf-8") as f:
            kalke_dict = json.load(f)
    else:
        raise FileNotFoundError(
            f"Dataset kaidah tidak ditemukan di {kalke_path}. "
            "Audit dibatalkan agar tidak menghasilkan laporan 'bersih' palsu."
        )

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

@functools.lru_cache(maxsize=4096)
def _compile_word_pattern(pattern_str, case_sensitive=False):
    flags = 0 if case_sensitive else re.IGNORECASE
    return re.compile(r'\b' + re.escape(pattern_str.strip()) + r'\b', flags)


def audit_text(text, kalke_dict, glosarium_dict, kampus_dict=None, preset="umum"):
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

        # Filter kaidah berdasarkan preset domain
        excluded_ids = PRESET_EXCLUSIONS.get(str(preset).lower(), set())

        # 1. Scan Kalke, Verba Ringan, Pola AI, Kata Baku
        for cat_key, cat_data in kalke_dict.get("kategori", {}).items():
            for entry in cat_data.get("entri", []):
                # Lewati kaidah yang dikecualikan oleh preset domain aktif
                if entry.get("id") in excluded_ids:
                    continue

                pattern_str = entry["pola"]
                # Deteksi pola template seperti "Meskipun X, bukan berarti Y", "antara A dengan B", "baik A ataupun B"
                # Entri [telaah] dievaluasi semantik oleh agent, dikecualikan dari scan regex otomatis
                if pattern_str.startswith("[telaah]"):
                    continue

                # Deteksi via tabel matcher data-driven (scripts/matchers.py)
                res = match_custom_rules(pattern_str, clean_line)
                is_handled, matched = res[0], res[1]
                span = res[2] if len(res) > 2 else None
                if not is_handled:
                    m = _compile_word_pattern(pattern_str).search(clean_line)
                    matched = bool(m)
                    span = m.span() if m else None
                if matched:
                    findings.append({
                        "baris": line_idx,
                        "kategori": cat_key,
                        "id": entry["id"],
                        "pola": pattern_str,
                        "saran": entry["saran_pengganti"],
                        "penjelasan": entry["penjelasan"],
                        "kalimat": clean_line,
                        "span": span
                    })

        # 2. Scan Glosarium Lintas Bidang (Istilah Asing Belum Dibakukan & Ungkapan Jenuh)
        for domain_key, domain_data in glosarium_dict.get("bidang", {}).items():
            # Cek istilah asing
            for item in domain_data.get("istilah", []):
                term_raw = item["asing"].split("(")[0].strip()
                if len(term_raw) >= 3:
                    # Akronim kapital (API, SDK, URL) dicocokkan case-sensitive agar tidak bentrok
                    # dengan kata bahasa Indonesia serupa (api = kereta api, sdk tidak ada, dst.)
                    is_upper = term_raw.isupper() and len(term_raw) <= 5
                    regex = _compile_word_pattern(term_raw, case_sensitive=is_upper)
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

def deduplicate_report_findings(findings):
    """Konsolidasikan temuan yang tumpang tindih pada baris yang sama.
    
    Jika beberapa kaidah berbeda memicu span kata/frasa yang beririsan (misal
    UNJA-005, KOH-001, dan TBG-003 pada kata 'Sedangkan'), satukan menjadi
    satu entri laporan dengan rujukan gabungan agar laporan bersih dan informatif.
    """
    if not findings:
        return []
    
    from collections import defaultdict
    by_line = defaultdict(list)
    for f in findings:
        by_line[f["baris"]].append(f)
        
    consolidated = []
    for line_num in sorted(by_line.keys()):
        items = by_line[line_num]
        merged = []
        for it in items:
            it_span = it.get("span")
            matched = None
            for ex in merged:
                ex_span = ex.get("span")
                # Jika span beririsan pada baris yang sama
                if it_span and ex_span:
                    if max(it_span[0], ex_span[0]) < min(it_span[1], ex_span[1]):
                        matched = ex
                        break
                # Fallback: pola teks serupa
                it_pola = str(it.get("pola", "")).strip().lower()
                ex_pola = str(ex.get("pola", "")).strip().lower()
                if it_pola == ex_pola or (len(it_pola) >= 4 and it_pola in ex_pola) or (len(ex_pola) >= 4 and ex_pola in it_pola):
                    matched = ex
                    break
            if matched:
                cur_ids = set(matched["id"].split(" / "))
                if it["id"] not in cur_ids:
                    matched["id"] = f"{matched['id']} / {it['id']}"
                if len(it.get("penjelasan", "")) > len(matched.get("penjelasan", "")):
                    matched["penjelasan"] = it["penjelasan"]
            else:
                merged.append(dict(it))
        consolidated.extend(merged)
    return consolidated


def print_report(findings, filename=""):
    findings = deduplicate_report_findings(findings)

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
        print("    --preset <nama>  Preset domain audit: umum (default), akademik, dinas, jurnalistik")
        sys.exit(0)

    args = sys.argv[1:]

    # Parse --preset flag
    preset = "umum"
    if "--preset" in args:
        idx = args.index("--preset")
        if idx + 1 < len(args):
            preset = args[idx + 1].lower()
            args.pop(idx + 1)
            args.pop(idx)
            if preset not in PRESET_EXCLUSIONS:
                print(f"[!] Preset '{preset}' tidak dikenal. Opsi: {', '.join(PRESET_EXCLUSIONS.keys())}", file=sys.stderr)
                sys.exit(1)
            print(f"[*] Preset domain aktif: {PRESET_LABELS[preset]}")

    # Parse --kampus flag
    kampus_id = None
    if "--kampus" in args:
        idx = args.index("--kampus")
        if idx + 1 < len(args):
            kampus_id = args[idx + 1]
            args.pop(idx + 1)
            args.pop(idx)

    try:
        kalke_dict, glosarium_dict, kampus_dict = load_data(kampus_id)
    except FileNotFoundError as exc:
        print(f"[!] {exc}", file=sys.stderr)
        sys.exit(2)

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

    findings = audit_text(content, kalke_dict, glosarium_dict, kampus_dict, preset)
    print_report(findings, filepath)

if __name__ == "__main__":
    main()
