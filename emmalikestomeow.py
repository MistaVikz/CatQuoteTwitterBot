#!/usr/bin/env python
import sys
import os
import random
from twython import Twython
from os import listdir
from random import choice

# Required for API access
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

iTags = " #cats #CatsOfTwitter"

# Access Twitter API
api = Twython (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )


# Current Directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Return acceptable file types
def contentType(filename):
    return contType[filename[filename.rfind(".")+1:].lower()]

# True if the file is an acceptable image
def isImage(filename):
    filename = filename.lower()
    return filename[filename.rfind(".")+1:] in contType

# Tweet a random picture from the specified directory
# Will need to switch to upload_media later
def tweetPic():
    dir = "/home/pi/Pictures/Emma/"
    images = [f for f in listdir(dir) if isImage(f)]
    r = choice(images)
    
    with open(dir + r, 'rb') as photo:
        message = 'Meow!' + iTags
        api.update_status_with_media(status=message, media=photo)

# Tweet a random quote from quotes.txt
def tweetQuote():
    
    try:
        quoteFile = open(os.path.join(__location__,'quotes.txt'),'r')
        quoteList = quoteFile.readlines()
        quoteFile.close()

        rChoice = random.randrange(len(quoteList))

        quoteTags = iTags + " #catquotes"
        api.update_status(status=quoteList[rChoice] + quoteTags)
        return None
        
    except IOError:
        return None
        
if __name__ == "__main__":
    tweetQuote()
    tweetPic()
