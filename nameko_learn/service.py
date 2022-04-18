from nameko.rpc import rpc


def func(value: str):
    return value


class Compute(object):
    name = "compute"

    @rpc
    def compute(self, value: str):
        return {"msg": func(value=value)}


# nameko run service --broker amqp://admin:password@192.168.1.65
