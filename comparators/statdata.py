import os

from common import MATCH, MISMATCH


def name():
    return 'StatData'


def file_list():
    patterns = []

    # QEDstatistics patterns
    for dir1 in ('ph', 'el', 'pos'):
        for dir2 in ('EnSp', 'EnSpSph', 'angSpSph', 'EnAngSp'):
            patterns.append('statdata{0}{1}{0}{2}{0}*.txt'.format(os.sep,
                dir1, dir2))
    patterns.append('statdata{0}ph{0}phAngle{0}*.txt'.format(os.sep))
    patterns.append('statdata{0}ph{0}EnSpPlane{0}*.txt'.format(os.sep))
    patterns.append('statdata{0}ph{0}NPlaneUp{0}*.txt'.format(os.sep))
    patterns.append('statdata{0}ph{0}NPlaneDown{0}*.txt'.format(os.sep))
    patterns.append('statdata{0}ph{0}ChiT{0}*.txt'.format(os.sep))
    patterns.append('statdata{0}ph{0}PhBirth{0}*.txt'.format(os.sep))
    patterns.append('statdata{0}ph{0}PhDeath{0}*.txt'.format(os.sep))
    patterns.append('statdata{0}ph{0}PhEnEl{0}*.txt'.format(os.sep))
    patterns.append('statdata{0}ph{0}PhChiEl{0}*.txt'.format(os.sep))
    patterns.append('statdata{0}ph{0}PhT{0}*.txt'.format(os.sep))
    patterns.append('statdata{0}el{0}ElEnPh{0}*.txt'.format(os.sep))
    patterns.append('statdata{0}el{0}ElChiPh{0}*.txt'.format(os.sep))

    # TODO: add other client modules of StatData

    return patterns


def compare(file1, file2, accuracy):
    file1_data = _load(file1)
    file2_data = _load(file2)
    filename = os.sep.join(file1.name.rsplit(os.sep, 3)[1:])

    if len(file1_data) != len(file2_data):
        print('{}: Different matrix sizes in StatData'.format(filename))
        return MISMATCH

    max_diff = 0
    for value1, value2 in zip(file1_data, file2_data):
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


def _load(datafile):
    strings = datafile.readline().rstrip().split()
    return map(float, strings)

