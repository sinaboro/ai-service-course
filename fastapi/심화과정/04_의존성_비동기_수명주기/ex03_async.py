# time.sleep: 기다리는 동안 그 일꾼(스레드)이 멈춰요 / asyncio.sleep: 기다리는 동안 다른 요청을 처리할 수 있어요
import asyncio
import time
from fastapi import FastAPI

app = FastAPI()


@app.get("/sync")
def sync_job():                       # 일반 함수: FastAPI 가 별도 스레드에서 실행
    time.sleep(0.2)                   # 계산·모델 예측처럼 CPU 를 쓰는 일이라고 생각
    return {"type": "sync", "slept": 0.2}


@app.get("/async")
async def async_job():                # 비동기 함수
    await asyncio.sleep(0.2)          # 다른 서버 응답·파일·DB 를 "기다리는" 일
    return {"type": "async", "slept": 0.2}


async def fetch(name: str, sec: float) -> str:
    await asyncio.sleep(sec)          # 외부 API 를 기다린다고 가정
    return f"{name} 완료"


@app.get("/gather")
async def gather():
    # 걸린 시간 재기 시작
    start = time.perf_counter()
    results = await asyncio.gather(fetch("날씨", 0.3), fetch("환율", 0.3), fetch("뉴스", 0.3))  # 동시에 기다리기
    # 세 일을 하나씩 하면 0.9초, 동시에 기다리면 약 0.3초
    took = time.perf_counter() - start
    return {"results": results, "under_0_5s": took < 0.5}
