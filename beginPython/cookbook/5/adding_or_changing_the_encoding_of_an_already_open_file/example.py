# Example of adding a text encoding to existing file-like object

import urllib.request
import io

u = urllib.request.urlopen('http://www.hao123.com')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()

print(text)

