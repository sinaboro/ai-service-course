# 실습 환경 점검 — 이 과정에 필요한 것이 모두 준비됐는지 확인해요 (python 으로 실행)
# 사용법: 가상환경을 켠 터미널에서  python check_setup.py
import importlib
import importlib.util
import socket
import sys

ok = True

# 1) 파이썬 버전: 3.10 이상이어야 str | None 같은 문법을 쓸 수 있어요
v = sys.version_info
if v >= (3, 10):
    print(f"[OK]  파이썬 {v.major}.{v.minor}.{v.micro}")
else:
    ok = False
    print(f"[X]   파이썬 {v.major}.{v.minor} — 3.10 이상을 설치하세요 (권장 3.12)")

# 2) 가상환경 안에서 실행 중인지 (권장 사항이라 없어도 실패로 보지는 않아요)
in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
print("[OK]  가상환경 사용 중" if in_venv else "[!]   가상환경이 꺼져 있어요 (0장 6절의 activate 명령으로 켜는 것을 권장)")

# 3) 패키지: (import 이름, 설치 이름, 쓰는 장)
PACKAGES = [
    ("fastapi", "fastapi", "1장~"),
    ("uvicorn", "uvicorn", "1장~ 서버 실행"),
    ("httpx2", "httpx2", "1장~ TestClient"),
    ("multipart", "python-multipart", "5장 파일 업로드"),
    ("PIL", "pillow", "5~6장 이미지"),
    ("numpy", "numpy", "5~6장 배열·모델"),
    ("pytest", "pytest", "7장 테스트"),
]
missing = []
for module, pip_name, where in PACKAGES:
    try:
        m = importlib.import_module(module)
        ver = getattr(m, "__version__", "")
        print(f"[OK]  {pip_name:<17} {ver:<10} ({where})")
    except ImportError:
        # httpx2 가 없어도 예전 이름인 httpx 가 있으면 TestClient 는 동작해요
        if module == "httpx2" and importlib.util.find_spec("httpx"):
            print(f"[OK]  httpx (httpx2 대신)          ({where})")
            continue
        missing.append(pip_name)
        print(f"[X]   {pip_name:<17} 설치 안 됨  ({where})")

# 4) 8000번 포트가 비어 있는지 (이미 쓰고 있으면 uvicorn 이 켜지지 않아요)
with socket.socket() as s:
    busy = s.connect_ex(("127.0.0.1", 8000)) == 0
print("[!]   8000번 포트를 다른 프로그램(켜 둔 서버?)이 쓰고 있어요 → 그 서버를 끄거나 --port 8001" if busy
      else "[OK]  8000번 포트 비어 있음")

print()
if missing:
    ok = False
    print("아래 명령으로 빠진 패키지를 설치하세요:")
    print("  pip install " + " ".join(missing))
print("준비 완료! 1장으로 가세요." if ok else "위의 [X] 항목을 해결한 뒤 다시 실행해 보세요.")
