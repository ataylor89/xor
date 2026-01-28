from exceptions import InvalidKeyError

def parse_key(path):
    key = []
    with open(path, 'r') as file:
        for index, line in enumerate(file):
            linenum = index + 1
            try:
                tokens = line.split("=")
                value = int(tokens[1])
                key.append(value)
            except ValueError as err:
                raise InvalidKeyError(f'Value could not be parsed as an integer in line {linenum} of key file')
            except IndexError as err:
                raise InvalidKeyError(f'Value missing in line {linenum} of key file')
    return key
