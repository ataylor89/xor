#!/usr/bin/env python3

from settings import default_key_path
from exceptions import KeyFileError
import parser
import argparse
import base64

def encrypt(msg, key):
    msglen = len(msg)
    keylen = len(key)
    codepoints = list(map(lambda x: ord(x), msg))
    ciphers = [chr(codepoints[i] ^ key[i % keylen]) for i in range(msglen)]
    bytearr = ''.join(ciphers).encode('utf-8')
    return base64.b64encode(bytearr).decode('utf-8')

def main():
    arg_parser = argparse.ArgumentParser(prog='encrypt.py', description='Encrypt a message using the XOR algorithm')
    group = arg_parser.add_mutually_exclusive_group(required=True)
    group.add_argument('message', type=str, nargs='?')
    group.add_argument('-i', '--inputfile', type=str)
    arg_parser.add_argument('-k', '--keyfile', type=str, default=default_key_path)
    arg_parser.add_argument('-o', '--outputfile', type=str)
    args = arg_parser.parse_args()

    if args.inputfile:
        with open(args.inputfile, 'r') as file:
            msg = file.read()
    else:
        msg = args.message

    try:
        key = parser.parse_key(args.keyfile)
    except KeyFileError as err:
        print(err)
        return

    ciphertext = encrypt(msg, key)
    if args.outputfile:
        with open(args.outputfile, 'w') as file:
            file.write(ciphertext)
    else:
        print(ciphertext, end='')

if __name__ == '__main__':
    main()
