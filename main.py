__author__ = 'jb567'
from datetime import datetime
from pprint import pprint #For Debugging
import praw #Python API
import time
#{{METHODS

def aristocrats(s):
    print('lords: ' + str(s.url))
    for lord in lords:
        print(lord)
        #do messages
    r.send_message('jb567', 'A Division in the House of Lords', '''
My Noble Lord,

There is a division bar in the House of Lords

[here](''' + s.url + ''')

*-The Gentleman Usher of the Black Rod*''')

def plebs(s):
    print('commons: ' + str(s.url))
    for mp in mps:
        print(mp)
    r.send_message('jb567', 'A Division in the House of Commons', '''
My Honorable Friend,

There is a division bar in the House of Commons

[here](''' + s.url + ''')

*-The Gentleman Usher of the Black Rod*''')
#do messages
#}}
#{{CHECK TIME ELAPSED
def check_lords(s, v):
    if (datetime.timestamp(datetime.now()) -  int(s.created_utc))  > 172800:
        r.send_message('/r/jb567', 'Division Ended', s.url)
        tbf.remove(v)

def check_commons(s, v):
    print('Stop Whining COmmons!')

    

r = praw.Reddit('Model House of Commons: Division Notifier - version 1')
p = str(input('Password for blackrodbot: '))
r.login("blackrodbot",p)
sub = r.get_subreddit('mhocmp+mholvote')
#GET MP AND LORD LIST:
with open('lords.txt') as f:
    lords = [x.strip('\n') for x in f.readlines()]

with open('mps.txt') as f:
    mps = [x.strip('\n') for x in f.readlines()]

with open('sent.txt') as f:
    lastSub = [x.strip('\n') for x in f.readlines()]

with open('toBeCompleted.txt') as f:
    tbf = [x.strip('\n') for x in f.readlines()]

#Start Loop here in production

new = sub.get_new(limit=10)

for submission in new:
    if not str(submission.id) in lastSub:
        if 'mhocmp' in submission.url.lower():
            plebs(submission)
        elif 'mholvote' in submission.url.lower():
            aristocrats(submission)
        lastSub.append(submission.id)
        tbf.append(str(submission.id))
        with open('sent.txt', 'r+') as f:
            f.write("\n".join(lastSub))


for vote in tbf:
    s = r.get_submission(submission_id=vote)
    if 'mholvote' in s.url.lower():
        check_lords(s, vote)
    else:
        check_commons(s, vote)
with open('toBeCompleted.txt', 'r+') as f:
    f.write("\n".join(tbf))
