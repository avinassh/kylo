wget -cq https://github.com/facebookresearch/InferSent/archive/master.zip -O infersent-master.zip
unzip -qq infersent-master.zip
rm infersent-master.zip
mv InferSent-master infersent

wget -cq https://s3.amazonaws.com/senteval/infersent/infersent1.pkl -O infersent/encoder/infersent1.pkl
wget -cq https://s3.amazonaws.com/senteval/infersent/infersent2.pkl -O infersent/encoder/infersent2.pkl

mkdir -p infersent/dataset/GloVe
wget -cq http://nlp.stanford.edu/data/glove.840B.300d.zip -O infersent/dataset/GloVe/glove.840B.300d.zip
unzip -qq infersent/dataset/GloVe/glove.840B.300d.zip -d infersent/dataset/GloVe/

mkdir -p infersent/dataset/fastText
wget -cq https://s3-us-west-1.amazonaws.com/fasttext-vectors/crawl-300d-2M.vec.zip -O infersent/dataset/fastText/crawl-300d-2M.vec.zip
unzip -qq infersent/dataset/fastText/crawl-300d-2M.vec.zip -d infersent/dataset/fastText/

python -m nltk.downloader -d /usr/local/share/nltk_data punkt

mkdir -p embeddings
