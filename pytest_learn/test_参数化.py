#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest


@pytest.mark.parametrize("passwd", ["1", "2", "32"])
def test_passwd_length(passwd):
    assert len(passwd) == 1


# 多参数样例
@pytest.mark.parametrize("a, b", [["2", "3"], ["21", "12"]])
def test_a_b(a, b):
    assert len(a) == len(b)


# 参数组合
@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_x_y(x, y):
    print(f"[{x}, {y}]")


if __name__ == "__main__":
    pytest.main(["-s", "./test_参数化.py"])
