from math import floor
""" merge_sort.py """

def merge_sort(alist):
    """ merge sort in one function """
    if len(alist) > 1:
        mid = len(alist) // 2
        left_half = alist[:mid]
        right_half = alist[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if (left_half[i] < right_half[j]):
                alist[k] = left_half[i]
                i += 1
            else:
                alist[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            alist[k] = left_half[i]
            i, k = i + 1, k + 1

        while j < len(right_half):
            alist[k] = right_half[j]
            j, k = j + 1, k + 1


def test_program():
    """ tests the program """
    in_arr = [5, 3, 1, 6, 7, 4, 2]
    ex_arr = sorted(in_arr)
    merge_sort(in_arr)
    assert in_arr == ex_arr, "Expected %r but got %r" % (ex_arr, in_arr)

    in_arr = [7, 1, -2, -5, 0, 6, 3, 15];
    ex_arr = sorted(in_arr)
    merge_sort(in_arr)
    assert in_arr == ex_arr, "Expected %r but got %r" % (ex_arr, in_arr)

    print("All tests have passed")

