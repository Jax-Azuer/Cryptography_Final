# Author: Ronghan Che
# Version 9 / 3 / 2020
# Implements a brutal force attack
# Reference to https://github.com/hrchlhck/Auth-hash.
from reader import DataReader
from decorator import timer
from itertools import product
from hashlib import md5
from time import time
import string
import os


class BruteForce:
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Get the root folder of the project

    def __init__(self, target, chars, size):
        self.target = target
        self.chars = chars
        self.size = size

    @timer
    def crack(self):
        data = DataReader(self.target).get_data()
        passwords = []
        try:
            for j in range(self.size):
                t0 = time()
                for i in product(self.chars, repeat=self.size):
                    md5_attempt = md5(''.join(i).encode('utf8')).hexdigest()
                    print(''.join(i), md5_attempt)

                    if md5_attempt == data[j][1]:
                        passwords.append(''.join(i))
                        DataReader(self.path + '\\md5\\cracked_passwords.txt').write_data(data[j][0], ''.join(i))
                        break
        except KeyboardInterrupt:
            print("Stopping brute force")


def main():
    path = BruteForce.path
    characters = string.digits + string.ascii_lowercase
    credentials = path + '\\md5\\password.txt'

    BruteForce(credentials, characters, size=4).crack()


if __name__ == '__main__':
    main()