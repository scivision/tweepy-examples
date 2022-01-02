import typing as T
from pathlib import Path

import tweepy


def get_api(key: Path, access: Path) -> tweepy.Client:
    bearer_token = Path(key).expanduser().read_text().strip()
    access_token = Path(access).expanduser().read_text().strip()
    # consumer_key, consumer_secret = Path(consumer).expanduser().read_text().split("\n")
    return tweepy.Client(bearer_token=bearer_token, access_token_secret=access_token)


def get_followed(client: tweepy.Client, username: str) -> T.Iterator[tweepy.User]:
    """
    Iterate over accounts followed
    """

    for user in tweepy.Paginator(client.get_users_following, username):
        yield user
