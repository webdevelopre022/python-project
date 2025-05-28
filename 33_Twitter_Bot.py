import tweepy
import time
from datetime import datetime

# Replace with your own credentials
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_TOKEN_SECRET = "your_access_token_secret"

# Authentication
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Tweets you want to schedule
scheduled_tweets = [
    {"time": "14:30", "text": "Hello Twitter! #firsttweet"},
    {"time": "15:00", "text": "Here's another scheduled tweet! #pythonbot"},
]

def post_tweet(text):
    try:
        api.update_status(text)
        print(f"[{datetime.now()}] Tweeted: {text}")
    except Exception as e:
        print(f"Error posting tweet: {e}")

def scheduler_loop():
    posted = set()
    while True:
        now = datetime.now().strftime("%H:%M")
        for tweet in scheduled_tweets:
            if tweet["time"] == now and tweet["time"] not in posted:
                post_tweet(tweet["text"])
                posted.add(tweet["time"])
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    print("Twitter bot started...")
    scheduler_loop()
