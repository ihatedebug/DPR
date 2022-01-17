python -m pyserini.search \
    --topics /data1/jongho/sigir/data/french_queries.train.tsv \
    --index indexes/french_collection \
    --output runs/run.french_train_new.txt \
    --language fr \
    --threads 24\
    --bm25 \
    --hits 20
