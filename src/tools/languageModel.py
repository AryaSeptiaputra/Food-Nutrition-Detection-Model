import os
from dotenv import load_dotenv
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

load_dotenv()  # Load .env

class LanguageModel:
    def __init__(self):
        model_id = "meta-llama/Llama-3.1-70B-Instruct"

        access_token = os.getenv("HF_TOKEN")
        if access_token is None:
            raise EnvironmentError("Hugging Face token tidak ditemukan di environment variable 'HF_TOKEN'.")

        # Load tokenizer & model
        self.tokenizer = AutoTokenizer.from_pretrained(model_id, token=access_token, use_fast=True)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            token=access_token,
            device_map="auto",
            torch_dtype="auto"  # Bisa diubah ke torch.float16 jika perlu
        )

        # Build huggingface pipeline
        self.pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_new_tokens=512,
            do_sample=True,
            temperature=0.7,
            top_p=0.95,
            repetition_penalty=1.1,
            eos_token_id=self.tokenizer.eos_token_id,
            pad_token_id=self.tokenizer.eos_token_id  # Hindari warning jika model tidak punya pad token
        )

    def format_prompt(self, user_prompt: str):
        return f"<|begin_of_text|><|user|>\n{user_prompt}<|end|>\n<|assistant|>\n"

    def generate(self, prompt: str):
        formatted_prompt = self.format_prompt(prompt)
        result = self.pipe(formatted_prompt, return_full_text=False)[0]["generated_text"]
        return result.strip()
