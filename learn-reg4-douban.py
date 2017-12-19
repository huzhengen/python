#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import re

content = requests.get('https://book.douban.com/').text
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
results = re.findall(pattern, content)
# print(results)
for result in results:
    url, name ,author, date = result
    author = re.sub('\s', '', author)
    author = re.sub('&nbsp;', ' ', author)
    date = re.sub('\s', '', date)
    print(name, author, date)