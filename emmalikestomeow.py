#!/usr/bin/env python
import sys
import os
import random
from twython import Twython

# Access to Twitter API
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

# Support different image types
contType= {"jpg" : "image/jpeg",
           "jpeg" : "image/jpeg",
           "png" : "image/png",
           "gif" : "image/gif"}

# Current Directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

#Tweet a picture of Emma
def tweetPic():
    photo = open('/home/pi/Pictures/Emma/Photo 2014-11-04, 8 45 59 PM.jpg', 'rb')
    twitter.update_status_with_media(status="Meow!", media=photo)

# Tweet a random quote from quotes.txt
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

        iTags = " #cats #CatsOfTwitter #catquotes"
        api.update_status(status=quoteList[rChoice] + iTags)
        return None
        
    except IOError:
        return None
        
if __name__ == "__main__":
    tweetQuote()
    # tweetPic()
