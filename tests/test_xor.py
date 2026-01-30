from tests import project_root
from xor import xor
import parser
import keygen
from unittest import TestCase

class TestXor(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.default_key = parser.parse_key(project_root / 'keys' / 'defaultkey.txt')
        cls.key1 = keygen.create_key(64, 0, 0x10FFFF)
        cls.key2 = keygen.create_key(1028, 0, 255)
        message_path = project_root / 'tests' / 'test_data' / 'message.txt'
        with open(message_path, 'r') as file:
            cls.message = file.read()
        specialchars_path = project_root / 'tests' / 'test_data' / 'specialchars.txt'
        with open(specialchars_path, 'r') as file:
            cls.specialchars = file.read()

    def process(self, content, key):
        assert xor(xor(content, key), key) == content

    def test_message(self):
        self.process(self.message, self.default_key)
        self.process(self.message, self.key1)
        self.process(self.message, self.key2)

    def test_specialchars(self):
        self.process(self.specialchars, self.default_key)
        self.process(self.specialchars, self.key1)
        self.process(self.specialchars, self.key2)
