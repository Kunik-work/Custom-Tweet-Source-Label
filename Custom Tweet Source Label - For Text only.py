import tweepy

auth = tweepy.OAuthHandler("write your API key", "write your API secret key")
auth.set_access_token("write your Access token", "write your Access token secret")
api = tweepy.API(auth)

tweet = input("Sass Up A Tweet")

api.update_status(status =(tweet))

print ("Done!")
