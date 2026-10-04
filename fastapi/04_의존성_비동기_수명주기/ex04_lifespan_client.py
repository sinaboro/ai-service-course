import json
from fastapi.testclient import TestClient
import ex04_lifespan
from ex04_lifespan import app

with TestClient(app) as client:                # with 블록 = 서버가 켜져 있는 동안
    for x in [1, 2.5, 10]:
        print(client.get("/predict", params={"x": x}).json())
    print("요청 3번 후 로그:", client.get("/log").json())

print("서버 종료 후 로그:", ex04_lifespan.LOG)
