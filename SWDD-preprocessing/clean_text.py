#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/5 14:56
# @Author  : cendeavor
# @Site    : 
# @File    : clean_text.py
# @Software: PyCharm

import jsonlines
from util import WeiboText

weibo_cleaner = WeiboText()

filename = 'depressed.jsonl'
    
with open(filename, "r", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        tweets = item['tweets']
        for tweet in tweets:
            print(tweet['text'])
            raw_text = weibo_cleaner.get_raw_text(tweet['text'])
            print(raw_text)
            cleaned_text = weibo_cleaner.get_cleaned_text(tweet['text'])
            print(cleaned_text)
            break
        break
