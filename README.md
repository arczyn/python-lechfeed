# python-lechfeed
Script that creates custom RSS feed from Lech Poznan's official website

It's one of my first Python scripts, written in April 2020. The official website of Lech Poznań doesn't provide any RSS feed, but I wanted to have it on my personal RSS reader. I run it on my private Synology NAS with a schedule. Script runs three times a day and keeps my updated with the news about my favourite football team.

Most important libraries used:
- request to connect
- BeautifulSoup to scrap
- re to remove problematic characters with regex
