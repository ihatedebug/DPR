#!/bin/bash
base_path="/data1/jongho/sigir/data/mrtydi_dataset"
langs=( 'bengali' 'russian' 'korean' 'telugu' 'japanese' 'arabic' )
set_names=( "train" "dev" )
qrel_paths=( )
for i in ${!langs[@]}; do
    lang=${langs[$i]}
    for set_name in ${set_names[@]}; do
        qrel_paths+=($base_path/mrtydi-v1.0-${lang}/qrels.${set_name}.txt)
    done;
done;

echo ${qrel_paths[@]}
python revise_id_file.py --qrel_paths ${qrel_paths[@]}