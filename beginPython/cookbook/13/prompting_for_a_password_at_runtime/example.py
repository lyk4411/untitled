import getpass
import shutil


print(shutil.get_archive_formats())

user = getpass.getuser()
passwd = getpass.getpass()


print('User:', user)
print('Passwd:', passwd)

