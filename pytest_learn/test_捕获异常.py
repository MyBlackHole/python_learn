#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


def test_raises():
    l = [1, 2]
    with pytest.raises(TypeError) as e:
        i = l['1']
    exec_msg = e.value.args[0]
    assert exec_msg == 'list indices must be integers or slices, not str'
