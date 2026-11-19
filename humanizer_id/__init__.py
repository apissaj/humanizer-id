"""Humanizer ID: mesin editorial bahasa Indonesia berbasis 740 kaidah preskriptif."""

__version__ = "2.5.0"

from .audit import audit_text  # noqa: F401
from .engine import fix_text   # noqa: F401
from .report import tulis_laporan, render_laporan, klasifikasi_prioritas  # noqa: F401
