# 6장 예제 1: AI 모델을 함수처럼 써 보기 — 서버 없이 파이썬으로 먼저 (python 으로 실행)
# 모델 = "숫자를 넣으면 답(확률)이 나오는 함수" 라고 생각하면 돼요
from ai_model import predict

# 함수 한 번 부르기: 공부 4시간, 수면 7시간, 휴대폰 2시간
p = predict(4, 7, 2)
print(f"합격 확률: {p * 100:.1f}%")

# 공부 시간만 바꿔 가며 불러 보기 (수면 7시간, 휴대폰 2시간은 같게)
print("\n공부 시간이 늘면 합격 확률은?")
for study in [0, 1, 2, 3, 4, 5]:
    p = predict(study, 7, 2)
    label = "합격" if p >= 0.5 else "불합격"         # 50% 이상이면 합격으로 판단
    print(f"  공부 {study}시간 → {p * 100:5.1f}%  {label}")

# 휴대폰 시간이 늘면?
print("\n휴대폰을 오래 쓰면? (공부 2시간, 수면 7시간)")
for phone in [0, 2, 4, 6]:
    print(f"  휴대폰 {phone}시간 → {predict(2, 7, phone) * 100:5.1f}%")
