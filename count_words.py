import json
import random

train_file = "/data1/jongho/sigir/output/dpr-mmarco-enen-train.json"
sample_ratio = 0.1
sampled_train_file = "/data1/jongho/sigir/output/dpr-mmarco-enen-train-sampled.json"

def count_queries(jdata):
    count = 0
    for data in jdata:
        count += len(data['question'].split())
    return count

with open(train_file) as f:
    jdata = json.load(f)
print(count_queries(jdata))

while True:
    jdata = random.sample(jdata, int(len(jdata)*sample_ratio))
    count = count_queries(jdata)
    print("query # words", count)
    if count <=1300000:
        break

with open(sampled_train_file, 'w') as f:
    json.dump(jdata, f)