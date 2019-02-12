# dailyrandomscpbot

A bot that posts a random SCP every day on dailyrandomscp.tumblr.com

# How It Works
The `scp.txt` file contains a list of SCP article names. A random line is chosen from this file and is posted onto the tumblr blog. The line is then removed from the file to prevent duplicates. The script is run daily by a cron job.
