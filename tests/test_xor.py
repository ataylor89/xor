from xor import xor
from parser import parse_key
from unittest import TestCase

class TestXor(TestCase):

    def process_file(self, path):
        with open(path, 'r') as file:
            contents = file.read()
        key = parse_key('keys/defaultkey.txt')
        assert xor(xor(contents, key), key) == contents

    def test_message(self):
        self.process_file('tests/test_data/message.txt')

    def test_specialchars(self):
        self.process_file('tests/test_data/specialchars.txt')
