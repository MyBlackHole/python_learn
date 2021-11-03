import grpc
import compute_pb2
import compute_pb2_grpc

_HOST = '127.0.0.1'
_PORT = '19999'


def main():
    with grpc.insecure_channel("{0}:{1}".format(_HOST, _PORT)) as channel:
        client = compute_pb2_grpc.ComputeStub(channel=channel)
        response = client.SayHello(compute_pb2.HelloRequest(helloworld="123456"))
    print("SayHello: " + response.result)
        response = client.SayHello(compute_pb2.HelloRequest(helloworld="123456"))
    print("SayHello: " + response.result)




if __name__ == '__main__':
    main()


