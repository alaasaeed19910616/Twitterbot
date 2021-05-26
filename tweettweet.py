import tweepy
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.me()
print(user.name)
print(user.screen_name)
print(user.followers_count)

# Print tweets from you timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000)
        except StopIteration:
            break


# Be nice to your followers. Follow everyone!
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    print(follower.name)
    if follower.name == 'Usernamehere':
        follower.follow()

search_string = 'chose a word to use in the search search '
numbersOfTweets = 2  # number of tweets you want to hit

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()  # like the tweet
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
