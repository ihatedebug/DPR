lang=japanese     # one of {'arabic', 'bengali', 'english', 'finnish', 'indonesian', 'japanese', 'korean', 'russian', 'swahili', 'telugu', 'thai'}
lang_abbr=ja   # one of {'ar', 'bn', 'en', 'fi', 'id', 'ja', 'ko', 'ru', 'sw', 'te', 'th'}
set_name=train   # one of {'train', 'dev', 'test'}
runfile=runs/run.bm25.mrtydi-v1.0-${lang}.${set_name}.txt

python -m pyserini.search --bm25 \
    --language ${lang_abbr} \
    --topics /data1/jongho/sigir/data/mrtydi_dataset/mrtydi-v1.0-${lang}/topic.${set_name}.tsv \
    --index /data1/jongho/sigir/data/mrtydi_bm25_index/lucene.mrtydi-v1.0-${lang} \
    --output ${runfile} \
    --batch-size 36 --threads 12 \
    --bm25 \
    --hits 100 \
    --k1 0.9 \
    --b 0.4 \

set_name=dev   # one of {'train', 'dev', 'test'}
runfile=runs/run.bm25.mrtydi-v1.0-${lang}.${set_name}.txt

python -m pyserini.search --bm25 \
    --language ${lang_abbr} \
    --topics /data1/jongho/sigir/data/mrtydi_dataset/mrtydi-v1.0-${lang}/topic.${set_name}.tsv \
    --index /data1/jongho/sigir/data/mrtydi_bm25_index/lucene.mrtydi-v1.0-${lang} \
    --output ${runfile} \
    --batch-size 36 --threads 12 \
    --bm25 \
    --hits 100 \
    --k1 0.9 \
    --b 0.4 \