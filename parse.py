#!/usr/bin/python

import csv
import sys

#Scan a row of a csv (single caption) for phrases and return an list of them
def handleRow(str):
    wordList = str.split()
    phrases = [""]
    numPhrases = 0
    for word in wordList:
        if word[0].isupper():
            #print word
            phrases[numPhrases] = phrases[numPhrases] + word.rstrip('.').rstrip(',') + " "
        else:
            phrases.append("");
            numPhrases = numPhrases +1
        #print phrases
    phrases = [x for x in phrases if x != ""]
    retval = []
    for phrase in phrases:
        retval.append(phrase[0:len(phrase)-1])
    return retval


sourceCSV = open(sys.argv[1], 'rb') #usage is ./parse.py test.csv
targetCSV = open('results.csv', 'wb')
try:
    reader = csv.reader(sourceCSV)
    phrases2D = [] #list of lists from handleRow
    for row in reader:
        phraseList = handleRow(row[0])
        if len(phraseList) != 0:
            phrases2D.append(phraseList)

    finals = {} #dictionary of unique phrases and their counts
    for phrases1D in phrases2D:
        for phrase in phrases1D:
            try:
                finals[phrase] = finals[phrase] + 1
            except:
                finals[phrase] = 1

    print finals
    writer = csv.writer(targetCSV)
    for key,value in finals.items():
        writer.writerow( (key, value) )

finally:
    sourceCSV.close()
    targetCSV.close()

