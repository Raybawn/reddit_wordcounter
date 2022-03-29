# Import dependencies
import os
import pathlib
import praw
import csv

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# Get credentials from .env file
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
user_agent = os.getenv("user_agent")

# Instantiate
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
subreddit = reddit.subreddit("Wallstreetbets")


# Set path for CSV File
csv_filename = "wsbReddit.csv"
csv_path = "Reddit Project/CSV/" + csv_filename
csv_exists = os.path.exists(csv_path)


# Set post limit
postLimit = 1000
posts = []

for submission in subreddit.new(limit=postLimit):
    print(f"Title: {submission.title}")
    print(f"Ratio: {submission.upvote_ratio}, Score: {submission.score}, Comments: {submission.num_comments}")
    print("")

    posts.append([submission.title, submission.upvote_ratio, submission.score, submission.num_comments])


allPosts = pd.DataFrame(posts, columns=["Title", "Upvote Ratio", "Score", "Number of comments"])
allPosts.to_csv(csv_path, mode="w")
print("All posts are added to the CSV file...")


# _____Coinmarketcap API_____
# This example uses Python 2.7 and the python-request library.
"""
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

cmcAPIkey = os.getenv("cmcAPI")

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
parameters = {"start": "1", "limit": "100", "convert": "USD"}
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "0bb654bb-5bf0-4fba-898b-e45b14f31713",
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
"""
