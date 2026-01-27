def parse_key(path):
    key = []
    with open(path, 'r') as file:
        for line in file:
            tokens = line.split("=")
            byte_value = int(tokens[1])
            key.append(byte_value)
    return key
