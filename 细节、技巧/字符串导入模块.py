import importlib

math = importlib.import_module('math')
print(math.sin(2))

fz = importlib.import_module('loguru_learn.封装')
fz.logger.info("1")

# logger = importlib('loguru_learn.封装')
