import pandas as pd
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

# --- Encoding ---
encoder = TextEncoder()
embeddings = encoder.encode(df['name'].tolist())  # Kolom teks yang ingin diencode

# --- Masukkan ke DataFrame ---
# Convert tensor to numpy, lalu ke list agar bisa masuk ke DataFrame/JSON/Postgres

df['name embedding'] = [emb.numpy().tolist() for emb in embeddings]

# --- Simpan ke file (opsional) ---
df.to_json(r'C:\Intrenship\Torhe Indonesia\Food Nutrition Detection\data\processed\Food_Dataset_with_embeddings.json', orient='records', lines=True)
