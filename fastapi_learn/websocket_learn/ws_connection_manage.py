from typing import Dict
from fastapi import WebSocket


class WsConnectionManager:
    ws_manage = None
    # 存放激活的ws连接对象
    active_connections: Dict[str, WebSocket] = {}

    def __new__(cls):
        if cls.ws_manage is None:
            cls.ws_manage = object.__new__(cls)
        return cls.ws_manage

    async def connect(self, uid: str, ws: WebSocket):
        # 等待连接
        await ws.accept()
        # 存储ws连接对象
        self.active_connections[uid] = ws
        return ws

    def disconnect(self, uid: str):
        # 关闭时 移除ws对象
        if uid in self.active_connections:
            self.active_connections.pop(uid)
