
# Multilingual marco dataset preprocessing for DPR
- quetion: fr, docs: en
- BM25는 **English query** to **English documents** 로 계산
- hard negative ctxs는 question 당 3~4개
- train triples (question, positive, negative) 에서 question 기준으로 중복되는 데이터 합침. 따라서 1 question : n positive docs
- train dataset 기존 39780811 개에서 
- train# : 913mb, 398787
- dev#: 526mb, 55578 
```
python prepare_bm25.py
./scripts/index_bm25_en.sh
./scripts/index_bm25_en_dev.sh
./scripts/index_bm25_en_train.sh
python revise_id_file.py
and use scripts in scripts/make_dpr/
+ python count_words.py # random sampling if needed
```
## issues
- [ ] pyserini로 BM25 계산 시 train queries(808731개) 중 920개, dev queries(59273개) 중 3개 Query에 대해서는 계산이 안됨
- [ ] ~~한 query가 여러 doc을 positive로 갖는 경우 고려하지 않음.~~ -> 고려하는 것으로 수정. train dataset에서 overlap되는 query들을 하나로 합침
- [ ] DPR dataset과 차이: answer, title 없음
- [ ] qrels.dev.tsv 와 qrels.dev.small.tsv 중 전자 사용

## random sampling
- train queries # words: 2,664,110 (fr) 2,377,466 (en)
- preferred # words : 130,000 ~ 1,300,000
- Let's sample 10%
- After sampling, train queries # words: 266632 (fr), 237597 (en)

# mrtydi dataset for DPR (2022.02)
- dev: query 1개 손실 (pyserini BM25 error)
- before use, run `revise_id_file.py`
- scripts in `./scripts/mrtydi` 

## mrtydi dataset for DPR (2022.05)
- https://github.com/castorini/mr.tydi#download dataset과 pre-built BM25 index 다운로드
- bm25 v1.1 issue -> use v1.1
```
git clone git@github.com:castorini/pyserini.git --recurse-submodules
Cloning into 'pyserini'...
The authenticity of host 'github.com (15.164.81.167)' can't be established.
ECDSA key fingerprint is SHA256:p2QAMXNIC1TJYWeIOttrVc98/R1BUFWu3/LiyKgUfQM.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com,15.164.81.167' (ECDSA) to the list of known hosts.
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```
- follow https://github.com/castorini/mr.tydi/tree/b11dcf3e52c4685d98bb6efaeabc0a356946da1e#baselines-and-evaluation for v1.0