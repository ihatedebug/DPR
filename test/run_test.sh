python -m pyserini.search \
    --topics /data1/jongho/sigir/test/english_queries_dev_sample.tsv \
    --index indexes/english_collection \
    --output runs/run.english_dev_test.txt \
    --bm25 \
    --hits 4 \
    --threads 12