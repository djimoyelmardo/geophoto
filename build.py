#!/usr/bin/env python3
"""Assemble index.html à partir de src/app.html et des bibliothèques de vendor/.

Usage : python build.py
Le fichier index.html produit est celui que sert GitHub Pages. Ne pas le modifier à la main.
"""
from pathlib import Path

root = Path(__file__).parent
html = (root / "src" / "app.html").read_text(encoding="utf-8")
parts = [("/*LIB:%s*/" % n, "vendor/%s.js" % n, "</script") for n in ("proj4", "piexif", "leaflet")]
parts += [("/*CSS:leaflet*/", "vendor/leaflet.css", "</style")]
for marker, path, forbidden in parts:
    content = (root / path).read_text(encoding="utf-8")
    if marker not in html:
        raise SystemExit(f"Marqueur {marker} introuvable dans src/app.html")
    if forbidden in content.lower():
        raise SystemExit(f"{path} contient une balise {forbidden}> : intégration impossible")
    html = html.replace(marker, content)
(root / "index.html").write_text(html, encoding="utf-8")
print(f"index.html généré ({len(html) // 1024} Ko)")
