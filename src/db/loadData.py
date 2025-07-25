import json

class LoadData:
    def __init__(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def get_texts_and_embeddings(self):
        # Extract texts and their corresponding embeddings
        texts = [item["Text"] for item in self.data]
        embeddings = [item["name_embedding"] for item in self.data]
        return texts, embeddings

