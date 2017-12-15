#!/usr/bin/python
# -*- coding: utf-8 -*-
from urllib import request,error

try:
	response = request.urlopen('http://pythonsite.com/1111.html')
except error.URLError as e:
	print(e)
	print(e.reason)