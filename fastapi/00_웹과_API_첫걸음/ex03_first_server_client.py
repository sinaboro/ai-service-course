# 클라이언트 예제: 서버를 켜지 않고 ex03_first_server 의 앱에 요청을 보내 봐요 (python 으로 실행)
# 1장에서 자세히 배우는 TestClient 를 미리 맛보는 예제예요. 브라우저로 확인했다면 건너뛰어도 돼요.
from fastapi.testclient import TestClient

from ex03_first_server import app

client = TestClient(app)                       # 가짜 브라우저 역할

res = client.get("/")                          # 브라우저 주소창에 http://127.0.0.1:8000/ 을 친 것과 같아요
print(res.status_code, res.json())             # 상태 코드(200 = 성공)와 JSON 응답

res = client.get("/time")
print(res.status_code, list(res.json()))       # 시각은 매번 달라서 키 이름만 출력

res = client.get("/없는주소")
print(res.status_code, res.json())             # 등록하지 않은 주소 → 404
