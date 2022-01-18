# Multilingual marco dataset preprocessing for DPR
- quetion: fr, docs: en
- BM25는 **English query** to **English documents** 로 계산
- hard negative ctxs는 question 당 3~4개
- train triples (question, positive, negative) 에서 question 기준으로 중복되는 데이터 합침. 따라서 1 question : n positive docs
- train dataset 기존 39780811 개에서 
- train# : 913mb, 398374 
- dev#: 526mb, 55578 
```
python prepare_bm25.py
./scripts/index_bm25_en.sh
./scripts/index_bm25_en_dev.sh
./scripts/index_bm25_en_train.sh
python revise_id_file.py
python make_dpr_dataset_new.py
```
## issues
- [ ] pyserini로 BM25 계산 시 train queries(808731개) 중 920개, dev queries(59273개) 중 3개 Query에 대해서는 계산이 안됨
- [ ] ~~한 query가 여러 doc을 positive로 갖는 경우 고려하지 않음.~~ -> 고려하는 것으로 수정. train dataset에서 overlap되는 query들을 하나로 합침
- [ ] DPR dataset과 차이: answer, title 없음
- [ ] qrels.dev.tsv 와 qrels.dev.small.tsv 중 전자 사용

## random sampling
- train queries # words: 2,662,841
- preferred # words : 130,000 ~ 1,300,000
- Let's sample 10%
- After sampling, train queries # words: 266294
