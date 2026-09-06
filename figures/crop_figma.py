"""Re-crop five phone frames from the Figma board for IEEE figure* layout."""

from PIL import Image
from pathlib import Path

out = Path(__file__).resolve().parent
# Prefer Downloads original if present; else prior copy may be gone.
candidates = [
    Path(r"C:\Users\karee\Downloads\CWC Health App - Lo-Fi Wireframes v0.1.png"),
    out / "figma_export_raw.png",
    out / "ui_wireframes.png",
]
src = next(p for p in candidates if p.exists())
im = Image.open(src).convert("RGB")
w, h = im.size
print("source", src.name, w, h)

# Phone row only (drop the scarlet banner and bottom caption strip).
top = int(h * 0.34)
bottom = int(h * 0.93)
# Five phones left of the "Why it looks this way" panel.
left = int(w * 0.01)
right = int(w * 0.81)
row = im.crop((left, top, right, bottom))
rw, rh = row.size
print("row", rw, rh)

# Keep the complete row for the manuscript so phone edges and labels are not
# clipped by per-column crop estimates.
row.crop((0, 0, rw, int(rh * 0.92))).save(out / "ui_screens.png", optimize=True)

names = ["nearby", "my_health", "learn", "more", "help_now"]
cw = rw / 5.0
for i, name in enumerate(names):
    # Inset slightly to drop column gutters / caption bleed.
    x0 = int(i * cw + cw * 0.04)
    x1 = int((i + 1) * cw - cw * 0.04)
    y0 = int(rh * 0.00)
    y1 = int(rh * 0.92)  # drop under-phone captions
    frame = row.crop((x0, y0, x1, y1))
    frame.save(out / f"ui_screen_{name}.png", optimize=True)
    print(name, frame.size)

print("done")
