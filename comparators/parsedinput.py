def name():
    return 'ParsedInput'


def file_list():
    return [ 'ParsedInput.txt' ]


def compare(file1, file2):
    file1_contents = _load(file1)
    file2_contents = _load(file2)

    if len(file1_contents) != len(file2_contents):
        print('Line count in ParsedInput.txt doesn\'t match.')
        return

    mismatches_exist = False
    for line1, line2 in zip(file1_contents, file2_contents):
        if line1 != line2:
            mismatches_exist = True
            print('Following lines in ParsedInput.txt don\'t match:')
            print('< {}\n---\n> {}'.format(line1.rstrip(), line2.rstrip()))

    if not mismatches_exist:
        print('Everything matches')


def _load(datafile):
    return datafile.readlines()

