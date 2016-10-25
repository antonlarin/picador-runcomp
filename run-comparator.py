#!/usr/bin/env python

from __future__ import print_function
import os, glob
import argparse

import comparators


def parse_args():
    parser = argparse.ArgumentParser(
            description='Compare outputs of Picador runs.')
    parser.add_argument('outdir1', help='Picador output directory')
    parser.add_argument('outdir2', help='Picador output directory')
    return parser.parse_args()


def find_files(base_dir, filenames):
    results = []
    old_wd = os.getcwd()
    os.chdir(base_dir)
    for filename in filenames:
        results.extend(glob.glob(filename))

    os.chdir(old_wd)
    return results


def compare_file_lists(dir1_files, dir2_files):
    dir1_files_set = frozenset(dir1_files)
    dir2_files_set = frozenset(dir2_files)
    
    unique_dir1 = dir1_files_set - dir2_files_set
    if (len(unique_dir1) != 0):
        print('Files in dir1 not found in dir2:')
        for f in unique_dir1:
            print(f)

    unique_dir2 = dir2_files_set - dir1_files_set
    if (len(unique_dir2) != 0):
        print('Files in dir2 not found in dir1:')
        for f in unique_dir2:
            print(f)

    return dir1_files_set & dir2_files_set


def main():
    args = parse_args()
    dir1, dir2 = args.outdir1, args.outdir2

    for comparator in comparators.get_all():
        print('Comparing {}'.format(comparator.name()))
        dir1_files = find_files(dir1, comparator.file_list())
        dir2_files = find_files(dir2, comparator.file_list())

        common_files = compare_file_lists(dir1_files, dir2_files)

        for filename in common_files:
            path1 = dir1 + os.sep + filename
            path2 = dir2 + os.sep + filename

            with open(path1, 'rt') as file1, open(path2, 'rt') as file2:
                comparator.compare(file1, file2)

        print()


if __name__ == '__main__':
    main()

