# 문제 2. requirements.txt를 읽어서 주석(#)과 빈 줄을 뺀 패키지 이름만 출력하세요. (>= 앞부분, [standard] 제외)

import re
from pathlib import Path

names = []
for line in Path("serving_project/requirements.txt").read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    names.append(re.split(r"[\[>=<]", line)[0])
print(names)
