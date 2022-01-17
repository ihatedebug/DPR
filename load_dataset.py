from datasets import load_dataset
import os
cache_dir = "/data1/jongho/sigir/.cache"
os.environ["HF_DATASETS_CACHE"] = "/data1/jongho/sigir/.cache"

dataset_e = load_dataset('unicamp-dl/mmarco', 'english', cache_dir=cache_dir) # dataset_e['train'][i] query, positive, negative
query_e = load_dataset('unicamp-dl/mmarco', 'queries-english', cache_dir=cache_dir) # query_e['train', 'validation'][i] id, text
collection_e = load_dataset('unicamp-dl/mmarco', 'collection-english', cache_dir=cache_dir) # 
#run_e = load_dataset('unicamp-dl/mmarco', 'runs-english', cache_dir=cache_dir)

dataset_f = load_dataset('unicamp-dl/mmarco', 'french', cache_dir=cache_dir)
query_f = load_dataset('unicamp-dl/mmarco', 'queries-french', cache_dir=cache_dir)
collection_f = load_dataset('unicamp-dl/mmarco', 'collection-french', cache_dir=cache_dir)
# run_f = load_dataset('unicamp-dl/mmarco', 'runs-french', cache_dir=cache_dir)
print(collection_e['bm25'][0])
print("english")