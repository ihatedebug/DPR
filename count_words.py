import json
import random

train_file = "/data1/jongho/sigir/output/dpr-mmarco-fren-train-rm-dup.json"
sample_ratio = 0.1
sampled_train_file = "/data1/jongho/sigir/output/dpr-mmarco-fren-train-sampled.json"

def count_queries(jdata):
    count = 0
    for data in jdata:
        count += len(data['question'].split())
    return count

with open(train_file) as f:
    jdata = json.load(f)
print(count_queries(jdata))
jdata_sampled = random.sample(jdata, int(len(jdata)*sample_ratio))
print(count_queries(jdata_sampled))

with open(sampled_train_file, 'w') as f:
    json.dump(jdata_sampled, f)