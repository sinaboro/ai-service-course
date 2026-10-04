# CSV 파일 직접 읽어서 계산하기
# 쉼표로 구분한 글자 4줄 (첫 줄은 열 이름)
rows = [
    "name,kor,eng,math",
    "홍길동,90,80,70",
    "이순신,85,95,75",
    "유관순,100,90,95",
]
# "w": 쓰기 모드로 열기 → 줄들을 줄바꿈 문자로 이어 붙여 저장
with open("scores.csv", "w", encoding="utf-8") as f:
    f.write("\n".join(rows) + "\n")

# "r": 읽기 모드로 다시 열기
with open("scores.csv", "r", encoding="utf-8") as f:
    header = f.readline().strip().split(",")       # 첫 줄: 제목
    print("열 이름:", header)
    # 남은 줄을 하나씩: 쉼표로 나눠 변수 4개에 담기
    for line in f:
        name, kor, eng, math = line.strip().split(",")
        # 글자로 읽혔으니 int() 로 바꿔 더하기
        total = int(kor) + int(eng) + int(math)
        print(f"{name}: 총점 {total}, 평균 {total / 3:.1f}")
