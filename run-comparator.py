#!/usr/bin/env python

from __future__ import print_function
import sys, os, glob
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


def find_files(base_dir, filenames):
    results = []
    old_wd = os.getcwd()
    for filename in filenames:
        os.chdir(base_dir)
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
    dir1, dir2 = parse_args()

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


if __name__ == '__main__':
    main()

