from pathlib import Path

from ultralytics import YOLO

HERE = Path(__file__).parent
model = YOLO(HERE / "models" / "best.pt")             # 학습한 모델 불러오기
m = model.val(data=str(HERE / "datasets" / "floats" / "data.yaml"), imgsz=320, batch=16, workers=0, device="cpu", plots=False, verbose=False)
print("\n===== 검증 요약 =====")
print(f"mAP50 {m.box.map50:.3f} | mAP50-95 {m.box.map:.3f} | 정밀도 {m.box.mp:.3f} | 재현율 {m.box.mr:.3f}")
for i, name in model.names.items():
    p, r, ap50, ap = m.box.class_result(i)
    print(f"  {name:7s} P {p:.3f}  R {r:.3f}  AP50 {ap50:.3f}")
print("사진 한 장 처리(ms):", {k: round(v, 1) for k, v in m.speed.items()})
