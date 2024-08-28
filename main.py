from tts.generate import generate_input
from llm.untils import model_to_llm, chat
from pathlib import Path
from dotenv import load_dotenv
from scipy.io import wavfile
from rvc.modules.vc.modules import VC

model = 'qwen2:7b'
llm = model_to_llm(model)
question = "你最讨厌什么东西"

text = chat(llm, question)
file_input = "./input/1.wav"
generate_input(text, file_input, False)

load_dotenv()
      
vc = VC()
vc.get_vc("tuopa&zhangzhang.pth")
tgt_sr, audio_opt, times, _ = vc.vc_inference(
    sid=1,
    input_audio_path=Path(file_input),
    f0_up_key=1
)
wavfile.write("./output/1.wav", tgt_sr, audio_opt)