from transformers import AutoTokenizer, AutoModel
import torch


class GlmModel:
    def __init__(self, model_name='THUDM/chatglm-6b-int4'):
        self.model_name = model_name
        if torch.cuda.is_available():
            self.device = "cuda"
        else:
            self.device = "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name, trust_remote_code=True)
        self.model = AutoModel.from_pretrained(
            self.model_name, trust_remote_code=True)
        self.max_length = 4096
        if self.device == 'cuda':
            self.model = self.model.half().cuda()
        else:
            self.model = self.model.cpu().float()
        self.test()

    def test(self):
        print(f"This is from {self.model_name} test. \nUsing " + self.device)

    def evaluate(self, message, history=[], temperature=0.9):
        response, history = self.model.chat(
            self.tokenizer, message, history=history, max_length=self.max_length, temperature=temperature)
        print(f"In class {self.model_name}, temperature = {temperature}")
        return response, history


class Glm6bModel(GlmModel):
    def __init__(self):
        super(Glm6bModel, self).__init__(model_name='THUDM/chatglm-6b')


class Glm6bInt4Model(GlmModel):
    def __init__(self):
        super(Glm6bModel, self).__init__(model_name='THUDM/chatglm-6b-int4')


class Glm6bV2Model(GlmModel):
    def __init__(self):
        super(Glm6bModel, self).__init__(model_name='THUDM/chatglm2-6b')

      
class Glm6bV2Int4Model(GlmModel):
    def __init__(self):
        super(Glm6bModel, self).__init__(model_name='THUDM/chatglm2-6b-int4')
