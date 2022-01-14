import tweepy
import csv
import pandas as pd
c_k="khb07AHhEEp5IYu89fihSNJPT"
c_skey="VJc0XhNjbsOaTZ0PDIvN4s3aIhhLxHGASBpb0z4VvckxRj7MPk"
acc_token="702507771724328960-J6HTeEAwGbST2DtTMaoqYaW5OTpS6P9"
acc_token_key="nQB0Zw8kQpUQBpqNGe9qlNemq0VWGCDU5tr5H6HGqxwii"
auth=tweepy.OAuthHandler(c_k,c_skey)
auth.set_access_token(acc_token,acc_token_key)
api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open('yoga1.csv','a+')
tweet1=[]

csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#yoga",count=100,
                           lang="en",
                           since="2019-01-01").items():
    print(tweet.created_at,tweet.text)
    tweet1.append(tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('ascii')])
    
   

