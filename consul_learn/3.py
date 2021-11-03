from tornado.ioloop import IOLoop
from tornado.gen import coroutine
from consul.base import Timeout
from consul.tornado import Consul


class Config(object):
    def __init__(self, loop):
        self.foo = None
        loop.add_callback(self.watch)

    @coroutine
    def watch(self):
        c = Consul()

        # asynchronously poll for updates
        index = None
        while True:
            try:
                index, data = yield c.kv.get('foo', index=index)
                if data is not None:
                    self.foo = data['Value']
            except Timeout:
                # gracefully handle request timeout
                pass


if __name__ == '__main__':
    loop = IOLoop.instance()
    _ = Config(loop)
    loop.start()
