#!/usr/bin/python3


def read_file(filename=""):
    """Read a file and print the lines
    Args:
        filename (str): str of path

    """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')


if __name__ == '__main__':
    read_file("my_file_0.txt")
