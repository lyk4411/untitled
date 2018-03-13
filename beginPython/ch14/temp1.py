from urllib.request import urlopen
import re
webpage = urlopen('http://www.baidu.com')

for line in webpage:
    m = re.search(r'<a href=(.*?)>',line.decode(),re.IGNORECASE | re.MULTILINE)
    if(m != None):
        print(m.group(1))


print("=================================================================================")
