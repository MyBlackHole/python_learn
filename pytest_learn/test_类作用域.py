#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope="class")
def class_scope():
    print("类级别的fixtue")


@pytest.mark.usefixtures("class_scope")
class TestClassScope:
    def test_1(self):
        pass

    def test_2(self):
        pass
