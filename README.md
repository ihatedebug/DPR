# CLIRMatrix to dpr

- 정답 label 이 없고, query와 관련한 BM25 Top100 docs만 제공되어 있음
- 가장 점수 높은 doc 중 하나를 positive로, TOP40 을 hard negative로 사용

- clirmatrix.ipynb : DPR 형식으로 변환하는 코드 base 
- align_fren : fr-en, en-en parallel data 생성
