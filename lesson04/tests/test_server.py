from lesson04.source_home_work.lesson03_python_advanced.server.__main__ import sendMessageClient, getMessageClient
import unittest


class test_getMessageClient(unittest.TestCase):
    def testequal(self):
        self.assertEqual(
            getMessageClient(
                b'{"command": "\\u043f\\u0440\\u0438\\u0432\\u0435\\u0442",'
                b' "text": ["\\u0441\\u0435\\u0440\\u0432\\u0435\\u0440",'
                b' "\\u044d\\u0442\\u043e", "\\u044f", ""]}'
            ),
            'введите help чтобы получить справку по командам'
        )

    def testequal2(self):
        self.assertEqual(
            getMessageClient(
                b'{"command": "\\u0441\\u0435\\u0440\\u0432\\u0435\\u0440", "text": []}'
            ),
            'туточки я'
        )


class test_sendMessageClient(unittest.TestCase):
    def testequal(self):
        self.assertEqual(
            sendMessageClient('ответ получен, отдыхай'),
            b'\xd0\xbe\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82 \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x83\xd1\x87\xd0\xb5\xd0\xbd, \xd0\xbe\xd1\x82\xd0\xb4\xd1\x8b\xd1\x85\xd0\xb0\xd0\xb9'
        )


if __name__ == '__main__':
    unittest.main()
