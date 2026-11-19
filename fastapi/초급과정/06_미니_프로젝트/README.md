# 06. 미니 프로젝트

배운 것을 조립해 나만의 웹 서비스를 만들고, 친구 폰에서 접속해 발표해요.

> 🧭 [초급 과정 처음으로](../README.md) · 교안: [FastAPI_초급교안.pdf](../../FastAPI_%EC%B4%88%EA%B8%89%EA%B5%90%EC%95%88.pdf)

| 파일 | 실행 (이 폴더에서) | 내용 |
|---|---|---|
| `guestbook/main.py + index.html` | `cd guestbook → uvicorn main:app --reload` | 방명록 예시 — 글을 posts.json 에 저장 |
| `(친구 폰 접속)` | `uvicorn main:app --host 0.0.0.0` | 같은 와이파이의 휴대폰에서 http://내컴퓨터IP:8000 |
| `my_project/` | `cd my_project → uvicorn main:app --reload` | 내 프로젝트 뼈대 + 기획서.md |

**친구 폰에서 접속하는 법**

1. 내 컴퓨터 IP 확인: 터미널에 `ipconfig` 입력 → **IPv4 주소** (예: `192.168.0.12`)
2. 서버를 `--host 0.0.0.0` 을 붙여 켜요. 처음 켤 때 **Windows 방화벽** 창이 뜨면 "허용"을 눌러요.
3. 같은 와이파이에 연결된 폰 브라우저에 `http://192.168.0.12:8000` 처럼 입력해요. (학교 · 회사 와이파이는 기기끼리 접속을 막아 두기도 해요. 그럴 때는 폰 핫스팟에 컴퓨터를 연결해 보세요.)
