python -m pyserini.search \
    --topics /data1/jongho/sigir/data/english_queries.train.tsv \
    --index indexes/english_collection \
    --output runs/run.english_train.txt \
    --batch-size 36 --threads 12 \
    --bm25 \
    --hits 4
    