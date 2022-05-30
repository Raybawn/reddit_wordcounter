# Import dependencies
import os
import pathlib
import praw
import sqlite3
import pandas as pd
import re
import emoji
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from dotenv import load_dotenv
from sqlalchemy import create_engine

# API Connection
load_dotenv()

# Get credentials from .env file
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
user_agent = os.getenv("user_agent")

# Instantiate
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
subreddit = reddit.subreddit("Wallstreetbets")


# Set different variables
postLimit = 100
posts = []
words = []
tablename = "wallstreetbets_tbl"
listOfTables = []
dbName = "Reddit.sqlite3"

# Add Posts to list and tokenize submission titles
for submission in subreddit.new(limit=postLimit):
    posts.append(
        [submission.title, submission.upvote_ratio, submission.score, submission.num_comments, submission.created_utc]
    )
    post_words = list(
        set(word_tokenize(submission.title.lower().replace("'", "")))
    )  # create list with unique words from submission title
    words.extend(post_words)

    # print(f"Title: {submission.title}")
    # print(f"Ratio: {submission.upvote_ratio}, Score: {submission.score}, Comments: {submission.num_comments}")
    # print("")

# Set different filters
stop_words = set(stopwords.words("english"))  # Filter out stopwords
nonPunct = re.compile(".*[A-Za-z0-9].*")  # Filter out words without alphanumeric characters

# Function to filter out emoji characters
def remove_emoji(string):
    return emoji.get_emoji_regexp().sub("", string)


# Filter stopwords and special characters out
filtered_words = [remove_emoji(w) for w in words if not w in stop_words and nonPunct.match(w)]

filtered_list_df = pd.DataFrame(filtered_words).stack().value_counts().reset_index(name="count")
filtered_list_df.columns = ["word", "count"]
print(filtered_list_df.head(10))

# Visualization with seaborn
sns.barplot(data=filtered_list_df.head(10), x="word", y="count")
plt.show()

'''
# SQLite Handling
try:
    sqliteConnection = sqlite3.connect(dbName)
    sqlite_create_table_query = f"""CREATE TABLE IF NOT EXISTS {tablename} (
        index INT PRIMARY KEY NOT NULL,
        title TEXT NOT NULL,
        upvote_ratio FLOAT NOT NULL,
        score INTEGER NOT NULL,
        number_of_comments INTEGER NOT NULL,
        created FLOAT NOT NULL
        );"""

    cursor = sqliteConnection.cursor()
    print("Successfully connected to SQLite")

    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("SQLite connection is closed")

# Create DataFrame with posts
allPosts = pd.DataFrame(posts, columns=["title", "upvote_ratio", "score", "number_of_comments", "created"])

# Add DataFrame to SQL Database
engine = create_engine("sqlite:///" + dbName, echo=False,)
allPosts.to_sql(tablename, con=engine, if_exists="replace")
'''
