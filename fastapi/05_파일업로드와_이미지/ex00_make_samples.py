# 실습용 이미지 만들기 (samples 폴더)
from pathlib import Path
from PIL import Image, ImageDraw

OUT = Path(__file__).parent / "samples"
OUT.mkdir(exist_ok=True)

for name, color in [("red", (220, 40, 40)), ("green", (40, 180, 70)), ("blue", (40, 80, 220))]:
    img = Image.new("RGB", (320, 240), "white")
    d = ImageDraw.Draw(img)
    d.ellipse((60, 30, 260, 210), fill=color)          # 색이 칠해진 원
    img.save(OUT / f"{name}_circle.png")

digit = Image.new("L", (200, 200), 0)                  # 검은 바탕 흑백(L) 이미지
ImageDraw.Draw(digit).rectangle((85, 30, 115, 170), fill=255)   # 숫자 1 모양
digit.save(OUT / "digit_one.png")

(OUT / "note.txt").write_text("이미지가 아닌 파일\n두 번째 줄\n", encoding="utf-8")
for p in sorted(OUT.iterdir()):
    print(f"{p.name:18} {p.stat().st_size:>6} bytes")
