import tweepy
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Set up Twitter authentication
client = tweepy.Client(
    consumer_key=os.getenv("TWITTER_CONSUMER_KEY"),
    consumer_secret=os.getenv("TWITTER_CONSUMER_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_KEY"),
    access_token_secret=os.getenv("TWITTER_ACCESS_SECRET"),
)

def run_twitter_etl():
    try:
        # Fetch tweets from Elon Musk's timeline using API v2
        response = client.get_users_tweets(
            id='elonmusk',
            max_results=100,  # Adjust as needed
            tweet_fields=['created_at', 'public_metrics']
        )

        # Extract relevant tweet details
        tweet_list = []
        for tweet in response.data:
            tweet_list.append({
                "user": tweet.author_id,  # v2 gives author_id instead of screen_name
                "text": tweet.text,
                "favorite_count": tweet.public_metrics['like_count'],
                "retweet_count": tweet.public_metrics['retweet_count'],
                "created_at": tweet.created_at
            })

        # Convert to DataFrame & save
        df = pd.DataFrame(tweet_list)
        filename = f'refined_tweets_{datetime.now().strftime("%Y%m%d%H%M%S")}.csv'
        df.to_csv(filename, index=False)
        print(f"✅ Data saved to {filename}")

    except tweepy.TweepyException as e:
        print(f"❌ Twitter API Error: {e}")

# Run the function
if __name__ == "__main__":
    run_twitter_etl()

