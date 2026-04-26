from tests import project_root
from encrypt import encrypt
from decrypt import decrypt
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

    def encrypt_decrypt(self, content, key):
        assert decrypt(encrypt(content, key), key) == content

    def test_message(self):
        self.encrypt_decrypt(self.message, self.default_key)
        self.encrypt_decrypt(self.message, self.key1)
        self.encrypt_decrypt(self.message, self.key2)

    def test_specialchars(self):
        self.encrypt_decrypt(self.specialchars, self.default_key)
        self.encrypt_decrypt(self.specialchars, self.key1)
        self.encrypt_decrypt(self.specialchars, self.key2)
