import asyncio
import time

async def generate_tts(text: str):
    start = time.time()

    # Simulate heavy CPU task
    await asyncio.sleep(3)

    end = time.time()
    return f"audio_generated_in_{round(end-start,2)}s.mp3"
