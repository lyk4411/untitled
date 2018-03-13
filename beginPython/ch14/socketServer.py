from socketserver import TCPServer,StreamRequestHandler
class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print("got connection from:")
        print(addr)
        self.wfile.write('thank you for connecting.'.encode())
server = TCPServer(('',6666),Handler)
server.serve_forever()