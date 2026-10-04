# 샘플 사진 만들기: 바다 + 모래사장 + 병 · 캔 · 비닐봉지
from pathlib import Path
from PIL import Image, ImageDraw

W, H = 640, 400
img = Image.new("RGB", (W, H), (110, 170, 220))          # 바다
d = ImageDraw.Draw(img)
d.rectangle([0, 230, W, H], fill=(240, 210, 150))        # 모래
d.rounded_rectangle([125, 215, 170, 315], 10, fill=(120, 190, 120))   # 병
d.rounded_rectangle([380, 225, 425, 315], 8, fill=(190, 190, 195))    # 캔
d.ellipse([262, 85, 325, 155], fill=(245, 245, 245))                  # 비닐봉지

out = Path(__file__).parent / "static" / "images" / "sample.png"
img.save(out)
print("저장:", out.relative_to(Path(__file__).parent).as_posix(), img.size)
