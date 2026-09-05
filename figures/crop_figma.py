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

# Phone row only (drop scarlet banner and bottom caption strip).
top = int(h * 0.235)
bottom = int(h * 0.88)
# Five phones left of the "Why it looks this way" panel.
left = int(w * 0.015)
right = int(w * 0.705)
row = im.crop((left, top, right, bottom))
rw, rh = row.size
print("row", rw, rh)

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
