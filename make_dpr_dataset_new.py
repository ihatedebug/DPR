
import json
from tqdm import tqdm
import random
import pickle

def generate_examples_train(filepath, collection_path, queries_path, bm25_path, output_path):
    print("################Train##################")
    print("processing docs...")
    collection = {}
    with open(collection_path, encoding="utf-8") as f:
        for line in f:
            doc_id, doc = line.rstrip().split("\t")
            collection[doc_id] = doc
    print(f"processed {len(collection)} docs")
    
    print("processing queries...")
    queries = {}
    with open(queries_path, encoding="utf-8") as f:
        for line in f:
            query_id, query = line.rstrip().split("\t")
            queries[query_id] = query
    print(f"processed {len(queries)} queries")

    print("processing bm25s...")
    bm25s = {}
    with open(bm25_path, encoding="utf-8") as f:
        for line in f:
            query_id, _, doc_id, rank, score, _  = line.rstrip().split(" ")
            #if int(rank) <= "" : # save only 50 hard-negatives
            if query_id in bm25s:
                bm25s[query_id].append({"doc_id": doc_id, "score": score})
            else:
                bm25s[query_id] = [{"doc_id": doc_id, "score": score}]
    print(f"processed {len(bm25s)} bm25s")

    print("writing file...")
    not_in_query_list = []
    not_in_bm25_list = []
    feature_list = []

    with open(filepath, encoding="utf-8") as f:
        jdata = json.load(f)
        for query_id, v in tqdm(jdata.items()):
            pos_ids = v['pos_id']
            neg_id = v['neg_id'][0]
            try:
                question = queries[query_id]
            except KeyError:
                #print("key error:")
                not_in_query_list.append(query_id)
                continue
            try:
                hard_negative_ctxs = [{"text": collection[docs["doc_id"]], "score": docs["score"], "passage_id": docs["doc_id"]} for docs in bm25s[query_id] if docs['doc_id'] not in pos_ids]
                if len(hard_negative_ctxs)>3:
                    hard_negative_ctxs=hard_negative_ctxs[:3]
            except KeyError:
                not_in_bm25_list.append(query_id)
                continue
            features = {
                'dataset': "mmarco",
                "question": question,
                "answers" : [""],
                "positive_ctxs": [{"text": collection[pos_id], "passage_id": pos_id} for pos_id in pos_ids],
                "negative_ctxs": [{"text": collection[neg_id], "passage_id": neg_id}],
                "hard_negative_ctxs" : hard_negative_ctxs
            }
            feature_list.append(features)
    
    with open(output_path, "w") as json_file:
        json.dump(feature_list, json_file)
    
    print(f"processed for DPR #{len(feature_list)}")
    print(f"key error query : #{len(not_in_query_list)}")
    print(f"key error bm25 : #{len(not_in_bm25_list)}")

    with open("output/not_in_query_train.pkl", 'wb') as f:
        pickle.dump(not_in_query_list, f)

    with open("output/not_in_bm25_train.pkl", 'wb') as f:
        pickle.dump(not_in_bm25_list, f)

def generate_examples_dev(filepath, collection_path, queries_path, bm25_path, output_path):
    print("################Dev##################")
    print("processing docs...")
    collection = {}
    with open(collection_path, encoding="utf-8") as f:
        for line in f:
            doc_id, doc = line.rstrip().split("\t")
            collection[doc_id] = doc
    print(f"processed {len(collection)} docs")
    
    print("processing queries...")
    queries = {}
    with open(queries_path, encoding="utf-8") as f:
        for line in f:
            query_id, query = line.rstrip().split("\t")
            queries[query_id] = query
    print(f"processed {len(queries)} queries")

    print("processing bm25s...")
    bm25s = {}
    with open(bm25_path, encoding="utf-8") as f:
        for line in f:
            query_id, _, doc_id, rank, score, _  = line.rstrip().split(" ")
            #if int(rank) <= "" : # save only 50 hard-negatives
            if query_id in bm25s:
                bm25s[query_id].append({"doc_id": doc_id, "score": score})
            else:
                bm25s[query_id] = [{"doc_id": doc_id, "score": score}]
    print(f"processed {len(bm25s)} bm25s")

    print("writing file...")
    not_in_query_list = []
    not_in_bm25_list = []
    feature_list = []
    with open(filepath, encoding="utf-8") as f:
        jdata = json.load(f)
        for query_id, v in tqdm(jdata.items()):
            pos_ids = v['pos_id']
            relevancy_l = v['relevancy']
            pos_ids = [pos_ids[i] for i in range(len(pos_ids)) if int(relevancy_l[i]) == 1]
            try:
                question = queries[query_id]
            except KeyError:
                not_in_query_list.append(query_id)
                continue
            try:
                hard_negative_ctxs = [{"text": collection[docs["doc_id"]], "score": docs["score"], "passage_id": docs["doc_id"]} for docs in bm25s[query_id] if docs['doc_id'] not in pos_ids]
            except:
                not_in_bm25_list.append(query_id)
                continue
            while True:
                neg_id = str(random.randrange(len(collection)))
                if neg_id not in pos_ids:
                    break
            features = {
                'dataset': "mmarco",
                "question": question,
                "answers" : [""],
                "positive_ctxs": [{"text": collection[pos_id], "passage_id": pos_id} for pos_id in pos_ids],
                "negative_ctxs": [{"text": collection[neg_id], "passage_id": neg_id}],
                "hard_negative_ctxs" : hard_negative_ctxs
            }
            feature_list.append(features)

    with open(output_path, "w") as json_file:
        json.dump(feature_list, json_file)

    print(f"processed for DPR #{len(feature_list)}")
    print(f"key error : #{len(not_in_query_list)}")
    print(f"key error bm25 : #{len(not_in_bm25_list)}")

    with open("output/not_in_query_dev.pkl", 'wb') as f:
        pickle.dump(not_in_query_list, f)

    with open("output/not_in_bm25_dev.pkl", 'wb') as f:
        pickle.dump(not_in_bm25_list, f)            



if __name__ == '__main__':
    collection_path = "/data1/jongho/sigir/data/english_collection.tsv"
    # train 
    queries_path = "/data1/jongho/sigir/data/french_queries.train.tsv"
    filepath = "/data1/jongho/sigir/data/triples.train.ids.small.json"
    bm25_path = "runs/run.french_train_new.txt"
    output_path = "output/dpr-mmarco-fren-train-rm-dup.json"
    
    generate_examples_train(filepath=filepath, collection_path=collection_path, queries_path=queries_path, bm25_path=bm25_path, output_path=output_path)
    # dev
    queries_path = "/data1/jongho/sigir/data/french_queries.dev.tsv"
    filepath = "/data1/jongho/sigir/data/qrels.dev.json"
    bm25_path = "runs/run.english_dev.txt"
    output_path = "output/dpr-mmarco-fren-dev-rm-dup.json"
    generate_examples_dev(filepath=filepath, collection_path=collection_path, queries_path=queries_path, bm25_path=bm25_path, output_path=output_path)