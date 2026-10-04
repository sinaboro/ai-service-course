# 기본값 매개변수와 키워드 인자
def order(menu, count=1, size="보통"):
    print(f"{menu} {count}개 ({size})")

order("커피")                        # count, size 는 기본값
order("커피", 3)
order("커피", size="큰")             # 키워드 인자: 이름을 지정
order(count=2, menu="라떼", size="작은")   # 순서를 바꿔도 OK

# 개수가 정해지지 않은 인자 *args
def total(*nums):
    return sum(nums)

print(total(1, 2), total(1, 2, 3, 4, 5))
