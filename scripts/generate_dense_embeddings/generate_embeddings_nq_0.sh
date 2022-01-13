
export PYTHONPATH=`pwd`
export CUDA_VISIBLE_DEVICES=1,2

export NUM_SHARDS=10
export MODEL_NAME=dpr_biencoder.35

for (( c=0; c<$NUM_SHARDS; c+=3 ))
do
    python generate_dense_embeddings.py \
	model_file=/root/DPR/outputs/2022-01-11/10-39-38/nq_out/$MODEL_NAME \
	ctx_src=dpr_wiki \
	shard_id=$c num_shards=$NUM_SHARDS \
	out_file=/data1/jongho/nq/embeddings/$MODEL_NAME
done