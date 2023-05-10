from transformers import GenerationConfig, LlamaForCausalLM, LlamaTokenizer, AutoTokenizer, AutoModel
import torch
import sys
from pathlib import Path
import os


class GlmModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            "THUDM/chatglm-6b-int4", trust_remote_code=True)
        self.model = AutoModel.from_pretrained(
            "THUDM/chatglm-6b-int4", trust_remote_code=True).half().cuda()


    def test(self):
        return "This is from glm test."


    def evaluate(self, message, history):
        response, history = self.model.chat(
            self.tokenizer, message, history=history)
        return response, history
