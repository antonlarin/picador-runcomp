def name():
    return 'FieldEnergy'


def file_list():
    return [ 'FieldEnergy.txt' ]


def compare(file1, file2):
    file1_contents = _load(file1)
    file2_contents = _load(file2)

    if len(file1_contents) != len(file2_contents):
        print('Different number of iterations in FieldEnergy files.')
        return

    diff = 0
    for item1, item2 in zip(file1_contents, file2_contents):
        diff = max((diff, abs(item1 - item2)))

    print('Maximum value of difference: {0:.6g}'.format(diff))


def _load(datafile):
    contents = []
    for line in datafile:
        _, energy = line.rstrip().split()
        contents.append(float(energy))

    return contents

