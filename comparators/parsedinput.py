import common

def name():
    return 'ParsedInput'


def file_list():
    return [ 'ParsedInput.txt' ]


def compare(file1, file2):
    common.compare_line_by_line(file1, file2)

