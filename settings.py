import os

model_version = 1
k_most_frequent_words = 1000000
data_dir = 'data'
embeddings_dir = 'embeddings'
embeddings_file = os.path.join(
    embeddings_dir, "data{}.dat".format(model_version))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(PROJECT_DIR, 'frontend/dist')
