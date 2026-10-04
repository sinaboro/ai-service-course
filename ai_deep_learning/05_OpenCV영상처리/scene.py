# 해변 장면 + 부유물 만들기 (6 · 7 · 8장과 같은 코드)
import random

import cv2
import numpy as np

# 클래스 이름 (번호 0, 1, 2 순서) — data.yaml · classes.txt 와 같은 순서여야 해요
CLASSES = ["bottle", "can", "bag"]


def make_scene(rng: random.Random, size: int = 320):
    """바다 · 모래 배경에 부유물 1 ~ 4개를 그리고, (이미지, [(클래스번호, x1, y1, x2, y2), ...]) 를 돌려줌"""
    # 빈 그림(검정) 만들기: (높이, 너비, 채널 3)
    img = np.zeros((size, size, 3), np.uint8)
    # 수평선 위치를 무작위로 → 위는 바다, 아래는 모래
    horizon = rng.randint(int(size * 0.45), int(size * 0.7))
    img[:horizon] = (rng.randint(170, 220), rng.randint(130, 170), rng.randint(60, 100))   # 바다 (BGR)
    img[horizon:] = (rng.randint(120, 160), rng.randint(190, 220), rng.randint(220, 245))  # 모래
    for _ in range(25):                                                                  # 물결 무늬
        y = rng.randint(0, horizon - 1)
        x = rng.randint(0, size - 40)
        cv2.line(img, (x, y), (x + rng.randint(15, 40), y), (230, 200, 160), 1)
    boxes = []
    # 물체 1 ~ 4개를 무작위로 그리기
    for _ in range(rng.randint(1, 4)):
        # 클래스 고르기: 0 = bottle, 1 = can, 2 = bag
        c = rng.randint(0, 2)
        if c == 0:                                   # bottle: 세로로 긴 초록 사각형 + 뚜껑
            w, h = rng.randint(14, 24), rng.randint(40, 70)
        elif c == 1:                                 # can: 회색 짧은 사각형
            w, h = rng.randint(18, 28), rng.randint(26, 38)
        else:                                        # bag: 흰 타원
            w, h = rng.randint(34, 56), rng.randint(26, 44)
        # 물체의 왼쪽 위 꼭짓점 위치를 무작위로 (그림 밖으로 나가지 않게)
        x1 = rng.randint(2, size - w - 2)
        y1 = rng.randint(2, size - h - 2)
        x2, y2 = x1 + w, y1 + h
        if any(not (x2 < a or x1 > c2 or y2 < b or y1 > d) for _, a, b, c2, d in boxes):
            continue                                 # 다른 물체와 겹치면 건너뛰기
        # 실제로 그리기: 병 = 초록 몸통 + 뚜껑, 캔 = 회색 사각형, 비닐봉지 = 흰 타원
        if c == 0:
            cv2.rectangle(img, (x1, y1 + h // 6), (x2, y2), (90, 170, 90), -1)
            cv2.rectangle(img, (x1 + w // 3, y1), (x2 - w // 3, y1 + h // 6), (40, 90, 200), -1)
        elif c == 1:
            cv2.rectangle(img, (x1, y1), (x2, y2), (185, 185, 190), -1)
            cv2.line(img, (x1, y1 + 4), (x2, y1 + 4), (120, 120, 120), 2)
        else:
            cv2.ellipse(img, ((x1 + x2) // 2, (y1 + y2) // 2), (w // 2, h // 2), 0, 0, 360, (245, 245, 245), -1)
        # 정답 상자(클래스, 꼭짓점 좌표) 기록 → 레이블 파일이 돼요
        boxes.append((c, x1, y1, x2, y2))
    noise = np.random.default_rng(rng.randint(0, 10**6)).normal(0, 6, img.shape)
    img = np.clip(img + noise, 0, 255).astype(np.uint8)            # 약간의 잡음 (실제 사진처럼)
    return img, boxes


def to_yolo_line(c, x1, y1, x2, y2, size):
    """픽셀 좌표 → YOLO 한 줄: 클래스 x중심 y중심 너비 높이 (0 ~ 1 비율)"""
    # 중심 = (x1 + x2) / 2, 너비 = x2 - x1, 모두 사진 크기로 나눠 0 ~ 1 비율로
    return f"{c} {(x1 + x2) / 2 / size:.6f} {(y1 + y2) / 2 / size:.6f} {(x2 - x1) / size:.6f} {(y2 - y1) / size:.6f}"
