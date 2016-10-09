#!/usr/bin/env python

from __future__ import print_function
import sys, os
import comparators


def parse_args():
    info = """
    Wrong number of args.

    USAGE: [python] run_comparator.py <run_dir1> <run_dir2>
    """
    if len(sys.argv) != 3:
        print(info)
        sys.exit(1)

    return sys.argv[1:3]


def main():
    dir1, dir2 = parse_args()

    filename = 'FieldEnergy.txt'
    path1 = dir1 + os.sep + filename
    path2 = dir2 + os.sep + filename

    file1 = open(path1, 'rt')
    file2 = open(path2, 'rt')

    comparators.fieldenergy.compare(file1, file2)


if __name__ == '__main__':
    main()

