from xor import xor
import parser
import keygen
from unittest import TestCase

class TestXor(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.default_key = parser.parse_key('keys/defaultkey.txt')
        cls.key1 = keygen.create_key(64, 0, 0x10FFFF)
        cls.key2 = keygen.create_key(1028, 0, 255)

    def process_file(self, path, key):
        with open(path, 'r') as file:
            contents = file.read()
        assert xor(xor(contents, key), key) == contents

    def test_message(self):
        self.process_file('tests/test_data/message.txt', self.default_key)
        self.process_file('tests/test_data/message.txt', self.key1)
        self.process_file('tests/test_data/message.txt', self.key2)

    def test_specialchars(self):
        self.process_file('tests/test_data/specialchars.txt', self.default_key)
        self.process_file('tests/test_data/specialchars.txt', self.key1)
        self.process_file('tests/test_data/specialchars.txt', self.key2)
