#!/usr/bin/python
# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq

doc = pq(url="http://www.baidu.com", encoding="utf-8")

print(doc('head'))