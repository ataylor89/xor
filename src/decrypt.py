#!/usr/bin/env python3

from settings import default_key_path
from exceptions import KeyFileError
import parser
import argparse
import base64

def decrypt(ciphertext, key):
    ciphertext = base64.b64decode(ciphertext).decode('utf-8')
    msglen = len(ciphertext)
    keylen = len(key)
    ciphers = list(map(lambda x: ord(x), ciphertext))
    message = [chr(ciphers[i] ^ key[i % keylen]) for i in range(msglen)]
    return ''.join(message)

def main():
    arg_parser = argparse.ArgumentParser(prog='decrypt.py', description='Decrypt a message using the XOR algorithm')
    group = arg_parser.add_mutually_exclusive_group(required=True)
    group.add_argument('ciphertext', type=str, nargs='?')
    group.add_argument('-i', '--inputfile', type=str)
    arg_parser.add_argument('-k', '--keyfile', type=str, default=default_key_path)
    arg_parser.add_argument('-o', '--outputfile', type=str)
    args = arg_parser.parse_args()

    if args.inputfile:
        with open(args.inputfile, 'r') as file:
            ciphertext = file.read()
    else:
        ciphertext = args.ciphertext

    try:
        key = parser.parse_key(args.keyfile)
    except KeyFileError as err:
        print(err)
        return

    plaintext = decrypt(ciphertext, key)
    if args.outputfile:
        with open(args.outputfile, 'w') as file:
            file.write(plaintext)
    else:
        print(plaintext, end='')

if __name__ == '__main__':
    main()
