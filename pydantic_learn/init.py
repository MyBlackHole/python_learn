from typing import Any, List

from pydantic import BaseModel


class BaseDomain(BaseModel):
    __exceptions: List[Any] = []
    a: int

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = 3
        self.print()

    def print(self):
        print(self.a)

b = BaseDomain(a=1)
print(b)
