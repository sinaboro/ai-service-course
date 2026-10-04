from pathlib import Path
from fastapi.testclient import TestClient
from ex03_image_app import app

S = Path(__file__).parent / "samples"
with TestClient(app) as client:
    for name in ["red.png", "green.png", "blue.png", "purple.png"]:
        res = client.post("/predict/image", files={"file": (name, (S / name).read_bytes(), "image/png")})
        r = res.json()
        others = ", ".join(f"{s['label']} {s['probability']:.1%}" for s in r["scores"][1:])
        print(f"{name:11} → {r['top']['label']:5} {r['top']['probability']:.1%}   (나머지: {others})")
    bad = client.post("/predict/image", files={"file": ("x.png", b"oops", "image/png")})
    print("잘못된 파일:", bad.status_code, bad.json())
