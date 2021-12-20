import tweepy
import pickle

class Tweeter:


    list_of_keys = []
    yourTweet = ""

    def __init__(self):
        try:
            with open('keys.pkl', 'rb') as f:
                self.list_of_keys = pickle.load(f)
        except:
            self.list_of_keys.append("consumer_key")
            self.list_of_keys.append("consumer_secret")
            self.list_of_keys.append("access_key")
            self.list_of_keys.append("access_secret")

            with open('keys.pkl', 'wb') as f:
                pickle.dump(self.list_of_keys, f)
        

    def post_tweet(self):
        tweet = self.get_tweet()
        self.enqueue_task(tweet) if self.should_post_tweet(tweet) else self.log_error()

    def get_tweet(self):
        return input("Enter a tweet\n")

    def should_post_tweet(self, tweet):
        return False if len(tweet) > 280 or len(tweet) < 1 else True

    def enqueue_task(self, tweet):
        auth = tweepy.OAuthHandler(self.list_of_keys[0], self.list_of_keys[1])
        auth.set_access_token(self.list_of_keys[2], self.list_of_keys[3])
        api = tweepy.API(auth)
        api.update_status(tweet)
