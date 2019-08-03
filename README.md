# Only runnable in Python3 due to FNV version

# Local Sensitivity Hashing School Project..

we will apply the locality sensitive hashing technique to a question dataset. The goal is: for each question X, find a set of questions Y in the data set such that Sim(X,Y) ⩾ 0.6, where the similarity is Jaccard. 

# Input Format:
The datasets are given in tvs (tab-separated) format. The file contains two columns: qid and question. Four datasets provided in a single zip-compressed file are

# Output Format:
output must be given in tsv forrmat, with two columns: qid and similar-qids where qid is the qid of the queried question and similar-qids is the set of similar questions given by their qids. The format of column similar-qids is comma-separated. If a question has no similar question, then this column is empty. Below is an example of the output format: 

# Run Instructions:
Git clone repository.
Run CMD and use command Python3 LSH.py [input_file] Of your choosing. Output file will be in the same folder.
