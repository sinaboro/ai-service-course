# serving_project 의 테스트를 실행하고 결과를 보여 주는 파일
# (터미널에서  cd serving_project  →  pytest -v  와 같아요)
import os
import sys
from pathlib import Path
import pytest

# 테스트는 serving_project 폴더 기준으로 실행해야 해요
project = Path(__file__).parent / "serving_project"
os.chdir(project)
sys.path.insert(0, str(project))
# pytest.main(): 파이썬 코드 안에서 pytest 실행 (-v: 테스트마다 결과 표시)
code = pytest.main(["-v", "-p", "no:cacheprovider", "--no-header", "-W", "ignore"])
print("종료 코드:", int(code), "(0 이면 모두 통과)")
