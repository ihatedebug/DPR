python -m pyserini.index \
  --input data/french_collection_jsonl \
  --collection JsonCollection \
  --generator DefaultLuceneDocumentGenerator \
  --index indexes/french_collection \
  --threads 12 \
  --language fr \
  --storePositions --storeDocvectors --storeRaw