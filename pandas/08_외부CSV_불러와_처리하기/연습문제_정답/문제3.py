# 문제 3. data/population.txt를 읽어 면적이 1,000km² 이상인 시도의 이름과 면적을 출력하세요. (합계 행은 제외)

import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)

pop = pd.read_csv("data/population.txt", sep="\t", comment="#", thousands=",",
                  skipfooter=1, engine="python")
print(pop[pop["면적"] >= 1000][["시도", "면적"]])
