# ex03_image_client.py : ex03_image_app 에 색깔 사진을 올려 분류 결과 보기
# 실행: python ex03_image_client.py (서버를 켜지 않아도 돼요)
from pathlib import Path  # 파일 · 폴더 경로를 다루는 도구
from fastapi.testclient import TestClient  # 서버를 켜지 않고 코드로 요청을 보내는 도구
from ex03_image_app import app

# 샘플 이미지가 있는 폴더
S = Path(__file__).parent / "samples"
with TestClient(app) as client:
    # 4장을 차례로 업로드해서 1등과 나머지 확률 출력
    for name in ["red.png", "green.png", "blue.png", "purple.png"]:
        res = client.post("/predict/image", files={"file": (name, (S / name).read_bytes(), "image/png")})
        r = res.json()
        others = ", ".join(f"{s['label']} {s['probability']:.1%}" for s in r["scores"][1:])
        print(f"{name:11} → {r['top']['label']:5} {r['top']['probability']:.1%}   (나머지: {others})")
    # 이미지가 아닌 내용을 보내면 400
    bad = client.post("/predict/image", files={"file": ("x.png", b"oops", "image/png")})
    print("잘못된 파일:", bad.status_code, bad.json())
