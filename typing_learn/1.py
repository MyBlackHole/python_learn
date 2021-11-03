# a = 2
# print('1 + a = ', 1 + a)


# def add(a):
#     return a + 1
#
#
# add('2')

# a: int = 1
# print('5 + a = ', 5 + a)


# def add(aa: [int, float]) -> [int, float]:
#     return aa + 1
#
#
# print(add(1.5))

# names: list = ['l', 'Guido']
# version: tuple = (1, 2)
# operations: dict = {'show': False, 'sort': True}

# # List
# from typing import List
#
# # a: List[int or float] = [1, 1.1]
# # print(a)
# # b: List[int or float or bool] = [1, True, 'a', dict()]
# # print(b)
#
# a: List[List[int]] = [[1], ['s']]
# print(a)

# # Tuple
# from typing import Tuple
#
# a: Tuple[int, str] = (1, 'st')
# b: Tuple[int, Tuple[str]] = (1, ('1ck',))


# # Dict, Mapping
# from typing import Dict, Mapping
#
#
# def size(rect: Mapping[str, int]) -> Dict[str, int]:
#     return {'a': rect['a'] + 100, 'b': rect['b']}

# # AbstractSet, Set
# from typing import AbstractSet, Set
#
# # s: set = set()
#
#
# def describe(s: AbstractSet[int]) -> Set[int]:
#     return set(s)


# # Sequence, List
# from typing import Sequence, List
#
#
# def square(elements: Sequence[float]) -> List[float]:
#     return [x ** 2 for x in elements]


# # NoReturn
# from typing import NoReturn
#
#
# def hello() -> NoReturn:
#     print('hello')

# # Any
# from typing import Any
#
#
# def add(a: Any) -> Any:
#     return a + 1


# # TypeVar
# from typing import TypeVar
#
# height = 1.75
# Height = TypeVar('Height', int, float, None)
#
#
# def get_height() -> Height:
#     return height


# # NewType
# from typing import Tuple, NewType
#
# Person = NewType('Person', Tuple[str, int, float])
# person = Person(('Mike', 22, 1.75))


# # Callable
# from typing import Callable, Any
#
#
# def add(a: Any) -> Any:
#     return "any"
#
#
# print(Callable, type(add), isinstance(add, Callable))
#
#
# def date(year: int, month: int, day: int) -> str:
#     return f'{year}-{month}-{day}'
#
#
# def get_date_fn() -> Callable[[int, int, int], str]:
#     return date
#
#
# print(get_date_fn()(1, 2, 3))

# # Union
# from typing import Union, Callable
#
#
# def process(fn: Union[str, Callable]):
#     if isinstance(fn, str):
#         # str2fn and process
#         pass
#     elif isinstance(fn, Callable):
#         fn()


# # Generator
# from typing import Generator
#
#
# def echo_round() -> Generator[int, float, str]:
#     sent = yield 0
#     while sent >= 0:
#         sent = yield round(sent)
#     return 'Done'
#
#
# def infinite_stream(start: int) -> Generator[int, None, None]:
#     while True:
#         yield start
#         start += 1

from typing import Union

data = Union[list, str, None]

i: data = None

