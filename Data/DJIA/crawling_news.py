import pandas as pd
import time
from datetime import datetime, timedelta
import praw

reddit = praw.Reddit(
    client_id="arp1qIyuSmQJB1sfGhjjwA", 
    client_secret="aef33TymFgJkrhCAjxZ9_amHqPAiQw", 
    user_agent="script:worldnews_scraper:v1.0 (by u/Ok_Pepper_7745)",
    redirect_uri="http://localhost:8080" 
)

def get_reddit_headlines(subreddit="worldnews", start_date="2016-01-01", end_date="2024-12-31", limit=25):
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
    all_headlines = []

    while current_date <= end_date:
        try:
            print(f"Fetching top {limit} posts for {current_date.strftime('%Y-%m-%d')}...")
            top_posts = reddit.subreddit(subreddit).top(time_filter="day", limit=limit)

            for post in top_posts:
                all_headlines.append({
                    "date": current_date.strftime("%Y-%m-%d"),
                    "title": post.title,
                    "score": post.score,
                    "num_comments": post.num_comments,
                    "url": post.url
                })

            current_date += timedelta(days=1)
            time.sleep(2)  
        
        except Exception as e:
            print(f"Error on {current_date.strftime('%Y-%m-%d')}: {e}")
            time.sleep(5)  # Wait before retrying
            continue

    return pd.DataFrame(all_headlines)

df = get_reddit_headlines()
df.to_csv("DJIA/reddit_worldnews_top25_2008_2016.csv", index=False)