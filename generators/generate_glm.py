import fire
import gradio as gr
import torch
from endpoint.llm.glm import Glm6bModel, Glm6bInt4Model


def main(
    model_name: str = 'Glm6bModel',
    # Allows to listen on all interfaces by providing '0.
    server_name: str = "0.0.0.0",
    share_gradio: bool = True,
    verbose: bool = True,
):
    my_model = None
    if model_name=='Glm6bModel':
        my_model=Glm6bModel()
    if model_name=='Glm6bInt4Model':
        my_model=Glm6bInt4Model()

    def evaluate(message='', chat_history=[], temperature=0.1, **kwargs):
        print(message, chat_history, temperature)
        response, history = my_model.evaluate(message, chat_history, temperature=temperature)
        print(response)
        return '', history

    with gr.Blocks() as demo:
        gr.Markdown(
        """
        # 来来来
        """)
        chatbot = gr.Chatbot()
        msg = gr.Textbox()
        clear = gr.Button("Clear")
        temperature = gr.components.Slider(
            minimum=0, maximum=1, value=0.1, label="Temperature"
        ),

        msg.submit(evaluate, [msg, chatbot, temperature], [msg, chatbot])
        clear.click(lambda: None, None, chatbot, queue=False)

    demo.launch(server_name=server_name, share=share_gradio)


if __name__ == "__main__":
    fire.Fire(main)
