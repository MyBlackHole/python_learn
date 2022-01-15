from nameko.rpc import rpc
from fastapi import FastAPI
import uvicorn

app = FastAPI()

def func(value:str):
    return value


class Compute(object):
    name = "compute"

    @rpc
    def compute(self, value:str):
        return {"msg": func(value=value)}

@app.get("/get/{value}")
def get(value:str):
    return func(value=value)

if __name__ == "__main__":
    uvicorn.run(app)
