import twitter_authentaction
from  bot_log import setup_logger
import logging
import tweepy
import pandas as pd
from openpyxl.workbook import Workbook

log=setup_logger(__name__, "logs/python_lan.txt",logging.INFO)
api=twitter_authentaction.create_api(log)

#Recent tweets from accounts you follow
#timeline = api.home_timeline()
#for tweet in timeline:
#    log.info(f"{tweet.user.name} said {tweet.text}")

#timeline = api.search(q="python language -filter:retweets",lan='en',count=200)
timeline = tweepy.Cursor(api.search, q="python language -filter:retweets", lang='en').items(2000)
df=pd.DataFrame([],columns=['user_name','text'])
print(df.shape)
for i,tweet in enumerate(timeline):
    #log.info(f"{tweet.user.name} said {tweet.text}")
    df.loc[i,'user_name'] = tweet.user.name
    df.loc[i,'text'] = tweet.text

print(df.shape)
df.to_excel('{}.xlsx'.format("pandas_search_tweet123"))



""" for tweets in tweepy.Cursor(api.home_timeline).items():
    log.info(tweets.text) """

#your Recent Tweets
#tweets = api.user_timeline()
#for tweet in tweets:
#    log.info(tweet.created_at)
#    log.info(tweet.id_str)
#    log.info(tweet.text)

#Make a Tweet
#tweet = api.update_status("Made with Tweepy")

# tweets from a specific user
#trump_tweets = api.user_timeline('realdonaldtrump',count=200)
#for tweet in trump_tweets:
#    log.info(tweet.text)



#User_statuses_count:The number of Tweets (including retweets) issued by the user.
#favorite_count:The number of Tweets this user has liked in the account’s lifetime.
#friends_count : The number of users this account is following (AKA their “followings”). 
#followers_count : 	The number of followers this account currently has


""" df = pd.DataFrame(columns = [ 'User', 'Tweets', 'User_statuses_count', 
                                'user_followers', 'User_location', 'User_verified',
                              'fav_count', 'rt_count', 'tweet_date'])



def stream(data, file_name):
    i = 0
    for tweet in tweepy.Cursor(api.search, q=data, count=100, lang='en').items():
        #log.info(tweet)
        #print.info(i, end='\r')
        df.loc[i, 'Tweets'] = tweet.text
        df.loc[i, 'User'] = tweet.user.name
        df.loc[i, 'User_statuses_count'] = tweet.user.statuses_count
        df.loc[i, 'user_followers'] = tweet.user.followers_count
        df.loc[i, 'User_location'] = tweet.user.location
        df.loc[i, 'User_verified'] = tweet.user.verified
        df.loc[i, 'fav_count'] = tweet.favorite_count
        df.loc[i, 'rt_count'] = tweet.retweet_count
        df.loc[i, 'tweet_date'] = tweet.created_at
        i+=1
        if i == 10000:
            df.to_excel('{}.xlsx'.format(file_name))
            break
        else:
            pass

stream(data = ['python'], file_name = 'Python_language')
##500KTweeplesForRamCharan
#stream(data = ['#SarkaruVaariPaata'], file_name = 'logs/SarkaruVaariPaata123') """