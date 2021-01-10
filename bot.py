import praw
from helper import read_cid, read_secret, read_agent

cid = read_cid()
secret = read_secret()
agent = read_agent()

reddit = praw.Reddit(
     client_id=cid,
     client_secret=secret,
     user_agent=agent
)

sr = reddit.subreddit("ProgrammerHumor")

for post in sr.hot(limit=10):
    print("***************************************************************************")
    print(post.title)