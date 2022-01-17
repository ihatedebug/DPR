# Multilingual marco dataset preprocessing for DPR
- quetion: fr, docs: en
- BM25는 **English query** to **English documents** 로 계산
- hard negative ctxs는 question 당 3~4개
- about 400GB..
```
python prepare_bm25.py
./scripts/index_bm25_en.sh
./scripts/index_bm25_en_dev.sh
./scripts/index_bm25_en_train.sh
python make_dpr_dataset.py
```
## issues
- [ ] pyserini로 BM25 계산 시 train queries(808731개) 중 920개, dev queries(59273개) 중 3개 Query에 대해서는 계산이 안됨
- [ ] 한 query가 여러 doc을 positive로 갖는 경우 고려하지 않음. 