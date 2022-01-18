import json
from tqdm import tqdm

def remove_dup_train():
    filename = "/data1/jongho/sigir/data/triples.train.ids.small.tsv"
    triples = {}
    with open(filename, encoding="utf-8") as f:
        for (idx, line) in tqdm(enumerate(f)):
            query_id, pos_id, neg_id = line.rstrip().split("\t")
            if query_id in triples:
                if pos_id not in triples[query_id]['pos_id']: 
                    triples[query_id]['pos_id'].append(pos_id)
                if neg_id not in triples[query_id]['neg_id']:
                    triples[query_id]['neg_id'].append(neg_id)
            else:
                triples[query_id] = {'pos_id': [pos_id], 'neg_id': [neg_id] }

    # with open(filename ,) as f:
    # #     json_data = json.load(f)

    print(f"max pos length: {max([len(v['pos_id']) for v in triples.values()])}")
    with open ("/data1/jongho/sigir/data/triples.train.ids.small.json", "w") as json_file:
        json.dump(triples, json_file)

def remove_dup_eval():
    quadraples = {}
    filename = "/data1/jongho/sigir/data/qrels.dev.small.tsv"
    with open(filename, encoding="utf-8") as f:
        for (idx, line) in tqdm(enumerate(f)):
            query_id, iteration, pos_id, relevancy = line.rstrip().split("\t")
            if query_id in quadraples:
                quadraples[query_id]['iter'].append(iteration)
                quadraples[query_id]['pos_id'].append(pos_id)
                quadraples[query_id]['relevancy'].append(relevancy)
            else:
                quadraples[query_id] = {'iter': [iteration], 'pos_id': [pos_id], 'relevancy': [relevancy]}
    print(f"max pos length: {max([len(v['pos_id']) for v in quadraples.values()])}")
    with open ("/data1/jongho/sigir/data/qrels.dev.small.json", "w") as json_file:
        json.dump(quadraples, json_file)

remove_dup_eval()