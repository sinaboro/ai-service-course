# 덕 타이핑: "오리처럼 걷고 꽥꽥거리면 오리다"
# speak 메서드를 가진 두 클래스 (서로 아무 관계 없음)
class Duck:
    def speak(self):
        return "꽥꽥"

class Robot:
    def speak(self):
        return "삐빅"

# speak 가 없는 클래스
class Stone:
    pass

def make_speak(thing):
    # 자료형을 묻지 않고, speak 할 수 있는지만 확인
    # hasattr: 그 이름의 속성이 있나? / callable: 호출할 수 있는 함수인가?
    if hasattr(thing, "speak") and callable(thing.speak):
        print(type(thing).__name__, "→", thing.speak())
    else:
        print(type(thing).__name__, "→ 말할 수 없어요")

# 세 객체를 같은 함수에 넣어 보기
for t in [Duck(), Robot(), Stone()]:
    make_speak(t)

# EAFP: 일단 해 보고, 안 되면 예외로 처리 (파이썬다운 방식)
def total_length(items):
    # len() 이 안 되는 값(123)이 섞이면 TypeError → 안내 문구로
    try:
        return sum(len(x) for x in items)
    except TypeError:
        return "길이를 잴 수 없는 값이 섞여 있어요"

print(total_length(["abc", [1, 2], "hi"]))
print(total_length(["abc", 123]))
