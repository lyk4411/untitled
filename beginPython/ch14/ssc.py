from socketserver import TCPServer,ThreadingMixIn,StreamRequestHandler
class Server(ThreadingMixIn,TCPServer):
    pass
class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('got connection from:')
        print(addr)
        self.wfile.write("thank you for connection.".encode())


server = Server(('',6666),Handler)
server.serve_forever()
