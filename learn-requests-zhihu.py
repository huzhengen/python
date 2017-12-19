import requests

headers={
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

r = requests.get('https://www.zhihu.com', headers=headers)

# print(r.cookies)

for key,value in r.cookies.items():
	print(key+'='+value)
