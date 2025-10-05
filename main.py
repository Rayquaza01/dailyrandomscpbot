import argparse
import json
import os
import random
import re

import requests
from bs4 import BeautifulSoup
import pytumblr


ap = argparse.ArgumentParser()
ap.add_argument("--refresh", action="store_true")
ap.add_argument("--series", type=str, nargs="?")
ap.add_argument("--count", type=int, nargs=1)
ap.add_argument("--dry-run", action="store_true")
args = ap.parse_args()


SCP_INDEX = [
    "scp-series",
    "scp-series-2",
    "scp-series-3",
    "scp-series-4",
    "scp-series-5",
    "scp-series-6",
    "scp-series-7",
    "scp-series-8",
    "scp-series-9",
]
JOKE_INDEX = "joke-scps"


articles = []


def refresh():
    # include main scps
    # check each series page to grabs links and titles for all scps
    for idx, page in enumerate(SCP_INDEX):
        res = requests.get("https://scp-wiki.wikidot.com/" + page)
        soup = BeautifulSoup(res.text, "html.parser")
        for item in soup.find(class_="content-panel").find_all("li"):
            link = item.find("a")
            # invalid scps have the "newpage" class.
            # only include a page if it does not have a class
            # also, links must match /scp-(numbers)
            if not link.has_attr("class") and re.match(r"^\/scp-\d+$", link.get("href")):
                articles.append({
                    "series": str(idx + 1),
                    "title": item.text,
                    "link": link.get("href"),
                })

    # include joke scps
    res = requests.get("https://scp-wiki.wikidot.com/" + JOKE_INDEX)
    soup = BeautifulSoup(res.text, "html.parser")
    for panel in soup.find_all(class_="content-panel"):
        for item in panel.find_all("li"):
            link = item.find("a")
            # include all links in <li> for joke scps
            articles.append({
                "series": "J",
                "title": item.text,
                "link": link.get("href"),
            })

    with open("scps.json", "w") as f:
        f.write(json.dumps(articles))


def main():
    if args.refresh:
        refresh()
    else:
        with open("scps.json", "r") as f:
            articles = json.loads(f.read())

        client = None
        if not args.dry_run:
            client = pytumblr.TumblrRestClient(
                os.environ["CONSUMER_KEY"],
                os.environ["CONSUMER_SECRET"],
                os.environ["OAUTH_TOKEN"],
                os.environ["OAUTH_SECRET"],
            )

        if args.series:
            articles = list(filter(lambda x: x["series"] == args.series, articles))

        for _ in range(args.count[0]):
            scp = random.choice(articles)
            post = f"# Today's random SCP of the day is [{scp['title']}](https://scp-wiki.wikidot.com{scp['link']})"
            print(post)
            if client:
                client.create_text("dailyrandomscp", state="queue", tags=["scp"], body=post, format="markdown")



if __name__ == "__main__":
    main()
