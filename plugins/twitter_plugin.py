import logging
import sys
import json

from datetime import datetime
from airflow.models import BaseOperator
from airflow.plugins_manager import AirflowPlugin
from airflow.utils.decorators import apply_defaults
from airflow.operators.sensors import BaseSensorOperator
import tweepy

log = logging.getLogger(__name__)

consumer_key = 'LpwQtgRjXmCFDPihxGWlnAA6M'
consumer_secret = '6cIdQJVKIRp3CKwqheu6sQEdjWam16zLlFcci4KelZhevaZJjP'
access_token = '60635122-6d6xVkFpeddtPQB3ltKeKnFak8eOkzg28vtsM9zC0'
access_token_secret = '9dbXPZTuTQJe4ipXU9QWYr9JtMNo4pTQLfx5SMdDbitQl'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class TwitterTimelineOperator(BaseOperator):

    @apply_defaults
    def __init__(self, my_operator_param, *args, **kwargs):
        self.operator_param = my_operator_param
        super(TwitterTimelineOperator, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info("Hello from TwitterTimelineOperator!")
        #from IPython import embed; embed()
        log.info('operator_param: %s', self.operator_param)

class TwitterTimelineSensor(BaseSensorOperator):

    @apply_defaults
    def __init__(self, *args, **kwargs):
        super(TwitterTimelineSensor, self).__init__(*args, **kwargs)
        #init tweepy conneciton


    def poke(self, context):
        user = api.me()
        #print("user.name:" + str(user))

        log.info("Get Followers:")

        #loop over tweepy followers

        try :
            number_of_followers = 0
            for follower in tweepy.Cursor(api.followers).items():
                #print(json.dumps(follower._json, indent=4, sort_keys=True))
                print("===========")
                print(follower.followers_count)
                print("===========")
                log.info(follower.screen_name+ "(" + str(follower.followers_count) + ")")
                number_of_followers += 1
                if number_of_followers > 20 :
                    break
        except tweepy.error.RateLimitError as e:
            log.info("Error: RateLimitError happends")
            return False 

        log.info("Going to check whether numbero_of_followers > 10")
        if(number_of_followers > 10):
            return True
        else:
            return False

class TwitterTimelinePlugin(AirflowPlugin):
    name = "TwitterTimelinePlugin"
    operators = [TwitterTimelineOperator, TwitterTimelineSensor]