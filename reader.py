# Author: Ronghan Che
# Version 9 / 3 / 2020
# Reference to https://github.com/hrchlhck/Auth-hash.
import os


class DataReader:

    def __init__(self, credential_file):
        self.credential_file = credential_file
        if not os.path.isfile(self.credential_file):
            open(self.credential_file, 'w+')
        else:
            pass

    def get_data(self, separator=', '):
        try:
            with open(self.credential_file, 'r') as file:
                lines = ''
                line_lst = []

                # Adds data into a string
                for line in file.readlines():
                    lines += line

                str_lines = lines.splitlines()  # Responsible to separate the data into lines, resulting a list

                # Splits the list into smaller lists, where the data is username and password
                for i in str_lines:
                    line_lst.append(i.split(separator))
                file.close()
                return line_lst
        except FileNotFoundError:
            print(r"Unable to open file. It may not exist or it's corrupted.")

    def get_line_count(self):
        try:
            with open(self.credential_file, 'r') as file:
                for index, line in enumerate(file):
                    pass
            return index + 1
        except FileNotFoundError:
            print(r"Unable to open file. It may not exist or it's corrupted.")

    def write_data(self, *args):
        try:
            with open(self.credential_file, 'a') as file:
                data = ''
                for _data in range(len(args)):
                    str_data = str(args[_data])
                    if _data < len(args) - 1:
                        data += str_data + ', '
                    elif _data == len(args) - 1:
                        data += str_data
                file.write(data + '\n')
        except FileNotFoundError:
            print(r"Unable to open file. It may not exist or it's corrupted.")