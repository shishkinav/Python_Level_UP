from lesson04.source_home_work.lesson03_python_advanced.client.__main__ import getMessageServer, sendMessageServer
import unittest


class test_getMessageServer(unittest.TestCase):
    def testequal(self):
        self.assertEqual(getMessageServer(b'hello'), 'hello')

class test_sendMessageServer(unittest.TestCase):
    def testequal(self):
        self.assertEqual(
            sendMessageServer('привет сервер это я '),
            b'{"command": "\\u043f\\u0440\\u0438\\u0432\\u0435\\u0442",'
            b' "text": ["\\u0441\\u0435\\u0440\\u0432\\u0435\\u0440",'
            b' "\\u044d\\u0442\\u043e", "\\u044f", ""]}'

        )

if __name__ == '__main__':
    unittest.main()
