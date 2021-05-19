import time
import tweepy
import logging
import os

from config import create_api
from  bot_log import setup_logger

def follow_followers(api,log):

    log = setup_logger(__name__, "bot_logs.txt")

    log.info("Retrieving and following followers")

    for follower in tweepy.Cursor(api.followers).items():
        if(not follower.following):
            log.info(follower.name)
            log.info(str(follower.name)[:5])
            if(str(follower.name)[:5] != "Pavan"):
                #log.info(f"haven't followed this FOllower ::  {follower.name}")
                log.info(f"NOW , Following {follower.name}")
                follower.follow()

def main(log):
    api = create_api(log)
    while True:
        follow_followers(api,log)
        log.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    log = setup_logger(__name__, "bot_logs.txt")   
    main(log)