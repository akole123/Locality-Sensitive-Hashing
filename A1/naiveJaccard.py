import hashlib
import re
import time

def sim(basket1,basket2):
	tempUnion = set(basket1).union(set(basket2))
	tempIntersection = set(basket1).intersection(set(basket2))
	if(len(tempUnion) != 0):
		return(len(tempIntersection)/len(tempUnion))
	else:
		return 0


def seperateEachSentence(listOfSentence):
	for sentence in listOfSentence:
		if len(sentence) == 1:
			sentence.append(" ")
	sentenceIndex = {}
	for sentence in listOfSentence:
		sentenceIndex[sentence[0]] = sentence[1]	

	for key in sentenceIndex:
		sentenceIndex[key] = sentenceIndex[key].split(' ')
		# print(sentenceIndex[key])
	del(sentenceIndex['qid'])

	return sentenceIndex


def openFile():
	fileReadName = "question_4k.tsv"
	fileRead = open(fileReadName,encoding ='utf8')
	temp =[line.rstrip('\n') for line in fileRead]
	
	listOfSentence = []
	for sentence in temp:
		tmp = re.split('\t',sentence)
		listOfSentence.append(tmp)
	return listOfSentence


def writeFile(sentenceIndex):
	fileOutPutName = "question_sim_4k2.tsv"
	fileWrite = open(fileOutPutName,"w") 

	fileWrite.write('qid,similar-qids \n')
	resultDict = {}
	for key1 in sentenceIndex:
		fileWrite.write(key1 + ' ')
		for key2 in sentenceIndex:
			if(sim(sentenceIndex[key1],sentenceIndex[key2]) >= 0.6 and key1 != key2):
				fileWrite.write(',' + key2)
		fileWrite.write('\n')
	fileWrite.close()


def main():
	start = time.time()
	listOfSentence = openFile()

	#Clean up data and hash them into dictionary with qid as index and sentence as value
	sentenceIndex = seperateEachSentence(listOfSentence)

	#Compare each sentence with every other sentence using jaccard similarity
	writeFile(sentenceIndex)
	elapsed = time.time() - start
	print("%.2f" % round(elapsed,2) + " Seconds")

if __name__ == "__main__":
	main()