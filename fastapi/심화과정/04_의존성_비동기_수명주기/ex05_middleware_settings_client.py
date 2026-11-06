import os
os.environ["MODEL_VERSION"] = "2.1.0"           # 앱을 불러오기 "전에" 환경 변수 설정 (터미널의 set/export 와 같음)

from fastapi.testclient import TestClient
from ex05_middleware_settings import app

client = TestClient(app)
# 응답 본문과 미들웨어가 붙인 헤더 확인
res = client.get("/info")
print(res.json())
print("헤더 X-Model-Version:", res.headers["X-Model-Version"])

res = client.get("/slow")
print("처리 시간 50ms 이상?", float(res.headers["X-Process-Time-ms"]) >= 50)

# OPTIONS 요청: 브라우저가 "이 출처에서 불러도 되나요?" 하고 먼저 물어보는 요청(CORS 사전 요청)
pre = client.options("/info", headers={"Origin": "http://localhost:3000", "Access-Control-Request-Method": "GET"})
print("허용된 출처 CORS:", pre.status_code, pre.headers.get("access-control-allow-origin"))
bad = client.options("/info", headers={"Origin": "http://evil.com", "Access-Control-Request-Method": "GET"})
print("허용 안 된 출처 CORS:", bad.status_code, bad.headers.get("access-control-allow-origin"))
