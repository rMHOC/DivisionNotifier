__author__ = 'jb567'
import praw
from pprint import pprint
#{{METHODS
def lords(s):
    print('lords: ' + str(s.url))

def pleb(s):
    print('commons: ' + str(s.url))
#}}

r = praw.Reddit('Model House of Commons: Division Notifier - version 1')
u = str(input('Reddit Username: '))
p = str(input('Password: '))
r.login(u,p)
sub = r.get_subreddit('mhocmp+mholvote')
lastSub = ''
#Start Loop here in production
new = sub.get_new(limit=10)

for submission in new:
#TODO
    if submission.id == lastSub:
#If the loop has already submitted it
        break
    if 'mhocmp' in submission.url.lower():
        pleb(submission)
    elif 'mholvote' in submission.url.lower():
        lords(submission)


