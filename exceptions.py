class KeyFileError(Exception):

    def __init__(self, message='Invalid key file'):
        super().__init__(message)

class KeyLengthError(Exception):

    def __init__(self, message='Invalid key length'):
        super().__init__(message)

class ThresholdError(Exception):

    def __init__(self, message='Invalid threshold'):
        super().__init__(message)
