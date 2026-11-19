# YOLO 탐지기: HTML/CSS 10장의 데모 detector.py 와 "약속(입력 · 출력 모양)"이 똑같아요
from pathlib import Path                   # 파일 · 폴더 경로를 다루는 도구

from PIL import Image, ImageDraw, ImageFont
from ultralytics import YOLO               # YOLO 모델을 불러오는 클래스

MODEL_PATH = Path(__file__).parent / "models" / "best.pt"
model = YOLO(MODEL_PATH)                   # ⭐ 서버가 켜질 때 한 번만 불러오기 (요청마다 부르면 느려요)
COLORS = {"bottle": (220, 0, 0), "can": (255, 140, 0), "bag": (112, 48, 160)}


# 사진 → 상자 목록. 결과의 xyxy(꼭짓점) · conf(신뢰도) · cls(클래스 번호)를 사전으로 바꿔요
def detect(img: Image.Image, conf: float = 0.25) -> list[dict]:
    r = model.predict(img, conf=conf, imgsz=320, verbose=False)[0]      # 학습 때와 같은 imgsz
    return [
        # 상자 하나마다 {"class": 이름, "conf": 신뢰도, "box": [x1, y1, x2, y2]} 를 만들어 리스트로 모아요
        # (아래 줄의 zip 이 좌표 · 신뢰도 · 클래스 번호를 같은 순서끼리 짝지어 줘요)
        {"class": r.names[int(c)], "conf": round(float(s), 2), "box": [round(v) for v in b]}
        for b, s, c in zip(r.boxes.xyxy.tolist(), r.boxes.conf.tolist(), r.boxes.cls.tolist())
    ]


# 결과 그리기 (HTML/CSS 10장 데모와 같은 함수)
def draw(img: Image.Image, boxes: list[dict]) -> Image.Image:
    out = img.copy()
    d = ImageDraw.Draw(out)
    font = ImageFont.load_default(size=16)
    for b in boxes:
        color = COLORS.get(b["class"], (0, 0, 0))  # 클래스별 색, 없으면 검정
        d.rectangle(b["box"], outline=color, width=3)
        # 클래스 이름 · 신뢰도 글자를 상자 위에
        d.text((b["box"][0], b["box"][1] - 20), f'{b["class"]} {b["conf"]:.2f}', fill=color, font=font)
    return out
