from fastapi import FastAPI

app = FastAPI(title="첫 번째 API", version="1.0")   # API 서버(앱) 만들기


@app.get("/")                         # GET 방식으로 "/" 주소에 요청이 오면
def root():                           # 이 함수가 실행되고
    return {"message": "안녕하세요, FastAPI!"}   # 딕셔너리가 JSON 으로 응답돼요


@app.get("/hello/{name}")             # 주소의 일부를 변수로 받기
def hello(name: str):
    return {"greeting": f"{name}님, 반가워요!"}


@app.get("/health")                   # 서버가 살아 있는지 확인용 (서빙에서 꼭 만들어요)
def health():
    return {"status": "ok"}
