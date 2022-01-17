import json

def doc_to_jsonl_bm25(file_read):
    assert file_read.endswith(".tsv")
    file_write = file_read.rstrip(".tsv")+".jsonl"
    print(f"doc to write: {file_write}")
    with open(file_write, 'w') as fw:
        with open(file_read) as fr:
            for line in fr:
                doc_id, text = line.split("\t")
                text = text.strip()
                store_d = {"id": doc_id,
                "contents": text}
                fw.write(json.dumps(store_d, ensure_ascii=False)+"\n")

# def query_to_tsv_bm25(file_read, file_write):
#     with open(file_write) as fw:
#         with open(file_read) as fr:
#             for line in fr:
#                 doc_id, text = line.split("\t")
#                 text = text.strip()
#                 store_d = {"id": doc_id,
#                 "contents": text}
#                 fw.write(json.dumps(store_d, ensure_ascii=False)+"\n")

if __name__ == '__main__':
    doc_to_jsonl_bm25("data/english_collection.tsv")
    