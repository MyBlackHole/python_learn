def consumer():
    r = ''
    print('start')
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200'


def produce(cs):
    cs.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = cs.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    cs.close()


c = consumer()
produce(c)
