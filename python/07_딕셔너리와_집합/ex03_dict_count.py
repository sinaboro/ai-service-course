# 딕셔너리로 개수 세기
votes = ["짜장", "짬뽕", "짜장", "볶음밥", "짜장", "짬뽕"]

count = {}
for menu in votes:
    if menu in count:
        count[menu] += 1
    else:
        count[menu] = 1
print(count)

# get 을 쓰면 더 짧게
count2 = {}
for menu in votes:
    count2[menu] = count2.get(menu, 0) + 1
print(count2)

best = max(count, key=count.get)      # 값이 가장 큰 키
print("1위 메뉴:", best)
