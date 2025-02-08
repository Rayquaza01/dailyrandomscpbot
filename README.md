# dailyrandomscpbot

A bot that posts a random SCP every day on dailyrandomscp.tumblr.com

# How It Works

A random number is generated (from 001 to 8999). The bot then looks up the article metadata on the SCP wiki, or generates a new number if there is no article with that number. Then, the post is queued to Tumblr.

The bot runs on GitHub Actions. It generates and queues 7 posts every Sunday.
