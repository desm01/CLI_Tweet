from main.tweet import Tweeter
from unittest.mock import patch

@patch('Tweeter.get_tweet', return_value='ABC')
def test_return_true_if_tweet_is_correct_length(self):
    classUnder = Tweeter()
    assert classUnder.should_post_tweet('ACV') == True
    assert Tweeter().should_post_tweet('ABC') == True