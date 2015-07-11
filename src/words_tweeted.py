#InsightData Challenge
#Author: Ying Wang
#This code counts the words in txt file

import sys
import re

WordCount = {}
InputFile = sys.argv[1]
OutputFile = sys.argv[2]



def main():
    #Read tweets
    with open(InputFile, "r") as fileIn:
        tweets = fileIn.read()
        
    countWord(tweets)

def countWord(tweets):
    #consider only lower cases
    tweets = tweets.lower()
    library = re.compile(r"\S+", re.IGNORECASE)
    colWidth = 0
    
    for word in library.findall(tweets):
        WordCount[word] = WordCount.setdefault(word,0) + 1
        #set the width of the column to be the max length 
        colWidth = max(len(word),colWidth)
                       
    #write to the output file
    with open(OutputFile,"w") as out:
        for word in sorted(WordCount):
            print>>out, "".join(word.ljust(colWidth)),"\t\t",WordCount[word]
        
if __name__ == "__main__"  :
    main()
    
