def name():
    return 'FieldEnergy'


def file_list():
    return [ 'FieldEnergy.txt' ]


def compare(file1, file2, accuracy):
    file1_contents = _load(file1)
    file2_contents = _load(file2)

    if len(file1_contents) != len(file2_contents):
        print('Different number of iterations in FieldEnergy files.')
        return

    max_diff = 0
    for value1, value2 in zip(file1_contents, file2_contents):
        abs_diff = abs(value1 - value2)
        try:
            base = min(filter(lambda x: x != 0, map(abs, [value1, value2])))
            rel_diff = abs_diff / base
        except ValueError:
            rel_diff = 0
        max_diff = max((max_diff, rel_diff))

    if max_diff > accuracy:
        print('Maximum value of difference: {0:.6g}'.format(max_diff))
    else:
        print('Everything matches')


def _load(datafile):
    contents = []
    for line in datafile:
        _, energy = line.rstrip().split()
        contents.append(float(energy))

    return contents

