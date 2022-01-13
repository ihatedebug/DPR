
export PYTHONPATH=`pwd`
export CUDA_VISIBLE_DEVICES=1,2,3,4,5,6

export MODEL_NAME=dpr_biencoder.39

python generate_dense_embeddings.py \
model_file=/root/DPR/outputs/2022-01-11/10-39-38/nq_out/$MODEL_NAME \
ctx_src=dpr_wiki \
shard_id=0 num_shards=1 batch_size=1024 \
out_file=/data1/jongho/nq/embeddings/$MODEL_NAME
