import sys
import re
import os


InputPath =sys.argv[1]
OutputPath = sys.argv[2]
WordCount = {}


def readTweets():
    #Read tweets
    os.chdir(InputPath)
    with open('tweets.txt', "r") as fileIn:
        tweets = fileIn.read()
        
    countWord(tweets)

def countWord(tweets):
    regex = re.compile(r'\S+', re.IGNORECASE)
    colWidth = 0
    
    for word in regex.findall(tweets):
        WordCount[word] = WordCount.setdefault(word,0)+1
        colWidth = max(len(word),colWidth)
                       
    #write to the output file
    os.chdir(OutputPath)
    with open('outV1.txt','w') as out:
        for word in sorted(WordCount):
            print>>out, "".join(word.ljust(colWidth)),"\t\t",WordCount[word]
        
if __name__ == '__main__'  :
    readTweets()
    
