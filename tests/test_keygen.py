import keygen
from unittest import TestCase

class TestKeygen(TestCase):

    def process_params(self, keylength, tmin, tmax):
        key = keygen.create_key(keylength, tmin, tmax)
        assert len(key) == keylength
        for value in key:
            assert isinstance(value, int)
            assert value >= tmin and value <= tmax

    def test_keygen(self):
        self.process_params(64, 0, 255)
    
    def test_keygen_with_large_keylength(self):
        self.process_params(1028, 0, 255)

    def test_keygen_with_large_keyvalues(self):
        self.process_params(64, 0, 0x10FFFF)
