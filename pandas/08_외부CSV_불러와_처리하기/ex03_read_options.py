from pathlib import Path
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)   # 한글 열 줄맞춤
DATA = Path(__file__).parent / "data"                      # 이 파일 옆의 data 폴더

# 탭 구분 + 주석 줄 + 숫자 콤마 + 마지막 합계 줄
pop = pd.read_csv(
    DATA / "population.txt",
    sep="\t",            # 탭으로 구분
    comment="#",          # # 로 시작하는 줄은 건너뛰기
    thousands=",",        # 9,386,034 → 9386034
    skipfooter=1,         # 마지막 1줄(합계) 버리기
    engine="python",      # skipfooter 를 쓰려면 필요
)
print(pop)
print(pop.dtypes)
pop["세대당인구"] = (pop["인구"] / pop["세대수"]).round(2)
pop["인구밀도"] = (pop["인구"] / pop["면적"]).round(0).astype(int)
print(pop.sort_values("인구밀도", ascending=False)[["시도", "인구밀도", "세대당인구"]])

# 필요한 열만, 자료형 지정, 인덱스 지정
st = pd.read_csv(DATA / "students.csv", usecols=["이름", "반", "수학"],
                 dtype={"반": "str"}, index_col="이름")
print(st.head(3))
print(st.dtypes)

# 제목 줄이 없는 파일이라면: header=None, names=[...]
raw = pd.read_csv(DATA / "students.csv", header=None, skiprows=1, nrows=2,
                  names=["name", "class", "kor", "eng", "math"])
print(raw)
