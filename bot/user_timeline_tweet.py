import csv
import config
from  bot_log import setup_logger
import logging
import tweepy
import pandas as pd
from openpyxl.workbook import Workbook

def get_all_tweets(api,screen_name,log):

    #Twitter only allows access to a users most recent 3240 tweets with this method    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []  
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print(f"getting tweets before {oldest}")
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        print(f"...{len(alltweets)} tweets downloaded so far")
    
    #transform the tweepy tweets into a 2D array that will populate the csv 
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]

    log.info(outtweets)
    
    #write the csv  
    with open(f'new_{screen_name}_tweets.csv', 'w',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)
    
    pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
    api=config.create_api()
    log=setup_logger(__name__, "bot_logs.txt",logging.INFO)
    get_all_tweets(api,'realdonaldtrump',log)