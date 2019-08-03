# Local Sensitivity Hashing School Project..

we will apply the locality sensitive hashing technique to a question dataset. The goal is: for each question X, find a set of questions Y in the data set such that Sim(X,Y) ⩾ 0.6, where the similarity is Jaccard. 

# Input Format:
The datasets are given in tvs (tab-separated) format. The file contains two columns: qid and question. Four datasets provided in a single zip-compressed file are

# Output Format:
output must be given in tsv forrmat, with two columns: qid and similar-qids where qid is the qid of the queried question and similar-qids is the set of similar questions given by their qids. The format of column similar-qids is comma-separated. If a question has no similar question, then this column is empty. Below is an example of the output format: 

# qid	similar-qids
11	
13	145970
15	229098,280602,6603,204128,164826,238609,65667,139632,265843,143673,217736,38330
