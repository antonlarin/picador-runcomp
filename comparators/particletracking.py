import os

from common import MATCH, MISMATCH


def name():
    return 'ParticleTracking'


def file_list():
    return [ 'ParticleTracking{0}*{0}*.txt'.format(os.sep) ]


def compare(file1, file2, accuracy):
    file1_contents = _load(file1)
    file2_contents = _load(file2)

    filename = os.sep.join(file1.name.rsplit(os.sep, 2)[1:])
    height1 = len(file1_contents)
    height2 = len(file2_contents)
    if height1 != height2:
        print('{}: Different number of output iterations'.format(filename))
        print('\t{0} vs {1}'.format(height1, height2))
        return MISMATCH

    width1 = len(file1_contents[1])
    width2 = len(file2_contents[2])
    if width1 != width2:
        print('{}: Different number of tracked values'.format(filename))
        print('\t{0} vs {1}'.format(width1, width2))
        return MISMATCH

    max_diff = 0
    for value_set1, value_set2 in zip(file1_contents, file2_contents):
        for value1, value2 in zip(value_set1, value_set2):
            abs_diff = abs(value1 - value2)
            try:
                base = min(filter(lambda x: x != 0,
                    [abs(value1), abs(value2)]))
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


def _load(datafile):
    contents = []
    for line in datafile:
        values = line.rstrip().split()[1:]
        contents.append(map(float, values))

    return contents

