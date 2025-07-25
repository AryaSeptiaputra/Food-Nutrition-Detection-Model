import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

class TextEncoder:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def encode(self, texts):
        """
        Encodes a list of texts into their corresponding embeddings.

        :param texts: List of strings to be encoded.
        :return: List of embeddings corresponding to the input texts.
        """
        return self.model.encode(texts, convert_to_tensor=True)


df = pd.read_csv(r'C:\Intrenship\Torhe Indonesia\Food Nutrition Detection\data\processed\Food_Dataset.csv', delimiter='|')

# Initialize the TextEncoder and encode the 'name' column
encoder = TextEncoder()
embeddings = encoder.encode(df['name'].tolist())

# Convert embeddings to a list and add to DataFrame
df['name_embedding'] = [emb.numpy().tolist() for emb in embeddings]

df = df[['code','Text', 'name_embedding']]

df.to_json(r'C:\Intrenship\Torhe Indonesia\Food Nutrition Detection\data\processed\Food_embeddings.json', orient='records', indent=2)
