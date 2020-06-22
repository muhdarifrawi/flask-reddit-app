from flask import Flask, render_template, request, redirect, url_for
import praw
import os

app = Flask(__name__)

#"magic code" - - boilerplate
if __name__ == "__main__":
   app.run(host=os.environ.get("IP"),
      port=int(os.environ.get("PORT")),
      debug=True)

reddit = praw.Reddit(
                        client_id=os.getenv("CLIENT_ID"),
                        client_secret=os.getenv("CLIENT_SECRET"),
                        user_agent=os.getenv("USER_AGENT")  
                    )

print(reddit.read_only)

subreddit = reddit.subreddit("NonZeroDay")

for submissions in subreddit.new(limit=10):
    print(submissions.title)

test = os.getenv("TEST")
print("look here" , test)