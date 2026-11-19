# ex03_timeseries.py : 날짜(시계열) 데이터 선 그래프와 이동평균(rolling) 겹쳐 그리기
import platform                                   # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                          # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt                   # 그래프 도구 (관례적으로 plt 라는 별명)

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)                          # images 폴더 만들기 (이미 있으면 그냥 넘어가요)
import pandas as pd                               # 판다스 (관례적으로 pd 라는 별명)

DATA = Path(__file__).parent / "data"
df = pd.read_csv(DATA / "store_sales.csv", parse_dates=["date"])

# 행 = 날짜, 열 = 지점인 표 → 열마다 선 하나씩 그려져요
ts = df.pivot_table(index="date", columns="store", values="sales", aggfunc="sum")
print(ts.head(3))

ax = ts.plot(figsize=(9, 4.5), marker="o", title="지점별 월 매출 추이")
ax.set_ylabel("매출 (만원)")
ax.figure.savefig(IMG / "ex03_store_trend.png", dpi=100, bbox_inches="tight")

# 월별 전체 매출 (가로 방향 합계)
total = ts.sum(axis=1)
ma3 = total.rolling(3).mean()                 # 3개월 이동평균
# 같은 칸(ax)에 원래 값과 이동평균을 겹쳐 그리기
fig, ax = plt.subplots(figsize=(9, 4.5))
total.plot(ax=ax, marker="o", alpha=0.5, label="월 매출")
ma3.plot(ax=ax, linewidth=3, label="3개월 이동평균")
ax.set_title("전체 매출과 3개월 이동평균")
ax.legend()
fig.savefig(IMG / "ex03_moving_avg.png", dpi=100, bbox_inches="tight")
print(ma3.round(1).tail(3))
plt.show()
