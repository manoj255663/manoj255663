
from tkinter import *
import tweepy

consumer_key="khb07AHhEEp5IYu89fihSNJPT"
consumer_secret="VJc0XhNjbsOaTZ0PDIvN4s3aIhhLxHGASBpb0z4VvckxRj7MPk"
access_token="702507771724328960-J6HTeEAwGbST2DtTMaoqYaW5OTpS6P9"
access_token_secret="nQB0Zw8kQpUQBpqNGe9qlNemq0VWGCDU5tr5H6HGqxwii"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

master = Tk()

Label(master, text='User ID').grid(row=0) 
def callback():
    api.create_friendship(e1.get())
    
b1=Button(text='Follow',command=callback)
def callback():
    api.destroy_friendship(e1.get())
b2=Button(text='UnFollow',command=callback)
e1 = Entry(master) 
e1.grid(row=0, column=1) 
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)

mainloop()


