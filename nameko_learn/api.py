from fastapi import FastAPI
from nameko.standalone.rpc import ClusterRpcProxy

app = FastAPI()
CONFIG = {"AMQP_URI": "amqp://admin:password@192.168.1.65"}


@app.get("/compute/{value}")
def compute(value: str):
    with ClusterRpcProxy(CONFIG) as rpc:
        result = rpc.compute.compute.call_async(value)
        return result.result()


@app.get("/opensmile")
def compute():
    with ClusterRpcProxy(CONFIG) as rpc:
        with open("./test.wav", "rb") as f:
            result = rpc.Opensmile.mq_opensmile_run.call_async(f.read())
        return result.result()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
