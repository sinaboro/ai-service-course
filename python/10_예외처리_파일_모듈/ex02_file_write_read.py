# 파일 쓰기와 읽기
with open("memo.txt", "w", encoding="utf-8") as f:    # w: 새로 쓰기
    f.write("첫째 줄\n")
    f.write("둘째 줄\n")

with open("memo.txt", "a", encoding="utf-8") as f:    # a: 이어 쓰기
    f.write("셋째 줄 (추가)\n")

with open("memo.txt", "r", encoding="utf-8") as f:    # r: 읽기
    content = f.read()
print(content)

with open("memo.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):            # 한 줄씩
        print(i, line.strip())
