import requests
data = {'name':'aaa','age':'22'}
r = requests.post("http://httpbin.org/post",data = data)
print(r.text)

r = requests.post('http://httpbin.org/post',data = data)
print(r.text)
