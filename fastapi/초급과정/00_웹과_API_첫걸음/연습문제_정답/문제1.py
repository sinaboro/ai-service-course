# 문제 1. JSON 글자 '{"city": "서울", "temp": 21.5, "rain": false}' 를 딕셔너리로 바꾼 뒤,
#        "서울의 기온은 21.5도, 비: 아니요" 처럼 출력하세요. (rain 이 true 면 "예")
import json

text = '{"city": "서울", "temp": 21.5, "rain": false}'
weather = json.loads(text)                     # JSON 글자 → 딕셔너리 (false → False)
rain = "예" if weather["rain"] else "아니요"
print(f"{weather['city']}의 기온은 {weather['temp']}도, 비: {rain}")
