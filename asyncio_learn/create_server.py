import asyncio
 
class EchoServer(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport
 
    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))
 
        print('Send: {!r}'.format(message))
        self.transport.write(data)
 
        print('Close the client socket')
        self.transport.close()
 
loop = asyncio.new_event_loop()
# loop = asyncio.get_event_loop()
# Each client connection will create a new protocol instance
coro = loop.create_server(EchoServer, '127.0.0.1', 8888)
server = loop.run_until_complete(coro)
print('Serving on {}'.format(server.sockets[0].getsockname()))
loop.run_forever()
