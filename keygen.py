from exceptions import InvalidKeyLengthError, InvalidThresholdError
import random
import argparse

def create_key(key_length, tmin, tmax):
    if key_length < 1:
        raise InvalidKeyLengthError('The key length must be a positive integer')
    if tmin < 0 or tmin >= 0x110000:
        raise InvalidThresholdError('tmin must be in the range [0, 0x110000)')
    if tmax < 0 or tmax >= 0x110000:
        raise InvalidThresholdError('tmax must be in the range [0, 0x110000)')
    if tmin > tmax:
        raise InvalidThresholdError('tmin must be less than or equal to tmax')
    return [random.randint(tmin, tmax) for i in range(key_length)]

def main():
    parser = argparse.ArgumentParser(prog='keygen.py', description='Create an XOR key')
    parser.add_argument('keylength', type=int, default=64, nargs='?')
    parser.add_argument('-tmin', '--min_threshold', type=int, default=0)
    parser.add_argument('-tmax', '--max_threshold', type=int, default=255)
    parser.add_argument('-o', '--outputfile', type=str, default='key.txt')
    args = parser.parse_args()
    keylength = args.keylength
    outputfile = args.outputfile
    tmin = args.min_threshold
    tmax = args.max_threshold

    try:
        key = create_key(keylength, tmin, tmax)
    except InvalidKeyLengthError as err:
        print(err)
        return
    except InvalidThresholdError as err:
        print(err)
        return

    with open(outputfile, 'w') as file:
        for i in range(keylength):
            file.write('key[%d] = %d\n' %(i, key[i]))
        print('Created keyfile %s' %args.outputfile)

if __name__ == '__main__':
    main()
