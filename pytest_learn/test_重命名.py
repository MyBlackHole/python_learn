#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(name='age')
def calculate_average_age():
    return 28


def test_age(age):
    assert age == 28
