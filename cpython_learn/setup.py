from distutils.core import setup
from Cython.Build import cythonize

# python3 setup.py build_ext
# 编译构建 so (动态连接库)
setup(ext_modules = cythonize("./test.py"))
