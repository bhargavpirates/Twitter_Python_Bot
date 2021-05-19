import tweepy
import logging
import os
from  bot_log import setup_logger

# Authenticatation to Twitter
def create_api(log):
    log.info("Start Authenthication Proces.......")
    auth = tweepy.OAuthHandler("SSSynQphdzOaYj34gsyvXxa35", "ISj85WgsCG68ERkNp539Y4qBg9GQXug3yR80lFEBASFRyuJlYo")
    auth.set_access_token("516506229-Vz1HPbK2qz1qrUyLBTyZXX0qYjrEvACjVk3kC2dj", "9CA3bPBHySeYE4bpAcsFQ9xhiuj1DHZULZ7P5k1F1LGCv")
    
    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    
    #log = setup_logger(__name__, "logs/bot_logs.txt")

    try:
        api.verify_credentials()
    except Exception as e:
        log.error("Error during authentication :: {}".format(e))
        raise e

    log.info("Authentication Completed")
    return api

if(__name__=="__main__"):
    log = setup_logger(__name__, "logs/bot_logs.txt")
    create_api(log)