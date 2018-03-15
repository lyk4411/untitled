from urllib.request import urlopen
import re
p = re.compile('<a .*?><a .*? href="(.*?)">(.*?)</a>')
text = urlopen('http://python.org/community/jobs').read()
print(str(text))
# for url, name in p.findall(str(text)):
#     print("(name: %s ( url: %s))" % (name,url))
