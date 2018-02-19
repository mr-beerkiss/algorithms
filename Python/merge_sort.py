from math import floor
""" merge_sort.py """
def merge_sort(arr):
    """ implements the merge sort algorithm """
    arr_len = len(arr)
    if (floor(arr_len / 2)):
        

    return arr

def test_program():
    """ tests the program """
    in_arr = [5, 3, 6, 1, 4, 2]
    ex_arr = sorted(in_arr)

    assert in_arr == ex_arr, "Expected %r but got %r" % (ex_arr, in_arr)

test_program()
