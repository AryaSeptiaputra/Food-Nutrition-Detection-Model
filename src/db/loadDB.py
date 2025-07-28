from langchain_community.vectorstores import Chroma
from src.features.textEncoder import TextEncoder

class LoadDB:
    def __init__(self, collection_name="knowladge food", persist_dir="./knowlagde_food"):
        self.embedding_function = TextEncoder().get_encoder()
        self.db = Chroma(
            collection_name=collection_name,
            embedding_function=self.embedding_function,
            persist_directory=persist_dir
        )

    def get_db(self):
        return self.db
