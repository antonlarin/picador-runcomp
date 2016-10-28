from common import MATCH, MISMATCH


def name():
    return 'FieldEnergy'


def file_list():
    return [ 'FieldEnergy.txt' ]


def compare(file1, file2, accuracy):
    file1_contents = _load(file1)
    file2_contents = _load(file2)

    size1 = len(file1_contents)
    size2 = len(file2_contents)
    if size1 != size2:
        print('Different number of output iterations')
        print('\t{0} vs {1}'.format(size1, size2))
        return MISMATCH

    max_diff = 0
    for value1, value2 in zip(file1_contents, file2_contents):
        abs_diff = abs(value1 - value2)
        try:
            base = min(filter(lambda x: x != 0, map(abs, [value1, value2])))
            rel_diff = abs_diff / base
        except ValueError:
            rel_diff = 0
        max_diff = max((max_diff, rel_diff))

    if accuracy == None:
        print('Maximum relative difference {0:.6g}'.format(max_diff))
        return MISMATCH
    elif max_diff > accuracy:
        print('Relative difference {0:.6g} too large'.format(max_diff))
        return MISMATCH
    else:
        return MATCH


def _load(datafile):
    contents = []
    for line in datafile:
        _, energy = line.rstrip().split()
        contents.append(float(energy))

    return contents

