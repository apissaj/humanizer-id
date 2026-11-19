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
from .matchers import match_custom_rules, _find_custom_rule
from .report import URUT_PRIORITAS, klasifikasi_prioritas

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

    # Pre-resolve exclusions and compiled regex scanners once per audit call
    excluded_ids = PRESET_EXCLUSIONS.get(str(preset).lower(), set())
    is_ipb_kampus = bool(kampus_dict and "ipb" in str(kampus_dict.get("nama", "")).lower())

    rule_scanners = []
    for cat_key, cat_data in kalke_dict.get("kategori", {}).items():
        for entry in cat_data.get("entri", []):
            if entry.get("id") in excluded_ids:
                continue
            pattern_str = entry["pola"]
            if pattern_str.startswith("[telaah]"):
                continue
            compiled_list = _find_custom_rule(pattern_str)
            word_rgx = None if compiled_list is not None else _compile_word_pattern(pattern_str)
            rule_scanners.append((cat_key, entry, compiled_list, word_rgx))

    glos_scanners = []
    ekonomi_scanners = []
    for domain_key, domain_data in glosarium_dict.get("bidang", {}).items():
        glos_kat = f"glosarium_{domain_key}"
        glos_id = f"GLOS-{domain_key[:3].upper()}"
        for item in domain_data.get("istilah", []):
            term_raw = item["asing"].split("(")[0].strip()
            if len(term_raw) >= 3:
                is_upper = term_raw.isupper() and len(term_raw) <= 5
                glos_scanners.append((glos_kat, glos_id, item, _compile_word_pattern(term_raw, case_sensitive=is_upper)))
        for item in domain_data.get("kaidah_ekonomi_kata", []):
            jenuh_str = item["jenuh"]
            ekonomi_scanners.append((jenuh_str.lower(), jenuh_str, item))

    for line_idx, line in enumerate(lines, start=1):
        clean_line = line.strip()
        if not clean_line or clean_line.startswith("```"):
            continue

        # Pemeriksaan Aturan Khusus Heading / Preset Kampus (bisa jalan pada baris markdown heading #)
        if is_ipb_kampus and clean_line.startswith("#"):
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
        for cat_key, entry, compiled_list, word_rgx in rule_scanners:
            matched = False
            span = None
            if compiled_list is not None:
                for rgx in compiled_list:
                    m = rgx.search(clean_line)
                    if m:
                        matched = True
                        span = m.span()
                        break
            else:
                m = word_rgx.search(clean_line)
                if m:
                    matched = True
                    span = m.span()
            if matched:
                findings.append({
                    "baris": line_idx,
                    "kategori": cat_key,
                    "id": entry["id"],
                    "pola": entry["pola"],
                    "saran": entry["saran_pengganti"],
                    "penjelasan": entry["penjelasan"],
                    "kalimat": clean_line,
                    "span": span
                })

        # 2. Scan Glosarium Lintas Bidang (Istilah Asing Belum Dibakukan & Ungkapan Jenuh)
        for glos_kat, glos_id, item, regex in glos_scanners:
            if regex.search(clean_line):
                findings.append({
                    "baris": line_idx,
                    "kategori": glos_kat,
                    "id": glos_id,
                    "pola": item["asing"],
                    "saran": [item["baku"]],
                    "penjelasan": item.get("catatan", "Padanan istilah resmi bahasa Indonesia."),
                    "kalimat": clean_line
                })

        if ekonomi_scanners:
            clean_lower = clean_line.lower()
            for jenuh_lower, jenuh_str, item in ekonomi_scanners:
                if jenuh_lower in clean_lower:
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



def fix_text(content, kalke_dict, glosarium_dict=None, kampus_dict=None, preset="umum"):
    """Lakukan perbaikan otomatis (autofix) untuk kesalahan leksikal deterministik.

    Hanya mengganti bentuk kata/frasa yang memiliki pemetaan 1-ke-1 pasti
    (misal: bentuk terikat EYD V, kata baku tunggal, dan verba transitif).
    Menghindari perubahan otomatis pada struktur kalimat majemuk yang ambigu.

    Return:
        (fixed_content, total_fixes, fix_log)
    """
    lines = content.splitlines(keepends=True)
    fixed_lines = []
    total_fixes = 0
    fix_log = []

    # Bangun peta penggantian deterministik dari kalke_dict
    deterministic_map = {}
    for cat_key, cat_val in kalke_dict.get("kategori", {}).items():
        for entry in cat_val.get("entri", []):
            pola = entry.get("pola", "").strip()
            if pola.startswith("[telaah]"):
                continue
            saran_list = entry.get("saran_pengganti", [])
            if isinstance(saran_list, str):
                saran_list = [saran_list]
            if not saran_list:
                continue

            # 1. Pola tunggal pendek 1-ke-1
            saran_pertama = saran_list[0].strip()
            if (
                len(pola) <= 40
                and not any(c in saran_pertama for c in ("/", "...", "[", "("))
                and not saran_pertama.endswith("-")
                and not saran_pertama.startswith("-")
                and re.match(r"^[a-zA-Z0-9\s\-]+$", pola)
            ):
                deterministic_map[pola.lower()] = (saran_pertama, entry["id"])
                continue

            # 2. Pasangan sejajar dipisahkan '/' khusus kategori kata baku & morfologi
            if (
                cat_key == "kata_baku_dan_morfologi"
                and "/" in pola
                and not any(c in pola for c in ("(", "[", "...", "*", ":"))
            ):
                p_parts = [x.strip() for x in pola.split("/")]
                if len(saran_list) == len(p_parts):
                    s_parts = [x.strip() for x in saran_list]
                elif len(saran_list) == 1 and "/" in saran_list[0]:
                    s_parts = [x.strip() for x in saran_list[0].split("/")]
                else:
                    continue
                if len(p_parts) == len(s_parts) and len(p_parts) >= 2:
                    for pp, sp in zip(p_parts, s_parts):
                        if len(pp) < 3 or len(pp) > 40 or len(sp) > 40:
                            continue
                        if len(pp.split()) > 3 or len(sp.split()) > 3:
                            continue
                        if any(c in sp for c in ("/", "...", "[", "(", ":")):
                            continue
                        if sp.endswith("-") or sp.startswith("-"):
                            continue
                        if not re.match(r"^[a-zA-Z0-9\s\-]+$", pp):
                            continue
                        if not re.match(r"^[a-zA-Z0-9\s\-]+$", sp):
                            continue
                        if pp.lower() == sp.lower():
                            continue
                        if pp.lower() not in deterministic_map:
                            deterministic_map[pp.lower()] = (sp, entry["id"])

    # Urutkan pola dari yang terpanjang ke terpendek & kompilasi sekali
    sorted_patterns = sorted(deterministic_map.keys(), key=len, reverse=True)
    compiled_fixes = [
        (re.compile(rf"(?<!\w){re.escape(p)}(?!\w)", re.IGNORECASE), deterministic_map[p][0], deterministic_map[p][1])
        for p in sorted_patterns
    ]

    for line_idx, line in enumerate(lines, 1):
        modified_line = line
        for pattern_regex, repl, rule_id in compiled_fixes:
            def make_replacement(match):
                nonlocal total_fixes
                orig = match.group(0)
                # Pertahankan TitleCase atau uppercase jika kata asli diawali huruf kapital
                if orig.isupper():
                    res = repl.upper()
                elif orig[0].isupper():
                    res = repl[0].upper() + repl[1:]
                else:
                    res = repl
                total_fixes += 1
                fix_log.append({
                    "baris": line_idx,
                    "id": rule_id,
                    "sebelum": orig,
                    "sesudah": res
                })
                return res

            modified_line = pattern_regex.sub(make_replacement, modified_line)
        fixed_lines.append(modified_line)

    return ("".join(fixed_lines), total_fixes, fix_log)


def _format_saran(saran_raw):
    if isinstance(saran_raw, str):
        return saran_raw
    if len(saran_raw) == 1:
        return saran_raw[0]
    return " / ".join(saran_raw)


def filter_findings(findings, only_priorities=None, top_n=None):
    """Deduplikasi, saring berdasarkan prioritas, dan batasi ke N temuan teratas."""
    deduped = deduplicate_report_findings(findings)
    total_before = len(deduped)
    filtered = deduped

    if only_priorities:
        allowed = {p.strip().upper() for p in only_priorities if p.strip()}
        filtered = [f for f in filtered if klasifikasi_prioritas(f["kategori"]) in allowed]

    if top_n is not None:
        filtered = sorted(
            filtered,
            key=lambda f: (URUT_PRIORITAS.get(klasifikasi_prioritas(f["kategori"]), 9), f["baris"]),
        )[: max(0, top_n)]

    return filtered, total_before


def format_compact_report(findings, filename="", total_before_filter=None):
    """Format ringkas 1 baris per temuan untuk menghemat token agen AI."""
    label = filename or "Naskah"
    if not findings:
        if total_before_filter:
            return f"[✓] {label}: 0 temuan ditampilkan ({total_before_filter} temuan di luar filter)."
        return f"[✓] {label}: 0 temuan."

    counts = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
    lines = [f"[{label}]"]
    for item in findings:
        prio = klasifikasi_prioritas(item["kategori"])
        counts[prio] = counts.get(prio, 0) + 1
        saran_val = _format_saran(item["saran"])
        lines.append(f'L{item["baris"]} [{prio}|{item["id"]}] "{item["pola"]}" -> "{saran_val}"')

    summary = (
        f"Total: {len(findings)} temuan "
        f"(HIGH={counts['HIGH']}, MEDIUM={counts['MEDIUM']}, LOW={counts['LOW']})"
    )
    if total_before_filter is not None and total_before_filter > len(findings):
        summary += f" (+{total_before_filter - len(findings)} temuan lain disembunyikan)"
    lines.append(summary)
    return "\n".join(lines)


def format_fix_diff(fix_log, filename=""):
    """Format hanya baris/frasa yang berubah dari autofix agar hemat token."""
    label = filename or "Naskah"
    if not fix_log:
        return f"[✓] {label}: 0 penggantian."

    lines = [f"[{label}]"]
    for entry in fix_log:
        lines.append(
            f'L{entry["baris"]} [{entry["id"]}] "{entry["sebelum"]}" -> "{entry["sesudah"]}"'
        )
    lines.append(f"Total: {len(fix_log)} perbaikan diterapkan.")
    return "\n".join(lines)


def extract_problem_lines(content, findings):
    """Ekstrak hanya baris asli yang memiliki temuan (1 baris per nomor baris unik)."""
    deduped = deduplicate_report_findings(findings)
    if not deduped:
        return "[✓] Tidak ada baris bermasalah."

    line_nums = sorted({item["baris"] for item in deduped})
    src_lines = content.splitlines()
    out = [f"L{ln}: {src_lines[ln - 1]}" for ln in line_nums if 1 <= ln <= len(src_lines)]
    return "\n".join(out) if out else "[✓] Tidak ada baris bermasalah."


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
    # Konsol Windows (cp1252) tidak selalu bisa mencetak panah dan simbol laporan;
    # paksa UTF-8 agar audit tidak gagal di tengah jalan saat menemukan kaidah.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        print("Pilihan tambahan:")
        print("    install          Pasang skill ke folder agen AI (Hermes/Claude Code/Antigravity); --target pilih satu, --with-references sertakan references/")
        print("    --fix            Lakukan perbaikan otomatis (autofix) pada bentuk leksikal deterministik")
        print("    --write, -w      Tulis hasil perbaikan langsung ke berkas asli (digunakan bersama --fix)")
        print("    --report         Tulis temuan bernomor ke humanizer/audit-NNN-YYYY-MM-DD.md (mode AFTER; naskah tidak diubah)")
        print("    --kampus <id>    Gunakan aturan format spesifik kampus (ui, itb, ugm, its, ipb, undip, unpad, unair, ub, telkom, udinus)")
        print("    --preset <nama>  Preset domain audit: umum (default), akademik, dinas, jurnalistik")
        print("    --compact        Laporan ringkas 1 baris per temuan (hemat token untuk agen AI)")
        print("    --only <prio>    Saring prioritas temuan, mis. high atau high,medium (HIGH/MEDIUM/LOW)")
        print("    --top <N>        Batasi ke N temuan teratas berdasarkan prioritas tertinggi")
        print("    --diff           Tampilkan hanya selisih perbaikan (digunakan bersama --fix)")
        print("    --extract        Ekstrak hanya baris naskah yang mengandung temuan")
        sys.exit(0)

    args = sys.argv[1:]

    # Parse --fix, --write, --compact, --diff, --extract flags
    do_fix = False
    write_in_place = False
    compact_mode = False
    diff_mode = False
    extract_mode = False
    if "--fix" in args:
        do_fix = True
        args.remove("--fix")
    if "--write" in args:
        write_in_place = True
        args.remove("--write")
    if "-w" in args:
        write_in_place = True
        args.remove("-w")
    if "--compact" in args:
        compact_mode = True
        args.remove("--compact")
    if "--diff" in args:
        diff_mode = True
        args.remove("--diff")
    if "--extract" in args:
        extract_mode = True
        args.remove("--extract")

    # Parse --only flag
    only_priorities = None
    if "--only" in args:
        idx = args.index("--only")
        if idx + 1 >= len(args):
            print("[!] --only membutuhkan nilai prioritas (mis. high atau high,medium).", file=sys.stderr)
            sys.exit(1)
        raw_only = args[idx + 1]
        args.pop(idx + 1)
        args.pop(idx)
        parsed_only = [p.strip().upper() for p in raw_only.split(",") if p.strip()]
        invalid = [p for p in parsed_only if p not in URUT_PRIORITAS]
        if not parsed_only or invalid:
            print(f"[!] Prioritas tidak dikenal: '{raw_only}'. Opsi: HIGH, MEDIUM, LOW", file=sys.stderr)
            sys.exit(1)
        only_priorities = set(parsed_only)

    # Parse --top flag
    top_n = None
    if "--top" in args:
        idx = args.index("--top")
        if idx + 1 >= len(args):
            print("[!] --top membutuhkan angka bulat positif.", file=sys.stderr)
            sys.exit(1)
        raw_top = args[idx + 1]
        args.pop(idx + 1)
        args.pop(idx)
        try:
            top_n = int(raw_top)
            if top_n < 1:
                raise ValueError
        except ValueError:
            print(f"[!] Nilai --top harus bilangan bulat >= 1, bukan '{raw_top}'.", file=sys.stderr)
            sys.exit(1)

    # Parse --report (mode AFTER: laporan bernomor, naskah tidak diubah)
    report_dir = None
    if "--report" in args:
        report_dir = "humanizer"
        args.remove("--report")

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

    if report_dir is not None:
        if args and args[0] == "--demo":
            print("[!] --report tidak berlaku untuk --demo.", file=sys.stderr)
            sys.exit(1)
        if not args:
            print("[!] --report butuh berkas naskah.", file=sys.stderr)
            sys.exit(1)
        filepath = args[0]
        if not os.path.exists(filepath):
            print(f"[!] Berkas tidak ditemukan: {filepath}", file=sys.stderr)
            sys.exit(1)
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        from .report import tulis_laporan
        findings = audit_text(content, kalke_dict, glosarium_dict, kampus_dict, preset)
        report_path = tulis_laporan(findings, filepath, report_dir)
        print(f"[✓] Laporan audit bernomor ditulis: {report_path}")
        print(f"    Temuan: {len(findings)} (prioritas HIGH/MEDIUM/LOW di laporan)")
        return

    if args and args[0] == "--demo":
        sample_text = """
Di era digital yang berkembang dengan sangat pesat saat ini, pemrosesan bahasa alami memegang peranan yang sangat krusial.
Dalam penelitian ini peneliti melakukan implementasi arsitektur Transformer dan menguji performa cache database.
Dapat disampaikan bahwa situasi force majeure menghalangi proses deployment ke server backend.
Meskipun akurat, bukan berarti arsitektur ini tanpa kompromi performa.
## 1.1. Latar Belakang Penelitian
        """
        findings = audit_text(sample_text, kalke_dict, glosarium_dict, kampus_dict, preset)
        demo_label = f"Teks Demo (Preset Kampus: {kampus_id or 'Umum'})"
        if extract_mode:
            selected, _ = filter_findings(findings, only_priorities, top_n)
            print(extract_problem_lines(sample_text, selected))
            return
        selected, total_before = filter_findings(findings, only_priorities, top_n)
        if compact_mode:
            print(format_compact_report(selected, demo_label, total_before))
        else:
            print("[*] Menjalankan demonstrasi pemindaian pada teks sampel lintas bidang...")
            print_report(selected, demo_label)
            if total_before > len(selected):
                print(f"(+{total_before - len(selected)} temuan lain disembunyikan oleh filter --only/--top)")
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

    if do_fix:
        fixed_content, fix_count, fix_log = fix_text(content, kalke_dict, glosarium_dict, kampus_dict, preset)
        if write_in_place:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(fixed_content)
            print(f"[✓] Berhasil memperbaiki {fix_count} temuan langsung pada berkas: {filepath}")
            if diff_mode:
                print(format_fix_diff(fix_log, filepath))
        elif diff_mode:
            print(format_fix_diff(fix_log, filepath))
        else:
            print(f"[*] Hasil autofix ({fix_count} penggantian diterapkan):\n")
            print(fixed_content)
        return

    findings = audit_text(content, kalke_dict, glosarium_dict, kampus_dict, preset)
    if extract_mode:
        selected, _ = filter_findings(findings, only_priorities, top_n)
        print(extract_problem_lines(content, selected))
        return

    selected, total_before = filter_findings(findings, only_priorities, top_n)
    if compact_mode:
        print(format_compact_report(selected, filepath, total_before))
    else:
        print_report(selected, filepath)
        if total_before > len(selected):
            print(f"(+{total_before - len(selected)} temuan lain disembunyikan oleh filter --only/--top)")

if __name__ == "__main__":
    main()
