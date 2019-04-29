

import os
names = os.listdir('.')
print(names)

names1 = [name for name in os.listdir('getting_a_directory_listing')
          if os.path.isfile(os.path.join('getting_a_directory_listing',name))]
print(names1)

names2 = [name for name in os.listdir('.')
          if os.path.isfile(os.path.join('.',name))]
print(names2)

import sys
print(sys.getfilesystemencoding())
