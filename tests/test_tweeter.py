from os import times_result
from src.tweeter import Tweeter
from tests.fake_api import FakeApi
import random
import string

def test_should_post_tweet():
    fakeApi = FakeApi()
    classUnder = Tweeter(fakeApi)
    assert classUnder.should_post_tweet('ABC') == True
    longString = ''.join(random.choice(string.ascii_lowercase) for x in range(300))
    assert classUnder.should_post_tweet(longString) == False

def test_enqueue_task():
    fakeApi = FakeApi()
    classUnderTest = Tweeter(fakeApi)
    result = classUnderTest.enqueue_task('ABC')
    assert result == 'ABC'
