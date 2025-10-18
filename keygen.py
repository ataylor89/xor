import random
import sys

key_length = 1024

def gen_key():
    key = [chr(random.randint(0, 255)) for i in range(0, key_length)]
    return "".join(key)

def main():
    if len(sys.argv) != 1:
        print("Usage: python keygen.py")
        sys.exit(0)
    key = gen_key()
    with open("key.txt", "w") as file:
        file.write(key)

if __name__ == "__main__":
    main()
