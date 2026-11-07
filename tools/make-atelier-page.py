#!/usr/bin/env python3
"""Build the offline Kiro Atelier showcase page shipped in usr/share/kiro-xfce/kiro-atelier/."""

import html
import re
import shutil
import sys
from pathlib import Path

from PIL import Image

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "usr/share/kiro-xfce/kiro-atelier"
COMFYUI = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.home() / "Insync/Kiro/Kiro-HQ/COMFYUI"
GALLERY = COMFYUI / "style-gallery-cc0"
HERO = COMFYUI / "showcase/hero-one-photo-six-styles.jpg"
KOFI = "https://ko-fi.com/s/6ff5175237"
# No portrait: the photo is CC0 but there is no model release, so she stays out of everything public.
PHOTOS = [("mountain-lake", "Mountain lake"), ("city", "City"), ("sea", "Sea")]
SIZE, QUALITY = 960, 80

ROW = re.compile(r'<h2>([^<]+)</h2><p class="meta">([^<]+)</p><p>([^<]+)</p>')


def _slug(name):
    return name.lower().replace(" ", "-")


def _save(src, dest, width):
    with Image.open(src) as im:
        im = im.convert("RGB")
        if im.width > width:
            im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
        im.save(dest, "JPEG", quality=QUALITY, optimize=True, progressive=True)


def _figure(slug, label, alt):
    return (f'<figure><img loading="lazy" src="img/{slug}.jpg" alt="{html.escape(alt)}">'
            f"<figcaption>{label}</figcaption></figure>")


def main():
    rows = ROW.findall((GALLERY / "index.html").read_text())
    if len(rows) != 13:
        sys.exit(f"expected 13 profiles in the gallery, found {len(rows)}")
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "img").mkdir(parents=True)
    _save(HERO, OUT / "img/hero.jpg", 1600)

    sections = []
    cells = []
    for key, label in PHOTOS:
        _save(GALLERY / f"img/original-{key}.jpg", OUT / f"img/original-{key}.jpg", SIZE)
        cells.append(_figure(f"original-{key}", label, f"{label}, the photo"))
    sections.append('<section class="row"><div class="info"><h3>The photos</h3><p>Every profile below starts '
                    'from these three photos.</p></div><div class="cells">' + "".join(cells) + "</div></section>")
    for name, meta, text in rows:
        meta = re.sub(r"\s*·\s*about \d+ s each", "", html.unescape(meta))
        cells = []
        for key, label in PHOTOS:
            slug = f"{_slug(name)}-{key}"
            _save(GALLERY / f"img/{slug}.jpg", OUT / f"img/{slug}.jpg", SIZE)
            cells.append(_figure(slug, label, f"{name}, {label}"))
        sections.append(f'<section class="row"><div class="info"><h3>{name}</h3><p class="meta">'
                        f"{html.escape(meta)}</p><p>{text}</p></div>"
                        f'<div class="cells">{"".join(cells)}</div></section>')

    page = (REPO / "tools/atelier-page.html").read_text()
    page = page.replace("@@STYLES@@", "\n".join(sections)).replace("@@KOFI@@", KOFI)
    (OUT / "index.html").write_text(page)
    total = sum(f.stat().st_size for f in OUT.rglob("*") if f.is_file())
    print(f"{OUT}: {len(list(OUT.rglob('*.jpg')))} images, {total / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
