import platform
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")             # seaborn 기본 스타일
# ⚠ set_theme 은 글꼴을 초기화하므로 한글 글꼴은 "그 다음에" 설정
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False

HERE = Path(__file__).parent
IMG = HERE / "images"; IMG.mkdir(exist_ok=True)
tips = pd.read_csv(HERE / "data" / "tips.csv")   # 식당 팁 데이터 (244건)

palettes = ["deep", "pastel", "Set2", "coolwarm"]
fig, axes = plt.subplots(1, 4, figsize=(15, 3.5), sharey=True)
for ax, pal in zip(axes, palettes):
    sns.barplot(data=tips, x="day", y="total_bill", hue="day", palette=pal, legend=False,
                order=["Thur", "Fri", "Sat", "Sun"], errorbar=None, ax=ax)
    ax.set_title(f'palette="{pal}"')
fig.tight_layout()
fig.savefig(IMG / "ex06_palette.png", dpi=100, bbox_inches="tight")
print(sns.color_palette("Set2").as_hex()[:4])
plt.show()
