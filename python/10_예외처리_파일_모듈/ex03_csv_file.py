# CSV 파일 직접 읽어서 계산하기
rows = [
    "name,kor,eng,math",
    "홍길동,90,80,70",
    "이순신,85,95,75",
    "유관순,100,90,95",
]
with open("scores.csv", "w", encoding="utf-8") as f:
    f.write("\n".join(rows) + "\n")

with open("scores.csv", "r", encoding="utf-8") as f:
    header = f.readline().strip().split(",")       # 첫 줄: 제목
    print("열 이름:", header)
    for line in f:
        name, kor, eng, math = line.strip().split(",")
        total = int(kor) + int(eng) + int(math)
        print(f"{name}: 총점 {total}, 평균 {total / 3:.1f}")
