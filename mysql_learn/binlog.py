import struct

class BinlogReader(object):
    BINLOG_HEADER_LEN = 19

    def __init__(self, binlog_fd):
        self.fd = binlog_fd
        self.consumers = []

    def __del__(self):
        self.fd.close()

    def add_consumer(self, consumer):
        self.consumers.append(consumer)

    def read_bytes(self, count):
        return self.fd.read(count)

    def loop(self):
        self.read_bytes(4)

        while True:
            type_code, event_length = self.read_header()

            if type_code is None or event_length == None:
                break

            for consumer in self.consumers:
                consumer.consume(type_code)

            self.fd.seek(event_length - self.BINLOG_HEADER_LEN, 1)


    def read_header(self):
        read_byte = self.read_bytes(self.BINLOG_HEADER_LEN)

        if read_byte:
            result = struct.unpack('=IBIIIH', read_byte)
            type_code, event_length = result[1], result[3]

            return type_code, event_length
        else:
            return None, None

class BinlogConsumer(object):
    def __init__(self):
        self.type_code_map = {}

    def consume(self, type_code):
        if type_code not in self.type_code_map:
            self.type_code_map[type_code] = 1
        else:
            self.type_code_map[type_code] += 1

    def print_obj(self):
        for type_code, count in self.type_code_map.items():
            print(type_code, count)

if __name__ == '__main__':
    binlog = input("Enter binlog file path: ")
    binlog_consumer = BinlogConsumer()

    binlog_fd = open(binlog, 'rb')
    binlog_reader = BinlogReader(binlog_fd)
    binlog_reader.add_consumer(binlog_consumer)
    binlog_reader.loop()

    print(binlog_consumer.print_obj())
