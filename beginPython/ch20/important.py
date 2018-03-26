import sys
print(sys.path)
import os

#获取项目路径下的目录

# os.chdir('项目路径')

#打印出项目路径下的目录
for file in os.listdir(os.getcwd()):
     print(file)

#将项目路径保存
# sys.path.append('项目路径')

# 注意：如果要导入该项目其他模块的包名，应将导入的方法写在上面方法的后面，如下：

import sys
print(sys.path)
import os
os.chdir('F:/Users/lyk/PycharmProjects/untitled/beginPython/ch20/')
for file in os.listdir(os.getcwd()):
     print(file)
sys.path.append('F:/Users/lyk/PycharmProjects/untitled/beginPython/ch20/')

print("==================================")
print(sys.path)
