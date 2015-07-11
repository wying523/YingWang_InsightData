Insight Data Engineering - Coding Challenge
===========================================================

Author: Ying WANG 

Graduate student at University of Michigan -- Ann Arbor

If you have any problem with running the program, please contact me: wying@umich.edu

This code is for Insight Data coding challenge. 

This code is written in python @version 2.7.10


Additional Modules
===========================================================


additional module: numpy

In order to run stream_tweeter/StreamData.py you will need additional module: tweepy


File Strcture
===========================================================


#### File src/words_tweeted.py 
counts the frequency that each word appears in the tweets.txt.


it coverts all letters to lower cases. e.g. "YOU" is the same as "you"

#### File src/median_unique.py
updates the number of unique words in each tweet as the tweet comes in.


it coverts all letters to lower cases. e.g. "YOU" is the same as "you"


#### File stream_tweeter/StreamData.py 
accesses the tweeter API and stream the real time tweets from tweeter.com


and save the tweets in tweet_input/tweets.txt

