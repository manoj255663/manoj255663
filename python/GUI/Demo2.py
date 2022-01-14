import tweepy
consumer_key="khb07AHhEEp5IYu89fihSNJPT"
consumer_secret="VJc0XhNjbsOaTZ0PDIvN4s3aIhhLxHGASBpb0z4VvckxRj7MPk"
access_token="702507771724328960-J6HTeEAwGbST2DtTMaoqYaW5OTpS6P9"
access_token_secret="nQB0Zw8kQpUQBpqNGe9qlNemq0VWGCDU5tr5H6HGqxwii"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user1 = api.get_user('@ManojCh68956115')
user2 = api.get_user('@Chetansunhare30')
print(user1.screen_name)
print(user2.screen_name)
api.show_friendship("@"+user1.screen_name,"@"+user2.screen_name)

