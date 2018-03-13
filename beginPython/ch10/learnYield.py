import os
import time
# file_list = []
def findFile(path):
    print("path:" + path)
    listFile = os.listdir(path)
    print("listFile：" + str(listFile))
    for file in listFile:
        try:
            file =os.path.join(path,file)
            if os.path.isfile(file):
                yield file               # test1
                #file_list.append(file)  # test2
                print("file:" + file)
            else:
                print("join file:" + str(file))
                # t1 = findFile(file) # yield会产生一个generator，需要你用for等语句来显示
                #                # 调用才会产生值，你在findFile函数里面调用的findFile
                #                # 只是一个generator，并没有用for语句来产生值。
                # t1.send(None)
                # t1.send(None)
                # t1.send(None)
                # t1.send(None)
                # t1.send(None)

                for i in findFile(file):
                     yield i

        except WindowsError as e:
            # 捕获系统不允许访问的文件夹导致的异常，会让程序无法进行下去
            # 将不允许访问的文件夹，直接跳过该文件夹
            print(e)
            continue
        except Exception as e:
            print(e)



start = time.time()
print('start time : ' + str(start))
t = findFile(r'F:\Users\lyk\PycharmProjects\untitled\beginPython\ch10')
# t.send(None)
# t.send(None)
# t.send(None)
# t.send(None)
print(list(t))
# for i in t:
#     try:
#         # print("str:" + str(i))
#         #str(i)
#         pass
#     except UnicodeDecodeError:
#         pass
print('use time : ' + str(time.time() - start))

# start = time.time()
# print('start time : ' + str(start))
# findFile(r'F:\Users\lyk\PycharmProjects\untitled\beginPython\ch10')
# for i in file_list:
#     try:
#         print("str:" + str(i))
#     except UnicodeDecodeError:
#         pass
# print('use time : ' + str(time.time() - start))