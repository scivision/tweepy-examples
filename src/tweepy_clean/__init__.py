import typing as T
from pathlib import Path

import tweepy


def get_api(username: str, key: Path) -> tweepy.API:
    consumer_key, consumer_secret = Path(key).expanduser().read_text().split("\n")
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    return api


def get_followed(api, username: str) -> T.Iterator[tweepy.User]:
    """Iterate over accounts followed"""
    for user in tweepy.Cursor(api.friends, screen_name=username).items():
        yield user
