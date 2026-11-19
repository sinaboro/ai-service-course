# ex02_korean_font.py : 한글 글꼴 설정: 한글 제목이 네모(□□)로 깨지지 않게 하기
import platform                                   # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                          # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt                   # 그래프 도구 (관례적으로 plt 라는 별명)

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)                          # images 폴더 만들기 (이미 있으면 그냥 넘어가요)

# x 축에 쓸 월 이름과 y 축 값
months = ["1월", "2월", "3월", "4월", "5월", "6월"]
sales = [120, 135, 150, 145, 170, 190]

plt.plot(months, sales)
# 위의 글꼴 설정 덕분에 제목 · 축 이름의 한글이 네모(□)로 깨지지 않아요
plt.title("월별 매출 (단위: 만원)")
plt.xlabel("월")
plt.ylabel("매출")
plt.savefig(IMG / "ex02_korean_font.png", dpi=100, bbox_inches="tight")
plt.show()
