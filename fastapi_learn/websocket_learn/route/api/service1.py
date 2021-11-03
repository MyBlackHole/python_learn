from fastapi import WebSocket


def test1(request_dict: dict, websocket: WebSocket):
    print(request_dict)
    websocket.send("")
