python make_dpr_dataset_refactored.py --collection_path "/data1/jongho/sigir/data/english_collection.tsv" \
    --queries_path "/data1/jongho/sigir/data/french_queries.train.tsv" \
    --filepath "/data1/jongho/sigir/data/triples.train.ids.small.json"  \
    --bm25_path "runs/run.english_train.txt" \
    --output_path "output/dpr-mmarco-fren-train.json" --train