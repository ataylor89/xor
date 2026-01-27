import random
import argparse

def create_key(key_length):
    return [random.randint(0, 255) for i in range(key_length)]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='keygen.py', description='Create an XOR key')
    parser.add_argument('keylength', type=int, default=64, nargs='?')
    parser.add_argument('-o', '--outputfile', type=str, default='key.txt')
    args = parser.parse_args()
    keylength = args.keylength
    outputfile = args.outputfile
    key = create_key(keylength)
    with open(outputfile, 'w') as file:
        for i in range(keylength):
            file.write('bytes[%d] = %d\n' %(i, key[i]))
        print('Created keyfile %s' %args.outputfile)
