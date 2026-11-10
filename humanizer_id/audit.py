"""Public API: muat dataset dan audit teks."""

import json
import os

from .matchers import match_custom_rules  # noqa: F401
from .engine import audit_text, _resolve_data_dir  # noqa: F401


def load_default_data():
    """Muat dataset kaidah & glosarium yang dibundel dalam paket (fail-closed)."""
    data_dir = _resolve_data_dir()
    with open(os.path.join(data_dir, "kalke-indonesia.json"), encoding="utf-8") as f:
        kalke = json.load(f)
    with open(os.path.join(data_dir, "glosarium-lintas-bidang.json"), encoding="utf-8") as f:
        glos = json.load(f)
    return kalke, glos
