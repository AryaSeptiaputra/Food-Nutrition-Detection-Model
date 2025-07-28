class Retriever:
    def __init__(self, vectorstore):
        self.vectorstore = vectorstore

    def retrieve(self, query, k=10, threshold=0.8):
        results = self.vectorstore.similarity_search_with_score(query, k=k)
        filtered = [doc for doc, score in results if score >= threshold]
        return filtered
