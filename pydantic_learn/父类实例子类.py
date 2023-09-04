from typing import Dict, List

from pydantic import BaseModel


class Base(BaseModel):
    __type_map__ = {
        "map": "base",
        "key": "type",
    }
    type: str
    sup: str

    class TypeMap:
        MAP_KEY = "map"
        TYPE_KEY = "key"
        types: Dict = {}

        @classmethod
        def add(cls, ins_cls) -> None:
            type_map = ins_cls.__type_map__
            print(type_map)
            print(ins_cls)
            type_ = type_map[cls.MAP_KEY]
            assert type_ not in cls.types, f"{ins_cls}已经存在"
            cls.types[type_] = ins_cls

    def __init_subclass__(cls, **kwargs) -> None:
        cls.TypeMap.add(cls)
        return super().__init_subclass__(**kwargs)

    def __new__(cls, *args, **kwargs):
        if cls.TypeMap.TYPE_KEY not in cls.__type_map__:
            return super().__new__(cls)
        type_key = cls.__type_map__[cls.TypeMap.TYPE_KEY]
        print(cls)
        assert type_key in kwargs, f"{type_key}不存在"

        type_value = kwargs[type_key]
        new_cls = cls.TypeMap.types[type_value]
        return super().__new__(new_cls)

class ModelBase(Base):
    pass

class sup1(ModelBase):
    __type_map__ = {"map": "sup1"}


class sup2(ModelBase):
    __type_map__ = {"map": "sup2"}


class sup3(sup2):
    __type_map__ = {"map": "sup3"}


class sup4(ModelBase):
    __type_map__ = {"map": "sup4"}

info = {"type": "sup2", "sup": "this is sup1"}
m = sup4.parse_obj(info)
print(m, type(m))

# info = [
#     {"type": "sup1", "sup": "this is sup1"},
#     {"type": "sup2", "sup": "this is sup2"},
#     {"type": "sup3", "sup": "this is sup2", "sup3": "this is sup3"},
#     # {"type": "unknown", "extra": "this is extra"},
# ]
# obj = parse_obj_as(List[ModelBase], info)

# print(obj)

# [sup1(type='sup1', sup='this is sup1'), sup2(type='sup2', sup='this is sup2'), sup3(type='sup3', sup='this is sup2')]
