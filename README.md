# Kylo - The FAQ Bot

## How does it work?

Using Facebook's Infersent model we create sentence embeddings of the existing data. When a new text is queried, we  calculate the cosine distance between the the query text and the existing embeddings. The highest value is considered as a match and returned as the answer.


## Infersent

InferSent is a sentence embeddings method that provides semantic representations for English sentences. It is trained on natural language inference data and generalizes well to many different tasks.

Read the original paper - [arxiv](https://arxiv.org/abs/1705.02364).


## Setup

Make sure you have Python 3. Install the Python requirements:

    pip install -r requirements.txt


run `setup.sh` to get the Infersent model and also all the word vectors. This project uses GloVe:

    ./setup.sh


## Training


For training, add any new data in `data/` directory. Check [data/README.md](data/README.md) for format instructions. Then run the training to save the embeddings in `embeddings/` dir:

    python train.py


## Inference

To check, import `find_best_match` from `inference`:

```
from inference import find_best_match

print(find_best_match(text="are you open source"))
```


## Server Deployment

This repository comes with a Tornado API server, with REST API and a websocket end point. To run the server:

    python server.py


## Todo

Check [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

- Build a dataset to evaluate accuracy
- Evaluate GLoVe vs FastText
- Work on improving accuracy
- Handle common typos


## Name

![](https://camo.githubusercontent.com/3f61269fca449896725df6a5e801783e9f4781df/68747470733a2f2f69352e77616c6d617274696d616765732e636f6d2f6173722f61396561386231652d636331662d343566302d386131382d3035356163653430663061625f312e33333237343863643164636438623436633239326135613633333339333837392e6a7065673f6f646e4865696768743d343530266f646e57696474683d343530266f646e42673d464646464646)

## License

The mighty MIT license. Check `LICENSE` for more details.
