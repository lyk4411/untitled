from concurrent.futures import ThreadPoolExecutor
import urllib.request

def fetch_url(url):
    u = urllib.request.urlopen(url)
    data = u.read()
    return data

pool = ThreadPoolExecutor(10)
# Submit work to the pool
a = pool.submit(fetch_url, 'http://hao123.com')
b = pool.submit(fetch_url, 'http://baidu.com')

# Get the results back
x = a.result()
y = b.result()
