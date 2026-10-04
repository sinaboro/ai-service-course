import json
from fastapi.testclient import TestClient
# 이 장의 앱과 LOG 목록을 함께 불러오기
import ex04_lifespan
from ex04_lifespan import app

with TestClient(app) as client:                # with 블록 = 서버가 켜져 있는 동안
    # 숫자 3개로 예측 요청 → 모델은 서버 시작 때 한 번만 불러와요
    for x in [1, 2.5, 10]:
        print(client.get("/predict", params={"x": x}).json())
    print("요청 3번 후 로그:", client.get("/log").json())

# with 블록을 나오면 서버가 꺼지고, lifespan 의 yield 뒤가 실행돼요
print("서버 종료 후 로그:", ex04_lifespan.LOG)
