#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

content = 'extra things hello 123455 world_this is a Re Extra things'

result = re.search('hello.*?(\d+).*?Re', content)

# print(result)
# print(result.group(1))


html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''

# result2 = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(result2)
# print(result2.group(1))
# print(result2.group(2))

result3 = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(result3)
# print(type(result3))
# for result in result3:
	# print(result)

result4 = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>',html,re.S)
# print(result4)
# for result in result4:
# 	print(result[1])



content5 = """hello 12345 world_this
123 fan
"""

pattern5 = re.compile("hello.*fan",re.S)

result5 = re.match(pattern5 ,content5)
print(pattern5)
print(result5)
print(result5.group())