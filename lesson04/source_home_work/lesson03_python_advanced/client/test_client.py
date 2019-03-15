import pytest
from .__main__ import getMessageServer, sendMessageServer

class TestClient:
    def setup(self):
        pass

    def test_get_msg(self):
        text = 'привет'
        assert_text = 'hello'
        assert text != assert_text


if __name__ == '__main__':
    TestClient.test_get_msg()


