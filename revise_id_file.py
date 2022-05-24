import json
from tqdm import tqdm
import os
import argparse

"""remove duplicates and for O(1) search revise txt qrel files to json format"""

# for version 1
# def remove_dup_train(filename):
#     triples = {}
#     with open(filename, encoding="utf-8") as f:
#         for (idx, line) in tqdm(enumerate(f)):
#             query_id, pos_id, neg_id = line.rstrip().split()
#             if query_id in triples:
#                 # without duplication
#                 if pos_id not in triples[query_id]['pos_id']: 
#                     triples[query_id]['pos_id'].append(pos_id)
#                 if neg_id not in triples[query_id]['neg_id']:
#                     triples[query_id]['neg_id'].append(neg_id)
#             else:
#                 triples[query_id] = {'pos_id': [pos_id], 'neg_id': [neg_id] }

#     print(f"max pos length: {max([len(v['pos_id']) for v in triples.values()])}")
#     save_name = os.path.splitext(filename)[0]+".json"
#     with open (save_name, "w") as json_file:
#         json.dump(triples, json_file)

def remove_dup_eval(filename):
    quadraples = {}
    
    with open(filename, encoding="utf-8") as f:
        for (idx, line) in tqdm(enumerate(f)):
            query_id, iteration, pos_id, relevancy = line.rstrip().split() # TODO: for marco: maybe "\t"? 
            if query_id in quadraples:
                quadraples[query_id]['iter'].append(iteration)
                quadraples[query_id]['pos_id'].append(pos_id)
                quadraples[query_id]['relevancy'].append(relevancy)
            else:
                quadraples[query_id] = {'iter': [iteration], 'pos_id': [pos_id], 'relevancy': [relevancy]}
    print(f"max pos length: {max([len(v['pos_id']) for v in quadraples.values()])}")
    save_name = os.path.splitext(filename)[0]+".json"
    with open (save_name, "w") as json_file:
        json.dump(quadraples, json_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--qrel_paths",
        nargs="+",
        default=[],
        help="The path list of docs",
    )

    args = parser.parse_args()
    for qrel_file in args.qrel_paths:
        print(qrel_file)
        #if 'train' in qrel_file:
        #    remove_dup_train(qrel_file)
        #elif 'dev' in qrel_file or 'test' in qrel_file:
        remove_dup_eval(qrel_file)