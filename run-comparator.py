#!/usr/bin/env python

from __future__ import print_function
import sys, os


def parse_args():
    info = """
    Wrong number of args.

    USAGE: [python] run_comparator.py <run_dir1> <run_dir2>
    """
    if len(sys.argv) != 3:
        print(info)
        sys.exit(1)

    return sys.argv[1:3]


def load(datafile):
    contents = []
    for line in datafile:
        _, energy = line.rstrip().split()
        contents.append(float(energy))

    return contents


def main():
    dir1, dir2 = parse_args()

    filename = 'FieldEnergy.txt'
    path1 = dir1 + os.sep + filename
    path2 = dir2 + os.sep + filename

    file1 = open(path1, 'rt')
    file2 = open(path2, 'rt')

    file1_contents = load(file1)
    file2_contents = load(file2)

    if len(file1_contents) != len(file2_contents):
        print('Dimensions of FieldEnergy don\'t match.')
        sys.exit(102)

    diff = 0
    for item1, item2 in zip(file1_contents, file2_contents):
        diff = max((diff, abs(item1 - item2)))

    print('Maximum value of difference: {0:.6g}'.format(diff))


if __name__ == '__main__':
    main()

