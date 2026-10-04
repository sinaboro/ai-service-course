# 예외처리: 오류가 나도 프로그램이 멈추지 않게
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("0으로 나눌 수 없어요.")
        return None
    except TypeError:
        print("숫자만 나눌 수 있어요.")
        return None
    else:
        print("정상 계산!")          # 오류가 없을 때만
        return result
    finally:
        print("-- divide 끝 --")    # 항상 실행

print(divide(10, 2))
print(divide(10, 0))
print(divide(10, "a"))

# 오류 메시지를 받아서 보기
try:
    num = int("abc")
except ValueError as e:
    print("오류 내용:", e)
