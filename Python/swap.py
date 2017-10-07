""" Swap """
def swap(array, first_index, second_index):
    """ swaps two elements in the array """
    array[first_index], array[second_index] = array[second_index], array[first_index]

def test_program():
    """ tests the program """
    in_arr = [7, 9, 4]
    swap(in_arr, 0, 1)

    assert in_arr == [9, 7, 4], "Expected [9, 7, 4] but got %r" % in_arr

    in_arr = [7, 9, 4]
    swap(in_arr, 1, 2)

    assert in_arr == [7, 4, 9], "Expected [9, 7, 4] but got %r" % in_arr

    print("All tests have passed!")


test_program()
