import os
import sys
import fire
import gradio as gr
import torch
from peft import PeftModel
from transformers import GenerationConfig, LlamaForCausalLM, LlamaTokenizer
from utils.prompter import Prompter
import time
from endpoint.llm.glm import GlmModel


if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"


def main(
    load_8bit: bool = False,
    # Allows to listen on all interfaces by providing '0.
    server_name: str = "0.0.0.0",
    share_gradio: bool = True,
    verbose: bool = True,
):
    my_model = GlmModel()

    def evaluate(message='', chat_history=[], **kwargs):
        response, history = my_model.evaluate(message, chat_history)
        return response, history

    with gr.Blocks() as demo:
        chatbot = gr.Chatbot()
        msg = gr.Textbox(value='Patient: ')
        clear = gr.Button("Clear")

        msg.submit(evaluate, [msg, chatbot, ], [msg, chatbot, ])
        clear.click(lambda: None, None, chatbot, queue=False)

    demo.launch(server_name=server_name, share=share_gradio)


if __name__ == "__main__":
    fire.Fire(main)
