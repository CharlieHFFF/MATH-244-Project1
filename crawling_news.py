import requests
import pandas as pd
import time
from datetime import datetime, timedelta, timezone

def get_reddit_headlines(subreddit="worldnews", start_date="2016-01-01", end_date="2024-12-31", limit=25):
    base_url = "https://api.pushshift.io/reddit/search/submission/"
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
    all_headlines = []

    while current_date <= end_date:
        unix_start = int(current_date.timestamp())
        unix_end = int((current_date + timedelta(days=1)).timestamp())

        print(unix_start)
        # Request top 25 posts for the day, sorted by score
        params = {
            "subreddit": subreddit,
            "after": unix_start,
            "before": unix_end,
            "sort_type": "score",  # Sorting by highest upvotes
            "sort": "desc",
            "size": limit,  # Limit top 25
            "fields": ["title", "score", "created_utc"]
        }

        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json().get("data", [])
            for post in data:
                all_headlines.append({
                    "date": current_date.strftime("%Y-%m-%d"),
                    "title": post.get("title", ""),
                    "score": post.get("score", 0),
                    "timestamp": datetime.fromtimestamp(post["created_utc"], timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
                })
        
        # Move to the next date
        current_date += timedelta(days=1)
        time.sleep(1)  # Delay to avoid rate limits

    return pd.DataFrame(all_headlines)

df = get_reddit_headlines()
df.to_csv("data/reddit_news.csv", index=False)