# A simple gradio UI to provide whisper, https://github.com/openai/whisper powered transcribe

import gradio as gr
import torch
import whisper

# INITIALIZE ENVIRONMENT
USE_GPU = True if torch.cuda.is_available() else False
use_fp16 = True if USE_GPU else False
DEVICE = "cuda" if USE_GPU else "cpu"


def launch():
    options = ["base", "small", "medium", "large"]
    interface = gr.Interface(
        fn=transcribe,  # The function to run
        inputs=["file", gr.Dropdown(options)],
        outputs=["textbox"],
        title="Whisper 簡單示範",
        description="上傳音訊檔案 - 聽打",
    )
    interface.launch(server_name="0.0.0.0", share=False)  # Make it accessible outside the container


def transcribe(file, choice):
    model = whisper.load_model(choice, device=DEVICE)
    try:
        result = model.transcribe(file, fp16=use_fp16)
        return result["text"]
    except:
        return ""


if __name__ == '__main__':
    launch()
