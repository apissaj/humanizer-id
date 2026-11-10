#!/usr/bin/env python3
"""Pembungkus kompatibilitas untuk tabel matcher.

Implementasi tunggal ada di `humanizer_id/matchers.py`; berkas ini hanya
meneruskan simbol lama (`CUSTOM_RULES`, `match_custom_rules`) agar impor
gaya lama (`from matchers import match_custom_rules`) tetap berjalan.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from humanizer_id.matchers import *  # noqa: E402,F401,F403
from humanizer_id.matchers import CUSTOM_RULES, match_custom_rules  # noqa: E402,F401
