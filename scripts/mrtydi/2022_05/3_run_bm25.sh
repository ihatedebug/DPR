
# langs=('bengali'  'russian'  'korean'  'swahili'  'telugu' 'japanese'  'arabic')
# lang_abbrs=('bn'  'ru'  'ko'  'te'  'ja'  'ar')
# set_names=('train'  'dev')
# #lang=arabic     # one of {'arabic'  'bengali'  'english'  'finnish'  'indonesian'  'japanese'  'korean'  'russian'  'swahili'  'telugu'  'thai'}
# #lang_abbr=ar    # one of {'ar'  'bn'  'en'  'fi'  'id'  'ja'  'ko'  'ru'  'sw'  'te'  'th'}
# #set_name=test   # one of {'train'  'dev'  'test'}

# for i in ${!lang[@]}; do
#     lang=${langs[$i]}
#     lang_addr=${lang_addrs[$i]}
#     for set_name in ${set_names[@]}; do
#         runfile=runs/run.bm25.mrtydi-v1.1-${lang}.${set_name}.txt
#         python -m pyserini.search --bm25 \
#             --language ${lang_abbr} \
#             --topics mrtydi-v1.1-${lang}-${set_name} \
#             --index mrtydi-v1.1-${lang} \
#             --output ${runfile}
#     done;
# done;

# why syntax error


lang=bengali     # one of {'arabic', 'bengali', 'english', 'finnish', 'indonesian', 'japanese', 'korean', 'russian', 'swahili', 'telugu', 'thai'}
lang_abbr=bn    # one of {'ar', 'bn', 'en', 'fi', 'id', 'ja', 'ko', 'ru', 'sw', 'te', 'th'}
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

set_name=dev
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

