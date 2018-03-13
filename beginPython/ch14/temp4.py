import socket,select

s = socket.socket()
host = socket.gethostname()
port = 8000
s.bind((host,port))

s.listen(5)
inputs = [s]

while True:
    rs,ws,es = select.select(inputs,[],[])
    for r in rs:
        if r is s:
            c,addr = s.accept()
            print('got connection from ')
            print(addr)
            inputs.append(c)
        else:
            try:
                data = r.recv(1024)
                disconnected = not data
            except socket.error:
                disconnected = True

            if disconnected:
                print(r.getpeername())
                print('disconnected.')
                inputs.remove(r)
            else:
                print(data)
