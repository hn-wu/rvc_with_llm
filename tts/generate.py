import asyncio
import edge_tts

def generate_input(text, input_file, gender=True):
    if gender:
        VOICE = "zh-CN-YunyangNeural"
    else:
        VOICE = "zh-CN-XiaoyiNeural"
    async def amain() -> None:
        communicate = edge_tts.Communicate(text, VOICE)
        await communicate.save(input_file)

    loop = asyncio.get_event_loop_policy().get_event_loop()
    try:
        loop.run_until_complete(amain())
    finally:
        loop.close()