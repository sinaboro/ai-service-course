# 덕 타이핑: "오리처럼 걷고 꽥꽥거리면 오리다"
class Duck:
    def speak(self):
        return "꽥꽥"

class Robot:
    def speak(self):
        return "삐빅"

class Stone:
    pass

def make_speak(thing):
    # 자료형을 묻지 않고, speak 할 수 있는지만 확인
    if hasattr(thing, "speak") and callable(thing.speak):
        print(type(thing).__name__, "→", thing.speak())
    else:
        print(type(thing).__name__, "→ 말할 수 없어요")

for t in [Duck(), Robot(), Stone()]:
    make_speak(t)

# EAFP: 일단 해 보고, 안 되면 예외로 처리 (파이썬다운 방식)
def total_length(items):
    try:
        return sum(len(x) for x in items)
    except TypeError:
        return "길이를 잴 수 없는 값이 섞여 있어요"

print(total_length(["abc", [1, 2], "hi"]))
print(total_length(["abc", 123]))
