cd data/mrtydi_dataset

wget https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-bengali.tar.gz
wget https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-russian.tar.gz
wget https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-korean.tar.gz
wget https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-telugu.tar.gz
wget https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-japanese.tar.gz
wget https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-arabic.tar.gz

tar -xvf mrtydi-v1.0-arabic.tar.gz 
tar -xvf mrtydi-v1.0-bengali.tar.gz 
tar -xvf mrtydi-v1.0-bengali.tar.gz 
tar -xvf mrtydi-v1.0-japanese.tar.gz 
tar -xvf mrtydi-v1.0-korean.tar.gz 
tar -xvf mrtydi-v1.0-russian.tar.gz 
tar -xvf mrtydi-v1.0-telugu.tar.gz 

rm *tar.gz
cd -  

# lucene files should be downloaded manually

# cd data/mrtydi_bm25_index
# wget https://vault.cs.uwaterloo.ca/s/7oDFnq8FmTazf2a/download
# wget https://vault.cs.uwaterloo.ca/s/HaPaz2wFbRMP2LK/download
# wget https://vault.cs.uwaterloo.ca/s/ema8i83zqJr7n48/download
# wget https://vault.cs.uwaterloo.ca/s/igmEHCTjTwNi3de/download
# wget https://vault.cs.uwaterloo.ca/s/Pbi9xrD7jSYaxnX/download
# wget https://vault.cs.uwaterloo.ca/s/DAB6ba5ZF98awH6/download
# cd - 