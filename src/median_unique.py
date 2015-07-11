#InsightData Challenge
#Author: Ying Wang
#This code calculates the median for the unique word as the tweet comes in

import sys
import re
import numpy

InputFile = sys.argv[1]
OutputFile = sys.argv[2]
ListofNum = []

def main():
    library = re.compile(r"\S+", re.IGNORECASE)
    
    #empty the output file
    open(OutputFile, "w").close()
    
    #Read tweets
    with open(InputFile, "r") as fileIn:
        tweets = fileIn.readlines()
        #consider only lower cases
        tweets = [item.lower() for item in tweets]
        
    for oneTweet in tweets:
        Words = library.findall(oneTweet)
        #ignore the empty tweets
        if len(Words) != 0:
            getNumofUniq(Words)                 

def getNumofUniq(Words):
    #this function find the number of unique words in a tweet
    WordCount = {}
    count = len(Words)
    
    for word in Words:
        WordCount[word] = WordCount.setdefault(word,0) + 1
        
    for word in WordCount:         
        if WordCount[word] != 1:
            count = count - WordCount[word] + 1
            
    ListofNum.append(count)
    getMedian(ListofNum)

def getMedian(ListofNum):
    #calculate the median number using numpy
    runningM = numpy.median(numpy.array(ListofNum))
    
    #write to file 
    with open(OutputFile, "a") as fileOut:
        print>>fileOut, "{0:.2f}".format(runningM)
    

if __name__ == "__main__" :
    main()
