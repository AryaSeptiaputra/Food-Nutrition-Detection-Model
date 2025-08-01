import os
from llama_cpp import Llama

class LanguageModel:
    def __init__(self):
        # Path ke model .gguf
        with open("config.txt", "r") as f:
            model_path = f.read().strip()

        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model tidak ditemukan di: {model_path}")

        # Inisialisasi model
        self.model = Llama(
            model_path=model_path,
            n_ctx=4096,            # Panjang konteks
            n_threads=16,          # Jumlah thread CPU
            n_gpu_layers=4         # Gunakan 0 jika hanya ingin CPU
        )

    def generate(self, user_prompt: str, sistem: str) -> str:
        response = self.model.create_chat_completion(
            messages=[
                {"role": "system", "content": sistem},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=512,
            temperature=0.7,
            top_p=0.95,
        )
        return response["choices"][0]["message"]["content"].strip()
