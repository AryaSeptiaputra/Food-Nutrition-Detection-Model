import json
from langchain.docstore.document import Document

class LoadData:
    def __init__(self, path):
        self.path = path

    def load(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        docs = []
        for item in data:
            metadata = {
                "code": item["code"],
                "text": item["text"]
            }
            docs.append(Document(page_content=item["name"], metadata=metadata))
        return docs
