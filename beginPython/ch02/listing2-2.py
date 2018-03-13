# Split up a URL of the form http://www.something.com
from pip._vendor.distlib.compat import raw_input

url = raw_input('Please enter the URL: ')
domain = url[11:-4]

print ("Domain name: " + domain)