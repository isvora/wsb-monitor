import praw

from constants.Credentials import API
from constants.Globals import SUBREDDIT_NAME


class WSBMonitor:

    @staticmethod
    def main():
        print("Starting Tickery...")

        # Obtain reddit object
        reddit = praw.Reddit(
            client_id=API["client_id"],
            client_secret=API["client_secret"],
            user_agent=API["user_agent"])

        # Create a subreddit object
        subreddit = reddit.subreddit(SUBREDDIT_NAME)


if __name__ == "__main__":
    WSBMonitor.main()