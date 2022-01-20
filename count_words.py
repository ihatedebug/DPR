import json
import random

train_file1 = "/data1/jongho/sigir/output/dpr-mmarco-enen-train.json"
train_file2 = "/data1/jongho/sigir/output/dpr-mmarco-fren-train.json"
sample_ratio = 0.1
sampled_train_file1 = "/data1/jongho/sigir/output/dpr-mmarco-enen-train-sampled.json"
sampled_train_file2 = "/data1/jongho/sigir/output/dpr-mmarco-fren-train-sampled.json"

def count_queries(jdata):
    count = 0
    for data in jdata:
        count += len(data['question'].split())
    return count

with open(train_file1) as f:
    jdata1 = json.load(f)
print(count_queries(jdata1))

with open(train_file2) as f:
    jdata2 = json.load(f)

while True:
    random_indexs = random.sample(range(len(jdata1)), int(len(jdata1)*sample_ratio) )
    jdata1 = [jdata1[i] for i in random_indexs]
    jdata2 = [jdata2[i] for i in random_indexs]
    count1 = count_queries(jdata1)
    count2 = count_queries(jdata2)
    print("query # words", count1, count2)
    if count1 <=1300000 and count2 <=1300000:
        break

with open(sampled_train_file1, 'w') as f:
    json.dump(jdata1, f)
with open(sampled_train_file2, 'w') as f:
    json.dump(jdata2, f)