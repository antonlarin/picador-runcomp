from  __future__ import print_function
import os, os.path

import common


def name():
    return 'BasicOutput'


def file_list():
    return [
        'BasicOutput' + os.sep + 'logs' + os.sep + '??????.log',
        'BasicOutput' + os.sep + 'data' + os.sep + '*' + os.sep + '*.txt'
    ]


def compare(file1, file2):
    _, extension = os.path.splitext(file1.name)

    if extension == '.log':
        print('Logs:', end=' ')
        common.compare_line_by_line(file1, file2)
    else: # extension == '.txt':
        path1 = file1.name
        filename = os.sep.join(path1.rsplit(os.sep, 2)[1:])
        print('{}:'.format(filename), end=' ')
        _compare_data(filename, file1, file2)


def _compare_data(filename, file1, file2):
    file1_data = _load_data(file1)
    file2_data = _load_data(file2)

    if len(file1_data) != len(file2_data):
        print('Different matrix sizes in BOData, filename: {}'.format(
            filename))
        return

    max_diff = 0
    for value1, value2 in zip(file1_data, file2_data):
        abs_diff = abs(value1 - value2)
        try:
            base = min(filter(lambda x: x != 0, [abs(value1), abs(value2)]))
            rel_diff = abs_diff / base
        except ValueError:
            rel_diff = 0

        max_diff = max((max_diff, rel_diff))

    print('Maximum relative difference: {0:.6g}'.format(max_diff))


def _load_data(datafile):
    strings = datafile.readline().rstrip().split()
    return map(float, strings)

