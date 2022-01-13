export PYTHONPATH=`pwd`
export CUDA_VISIBLE_DEVICES=1,2,3,4

export MODEL_NAME=dpr_biencoder.35

python dense_retriever.py \
	model_file=/root/DPR/outputs/2022-01-11/10-39-38/nq_out/$MODEL_NAME \
	qa_dataset=nq_test \
	ctx_datatsets=[dpr_wiki] \
	encoded_ctx_files=["/data1/jongho/nq/embeddings/*"] \
	out_file="./nq_eval"