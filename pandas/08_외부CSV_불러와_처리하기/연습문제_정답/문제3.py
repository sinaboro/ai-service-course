# 문제 3. data/population.txt를 읽어 면적이 1,000km² 이상인 시도의 이름과 면적을 출력하세요. (합계 행은 제외)

from pathlib import Path
import pandas as pd

# 정답 파일은 "연습문제_정답" 폴더 안에 있고, data 폴더는 한 단계 위(예제 폴더)에 있어요.
# 그래서 이 파일의 위치를 기준으로 경로를 만들어요. (어느 폴더에서 실행해도 동작 — 1-2절)
DATA = Path(__file__).parent.parent / "data"
pd.set_option("display.unicode.east_asian_width", True)

pop = pd.read_csv(DATA / "population.txt", sep="\t", comment="#", thousands=",",
                  skipfooter=1, engine="python")
print(pop[pop["면적"] >= 1000][["시도", "면적"]])
