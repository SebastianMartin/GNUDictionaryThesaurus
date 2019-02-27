wordList = []
f = open("finalOut.txt","r")	
for line in f:
	words = line.replace("\n","").split("\t")
	wordList.append(words)
count = 0
for word in wordList:
	if float(word[2]) > .95:
		print(word)
		count+=1
print(count)