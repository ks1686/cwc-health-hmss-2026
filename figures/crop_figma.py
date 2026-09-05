from PIL import Image
from pathlib import Path

out_dir = Path(r"C:\Users\karee\OneDrive\Documents\GitHub\cwc-health-hmss-2026\figures")
src = out_dir / "figma_export_raw.png"
im = Image.open(src).convert("RGB")
w, h = im.size
print("size", w, h)

# Drop scarlet cover banner; keep phone row + captions.
top = int(h * 0.22)
bottom = int(h * 0.92)

# Five phones occupy most of the left; rationale panel is on the right.
phones_right = int(w * 0.72)
phones = im.crop((int(w * 0.01), top, phones_right, bottom))
phones.save(out_dir / "ui_wireframes.png", optimize=True)
print("phones board", phones.size)

# Also save a slightly wider crop including a bit of rationale if needed for alt fig
board = im.crop((0, top, w, bottom))
board.save(out_dir / "ui_wireframes_fullrow.png", optimize=True)

pw, ph = phones.size
n = 5
cw = pw // n
names = ["nearby", "my_health", "learn", "more", "help_now"]
for i, name in enumerate(names):
    left = i * cw + int(cw * 0.03)
    right = (i + 1) * cw - int(cw * 0.03)
    frame = phones.crop((left, 0, right, ph))
    frame.save(out_dir / f"ui_screen_{name}.png", optimize=True)
    print(name, frame.size)

print("done")
