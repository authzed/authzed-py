import uuid

import pytest


@pytest.fixture(scope="function")
def token():
    return str(uuid.uuid4())
