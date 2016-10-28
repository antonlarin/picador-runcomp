from  __future__ import print_function
import os

from common import MATCH, MISMATCH

def name():
    return 'BasicOutput-data'


def file_list():
    pattern = 'BasicOutput{0}data{0}*{0}{1}.txt'.format(os.sep, '[0-9]' * 6)
    return [ pattern ]


def compare(file1, file2, accuracy):
    file1_contents = _load_data(file1)
    file2_contents = _load_data(file2)
    filename = os.sep.join(file1.name.rsplit(os.sep, 2)[1:])

    size1 = len(file1_contents)
    size2 = len(file2_contents)
    if size1 != size2:
        print('{}: Different matrix sizes in BOData'.format(filename))
        print('\t{0} vs {1}'.format(size1, size2))
        return MISMATCH

    max_diff = 0
    for value1, value2 in zip(file1_contents, file2_contents):
        abs_diff = abs(value1 - value2)
        try:
            base = min(filter(lambda x: x != 0, [abs(value1), abs(value2)]))
            rel_diff = abs_diff / base
        except ValueError:
            rel_diff = 0

        max_diff = max((max_diff, rel_diff))

    if accuracy == None:
        print('{0}: Maximum relative difference {1:.6g}'.format(
            filename, max_diff))
        return MISMATCH
    elif max_diff > accuracy:
        print('{0}: Relative difference {1:.6g} too large'.format(
            filename, max_diff))
        return MISMATCH
    else:
        return MATCH


def _load_data(datafile):
    strings = datafile.readline().rstrip().split()
    return map(float, strings)

