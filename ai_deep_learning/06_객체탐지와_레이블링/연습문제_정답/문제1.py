# 문제 1. iou((0, 0, 100, 100), (50, 50, 150, 150)) 를 손으로 먼저 계산하고 코드로 확인하세요.

def iou(a, b):
    ix1, iy1, ix2, iy2 = max(a[0], b[0]), max(a[1], b[1]), min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, ix2 - ix1) * max(0, iy2 - iy1)
    return inter / ((a[2] - a[0]) * (a[3] - a[1]) + (b[2] - b[0]) * (b[3] - b[1]) - inter)
print(round(iou((0, 0, 100, 100), (50, 50, 150, 150)), 4))
