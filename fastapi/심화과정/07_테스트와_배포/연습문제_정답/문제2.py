# 문제 2. requirements.txt를 읽어서 주석(#)과 빈 줄을 뺀 패키지 이름만 출력하세요. (>= 앞부분, [standard] 제외)

import re                                          # 정규식: 글자 패턴 찾기 · 나누기
from pathlib import Path                           # 파일 · 폴더 경로를 다루는 도구

# 정답 폴더(연습문제_정답)에서 실행해도 되도록, 이 파일 기준으로 requirements.txt 를 찾아요
REQ = Path(__file__).parent.parent / "serving_project" / "requirements.txt"

names = []                                         # 패키지 이름을 모을 리스트
for line in REQ.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    # re.split: [, >, =, < 중 하나를 만나면 자르기 → 첫 조각이 패키지 이름
    # 예) "uvicorn[standard]>=0.30" → ["uvicorn", "standard]", "", "0.30"] → "uvicorn"
    names.append(re.split(r"[\[>=<]", line)[0])
print(names)
