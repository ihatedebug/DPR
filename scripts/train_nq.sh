# python train_dense_encoder.py \
# train_datasets=[nq_train] \
# dev_datasets=[nq_dev] \
# train=biencoder_local \
# output_dir={path to checkpoints dir}

export PYTHONPATH=`pwd`
export CUDA_VISIBLE_DEVICES=1,2,3,4

python -m torch.distributed.launch --nproc_per_node=4 train_dense_encoder.py \
train=biencoder_nq \
train_datasets=[nq_train] \
dev_datasets=[nq_dev] \
train=biencoder_nq \
output_dir="./nq_out"