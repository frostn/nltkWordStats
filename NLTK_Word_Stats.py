#Nolan Frost
#File Stats Practice

from nltk import *

fileName = input("Enter file name: ")
file = open(fileName, 'r')
fileWords = []
fileWords2 = []
for line in file:
    fileWords.append(line.split())
    fileWords2 = sum(fileWords, [])

for a in range(len(fileWords2)):
    fileWords2[a] = fileWords2[a].lower()

for x in range(len(fileWords2)):
    if '.' in fileWords2[x]:
        fileWords2[x] = fileWords2[x].strip('.')
    if '!' in fileWords2[x]:
        fileWords2[x] = fileWords2[x].strip('!')
    if ',' in fileWords2[x]:
        fileWords2[x] = fileWords2[x].strip(',')
    if ':' in fileWords2[x]:
        fileWords2[x] = fileWords2[x].strip(':')
    if '?' in fileWords2[x]:
        fileWords2[x] = fileWords2[x].strip('?')

#How many words are in the file?
print("There are", len(fileWords2), "words in the file.")

#What is the average length of the words in the file?
total = 0
averageLen = 0
for y in fileWords2:
    total = total + len(y)
averageLen = total / len(fileWords2)
print("The average word length is", format(averageLen, ',.2f'), "characters long.")

#How long is the longest word in the file?
longestWord = 0
for z in fileWords2:
    if len(z) > longestWord:
        longestWord = len(z)
print("The longest word is", longestWord, "characters long.")

fdist = FreqDist(fileWords2)

keyword = input("Enter a word: ")
keyword = keyword.lower()

#Is keyword in file?
if keyword in fileWords2:
    print(keyword, "is in file.")
else:
    print(keyword, "is not in file.")
    
#How many times is keyword in file?
if keyword in fdist:
    print(keyword, "is in file", fdist[keyword], "times.")

#What are the indices of the keyword in the list of words in the file?
indices = []
if keyword in fileWords2:
    for w in range(0, len(fileWords2)):
        if fileWords2[w] == keyword:
            indices.append(w)
    print("The indices of the keyword in the list of words in the file are:", indices)
        

        
