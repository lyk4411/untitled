
import http.cookiejar, urllib.request
cookie = http.cookiejar.CookieJar()
handle = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handle)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + " = " + item.value)


from urllib.parse import quote,unquote
keyword = '你好'
url = 'http://www.baidu.com/s?wd=' + quote(keyword)
print(url)
print(unquote('http://www.baidu.com/s?wd=%E4%BD%A0%E5%A5%BD'))