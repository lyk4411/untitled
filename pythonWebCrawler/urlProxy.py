from urllib import request, parse
url = r'http://www.lagou.com/zhaopin/Python/?labelWords=label'

data = {
        'first': 'true',
        'pn': 1,
        'kd': 'Python'
    }
proxy = request.ProxyHandler({'http': '5.22.195.215:80'})  # 设置proxy
opener = request.build_opener(proxy)  # 挂载opener
request.install_opener(opener)  # 安装opener
data = parse.urlencode(data).encode('utf-8')
page = opener.open(url, data).read()
page = page.decode('utf-8')
print(page)