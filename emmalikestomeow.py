#!/usr/bin/env python
import sys
import os
import random
from twython import Twython

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def tweetQuote():
    api = Twython (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

    try:
        quoteFile = open(os.path.join(__location__,'quotes.txt'),'r')
        quoteList = quoteFile.readlines()
        quoteFile.close()

        rChoice = random.randrange(len(quoteList))
        
        api.update_status(status=quoteList[rChoice] + "#cats #CatsOfTwitter")
        return None
        
    except IOError:
        return None
        
if __name__ == "__main__":
    tweetQuote()
