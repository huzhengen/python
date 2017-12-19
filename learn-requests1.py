import requests

# r = requests.get('https://www.baidu.com/')
r = requests.get('http://httpbin.org/get?name=zhangsan&age=33')
# print(type(r))
# print(r.status_code)
print(type(r.text))
# print(r.text)
# print(r.cookies)
# print(r.content)
print(r.content.decode('utf-8'))
print(r.json())