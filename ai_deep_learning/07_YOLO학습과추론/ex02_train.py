import shutil
from pathlib import Path

from ultralytics import YOLO

HERE = Path(__file__).parent
# 학습할 데이터셋의 설정 파일 (images · labels · 클래스 이름이 적혀 있어요)
DATA = HERE / "datasets" / "floats" / "data.yaml"      # 6장에서 만든 것과 같은 구조

model = YOLO("yolo11n.pt")                             # ⭐ 사전 학습 가중치에서 출발 (전이 학습)
# ⭐ 학습 시작: 아래 값들을 바꿔 가며 실험해요
results = model.train(
    data=str(DATA),
    epochs=30,            # 전체 데이터를 30번 반복
    imgsz=320,            # 학습 사진 크기 (기본 640, CPU 실습이라 작게)
    batch=16,             # 한 번에 16장
    patience=10,          # 10 에폭 동안 좋아지지 않으면 일찍 멈추기
    workers=0,            # Windows 에서 오류를 줄이는 설정
    device="cpu",         # GPU 가 있으면 0
    project=str(HERE / "runs"),
    name="floats",
    exist_ok=True,        # 같은 이름이면 덮어쓰기
    seed=0,
)

# 결과가 저장된 폴더 (runs/floats) 와 가장 좋은 모델 파일 위치
save_dir = Path(results.save_dir)
best = save_dir / "weights" / "best.pt"
shutil.copy(best, HERE / "models" / "best.pt")        # 8장에서 쓸 수 있게 복사
print("\n===== 요약 =====")
print("결과 폴더:", save_dir.parent.name + "/" + save_dir.name)
print(f"mAP50 = {results.box.map50:.3f} | mAP50-95 = {results.box.map:.3f}")
# 클래스별 AP50 출력
for i, name in model.names.items():
    print(f"  {name:7s} AP50 = {results.box.ap50[i]:.3f}")
print("저장한 모델: models/best.pt")
