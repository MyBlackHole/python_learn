from threading import Timer


class H:
    def __init__(self) -> None:
        self.a = "asa"
        pass

    def run(self):
        t = Timer(4.0, self.handler, [self.a])
        t.start()
        return t

    def handler(self, fh):
        print(fh)
        self.run()


print("end")
h = H()
h.run()
# t.cancel()
