from flask import url_for

HTTP_OK = 200


def test_alive_response(client):
    """Test aliveness endpoint."""
    res = client.get(url_for('alive'))
    assert res.status_code == HTTP_OK
    assert res.data == b'Application is alive'


def test_readiness_response(client):
    """Test readiness endpoint."""
    res = client.get(url_for('healthy'))
    assert res.status_code == HTTP_OK
    assert res.data == b'Application is healthy'


def test_index_response(client):
    """Test homepage."""
    res = client.get(url_for('index'))
    assert res.status_code == HTTP_OK
    assert res.data == b'Hello world!'
