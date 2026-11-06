# 클라이언트 예제: 6-1 ~ 6-3단계 페이지가 서버에 보내는 요청을 코드로 똑같이 보내 봐요 (python 으로 실행)
# 화면의 버튼 하나 = fetch 한 줄 = 아래 client.get/post 한 줄
import time

from fastapi.testclient import TestClient

import ex03_step1_html
import ex03_step2_fetch
import ex03_step3_post

# ── 1단계: 주소마다 돌려주는 내용의 종류(content-type)가 달라요 ──
c1 = TestClient(ex03_step1_html.app)
for path in ["/api/hello", "/inline", "/"]:
    res = c1.get(path)
    print(f"[1단계] GET {path:<11} → {res.status_code}  {res.headers['content-type']}")
print("        /api/hello 의 내용:", c1.get("/api/hello").json())

# ── 2단계: 버튼이 보내는 GET 요청 ──
c2 = TestClient(ex03_step2_fetch.app)
print("\n[2단계] 시각 가져오기 →", list(c2.get("/api/time").json()))        # 시각은 매번 달라서 키만
print("[2단계] 인사 받기      →", c2.get("/api/hello", params={"name": "철수"}).json())
start = time.perf_counter()
res = c2.get("/api/slow", params={"seconds": 1})
print(f"[2단계] 느린 요청      → {res.json()['message']} (실제로 {time.perf_counter() - start:.1f}초 걸림)")

# ── 3단계: 입력 칸 → POST + JSON 본문 ──
c3 = TestClient(ex03_step3_post.app)
print("\n[3단계] 정상   →", c3.post("/api/grade", json={"name": "영희", "score": 87}).json())
res = c3.post("/api/grade", json={"name": "영희", "score": 150})
err = res.json()["detail"][0]
print(f"[3단계] 점수 150 → {res.status_code}, 칸: {err['loc'][-1]}, 이유: {err['msg']}")
res = c3.post("/api/grade", json={"name": "", "score": 50})
print(f"[3단계] 빈 이름  → {res.status_code}, 칸: {res.json()['detail'][0]['loc'][-1]}")
