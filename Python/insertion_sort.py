""" insertion_sort.py """
def insertion_sort(arr):
    """ performs an insertion sort on the input """
    arr_len = len(arr)
    for i in range(1, arr_len):
        last_index = i
        for j in reversed(range(i)):
            if arr[last_index] < arr[j]:
                arr[last_index], arr[j] = arr[j], arr[last_index]
                last_index = j
            else:
                break

    return arr

def test_program():
    """ tests the program """
    in_test = [22, 11, 99, 88, 9, 7, 42]
    ex_res = [7, 9, 11, 22, 42, 88, 99]
    res = insertion_sort(in_test)
    assert res == ex_res, "Expected %r but got %r" % (ex_res, res)

    in_test = [5, 4, 6, 3, 7, 2, 1]
    ex_res = [1, 2, 3, 4, 5, 6, 7]
    res = insertion_sort(in_test)
    assert res == ex_res, "Expected %r but got %r" % (ex_res, res)

    in_test = [9, 6, 3, 1]
    ex_res = [1, 3, 6, 9]
    res = insertion_sort(in_test)
    assert res == ex_res, "Expected %r but got %r" % (ex_res, res)

    in_test = [3, 1, 2, 2, 3, 1]
    ex_res = [1, 1, 2, 2, 3, 3]
    res = insertion_sort(in_test)
    assert res == ex_res, "Expected %r but got %r" % (ex_res, res)

    in_test = [5, -1, 3, -10, 17, 47]
    ex_res = [-10, -1, 3, 5, 17, 47]
    res = insertion_sort(in_test)
    assert res == ex_res, "Expected %r but got %r" % (ex_res, res)

    in_test = [5, 51, 21, 19, 17, 47]
    ex_res = [5, 17, 19, 21, 47, 51]
    res = insertion_sort(in_test)
    assert res == ex_res, "Expected %r but got %r" % (ex_res, res)

    print("All tests have passed")

test_program()
