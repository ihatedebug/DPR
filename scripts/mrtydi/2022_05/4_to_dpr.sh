lang=bengali     # one of {'arabic', 'bengali', 'english', 'finnish', 'indonesian', 'japanese', 'korean', 'russian', 'swahili', 'telugu', 'thai'}
set_name=train   # one of {'train', 'dev', 'test'}

python make_dpr_dataset_refactored.py --collection_path "/data1/jongho/sigir/data/mrtydi_dataset/mrtydi-v1.0-${lang}/collection/docs.jsonl.gz" \
    --queries_path "/data1/jongho/sigir/data/mrtydi_dataset/mrtydi-v1.0-${lang}/topic.${set_name}.tsv" \
    --filepath "/data1/jongho/sigir/data/mrtydi_dataset/mrtydi-v1.0-${lang}/qrels.${set_name}.json"  \
    --bm25_path "runs/run.bm25.mrtydi-v1.0-${lang}.${set_name}.txt" \
    --output_path "output/mrtydi/dpr-mrtydi-${lang}.${set_name}.json" \
    --task mrtydi \
    --n_negatives 30 \
    --n_hard_negatives 30

lang=bengali     # one of {'arabic', 'bengali', 'english', 'finnish', 'indonesian', 'japanese', 'korean', 'russian', 'swahili', 'telugu', 'thai'}
set_name=dev   # one of {'train', 'dev', 'test'}

python make_dpr_dataset_refactored.py --collection_path "/data1/jongho/sigir/data/mrtydi_dataset/mrtydi-v1.0-${lang}/collection/docs.jsonl.gz" \
    --queries_path "/data1/jongho/sigir/data/mrtydi_dataset/mrtydi-v1.0-${lang}/topic.${set_name}.tsv" \
    --filepath "/data1/jongho/sigir/data/mrtydi_dataset/mrtydi-v1.0-${lang}/qrels.${set_name}.json"  \
    --bm25_path "runs/run.bm25.mrtydi-v1.0-${lang}.${set_name}.txt" \
    --output_path "output/mrtydi/dpr-mrtydi-${lang}.${set_name}.json" \
    --task mrtydi \
    --n_negatives 30 \
    --n_hard_negatives 30