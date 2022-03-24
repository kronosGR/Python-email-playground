import tweepy

# regenerate all when finished
auth = tweepy.OAuthHandler('jDJSllbgO4uvgGlArUw0yk1Nl',
                           'eLZN6dsnxGWJstpppfWVkuvRJivYqXHGADiJXvSGqwviSmvsOv')
auth.set_access_token('261268802-BVe2nRyIHsfHZfsUlveYGhDCNtaS2FYmwByIbZAw',
                      'bvDAxUhuXabFem9cm6m0lFg2u2Gte4rBA2OV3ukVqxeTl')

api = tweepy.API(auth)
user = api.me()

print(user.name)

# public_tweets = api.home_timeline()

# for tweet in public_tweets:
#     print(tweet.text)
