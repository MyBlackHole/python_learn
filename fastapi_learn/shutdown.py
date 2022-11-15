from fastapi import FastAPI
from loguru import logger

app = FastAPI()


@app.on_event("shutdown")
def shutdown_event():
    logger.info("shutdown")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
