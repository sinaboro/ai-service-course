from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/upload")
async def upload(file: UploadFile):                  # 파일 하나
    data = await file.read()                         # 파일 내용 (bytes)
    return {"filename": file.filename, "content_type": file.content_type, "size": len(data)}


@app.post("/upload/text-lines")
async def count_lines(file: UploadFile):
    text = (await file.read()).decode("utf-8")        # bytes → 문자열
    lines = text.splitlines()
    return {"filename": file.filename, "lines": len(lines), "first_line": lines[0] if lines else None}


@app.post("/upload/many")
async def upload_many(files: list[UploadFile] = File(...)):   # 여러 파일
    return [{"filename": f.filename, "size": len(await f.read())} for f in files]
