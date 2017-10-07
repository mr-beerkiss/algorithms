""" Selecton sort """
def selection_sort(arr):
    """ sorts input arr using selection sort """
    arr_len = len(arr)
    for i in range(arr_len-1):
        min_index = i
        min_value = arr[i]
        for j in range(min_index + 1, arr_len):
            if arr[j] < min_value:
                min_value = arr[j]
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]

def test_program():
    """ tests the program """
    in_arr = [5, 6, 2, 3, 1, 4]
    ex_arr = [1, 2, 3, 4, 5, 6]
    selection_sort(in_arr)

    assert in_arr == ex_arr, "Expected %r but got %r" % (ex_arr, in_arr)

    in_arr = [3, 1, 2]
    ex_arr = [1, 2, 3]
    selection_sort(in_arr)

    assert in_arr == ex_arr, "Expected %r but got %r" % (ex_arr, in_arr)

    in_arr = [-1, -7]
    ex_arr = [-7, -1]
    selection_sort(in_arr)

    assert in_arr == ex_arr, "Expected %r but got %r" % (ex_arr, in_arr)

    in_arr = [-1, -5, 7, 1, 3, 9, 6, 4, -2]
    ex_arr = [-5, -2, -1, 1, 3, 4, 6, 7, 9]
    selection_sort(in_arr)

    assert in_arr == ex_arr, "Expected %r but got %r" % (ex_arr, in_arr)


    in_arr = [7, 3, 2, 11, 2, 11, 7, 7, 10, 11]
    ex_arr = [2, 2, 3, 7, 7, 7, 10, 11, 11, 11]
    selection_sort(in_arr)

    assert in_arr == ex_arr, "Expected %r but got %r" % (ex_arr, in_arr)


    print("All tests have passed")

test_program()