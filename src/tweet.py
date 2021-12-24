class Tweeter:
    def __init__(self, api):
        self.api = api        

    def post_tweet(self):
        tweet = self.get_tweet()
        self.enqueue_task(tweet) if self.should_post_tweet(tweet) else self.log_error()

    def get_tweet(self):
        return input("Enter a tweet\n")

    def should_post_tweet(self, tweet):
        return False if len(tweet) > 280 or len(tweet) < 1 else True

    def enqueue_task(self, tweet):
        return self.api.update_status(tweet)

    def log_error():
        print("Error, Tweet is not the correct length")
