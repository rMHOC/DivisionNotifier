__author__ = 'jb567'
import praw
import json
import gspread
import re
from oauth2client.client import SignedJwtAssertionCredentials

r = praw.Reddit('Model House of Commons: Division Notifier - version 1')
u = str(input('Reddit Username: '))
p = str(input('Password: '))
r.login(u,p)
sub = r.get_subreddit('mhocmp+mholvote')
lastSub = ''
#Start Loop here in production
new = sub.get_new(limit=10)
