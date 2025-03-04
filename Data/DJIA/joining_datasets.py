import pandas as pd

news = pd.read_csv("DJIA/data/news.csv", header=0)
stock = pd.read_csv("DJIA/data/dow_jones_data.csv", skiprows=2)

# Select only the date and title columns
news = news[['date', 'title']]

# Pivot the table so that each unique date has titles as separate columns
news['title_number'] = news.groupby('date').cumcount() + 1
news = news.pivot(index='date', columns='title_number', values='title')

# Rename columns to "title 1", "title 2", etc.
news.columns = [f"title {col}" for col in news.columns]

# Reset index for a clean look
news.reset_index(inplace=True)

stock.columns = ["date", "close", "high", "low", "open", "volume"]

# Convert the date column to datetime format
stock["date"] = pd.to_datetime(stock["date"])
news['date'] = pd.to_datetime(news['date'])

merged_df = pd.merge(stock, news, on="date", how="left")

merged_df.to_csv("DJIA/data/combined_dataset.csv", index=False)