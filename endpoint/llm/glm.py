from transformers import AutoTokenizer, AutoModel
import torch

class Glm6bModel:
    def __init__(self):
        if torch.cuda.is_available():
            self.device = "cuda"
        else:
            self.device = "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(
            "THUDM/chatglm-6b", trust_remote_code=True)
        self.model = AutoModel.from_pretrained(
            "THUDM/chatglm-6b", trust_remote_code=True)
        if self.device == 'cude':
            self.model = self.model.half().cuda()
        else:
            self.model = self.model.cpu().float()
        self.test()


    def test(self):
        return "This is from Glm6bModel test."


    def evaluate(self, message, history):
        response, history = self.model.chat(
            self.tokenizer, message, history=history)
        return response, history


class Glm6bInt4Model:
    def __init__(self):
        if torch.cuda.is_available():
            self.device = "cuda"
        else:
            self.device = "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(
            "THUDM/chatglm-6b-int4", trust_remote_code=True)
        self.model = AutoModel.from_pretrained(
            "THUDM/chatglm-6b-int4", trust_remote_code=True)
        if self.device == 'cude':
            print("444444444444444444444444444444444444", self.device)
            self.model = self.model.half().cuda()
        else:
            self.model = self.model.cpu().float()
        self.test()


    def test(self):
        return "This is from Glm6bInt4Model test."


    def evaluate(self, message, history):
        response, history = self.model.chat(
            self.tokenizer, message, history=history)
        return response, history