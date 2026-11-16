"""CLI entrypoint untuk perintah `humanizer-id`."""

import sys
import os

from .engine import load_data, main as engine_main


def main():
    # Delegasikan seluruh argumen ke CLI engine asli (sudut perilaku identik)
    # engine.main membaca sys.argv[1:] sendiri
    if len(sys.argv) >= 2 and sys.argv[1] in ("-v", "--version"):
        from . import __version__
        print(f"humanizer-id v{__version__}")
        sys.exit(0)
    if len(sys.argv) >= 2 and sys.argv[1] == "install":
        from .installer import install

        target = None
        with_refs = False
        args = sys.argv[2:]
        i = 0
        while i < len(args):
            if args[i] in ("--target", "-t") and i + 1 < len(args):
                target = args[i + 1]
                i += 2
            elif args[i] == "--with-references":
                with_refs = True
                i += 1
            elif args[i] in ("-h", "--help"):
                print("Pemakaian: humanizer-id install [--target hermes|claude|antigravity] [--with-references] [path-repo]")
                sys.exit(0)
            else:
                i += 1
        # argumen non-flag terakhir = path sumber eksplisit
        posisi = [a for a in args if not a.startswith("-") and a != target]
        sumber = posisi[0] if posisi else None
        install(sumber_eksplisit=sumber, eksplisit_target=target, dengan_referensi=with_refs)
        sys.exit(0)
    engine_main()


if __name__ == "__main__":
    main()
