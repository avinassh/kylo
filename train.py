import os
import json

from settings import data_dir, embeddings_file
from commons import encode, get_loaded_model
from utils import save_embeddings

# initial data is of the form
# [
#   {
#       "questions": [" "],
#       "answers": [" "],
#   },
# ]
# which we will convert to
# [
#   {
#       "question": "",
#       "answers": [" "],
#   },
# ]
# trained data will be of the form
# [
#   {
#       "embedding": tensor,
#       "answers": [" "],
#   },
# ]


def get_data():
    initial_data = []
    for file in os.listdir(data_dir):
        if file.endswith('.json'):
            with open(os.path.join(data_dir, file)) as f:
                try:
                    initial_data.extend(json.load(f))
                except json.JSONDecodeError as e:
                    print('invalid json file: ', os.path.join(data_dir, file))
                    raise e

    all_questions = []
    for qa_pair in initial_data:
        answers = qa_pair['answer']
        for question in qa_pair['question']:
            all_questions.append({'question': question, 'answers': answers})
    return all_questions


def get_embeddings(model, data):
    embeddings = []
    for qa_pair in data:
        embedding = encode(model=model, text=qa_pair['question'])
        embeddings.append(
            {'embedding': embedding, 'answers': qa_pair['answers']})
    return embeddings


def train():
    model = get_loaded_model(force_gpu=True)
    embeddings = get_embeddings(model=model, data=get_data())
    save_embeddings(embeddings, embeddings_file)


if __name__ == '__main__':
    train()
