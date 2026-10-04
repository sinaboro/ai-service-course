# 딕셔너리로 개수 세기
votes = ["짜장", "짬뽕", "짜장", "볶음밥", "짜장", "짬뽕"]

# 메뉴 이름을 키, 표 수를 값으로 담을 빈 사전
count = {}
for menu in votes:
    # 이미 있는 메뉴면 1 더하고, 처음 나온 메뉴면 1 로 시작
    if menu in count:
        count[menu] += 1
    else:
        count[menu] = 1
print(count)

# get 을 쓰면 더 짧게
count2 = {}
for menu in votes:
    # get(키, 0): 키가 없으면 0 을 돌려줘서 if 없이 쓸 수 있어요
    count2[menu] = count2.get(menu, 0) + 1
print(count2)

best = max(count, key=count.get)      # 값이 가장 큰 키
print("1위 메뉴:", best)
