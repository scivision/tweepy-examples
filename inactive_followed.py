#!/usr/bin/env python
"""
writes accounts a username is following to CSV file

uses a read-only Oauth2 Twitter key
"""

import typing as T
import argparse
from pathlib import Path

import tweepy_clean
import tweepy


p = argparse.ArgumentParser()
p.add_argument("username", help="Twitter username")
p.add_argument("out_csv", help=".csv file to write")
p.add_argument("keyfile", help="path to oauth key")
P = p.parse_args()

api = tweepy_clean.get_api(P.username, P.keyfile)

times: T.Dict[str, tweepy.User] = {}

followed = tweepy_clean.get_followed(api, P.username)

outfile = Path(P.out_csv).expanduser()
cols = ["username", "name", "last_tweet_time", "followed"]
with outfile.open("wt", encoding="utf-8", errors="ignore") as f:
    f.write(",".join(cols) + "\n")
    for user in followed:
        name = user.name.replace(",", "")
        try:
            last_time = user.status.created_at
        except AttributeError:
            last_time = ""
        line = f"{user.screen_name},{name},{last_time}, {user.friends_count}\n"
        f.write(line)
        print(line, end="")
