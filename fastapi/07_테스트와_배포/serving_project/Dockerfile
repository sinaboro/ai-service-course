# 1) 파이썬이 설치된 가벼운 기본 이미지
FROM python:3.12-slim

# 2) 작업 폴더
WORKDIR /app

# 3) 패키지 먼저 설치 (코드가 바뀌어도 이 단계는 캐시로 재사용돼 빨라요)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4) 코드와 모델 복사
COPY app ./app
COPY model ./model

# 5) 서버 실행 (컨테이너 밖에서 접속하려면 0.0.0.0)
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
