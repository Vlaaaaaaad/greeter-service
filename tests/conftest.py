import pytest
from greeter.app import make_app


@pytest.fixture
def app():
    return make_app()
