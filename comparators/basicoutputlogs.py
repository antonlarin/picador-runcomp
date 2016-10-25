import os

import common


def name():
    return 'BasicOutput-logs'


def file_list():
    return [ 'BasicOutput{0}logs{0}??????.log'.format(os.sep) ]


def compare(file1, file2, accuracy):
    return common.compare_line_by_line(file1, file2)

