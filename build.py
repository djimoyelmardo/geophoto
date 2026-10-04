#!/usr/bin/env python3
"""Assemble index.html à partir de src/app.html et des bibliothèques de vendor/.

Usage : python build.py
Le fichier index.html produit est celui que sert GitHub Pages. Ne pas le modifier à la main.
"""
from pathlib import Path

root = Path(__file__).parent
html = (root / "src" / "app.html").read_text(encoding="utf-8")
for name in ("proj4", "piexif"):
    marker = f"/*LIB:{name}*/"
    lib = (root / "vendor" / f"{name}.js").read_text(encoding="utf-8")
    if marker not in html:
        raise SystemExit(f"Marqueur {marker} introuvable dans src/app.html")
    if "</script" in lib.lower():
        raise SystemExit(f"vendor/{name}.js contient une balise </script> : intégration impossible")
    html = html.replace(marker, lib)
(root / "index.html").write_text(html, encoding="utf-8")
print(f"index.html généré ({len(html) // 1024} Ko)")
