import keygen
from unittest import TestCase

class TestKeygen(TestCase):

    def verify_key(self, keylength, tmin, tmax):
        key = keygen.create_key(keylength, tmin, tmax)
        assert len(key) == keylength
        for value in key:
            assert isinstance(value, int)
            assert value >= tmin and value <= tmax

    def test_keygen(self):
        self.verify_key(64, 0, 255)
    
    def test_keygen_with_large_keylength(self):
        self.verify_key(1028, 0, 255)

    def test_keygen_with_large_keyvalues(self):
        self.verify_key(64, 0, 0x10FFFF)
