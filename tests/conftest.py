import pytest
import uuid


@pytest.fixture(scope="function")
def token():
    return str(uuid.uuid4())
