#Author: Ying WANG
#This code will stream real time tweets from tweeter
#in this particular case I am reading all tweets that contains 'data'
import tweepy
import json

# Authentication details.
consumer_key = 'nbvMJ1Vp4tIO9UikIcxbcpitq'
consumer_secret = '8xIx1bzJAnYHVwPXUQW7cVFlBfSLJ5zRI0djz2CTBEeHW7RVwk'
access_token = '3368702555-PLFZuWzWCwVJhWkpqk7gJo4AR3RIlfmCUQIZ4Ny'
access_token_secret = 'zeAdGpfyx101Hj3oQzi3iWgaEugEZidT3l4HdyWumufCe'

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # convert UTF-8 to ASCII 
        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'])
        print ''
        with open('./tweet_input/tweets.txt', "a") as tweetFile:
            print>>tweetFile, '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
            
        
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    #empty the output file
    open('tweets.txt', "w").close()
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print "Showing all new tweets for #data"

    stream = tweepy.Stream(auth, l)
    stream.filter(languages=["en"],track=['data'])
