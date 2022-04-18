from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/cookie/")
def Login(request: Request):
    content = {"message": "yy_cookie"}
    response = JSONResponse(content=content)
    response.set_cookie(key="username", value="zlkt")
    return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
    # uvicorn.run(app="app:app", host="::", port=8080, reload=True)
