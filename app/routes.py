from fastapi import APIRouter
from fastapi.responses import FileResponse
from concurrent.futures import ThreadPoolExecutor
import os
import uuid
import time

router = APIRouter()
executor = ThreadPoolExecutor(max_workers=12)

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def process_tts(text: str, file_path: str):
    time.sleep(3)
    with open(file_path, "wb") as f:
        f.write(b"Dummy MP3 Data")


@router.post("/generate")
async def generate(topic: dict):

    filename = f"{uuid.uuid4()}.mp3"
    file_path = os.path.join(OUTPUT_DIR, filename)

    executor.submit(process_tts, topic["text"], file_path)

    return {"status": "started", "file": filename}


@router.get("/download/{filename}")
async def download(filename: str):
    file_path = os.path.join(OUTPUT_DIR, filename)
    return FileResponse(file_path, media_type="audio/mpeg")
