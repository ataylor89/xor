class InvalidKeyError(Exception):

    def __init__(self, message='Invalid key'):
        super().__init__(message)

class InvalidThresholdError(Exception):

    def __init__(self, message='Invalid threshold'):
        super().__init__(message)

class InvalidKeyLengthError(Exception):

    def __init__(self, message='Invalid key length'):
        super().__init__(message)
