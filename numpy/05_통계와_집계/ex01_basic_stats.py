import numpy as np

# 학생 6명의 점수 배열
scores = np.array([85, 92, 78, 64, 95, 70])

# 배열.함수() 로 기본 통계 구하기
print("합계  :", scores.sum())
print("평균  :", scores.mean())
print("최댓값:", scores.max())
print("최솟값:", scores.min())
# median 은 메서드가 없어서 np.median(배열) 으로
print("중앙값:", np.median(scores))
# std: 표준편차 (점수가 평균에서 얼마나 흩어져 있나), round 로 소수 둘째 자리까지
print("표준편차:", round(scores.std(), 2))
# size: 원소 개수
print("개수  :", scores.size)

# 함수 방식과 메서드 방식은 같아요
print(np.sum(scores) == scores.sum())
