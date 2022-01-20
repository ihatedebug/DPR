
import argparse
import json
from tqdm import tqdm
import random
import pickle
import gzip
import sys

def generate_examples_train(args):
    filepath=args.filepath
    collection_path=args.collection_path
    queries_path=args.queries_path
    bm25_path=args.bm25_path
    output_path=args.output_path
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
                hard_negative_ctxs=hard_negative_ctxs[:args.n_hard_negatives]
            except KeyError:
                not_in_bm25_list.append(query_id)
                continue
            features = {
                'dataset': args.task,
                "question": question,
                "answers" : [""],
                "positive_ctxs": [{"text": collection[pos_id], "passage_id": pos_id} for pos_id in pos_ids],
                "negative_ctxs": [{"text": collection[neg_id], "passage_id": neg_id}],
                "hard_negative_ctxs" : hard_negative_ctxs
            }
            feature_list.append(features)
    
    with open(output_path, "w") as json_file:
        json.dump(feature_list, json_file, indent=4)
    
    print(f"processed for DPR #{len(feature_list)}")
    print(f"key error query : #{len(not_in_query_list)}")
    print(f"key error bm25 : #{len(not_in_bm25_list)}")

    with open("output/not_in_query_train.pkl", 'wb') as f:
        pickle.dump(not_in_query_list, f)

    with open("output/not_in_bm25_train.pkl", 'wb') as f:
        pickle.dump(not_in_bm25_list, f)

def generate_examples_dev(args):
    filepath=args.filepath
    collection_path=args.collection_path
    queries_path=args.queries_path
    bm25_path=args.bm25_path
    output_path=args.output_path
    print("################Dev##################")
    print("processing docs...")
    collection = {}
    if args.task == "mmarco":
        with open(collection_path, encoding="utf-8") as f:
            for line in f:
                doc_id, doc = line.rstrip().split("\t")
                collection[doc_id] = doc
    elif args.task =='mrtydi':
        with gzip.open(collection_path,'r') as f:
            for line in f:
                jdata = json.loads(line.decode())
                collection[jdata['id']] = jdata['contents']
    else:
        sys.exit(f"The dataset {args.task} is not implemented")

    print(f"processed {len(collection)} docs")
    
    print("processing queries...")
    queries = {} # mrtydi: topics
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

            # hard negatives
            try:
                hard_negative_ctxs = [{"text": collection[docs["doc_id"]], "score": docs["score"], "passage_id": docs["doc_id"]} for docs in bm25s[query_id] if docs['doc_id'] not in pos_ids]
                hard_negative_ctxs=hard_negative_ctxs[:args.n_hard_negatives]
            except:
                not_in_bm25_list.append(query_id)
                continue

            #negatives
            if args.n_negatives > 1:
                neg_ids = random.sample(list(collection.keys()), args.n_negatives+len(pos_ids)) # TODO: its time consuming
                neg_ctxs = [{"text": collection[neg_id], "passage_id": neg_id} for neg_id in neg_ids if neg_id not in pos_ids]
                neg_ctxs = neg_ctxs[:args.n_negatives]
            else:
                while True:
                    neg_id = str(random.randrange(len(collection)))
                    if neg_id not in pos_ids:
                        break
                neg_ctxs = [{"text": collection[neg_id], "passage_id": neg_id}]

            features = {
                'dataset': args.task,
                "question": question,
                "answers" : [""],
                "positive_ctxs": [{"text": collection[pos_id], "passage_id": pos_id} for pos_id in pos_ids],
                "negative_ctxs": neg_ctxs,
                "hard_negative_ctxs" : hard_negative_ctxs
            }
            feature_list.append(features)

    with open(output_path, "w") as json_file:
        json.dump(feature_list, json_file, indent=4)

    print(f"processed for DPR #{len(feature_list)}")
    print(f"key error : #{len(not_in_query_list)}")
    print(f"key error bm25 : #{len(not_in_bm25_list)}")

    with open("output/not_in_query_dev.pkl", 'wb') as f:
        pickle.dump(not_in_query_list, f)

    with open("output/not_in_bm25_dev.pkl", 'wb') as f:
        pickle.dump(not_in_bm25_list, f)            



if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--collection_path",
        default="",
        type=str,
        help="The path of docs",
    )
    parser.add_argument(
        "--queries_path",
        default="output/dpr-mmarco-fren-train.json",
        type=str,
        help="The output path of json file",
    )
    parser.add_argument(
        "--filepath",
        default="",
        type=str,
        help="The path of train triples or dev qrels",
    )
    parser.add_argument(
        "--bm25_path",
        default="",
        type=str,
        help="The output path of bm25 results by Pyserini",
    )
    parser.add_argument(
        "--output_path",
        default="",
        type=str,
        help="The output path of json file",
    )
    parser.add_argument(
        "--task",
        default="mmarco",
        type=str,
        required=False,
        help="task name",
    )
    parser.add_argument(
        "--n_negatives",
        default=1,
        type=int,
        required=False,
        help="",
    )
    parser.add_argument(
        "--n_hard_negatives",
        default=3,
        type=int,
        required=False,
        help="",
    )
    parser.add_argument(
        "--train",
        default=False,
        action='store_true',
        help="Train or Dev",
    )

    args = parser.parse_args()

    if args.train:
        generate_examples_train(args)
    else:
        generate_examples_dev(args)
