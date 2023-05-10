from transformers import GenerationConfig, LlamaForCausalLM, LlamaTokenizer, AutoTokenizer, AutoModel
import torch
import sys
from pathlib import Path
import os


class Glm6bModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            "THUDM/chatglm-6b", trust_remote_code=True)
        self.model = AutoModel.from_pretrained(
            "THUDM/chatglm-6b", trust_remote_code=True).half().cuda()
        self.test()


    def test(self):
        return "This is from Glm6bModel test."


    def evaluate(self, message, history):
        response, history = self.model.chat(
            self.tokenizer, message, history=history)
        return response, history


class Glm6bInt4Model:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            "THUDM/chatglm-6b-int4", trust_remote_code=True)
        self.model = AutoModel.from_pretrained(
            "THUDM/chatglm-6b-int4", trust_remote_code=True).half().cuda()
        self.test()


    def test(self):
        return "This is from Glm6bInt4Model test."


    def evaluate(self, message, history):
        response, history = self.model.chat(
            self.tokenizer, message, history=history)
        return response, history