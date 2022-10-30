#!/usr/bin/env python3
import pyscp
import pyperclip
import random


def randomSCP():
    num = random.randint(1, 7999)
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
            print(rand + " failed!")
            continue
        break

    post = "# Today's random SCP of the day is [" + title + "](" + url + ")"

    print(post)
    pyperclip.copy(post)


if __name__ == "__main__":
    main()
