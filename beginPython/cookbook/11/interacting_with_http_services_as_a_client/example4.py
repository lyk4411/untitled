# Example of a HEAD request

import requests

resp = requests.head('http://www.python.org/index.html')

status = resp.status_code
print(resp.headers)
last_modified =	resp.headers['Location']
content_type = resp.headers['Connection']
content_length = resp.headers['Content-length']

print(status)
print(last_modified)
print(content_type)
print(content_length)
