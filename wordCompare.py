from collections import Counter
import sys, os
import time
def compareWords(w1,w2):
	'''listw = w1.copy()+w2.copy()
	count = 0
	#print(listw)
	wordFreq = {}
	for word in listw:
		if word not in wordFreq:
			wordFreq[word] = 0
		wordFreq[word]+=1
	for word in wordFreq:
		if(wordFreq[word] != 1):
			count+=wordFreq[word]
	return len(listw)-count
		#print(word,wordFreq[word])'''
	one = w1.copy()
	two = w2.copy()
	count = 0
	for i in range(len(one)):
		for j in range(len(two)):
			if one[i]==two[j] and one[i] != "\k/":
				#print(one)
				#print(two)
				count+=1
				one[i] = "\k/"
				two[j] = "\k/"
	#if count >1: print(count)
	return len(w1) - count
	c1 = Counter(w1)
	c1.subtract(w2)
	return(len(list(c1.elements())))
def main():
	start = time.time()


	wordList = []
	f = open("dict/stopLess.txt","r")	
	for line in f:
		word = line.replace(" \n","")
		splitLine = word.split("\t}{\t")
		defintion = splitLine[1].split(" ")
		wordList.append([splitLine[0],defintion])
	'''wordList.append(['word1',['this','is','good','shit']])
	wordList.append(['word1',['this','is','good','shit']])'''
	print(len(wordList))
	temps = 0
	boi = 0
	f2 = open("outPut3.txt","w+")
	for i in range(len(wordList)):
		s = os.popen('sensors').readlines()
		temps += float(s[11][16:20])
		if float(s[11][16:20]) >70:
			break
		for j in range(i+1,len(wordList)):
			boi+=1

			w1 = wordList[i][1]
			w2 = wordList[j][1]
			if len(w1) > 3 and len(w2) > 3:



				x = compareWords(w1,w2)
				#print(w1)
				#print(x)

				#wordOneCompare = ((len(w1)-x)/len(w1))

				y = compareWords(w2,w1)
				'''print(w2)
				print(y)'''
				wordOneCompare = ((len(w1)+len(w2))-(x+y))/(len(w1)+len(w2))

				'''wordTwoCompare = ((len(w2)-y)/len(w2))'''

				if wordOneCompare > 0.7:# or wordTwoCompare > 0.99:
					#print(wordList[i][0],'\t',wordList[j][0],'\t',wordOneCompare)
					f2.write(wordList[i][0]+'\t'+wordList[j][0]+'\t'+str(wordOneCompare)+"\n")
	f2.close()
	f.close()
	print("count: ",boi)
	#print("total: ", boi*100)
	end = time.time()
	print("Average CPU temp (C):  ",temps/len(wordList))
	print("Elapsed Time(seconds): ",end - start)
	print('Elapsed Time(hours  ): ',((end-start)/3600))
main()