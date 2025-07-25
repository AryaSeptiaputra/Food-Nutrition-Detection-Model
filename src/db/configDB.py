from langchain_chroma import Chroma

class ConfigDB:
    def __init__(self, texts, embeddings, persist_directory="src/db/chroma_db"):
        """
        Create and automatically persist a Chroma vector store.

        :param texts: List of texts to store (e.g., food names)
        :param embeddings: List of embeddings corresponding to the texts
        :param persist_directory: Path to directory where Chroma DB will be saved
        """
        self.vectorstore = Chroma(
            collection_name="food_embeddings",
            embedding_function=None, 
            persist_directory=persist_directory
        )

        # Add data to Chroma with manual embedding input
        self.vectorstore._collection.add(
            documents=texts,
            embeddings=embeddings,
            ids=[str(i) for i in range(len(texts))]
        )

    def get_vectorstore(self):
        """
        Returns the vectorstore instance.
        """
        return self.vectorstore
