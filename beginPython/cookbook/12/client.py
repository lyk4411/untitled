import socket
import sys
from base64 import encode

messages = ['This is the message. ',
            'It will be sent ',
            'in parts.',
            ]
server_address = ('localhost', 15000)

# Create a TCP/IP socket
socks = [socket.socket(socket.AF_INET, socket.SOCK_STREAM),
         socket.socket(socket.AF_INET, socket.SOCK_STREAM),
         ]

# Connect the socket to the port where the server is listening
print ( sys.stderr, 'connecting to %s port %s' % server_address)
for s in socks:
    s.connect(server_address)

for message in messages:

    # Send messages on both sockets
    for s in socks:
        print ( sys.stderr, '%s: sending "%s"' % (s.getsockname(), message))
        s.send(message.encode())

    # Read responses on both sockets
    for s in socks:
        data = s.recv(1024)
        print ( sys.stderr, '%s: received "%s"' % (s.getsockname(), data))
        if not data:
            print ( sys.stderr, 'closing socket', s.getsockname())
            s.close()