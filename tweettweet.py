from sqlite3 import Cursor
import tweepy
import time

# regenerate all when finished
auth = tweepy.OAuthHandler('jDJSllbgO4uvgGlArUw0yk1Nl',
                           'eLZN6dsnxGWJstpppfWVkuvRJivYqXHGADiJXvSGqwviSmvsOv')
auth.set_access_token('261268802-BVe2nRyIHsfHZfsUlveYGhDCNtaS2FYmwByIbZAw',
                      'bvDAxUhuXabFem9cm6m0lFg2u2Gte4rBA2OV3ukVqxeTl')

api = tweepy.API(auth)
user = api.me()

# public_tweets = api.home_timeline()

# for tweet in public_tweets:
#     print(tweet.text)

def limit_handler(cursor):
  try:
    while True:
      yield cursor.next()
  except tweepy.RateLimitError:
    time.sleep(1000)

# bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
  if follower.name =='afasia.gr':
    follower.follow()
  print(follower.name)
