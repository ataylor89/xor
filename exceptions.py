class InvalidKeyError(Exception):

    def __init__(self, message='Invalid key'):
        super().__init__('InvalidKeyError: %s' %message)

class InvalidThresholdError(Exception):

    def __init__(self, message='The min and max values must be in the range [0, 0x110000)'):
        super().__init__('InvalidThresholdError: %s' %message)

class InvalidKeyLengthError(Exception):

    def __init__(self, message='The key length must be a positive integer'):
        super().__init__('InvalidThresholdError: %s' %message)
