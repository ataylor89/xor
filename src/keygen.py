#!/usr/bin/env python3

from settings import default_keylength
from settings import default_tmin, default_tmax
from settings import default_generated_key_path
from exceptions import KeyLengthError, ThresholdError
import random
import argparse

def create_key(key_length, tmin, tmax):
    validate_parameters(key_length, tmin, tmax)
    key = []
    for i in range(key_length):
        key.append(random.randint(tmin, tmax))
    return key

def validate_parameters(key_length, tmin, tmax):
    if key_length < 1:
        raise KeyLengthError('The key length must be a positive integer')
    if tmin < 0 or tmin >= 0x110000:
        raise ThresholdError('tmin must be in the range [0, 0x110000)')
    if tmax < 0 or tmax >= 0x110000:
        raise ThresholdError('tmax must be in the range [0, 0x110000)')
    if tmin > tmax:
        raise ThresholdError('tmin must be less than or equal to tmax')

def main():
    parser = argparse.ArgumentParser(prog='keygen.py', description='Create an XOR key')
    parser.add_argument('keylength', type=int, default=default_keylength, nargs='?')
    parser.add_argument('-tmin', '--min_threshold', type=int, default=default_tmin)
    parser.add_argument('-tmax', '--max_threshold', type=int, default=default_tmax)
    parser.add_argument('-o', '--outputfile', type=str, default=default_generated_key_path)
    args = parser.parse_args()
    keylength = args.keylength
    outputfile = args.outputfile
    tmin = args.min_threshold
    tmax = args.max_threshold

    try:
        key = create_key(keylength, tmin, tmax)
    except (KeyLengthError, ThresholdError) as err:
        print(err)
        return

    with open(outputfile, 'w') as file:
        for i in range(keylength):
            file.write('key[%d] = %d\n' %(i, key[i]))
        print('Created keyfile %s' %args.outputfile)

if __name__ == '__main__':
    main()
