import sys, os
import time
from collections import defaultdict

def main():	
	start = time.time()
	stopWords = []
	f0 = open("dict/stop.txt","r")
	for line in f0:
		word = line.replace("\n","")
		stopWords.append(word)
	count = 0
	dirs = os.listdir( "dict" )
	f1 = open("dict/form.txt","w+")				
	inFile = open('dict/entire.txt')
	for line in inFile:
		splitLine = line.lower().replace('\n','').split('|')
		splitWord = splitLine[0].rstrip().lstrip().split(' ')
		splitDef = splitLine[1].rstrip().lstrip().split(';')
		s = str(splitDef[0])
		s1 = s.translate(str.maketrans('','', "(,),\',\",!,@,#,$,%,^,&,*,{,},{,},-,_,=,+,;,:,,,.,<,>,/,?,\\,|,`,~"))
		f1.write(splitWord[4]+"\t}{\t"+s1+" \n")
		count = count+1
	f1.close()
	f2 = open("dict/stopLess.txt","w+")	
	f3= open("dict/form.txt","r")	
	for line in f3:
		splitLine = line.split("\t}{\t")
		new = list(set(splitLine[1].replace(" \n","").split(" "))-set(stopWords))
		new2 = list(set(new)-set(weirdChars))
		f2.write(splitLine[0]+"\t}{\t"+" ".join(new2)+" \n")
	f2.close()
	f3.close()	
	print(count)
	end = time.time()
	print("Elapsed Time(seconds): ",end - start)

main()
