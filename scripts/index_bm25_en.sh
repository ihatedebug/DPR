python -m pyserini.index \
  --input data/english_collection_jsonl \
  --collection JsonCollection \
  --generator DefaultLuceneDocumentGenerator \
  --index indexes/english_collection \
  --threads 12 \
  --storePositions --storeDocvectors --storeRaw