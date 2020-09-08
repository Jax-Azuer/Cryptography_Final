# Author: Ronghan Che
# Version 9 / 3 / 2020
# Reference to https://github.com/timvandermeij.
from argparse import ArgumentParser

from md5 import MD5


def main():
    argument_parser = ArgumentParser(
        description="Compute the MD5 hash of a given string.",
    )
    argument_parser.add_argument(
        "string",
        type=str,
        help="The string to hash",
    )

    arguments = argument_parser.parse_args()
    md5_hash = MD5.hash(arguments.string)

    f = open("password.txt", "a")
    userID = input("Enter your user name:")
    print(md5_hash)

    print(userID + ", " + md5_hash, file = f)


if __name__ == "__main__":
    main()