import sys

import numpy as np
import torch

from settings import model_version


# monkey patch the path to infersent
if 'infersent' not in sys.path:
    sys.path.insert(0, 'infersent')

from models import InferSent  ## noqa


class GPUNotFoundException(Exception):
    pass


def get_loaded_model(force_gpu=False, k_most_frequent_words=1000000):

    model_path = "infersent/encoder/infersent{}.pkl".format(model_version)
    params_model = {'bsize': 64, 'word_emb_dim': 300, 'enc_lstm_dim': 2048,
                    'pool_type': 'max', 'dpout_model': 0.0,
                    'version': model_version}

    model = InferSent(params_model)
    model.load_state_dict(torch.load(model_path))

    if (not torch.cuda.is_available()) and force_gpu:
        raise GPUNotFoundException()

    if torch.cuda.is_available():
        model = model.cuda()

    # If infersent1 -> use GloVe embeddings.
    # If infersent2 -> use InferSent embeddings.
    W2V_PATH = 'infersent/dataset/GloVe/glove.840B.300d.txt' if model_version == 1 else 'infersent/dataset/fastText/crawl-300d-2M.vec'  ## noqa
    model.set_w2v_path(W2V_PATH)

    # Load embeddings of K most frequent words
    model.build_vocab_k_words(K=k_most_frequent_words)
    return model


def encode(model, text):
    embedding = model.encode([text])[0]
    embedding /= np.linalg.norm(embedding)
    return embedding
