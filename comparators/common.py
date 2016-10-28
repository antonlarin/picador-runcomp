import os.path

def compare_line_by_line(file1, file2):
    filename = os.path.basename(file1.name)
    file1_contents = file1.readlines()
    file2_contents = file2.readlines()

    size1 = len(file1_contents)
    size2 = len(file2_contents)
    if size1 != size2:
        print('Line count in {} doesn\'t match.'.format(filename))
        print('\t{0} vs {1}'.format(size1, size2))
        return MISMATCH

    mismatches_exist = False
    for line1, line2 in zip(file1_contents, file2_contents):
        if line1 != line2:
            mismatches_exist = True
            print('Following lines in {} don\'t match:'.format(filename))
            print('< {}\n---\n> {}'.format(line1.rstrip(), line2.rstrip()))

    return MISMATCH if mismatches_exist else MATCH


class _ComparisonResult(object):
    def __init__(self, match):
        self.match = match

    def __eq__(self, other):
        return self.match == other.match

    def update(self, other):
        return _ComparisonResult(self.match and other.match)


MATCH, MISMATCH = _ComparisonResult(True), _ComparisonResult(False)

