import sys,re
from beginPython.ch20.util import *

print ('<html><head><title>...</title><body>')

title = True
for block in blocks(sys.stdin):
    block = re.sub()
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')
        print('</body></html>')

