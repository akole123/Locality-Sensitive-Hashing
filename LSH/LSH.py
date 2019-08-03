from fnv import *
import uuid
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


def wordMap(listOfSentence):
	fvnToWordMap = {}
	for sentence in listOfSentence:
		sentence[1] = re.split(' ',sentence[1])
		for word in sentence[1]:
			# print(word)
			fvnToWordMap[word] = hash(word.encode('utf-8'), algorithm=fnv_1a, bits=64)
	return fvnToWordMap


def minHashFunction(listOfSentence,fvnToWordMap):
	minList = {}
	randA = uuid.uuid4().int & (1<<64)-1
	randB = uuid.uuid4().int & (1<<64)-1
	for sentence in listOfSentence:
		tmpListOfVals = []
		for word in sentence[1]:
			word = (randA*fvnToWordMap[word] + randB)%15373875993579943603 
			tmpListOfVals.append(word)
		minList[sentence[0]] = min(tmpListOfVals)

	for i in range(5):
		randA = uuid.uuid4().int & (1<<64)-1
		randB = uuid.uuid4().int & (1<<64)-1

		for sentence in listOfSentence:
			tmpListOfVals = []
			for word in sentence[1]:
				word = (randA*fvnToWordMap[word] + randB)%15373875993579943603 
				tmpListOfVals.append(word)
			minList[sentence[0]] = minList[sentence[0]] + min(tmpListOfVals)
	return minList	


def collectHashPairs(minList,pairHashValue):
	finalHashTable = {}
	for leist in minList:
		finalHashTable[minList[leist]] = "|"

	for leist in minList:
			finalHashTable[minList[leist]]  = str(finalHashTable[minList[leist]])  + "," + str(leist)
	for leist in finalHashTable:
		tmp = re.split(',',finalHashTable[leist])
		if len(tmp) > 2:
			tmp.pop(0)
			for x in tmp:
				for y in tmp:
					if(x!=y):
						pairHashValue[(int(x),int(y))] = 1	
	return pairHashValue


def seperateEachSentence(listOfSentence):
	sentenceIndex = {}
	for sentence in listOfSentence:
		sentenceIndex[sentence[0]] = sentence[1]	
	return sentenceIndex


def openFile():
	fileReadName = "question_150k.tsv"
	fileRead = open(fileReadName,encoding ='utf8')
	temp =[line.rstrip('\n') for line in fileRead]

	listOfSentence = []
	for sentence in temp:
		tmp = re.split('\t',sentence)
		listOfSentence.append(tmp)
	return listOfSentence


def fileWrite(listofPairs,sentenceIndex):
	timeSaveIndex = 0
	pairLength = (len(listofPairs))

	fileOutPutName = "question_sim_150k.tsv"
	fileWrite = open(fileOutPutName,"w") 

	fileWrite.write('qid,similar-qids \n')
	for key in sentenceIndex:
		fileWrite.write(key + ' ')
		while(timeSaveIndex != pairLength and int(key) == (listofPairs[timeSaveIndex])[0]):
			if( sim( sentenceIndex[str((listofPairs[timeSaveIndex])[0])] ,sentenceIndex[str((listofPairs[timeSaveIndex])[1])]) >= 0.6):
				fileWrite.write(',' + str((listofPairs[timeSaveIndex])[1]))
				timeSaveIndex = timeSaveIndex + 1
			else:
				timeSaveIndex = timeSaveIndex + 1	
		else:
			fileWrite.write('\n')
	fileWrite.close()	


def cleanData(listOfSentence):
	#---------------------------
	del(listOfSentence[0])
	listOfSentence.sort()
	del(listOfSentence[0])
	#---------------------------
	for sentence in listOfSentence:
		sentence[0] = int(sentence[0])
	listOfSentence.sort()
	for sentence in listOfSentence:
		sentence[0] = str(sentence[0])
	return listOfSentence


def main():
	#Start timer to calculate run time.
	start = time.time()

	# Take information from file and split them into a list of sentences.
	listOfSentence = openFile()

	#Clean the clutter in the database, kind of specific for this database.
	cleanData(listOfSentence)

	#Take a fnv mapping of each possible word from the document
	fvnToWordMap = wordMap(listOfSentence)

	#Turn the list of sentences into a dictionary.
	sentenceIndex = seperateEachSentence(listOfSentence)

	#Taking 14 hash tables, calculate signature with r = 6. Then collect each pair per hash table.
	pairHashValue = {}
	for i in range(14):
		minList = minHashFunction(listOfSentence,fvnToWordMap)
		pairHashValue = collectHashPairs(minList,pairHashValue)

	#Take each pair from the 14 hash tables and create a tuple of pairs, sort them
	listofPairs = []
	for key in pairHashValue:
		listofPairs.append((key[0],key[1]))
	listofPairs.sort()
	print('Number of pairs in this execution' + " : " + str(len(listofPairs)))


	#Take the pairs, and index of their original sentences,compute their jaccard similarity.
	 # If JS is greater then 0.6,write their sentenceIndex into output file.
	fileWrite(listofPairs,sentenceIndex)

	elapsed = time.time() - start
	print("%.2f" % round(elapsed,2) + " Seconds")

if __name__ == "__main__":
	main()