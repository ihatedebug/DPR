def generate_examples_tuples(filepath):
    features = dict()
    with open(filepath, encoding="utf-8") as f:
        for (idx, line) in enumerate(f):
            idx, text = line.rstrip().split("\t")
            features[idx] = text
    return features

generate_examples_tuples("/data1/jongho/sigir/data/english_queries.train.tsv")