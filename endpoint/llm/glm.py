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
        self.max_length = 4096
        if self.device == 'cuda':
            self.model = self.model.half().cuda()
        else:
            self.model = self.model.cpu().float()
        self.test()


    def test(self):
        print("This is from Glm6bModel test. Using " + self.device)


    def evaluate(self, message, history = [], temperature=0.9):
        response, history = self.model.chat(
            self.tokenizer, message, history=history, max_length=self.max_length, temperature=temperature)
        print(f"In class GLM, temperature = {temperature}")
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
        self.max_length = 4096
        if self.device == 'cuda':
            self.model = self.model.half().cuda()
        else:
            self.model = self.model.cpu().float()
        self.test()


    def test(self):
        print("This is from Glm6bInt4Model test. Using " + self.device)


    def evaluate(self, message, history = [], temperature=0.9):
        response, history = self.model.chat(
            self.tokenizer, message, history=history, max_length=self.max_length, temperature=temperature)
        print(f"In class GLM, temperature = {temperature}")
        return response, history