#!/usr/bin/env python
#coding:utf-8

import select
import socket
import queue


listen_addr=('0.0.0.0',8000)
#监听服务器
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    server.bind(listen_addr)
    server.setblocking(0)
except socket.error as e:
    print (e)
    exit(0)

server.listen(500)

print("starting up on %s port %s"%listen_addr)

inputs=[server,]  #监测服务器端，毕竟server本身也是一个fd，文件描述符

outputs=[]    #这里存放的是内核返回的活跃的客户端连接，就是服务器需给send data的客户端连接


message_queue={}

#开始循环监测事件
while True:
    print("waiting for next event...")   #

    readable,writeable,exceptionl=select.select(inputs,outputs,inputs)#如果没有任何fd就绪，那么程序一直会阻塞在这里
    "可以recv  可以send  exception"
    for s in readable:  #每一个s就是一个socket
        "处理新的客户端连接，并统一接受他们的数据"
        if s is server:   #由于上面我们server自己页当成一个fd放在了inputs列表里，传给了select，如果这个s是select代表这个fd就绪
            #如果server就绪，那就说明又有新的客户端的连接到了
            client,addr=s.accept()
            print("new connection from",addr)
            client.setblocking(0)

            """有客户端连接进来就把这个连接先放在select列表中，
                现在这些列表中的连接都会交给select去监听，如果列表中有一个客户端发来数据
                那么这个客户端所连接的对应fd就会转变成就绪状态，select就会将这个就绪状态的连接
                返回给用户程序的（即readable中）
                最后循环这个readable列表，取出这个连接，并只接受这些数据暂时存放
            """
            inputs.append(client)

            #往字典中添加一个队列用于暂时存放这个客户端连接传来的数据
            message_queue[client]=queue.Queue()

        #如果不是server，那么就是原来连接的客户端有数据来了
        else:
            #接受
            data=s.recv(1024)
            if data:
                print("receive come from %s",s.getpeername()[0],data)
                message_queue[s].put(data)  #收到的数据先放到对应的queue中，一会返回数据给客户端
                if s not in outputs:
                    outputs.append(s)  #为了不影响处理与其他客户端的连接。这里不立刻返回数据给客户端， 先放着，等会一起处理发送数据

            else: #如果没有收到客户端的数据，表示客户端断开了
                print("client connection break")

                if s in outputs:
                    outputs.remove(s) #清除已经断开的连接，没不会有信息发送给客户端了
                inputs.remove(s)

                del message_queue[s]


    for s in writeable:   #现在处理没有处理完客户端连接，就是接着前面向客户端发送数据
        try:
            next_msg=message_queue[s].get_nowait() #从队列中删除这个项目并伴随没有阻塞的返回这个项目（get）

        except queue.Empty:
            print("client [%s] ")%(s.getpeername()[0]),
            print("queue is empty")
            outputs.remove(s)

        else:
            print("sending msg to [%s]"%(s.getpeername()[0].encode()),next_msg) #输出客户端的信息
            s.send(next_msg.upper())

    for s in exceptionl:   #处理出现异常的连接
        print("handling exception for",s.getpeername())
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queue[s]