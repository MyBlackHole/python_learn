#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.mark.xfail(reason="我知道他是错的")
def test_api():
    a = 1
    b = 1
    assert a != b
