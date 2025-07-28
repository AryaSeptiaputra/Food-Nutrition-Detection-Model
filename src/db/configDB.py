from langchain_community.vectorstores import Chroma

class ConfigDB:
    def __init__(self, collection_name="knowledge_food", persist_dir="./src/db/food_knowledge_english", embedding_function=None):
        self.db = Chroma(
            collection_name=collection_name,
            embedding_function=embedding_function,
            persist_directory=persist_dir
        )

    def get_db(self):
        return self.db

    def add_documents(self, documents):
        self.db.add_documents(documents)

