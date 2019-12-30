
import http.cookiejar, urllib.request
cookie = http.cookiejar.CookieJar()
handle = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handle)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + " = " + item.value)