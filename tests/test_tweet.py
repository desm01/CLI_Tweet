from main.tweet import Tweeter

def test_return_true_if_tweet_is_correct_length():
    classUnder = Tweeter()
    assert classUnder.should_post_tweet('ABC') == True