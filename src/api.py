import tweepy
import pickle

class Api:

    def __init__(self):
        list_of_keys = []
        try:
            with open('keys.pkl', 'rb') as f:
                list_of_keys = pickle.load(f)
        except:
                list_of_keys.append(input("Enter your consumer key"))
                list_of_keys.append(input("Enter your consumer secret"))
                list_of_keys.append(input("Enter your access key"))
                list_of_keys.append(input("Enter your access secret"))

                with open('keys.pkl', 'wb') as f:
                    pickle.dump(list_of_keys, f)

        auth = tweepy.OAuthHandler(list_of_keys[0], list_of_keys[1])
        auth.set_access_token(list_of_keys[2], list_of_keys[3])
        self.api = tweepy.API(auth)

    def update_status(self, tweet):
        self.api.update_status(tweet)