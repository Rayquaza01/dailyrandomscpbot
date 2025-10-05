#!/usr/bin/env python3
import random
import argparse
import os
import pyscp
import pytumblr

client = pytumblr.TumblrRestClient(
    os.environ["CONSUMER_KEY"],
    os.environ["CONSUMER_SECRET"],
    os.environ["OAUTH_TOKEN"],
    os.environ["OAUTH_SECRET"],
)

def randomSCP():
    num = random.randint(1, 8999)
    link = "scp-" + str(num).zfill(3)
    return link


def main():
    wiki = pyscp.wikidot.Wiki("scp-wiki.wikidot.com")

    # hack to retry if generates a bad article
    while True:
        try:
            rand = wiki(randomSCP())
            title = rand.title
            url = rand.url
        except:
            continue
        break

    post = "# Today's random SCP of the day is [" + title + "](" + url + ")"
    # client.create_text("dailyrandomscp", state="queue", tags=["scp"], body=post, format="markdown")
    print(post)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("number", help="Number of posts to queue", type=int)
    args = vars(ap.parse_args())

    for i in range(args["number"]):
        main()
