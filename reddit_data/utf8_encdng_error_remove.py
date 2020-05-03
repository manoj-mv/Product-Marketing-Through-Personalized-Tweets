# -*- coding: utf-8 -*-

# !!!!! place the file into /home/manoj/twitter_interest/reddit_data/reddit_extracted
import os
import re
files = os.listdir("/home/manoj/twitter_interest/reddit_data/reddit_extracted")
files.sort()
print(files)
count = 0
for i in files:
    f = open(i,'r',encoding='utf-8',errors='ignore')
    content = f.read()
    f.close()
    f = open(i,'w',encoding='utf-8',errors='ignore')
    f.write(content)
    f.close()
        