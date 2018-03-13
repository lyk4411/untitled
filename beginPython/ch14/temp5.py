import socket,select

s = socket.socket()
host = socket.gethostname()
port = 8000
s.bind(('0.0.0.0',port))

fdmap = {s.fileno():s}

s.listen(5)
p = select.poll()
p.register(s)

while True:
    events = p.poll()
    for fd,event in events:
        if fd in fdmap:
            c,addr = s.accept()
            print('got connection from :')
            print(addr)
            p.register(c)
            fdmap[c.fileno()]=c
        elif event & select.POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                print(fdmap[fd].getpeername())
                print('disconnect')
                p.unregister(fd)
                del fdmap[fd]
            else:
                print(data)
