#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

content = '''hello 123456 world_this
my name is zhangsan'''

result1 = re.match('^hello.*?(\d+).*?san$', content, re.S)
print(result1)
print(result1.group(1))