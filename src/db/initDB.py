from loadData import LoadData
from configDB import ConfigDB

loader = LoadData("C:\Intrenship\Torhe Indonesia\Food Nutrition Detection\data\processed\Food_embeddings.json")
texts, embeddings = loader.get_texts_and_embeddings()

db = ConfigDB(texts, embeddings)
vectorstore = db.get_vectorstore()
