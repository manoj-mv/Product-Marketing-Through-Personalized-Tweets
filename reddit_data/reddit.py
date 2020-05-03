# -*- coding: utf-8 -*-

import praw
import re
#import itertools
import threading
#import os

cliend_id = "TcFb5VctDT8gQg"
cliend_secret = "gqfnfOSqhvHQHAyndC32BroEeA8"

reddit = praw.Reddit(client_id=cliend_id,
                     client_secret=cliend_secret, user_agent='USERAGENT')

labels = ['automotive', 'movies', 'food',
          'travel', 'technology', 'sports', 'politics','health']

path_to_save = "/home/manoj/twitter_interest/reddit_data/reddit_extracted/"
def extract_by_label(subreddit):
    print(subreddit)
    a = reddit.subreddit(subreddit).top('all')
    print(a)
    #count = 0
    for k, i in enumerate(a):
        #count = 0
        title = i.title
        submission = reddit.submission(id=i.id)
        for j in submission.comments:
            try:
                body = j.body
                #print(type(body))
                body = re.sub(
                    '(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '', body)
                if(len(body) < 35):
                    continue
                txt = open(path_to_save+subreddit+"_"+str(k)+".txt", "w",encoding='utf-8',errors = 'ignore')
                lab = open(path_to_save+subreddit+"_"+str(k)+".lab", "w",encoding='utf-8',errors = 'ignore')

                txt.write(title+"\n"+body)
                lab.write(subreddit)
            except:
                pass

threads = len(labels)
threads_list = []
for i in range(threads):
    t1 = threading.Thread(target=extract_by_label, args=(labels[i],))
    threads_list.append(t1)


for i in threads_list:
    i.start()
    
