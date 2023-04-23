# !/usr/bin/env python
# -*- coding: utf-8 -*-


class TestClass(object):
    x = "this"

    def test_one(self):
        assert "h" in self.x

    def test_two(self):
        x = "hello"
        assert x == "hi"
