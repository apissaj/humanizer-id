#!/usr/bin/env python3
"""Skrip CLI untuk memeriksa teks bahasa Indonesia terhadap kaidah kalke,
verba ringan, istilah asing yang belum dibakukan, dan gaya klise AI.

Repositori: https://github.com/apissaj/humanizer-id

Penggunaan:
    python scripts/audit.py <path_ke_file.md>
    python scripts/audit.py --demo

Catatan: berkas ini hanya pembungkus. Implementasi tunggal berada di paket
`humanizer_id` (humanizer_id/engine.py) agar tidak ada dua salinan kode yang
bisa melenceng saat salah satunya diperbarui.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from humanizer_id.engine import (  # noqa: E402
    PRESET_EXCLUSIONS,
    PRESET_LABELS,
    audit_text,
    load_data,
    main,
    print_report,
)

if __name__ == "__main__":
    main()
