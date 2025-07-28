from src.features.textEncoder import TextEncoder
from src.db.loadData import LoadData
from src.db.configDB import ConfigDB

def init_chroma_db():
    loader = LoadData(r"data\processed\food_knowledge_english.json")
    documents = loader.load()

    encoder = TextEncoder()
    embedding = encoder.get_encoder()

    vectordb = ConfigDB(embedding_function=embedding)
    vectordb.add_documents(documents)

if __name__ == "__main__":
    init_chroma_db()
