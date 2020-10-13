import praw

from constants.Credentials import API
from constants.Globals import SUBREDDIT_NAME


def monitor_daily_thread(subreddit):
    while True:
        # A subreddit stream will constantly look for new comments posted
        # skip_existing=True is used to only retrieve new submissions starting when the stream is created
        for comment in subreddit.stream.comments(skip_existing=True):
            # Get the submission of the comment. We are only interested in the daily discussion thread
            submission = comment.link_title
            if "Daily Discussion Thread" in submission:
                # Do stuff with our comment
                print(comment.body)


class WSBMonitor:

    @staticmethod
    def main():
        print("Starting WSB Monitor...")

        # Obtain reddit object
        reddit = praw.Reddit(
            client_id=API["client_id"],
            client_secret=API["client_secret"],
            user_agent=API["user_agent"])

        # Create a subreddit object
        print("Creating subreddit object...")
        subreddit = reddit.subreddit(SUBREDDIT_NAME)

        # Begin monitoring subreddit daily thread
        print("Begin monitoring daily thread...")
        monitor_daily_thread(subreddit)


if __name__ == "__main__":
    WSBMonitor.main()
