import pickle


def save_embeddings(contents, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(contents, f)


def load_embeddings(file_path):
    with open(file_path, 'rb') as f:
        embeddings = pickle.load(f)
    return embeddings
