#!/usr/bin/env python3
"""
Pemeriksa batas kata & kelengkapan bagian naskah jurnal ilmiah.
Tanpa dependensi eksternal (stdlib Python saja).

Penggunaan:
    python jurnal/scripts/word_count_check.py <naskah.md>

Output:
    Laporan batas kata per bagian + status OK/WARNING.
"""
import sys
import re
from pathlib import Path


SECTIONS = {
    "abstrak": (150, 250),
    "abstract": (150, 250),
    "introduction": (500, 1500),
    "pendahuluan": (500, 1500),
    "methods": (400, 1500),
    "metode": (400, 1500),
    "results": (300, 1500),
    "hasil": (300, 1500),
    "discussion": (400, 2000),
    "pembahasan": (400, 2000),
    "conclusion": (100, 500),
    "simpulan": (100, 500),
    "references": (0, 10**9),
    "daftar pustaka": (0, 10**9),
}


def parse_sections(text: str):
    """Pisahkan naskah markdown menjadi bagian-bagian utama."""
    sections = {}
    current = None
    buf = []
    for line in text.splitlines():
        if line.startswith("#"):
            heading = re.sub(r"^#+\s*", "", line).strip().lower()
            matched = None
            for key in SECTIONS:
                if key in heading:
                    matched = key
                    break
            if matched:
                if current is not None:
                    sections[current] = "\n".join(buf)
                current = matched
                buf = []
                continue
        buf.append(line)
    if current is not None:
        sections[current] = "\n".join(buf)
    return sections


def word_count(text: str) -> int:
    # buang baris markdown list/tabel agar hitungan murni prosa
    cleaned = "\n".join(
        l for l in text.splitlines() if not l.strip().startswith(("-", "|", "#"))
    )
    words = re.findall(r"\b\w+\b", cleaned)
    return len(words)


def count_citations(text: str) -> int:
    """Hitung sitasi in-text pola [1] atau (Kusuma, 2024)."""
    numeric = len(re.findall(r"\[\d+\]", text))
    author_year = len(re.findall(r"\([A-Z][a-z]+,?\s*\d{4}\)", text))
    return numeric + author_year


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File tidak ditemukan: {path}")
        sys.exit(2)

    text = path.read_text(encoding="utf-8")
    sections = parse_sections(text)

    print("=" * 60)
    print("  LAPORAN PEMERIKSAAN BATAS KATA NASKAH JURNAL")
    print(f"  Berkas: {path.name}")
    print("=" * 60)

    total_words = 0
    issues = 0

    for key, (lo, hi) in SECTIONS.items():
        if key not in sections:
            continue
        wc = word_count(sections[key])
        total_words += wc
        status = "OK"
        if wc < lo:
            status = f"WARNING: di bawah minimum ({lo})"
            issues += 1
        elif wc > hi:
            status = f"WARNING: di atas maksimum ({hi})"
            issues += 1
        print(f"  {key:<15} {wc:>5} kata  [{lo}-{hi}]  {status}")

    # Abstract check: larangan sitasi
    if "abstrak" in sections or "abstract" in sections:
        abstract = sections.get("abstrak") or sections.get("abstract", "")
        cites = count_citations(abstract)
        if cites > 0:
            print(f"  [WARNING] Abstrak mengandung {cites} sitasi (seharusnya 0)")
            issues += 1

    total_cites = count_citations(text)
    print("-" * 60)
    print(f"  Total kata prosa          : {total_words}")
    print(f"  Total sitasi in-text      : {total_cites}")
    print(f"  Masalah ditemukan         : {issues}")
    print("=" * 60)

    sys.exit(0 if issues == 0 else 3)


if __name__ == "__main__":
    main()
