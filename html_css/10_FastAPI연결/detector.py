# 데모 탐지기: 아직 AI 모델이 없으니 "정해진 위치"를 돌려줘요.
# AI 과정 8장에서 이 파일만 YOLO 로 바꾸면 웹 페이지는 그대로 동작해요.
from PIL import Image, ImageDraw, ImageFont

# (클래스, 신뢰도, 상자 위치를 사진 크기에 대한 비율로: x1, y1, x2, y2)
FAKE = [
    ("bottle", 0.91, (0.18, 0.52, 0.29, 0.81)),
    ("can", 0.84, (0.58, 0.54, 0.68, 0.81)),
    ("bag", 0.32, (0.40, 0.19, 0.52, 0.41)),
]
# 결과를 그릴 때 클래스마다 쓸 색 (빨강, 초록, 파랑)
COLORS = {"bottle": (220, 0, 0), "can": (255, 140, 0), "bag": (112, 48, 160)}


def detect(img: Image.Image, conf: float = 0.25) -> list[dict]:
    # 사진 크기(픽셀)를 알아야 비율 → 픽셀 좌표로 바꿀 수 있어요
    w, h = img.size
    # 결과를 모을 빈 목록
    boxes = []
    for name, score, (x1, y1, x2, y2) in FAKE:
        if score >= conf:                     # 기준보다 낮은 것은 버리기
            boxes.append({"class": name, "conf": score,
                          "box": [round(x1 * w), round(y1 * h), round(x2 * w), round(y2 * h)]})
    return boxes


def draw(img: Image.Image, boxes: list[dict]) -> Image.Image:
    # 원본은 그대로 두고 복사본에 그리기
    out = img.copy()
    d = ImageDraw.Draw(out)
    font = ImageFont.load_default(size=16)    # 글자 크기 16
    # 상자 하나씩 그리기: 테두리 → 그 위에 "이름 신뢰도" 글자
    for b in boxes:
        color = COLORS.get(b["class"], (0, 0, 0))
        d.rectangle(b["box"], outline=color, width=3)
        d.text((b["box"][0], b["box"][1] - 20), f'{b["class"]} {b["conf"]:.2f}', fill=color, font=font)
    return out
