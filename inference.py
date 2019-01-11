import numpy as np

from commons import encode, get_loaded_model
from settings import embeddings_file
from utils import load_embeddings

embeddings = load_embeddings(embeddings_file)
model = get_loaded_model()


def find_best_match(text):
    best_cosine = 0
    best_match = None

    query_embedding = encode(model, text)

    for item in embeddings:
        cosine_sim = np.dot(query_embedding, item['embedding'])

        if best_cosine < cosine_sim:
            best_cosine = cosine_sim
            best_match = item

    return {'cos_sim': best_cosine, 'best_match': best_match['answers']}
