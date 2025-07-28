from langchain_community.embeddings import SentenceTransformerEmbeddings

class TextEncoder:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.encoder = SentenceTransformerEmbeddings(model_name=model_name)

    def get_encoder(self):
        return self.encoder
