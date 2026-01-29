from xor import xor
from tests import default_key
from unittest import TestCase

class TestXor(TestCase):

    def process_file(self, path):
        with open(path, 'r') as file:
            contents = file.read()
        assert xor(xor(contents, default_key), default_key) == contents

    def test_message(self):
        self.process_file('tests/test_data/message.txt')

    def test_specialchars(self):
        self.process_file('tests/test_data/specialchars.txt')
