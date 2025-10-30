import random
import argparse

def gen_key(key_length):
    key = [chr(random.randint(0, 255)) for i in range(0, key_length)]
    return "".join(key)

def main():
    parser = argparse.ArgumentParser(prog="keygen.py", description="Create an XOR key")
    parser.add_argument("-kl", "--keylength", type=int, default=64)
    parser.add_argument("-o", "--output", type=str, default="key.txt")
    args = parser.parse_args()
    key = gen_key(args.keylength)
    with open(args.output, "w") as file:
        file.write(key)

if __name__ == "__main__":
    main()
