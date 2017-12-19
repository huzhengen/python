#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

content = 'hello 123 4567 World_This is a regex Demo'

# result1 = re.match('^hello\s\d{3}\s\d{4}\s\w{10}.*Demo$', content)
# print(result1)
# print(result1.group())
# print(result1.span())

# result2 = re.match('^hello.*emo$', content)
# print(result2)

# result3 = re.match('^hello\s(\d+)\s(\d+)\sWorld.*Demo$', content)
# print(result3)
# print(result3.group(1))

result4 = re.match('^hello.*(\d+).*mo$', content)
print(result4.group(1))

result5 = re.match('^hello.*?(\d+).*mo$', content)
print(result5.group(1))