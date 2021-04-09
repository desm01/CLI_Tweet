import tweepy
import pickle

list_of_keys = []
yourTweet = ""

try:
    with open('keys.pkl', 'rb') as f:
         list_of_keys = pickle.load(f)
except:
    print("Enter Consumer Key")
    consumer_key = input()
    
    print ("Enter Consumer Secret Key")
    consumer_secret = input()

    print("Enter Access Key")
    access_key = input()

    print("Enter Access Secret")
    access_secret = input()

    list_of_keys.append(consumer_key)
    list_of_keys.append(consumer_secret)
    list_of_keys.append(access_key)
    list_of_keys.append(access_secret)

    with open('keys.pkl', 'wb') as f:
        pickle.dump(list_of_keys, f)
    
def getTweet():
    tweet = input("Enter a tweet\n")
    return tweet

yourTweet = getTweet()

while(len(yourTweet) < 1 or len(yourTweet) > 280):
    print("Error, please try again\n\nTweets must be between 1-280 characters long")
    yourTweet = getTweet()

auth = tweepy.OAuthHandler(list_of_keys[0], list_of_keys[1])

auth.set_access_token(list_of_keys[2], list_of_keys[3])

api = tweepy.API(auth)
api.update_status(yourTweet)
