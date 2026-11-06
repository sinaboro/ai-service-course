# 1장 예제 4 (한 번만 보고 넘어가요): 브라우저 대신 "코드로" 요청 보내기 (python 으로 실행)
# TestClient 는 서버를 켜지 않고 앱에 요청을 보내 주는 "코드로 만든 브라우저" 예요.
# 이 과정에서는 브라우저와 /docs 로 확인하니, 이런 방법도 있다는 것만 알아 두세요.
from fastapi.testclient import TestClient

from ex02_path import app             # 예제 2의 앱 가져오기

client = TestClient(app)

res = client.get("/menu/3")           # 브라우저 주소창에 /menu/3 을 친 것과 같아요
print(res.status_code)                # 상태 코드: 200 이면 성공
print(res.json())                     # 응답 JSON → 파이썬 딕셔너리
