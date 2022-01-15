import os
from multiprocessing import Process
from fastapi import FastAPI
import uvicorn


cmd = "/home/black/Firmcode/PythonProjects/ZFDM/gitee/deployment-warehouse/Code/ser_service/configs/opensmile-linux/bin/SMILExtract -C /home/black/Firmcode/PythonProjects/ZFDM/gitee/deployment-warehouse/Code/ser_service/configs/is09-13/IS10_paraling.conf -I /home/black/Firmcode/PythonProjects/ZFDM/gitee/deployment-warehouse/Code/ser_service/tmp/upload_audio/aa5eb541-7a47-41ad-915b-0308ae0251e5.wav -O /home/black/Firmcode/PythonProjects/ZFDM/gitee/deployment-warehouse/Code/ser_service/tmp/features/single_feature_163807626173.csv"


def process1():
    print("process1 start")
    os.system(cmd)
    print("process1 end")
    return 0


def process2():
    print("process2 start")
    print("process2 end")
    return 0


app = FastAPI()


@app.get("/")
def get():
    process1()
    return "ok"


if __name__ == "__main__":
    # uvicorn.run(app)
    # Process(target=process1).start()
    Process(target=uvicorn.run, args=(app,)).start()
