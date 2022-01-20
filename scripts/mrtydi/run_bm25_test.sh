python -m pyserini.search \
    --topics /data1/jongho/sigir/data/mrtydi-v1.0-korean/topic.test.tsv \
    --index indexes/lucene.mrtydi-v1.0-korean \
    --output runs/run.mrtydi_ko_test.txt \
    --batch-size 36 --threads 12 \
    --bm25 \
    --hits 100 \
    --k1 0.9 \
    --b 0.4 \
    --language ko