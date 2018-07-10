"""
Welcome to the SlowComcast community! Please contact u/McCossum to be an approved poster.

To set up make sure you pip install pyspeedtest and praw
You will also need to create an app permission at https://www.reddit.com/prefs/apps/
Select 'create application' and 'script'
Name it 'SlowComcastBot' with the description of 'Bot to post to r/SlowComcast when Comcast is slow'
'About url' can be left blank but 'redirect uri' should be 'http://localhost:8080'
Click 'create app' then add McCossum as a developer if you are so kind
You will relieve 'secret' and 'personal use script' codes to input below
'Personal use script' can be input for the clientID and 'secret for the clientSecret
This code can be run by navigating to the installed directory in command prompt and typing 'python SlowComcast.py'
"""

import pyspeedtest
import praw
from time import sleep

"""Things to personalize!"""
desiredSpeed = 50  # Please change 50 to the speed you are paying for!
isProvider = 'Comcast'  # Please change Comcast to your current provider
redditUsername = 'McCossum'  # Please change McCossum to your reddit username
redditPassword = 'NotMyPassword'  # Please change to your reddit password
clientID = 'NotMyClientID'  # Please change NotMyClientID to the ID given by oAuth
clientSecret = 'NotMyClientSecret'  # Please change NotMyClientSecret to the secret token given by oAuth
"""Ok that's enough personalization. Leave the rest to me."""

userAgent = 'SlowComcast used by u/' + str(redditUsername)
reddit = praw.Reddit(user_agent=userAgent, client_id=clientID, client_secret=clientSecret,
                     username=redditUsername, password=redditPassword)
t = 60
while True:
    speedTest = pyspeedtest.SpeedTest()
    currentSpeed = int(speedTest.download() / 1000000)
    if currentSpeed <= int(desiredSpeed * 0.75):
        sleep(60*5)
        t = 55
        speedTest = pyspeedtest.SpeedTest()
        currentSpeed = int(speedTest.download() / 1000000)
        if currentSpeed <= int(desiredSpeed * 0.75):
            print('Posting as u/' + redditUsername + ' to SlowComcast')
            postTitle = 'Hey ' + isProvider + ' I am paying for ' + str(desiredSpeed) +\
                        ' Mbps, but am only getting' + str(currentSpeed) + 'Mbps'
            reddit.subreddit('SlowComcast').submit(str(postTitle), selftext='To ensure the accuracy of this post 2 '
                                                                            'tests were done 5 minutes apart. Both '
                                                                            'came back at least 25% slower than '
                                                                            'I thought I was paying for.')
    else:
        t = 60
    sleep(60*t)
