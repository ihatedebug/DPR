import gzip
import pandas as pd
from tqdm import tqdm
import json
import os

total_data_path = 'data/en.tsv.gz'

total_data = gzip.open(total_data_path,'r')
documents = {}
for i, line in enumerate(total_data):
    tmp = line.decode().strip().split('\t')
    try:
        documents[int(tmp[0])] = tmp[1]
    except ValueError:
        print(i, line)


def to_dpr(input_data, input_data_e, output_data_path):
    data = []
    data_e = []
    for i ,row in tqdm(input_data.iterrows()):
        row_data = {}
        
        # question
        row_data['question'] = row['src_query']
        # answer
        row_data['answers'] = [row['src_query']]
        
        # positive_ctxs
        row_data['positive_ctxs'] = []
        positive_ctxs={}
        # negative_ctxs
        row_data['negative_ctxs'] = []
        negative_ctxs={}
        # hard_negative_ctxs
        row_data['hard_negative_ctxs'] = []
        hard_negative_ctxs={}
        #########
        #print('Starting PHASE 1')
        # process through whole data (positive)
        found_positive = False
        assert len(row['tgt_results']) == 100
        for item in row['tgt_results']:
            #positive_ctxs['title']=row['src_query']
            if item[1]==6:
                positive_ctxs['text']=documents[int(item[0])]
                found_positive = True
                break
        if found_positive==False:
            for item in row['tgt_results']:
                if item[1]==5:
                    positive_ctxs['text']=documents[int(item[0])]
                    found_positive=True
                    break
        if found_positive==False:
            positive_ctxs['text']=documents[int(row['tgt_results'][0][0])]
            found_positive=True
        #print('Ending PHASE 1')
        #########
        #print('Starting PHASE 2')
        # process through whole data (negative)
        # 40 번쨰를 hard negative로
        hard_negative_ctxs['text']=documents[int(row['tgt_results'][int(len(row['tgt_results'])*0.4)][0])]
        #print('Ending PHASE 2')
        #########
        # process through whole data (hard_negative)
        negative_ctxs['text']=documents[int(row['tgt_results'][-1][0])]
        #########
        row_data['positive_ctxs'].append(positive_ctxs)
        row_data['negative_ctxs'].append(negative_ctxs)
        row_data['hard_negative_ctxs'].append(hard_negative_ctxs)
        data.append(row_data)

        assert input_data_e.iloc[i]['eid'] == row['eid']
        # question
        row_data['question'] = input_data_e.iloc[i]['src_query']
        # answer
        row_data['answers'] = [input_data_e.iloc[i]['src_query']]
        data_e.append(row_data)
    print(len(data))
    with open(output_data_path,'w') as o:
        json.dump(data, o, indent=4)

    output_data_path_e = os.path.splitext(output_data_path)[0]
    with open(output_data_path_e+"-ee.json",'w') as o:
        json.dump(data_e, o, indent=4)

if __name__ == '__main__':


    train_data_path = 'data/fr.en.train.jl'
    dev_data_path = 'data/fr.en.dev.jl'
    test1_data_path = 'data/fr.en.test1.jl'
    test2_data_path = 'data/fr.en.test2.jl'

    train_data_path_e = 'data/en.fr.train.jl'
    dev_data_path_e = 'data/en.fr.dev.jl'
    test1_data_path_e = 'data/en.fr.test1.jl'
    test2_data_path_e = 'data/en.fr.test2.jl'

    #output_path = os.path.join(os.getcwd(),'clir_to_dpr')

    train_data = pd.read_json(train_data_path, lines=True)
    train_data_e = pd.read_json(train_data_path_e, lines=True)
    to_dpr(train_data, train_data_e, 'clir_to_dpr/clirmatrix_train.json')

    dev_data = pd.read_json(dev_data_path,lines=True)
    dev_data_e = pd.read_json(dev_data_path_e,lines=True)
    to_dpr(dev_data, dev_data_e, 'clir_to_dpr/clirmatrix_dev.json')

    test1_data = pd.read_json(test1_data_path, lines=True)
    test1_data_e = pd.read_json(test1_data_path_e, lines=True)
    to_dpr(test1_data, test1_data_e, 'clir_to_dpr/clirmatrix_test1.json')
    
    test2_data = pd.read_json(test2_data_path, lines=True)
    test2_data_e = pd.read_json(test2_data_path_e, lines=True)
    to_dpr(test2_data, test2_data_e, 'clir_to_dpr/clirmatrix_test2.json')    
