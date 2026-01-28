#!/usr/bin/env python3

from exceptions import InvalidKeyError
import parser
import argparse
import sys

def crypt(msg, key):
    msglen = len(msg)
    keylen = len(key)
    codepoints = list(map(lambda x: ord(x), msg))
    result = [chr(codepoints[i] ^ key[i % keylen]) for i in range(msglen)]
    return ''.join(result)

def main():
    base_dir = sys.path[0]
    default_key = base_dir + '/keys/defaultkey.txt'
    arg_parser = argparse.ArgumentParser(prog='xor.py', description='Encrypt or decrypt a message using the XOR algorithm')
    group = arg_parser.add_mutually_exclusive_group(required=True)
    group.add_argument('message', type=str, nargs='?')
    group.add_argument('-i', '--inputfile', type=str)
    arg_parser.add_argument('-k', '--keyfile', type=str, default=default_key)
    arg_parser.add_argument('-o', '--outputfile', type=str)
    args = arg_parser.parse_args()

    if args.inputfile:
        with open(args.inputfile, 'r') as file:
            msg = file.read()
    else:
        msg = args.message

    try:
        key = parser.parse_key(args.keyfile)
    except InvalidKeyError as err:
        print(err)
        return

    output = crypt(msg, key)
    if args.outputfile:
        with open(args.outputfile, 'w') as file:
            file.write(output)
    else:
        print(output, end='')

if __name__ == '__main__':
    main()
