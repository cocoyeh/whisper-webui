# Whisper 簡單示範 - https://github.com/openai/whisper

import logging
import traceback

import gradio as gr
import torch
import whisper

logging.basicConfig(filename='whisper_app.log', level=logging.INFO)

USE_GPU = True if torch.cuda.is_available() else False
use_fp16 = True if USE_GPU else False
DEVICE = "cuda" if USE_GPU else "cpu"


def launch():
    options = ["tiny", "base", "small", "medium", "large"]
    interface = gr.Interface(
        fn=transcribe,
        inputs=["file", gr.Dropdown(choices=options, value="base")],
        outputs=["textbox"],
        title="Whisper 簡單示範",
        description="上傳音訊檔案 - 聽打",
    )
    interface.launch(server_name="0.0.0.0", share=True, debug=True,
                     show_error=True)  # Make it accessible outside the container


def transcribe(name, model_size):
    try:
        model = whisper.load_model(model_size, device=DEVICE)
        result = model.transcribe(name, fp16=use_fp16)
        logging.info(result)
        return result["text"]
    except:
        traceback.print_exc()
        return "自動語音辨識發生錯誤"


if __name__ == "__main__":
    try:
        # demo.launch(server_name="0.0.0.0", share=True, debug=True, show_error=True)
        launch()
    except Exception as e:
        print(e)
