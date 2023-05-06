from transformers import GenerationConfig, LlamaForCausalLM, LlamaTokenizer
from peft import PeftModel
import torch
import sys
from pathlib import Path
import os

class LlamaModel:
    def __init__(self, load_8bit: bool = False,
                base_model: str = "decapoda-research/llama-7b-hf",
                lora_weights: str = "training_results/therapy_6420_try_1",
                verbose: bool = True,):
        self.base_model = base_model or os.environ.get("BASE_MODEL", "")
        self.tokenizer = LlamaTokenizer.from_pretrained(base_model)
        self.model = self.get_model(
            load_8bit, base_model, lora_weights, self.tokenizer)

    def get_model(self, load_8bit: bool = False, base_model: str = '', lora_weights: str = '', tokenizer=None):
        model = LlamaForCausalLM.from_pretrained(
            base_model,
            load_in_8bit=load_8bit,
            torch_dtype=torch.float16,
            device_map="auto",
        )
        model = PeftModel.from_pretrained(
            model,
            lora_weights,
            torch_dtype=torch.float16,
        )
        # unwind broken decapoda-research config
        model.config.pad_token_id = tokenizer.pad_token_id = 0  # unk
        model.config.bos_token_id = 1
        model.config.eos_token_id = 2

        if not load_8bit:
            model.half()  # seems to fix bugs for some users.
        model.eval()
        if torch.__version__ >= "2" and sys.platform != "win32":
            model = torch.compile(model)
        return model
    
    def test(self):
        return "hahaha"

    def evaluate(self,
                 prompt='',
                 temperature=0.1,
                 top_p=0.75,
                 top_k=40,
                 num_beams=4,
                 max_new_tokens=128,
                 **kwargs,
                 ):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        input_ids = inputs["input_ids"].to('cuda')
        generation_config = GenerationConfig(
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            num_beams=num_beams,
            **kwargs,
        )

        generate_params = {
            "input_ids": input_ids,
            "generation_config": generation_config,
            "return_dict_in_generate": True,
            "output_scores": True,
            "max_new_tokens": max_new_tokens,
        }

        with torch.no_grad():
            generation_output = self.model.generate(
                input_ids=input_ids,
                generation_config=generation_config,
                return_dict_in_generate=True,
                output_scores=True,
                max_new_tokens=max_new_tokens,
            )
        s = generation_output.sequences[0]
        output = self.tokenizer.decode(s)
        return output