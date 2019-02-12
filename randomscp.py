#!/usr/bin/env python3
import json
import pytumblr
import pyscp
import random


def randomSCP():
    with open("scp.txt", "r") as scp:
        choices = scp.read().split("\n")
    choices.pop()  # remove last item, always empty string
    choice = random.choices(choices)[0]
    choices.remove(choice)
    with open("scp.txt", "w") as scp:
        scp.write("\n".join(choices))
    return choice


def main():
    wiki = pyscp.wikidot.Wiki("www.scp-wiki.net")
    with open("tumblr_creds.json", "r") as js:
        creds = json.loads(js.read())
    client = pytumblr.TumblrRestClient(
        creds["consumer_key"],
        creds["consumer_secret"],
        creds["oauth_token"],
        creds["oauth_secret"]
    )
    rand = wiki(randomSCP())
    client.create_link("dailyrandomscp", title=rand.title, url=rand.url, state="published",
                       tags=["scp"], description="Today's random SCP of the day is:" + rand.title)


if __name__ == "__main__":
    main()
