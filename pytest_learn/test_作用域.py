#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope='function')
def func_scope():
    pass


@pytest.fixture(scope='module')
def mod_scope():
    pass


@pytest.fixture(scope='session')
def sess_scope():
    pass


@pytest.fixture(scope='class')
def class_scope():
    pass


def test_multi_scope(sess_scope, mod_scope, func_scope):
    pass
