"""
Merge function for 2048 game.
"""

def _slide_tiles(line):
    """
    Function that slides a single row to the left without merging in 2048.
    """
    res_line = [0] * len(line)
    next_idx = 0
    for num in line:
        if num > 0:
            res_line[next_idx] = num
            next_idx += 1
    return res_line

def _merge_tiles(line):
    """
    Function that merge titles in a slided line without sliding in 2048.
    """
    res_line = line[:]
    idx = 0
    while idx < len(res_line) and res_line[idx] > 0:
        if idx < len(res_line) - 1 and res_line[idx + 1] == res_line[idx]:
            res_line[idx] *= 2
            res_line[idx + 1] = 0
            idx += 2
        else:
            idx += 1
    return res_line

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    return _slide_tiles(_merge_tiles(_slide_tiles(line)))

if __name__ == '__main__':
    # list for tuples of case: (input, output)
    TEST_CASES = [([], []),
                  ([0, 0, 0], [0, 0, 0]),
                  ([2, 0, 2, 4], [4, 4, 0, 0]),
                  ([0, 0, 2, 2], [4, 0, 0, 0]),
                  ([2, 2, 0, 0], [4, 0, 0, 0]),
                  ([2, 2, 2, 2, 2], [4, 4, 2, 0, 0]),
                  ([8, 16, 16, 8], [8, 32, 8, 0])]

    for index, (in_list, out_list) in enumerate(TEST_CASES):
        res_list = merge(in_list)
        if cmp(res_list, out_list) == 0:
            print 'test %d passed.' % index
        else:
            print 'test %d failed.' % index
            print 'input:', in_list
            print 'expected output:', out_list
            print 'your output:', res_list
            break
