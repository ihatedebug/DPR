python make_dpr_dataset_refactored.py --collection_path "/data1/jongho/sigir/data/mrtydi-v1.0-korean/collection/docs.jsonl.gz" \
    --queries_path "/data1/jongho/sigir/data/mrtydi-v1.0-korean/topic.test.tsv" \
    --filepath "/data1/jongho/sigir/data/mrtydi-v1.0-korean/qrels.test.json"  \
    --bm25_path "/data1/jongho/sigir/runs/run.mrtydi_ko_test.txt" \
    --output_path "output/dpr-mrtydi-test.json" \
    --task mrtydi \
    --n_negatives 30 \
    --n_hard_negatives 30