#!/usr/bin/env python

import pytest
from greeter import make_app


@pytest.fixture
def app():
    return make_app()
