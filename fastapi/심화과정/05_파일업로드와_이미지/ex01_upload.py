# UploadFile: 업로드된 파일 (이름 · 종류 · 내용)
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/upload")
async def upload(file: UploadFile):                  # 파일 하나
    data = await file.read()                         # 파일 내용 (bytes)
    # 받은 파일의 이름 · 종류 · 크기를 돌려주기
    return {"filename": file.filename, "content_type": file.content_type, "size": len(data)}


@app.post("/upload/text-lines")
async def count_lines(file: UploadFile):
    text = (await file.read()).decode("utf-8")        # bytes → 문자열
    # 줄 단위로 나누기
    lines = text.splitlines()
    return {"filename": file.filename, "lines": len(lines), "first_line": lines[0] if lines else None}


@app.post("/upload/many")
async def upload_many(files: list[UploadFile] = File(...)):   # 여러 파일
    return [{"filename": f.filename, "size": len(await f.read())} for f in files]
