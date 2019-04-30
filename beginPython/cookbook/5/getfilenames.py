

import os
names = os.listdir('.')
print(names)
print("================================================================")
names1 = [name for name in os.listdir('getting_a_directory_listing')
          if os.path.isfile(os.path.join('getting_a_directory_listing',name))]
print(names1)
print("================================================================")
names2 = [name for name in os.listdir('.')
          if os.path.isfile(os.path.join('.',name))]
print(names2)
print("================================================================")
import sys
print(sys.getfilesystemencoding())
print("================================================================")

print(os.listdir('.'))
print(os.listdir(b'.'))

print("================================================================")
def bad_filename(filename):
    return repr(filename)[1:-1]


print("================================================================")
for name in os.listdir('.'):
    try:
        print(bad_filename(name))
    except UnicodeEncodeError:
        print("=====================================")
        print(bad_filename(name))