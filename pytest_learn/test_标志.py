#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


# 1. 显式指定函数名，通过::标记
# pytest test_标志.py::test_fun1
# 2. 使用模糊匹配，-k 选项标记
# pytest -k func1 def test_标志.py
# 3. 第三种，使用 pytest.mark 在函数上进行标记。
@pytest.mark.func1
def test_func1():
    assert 1 == 1


@pytest.mark.func2
def test_func2():
    assert 1 != 1
