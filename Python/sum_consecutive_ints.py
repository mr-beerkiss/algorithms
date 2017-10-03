""" sum_consecutive_ints """
def sum_consecutive_ints(arr):
    """ returns sum of a consecutive list of integers """
    arr_length = len(arr)
    end_sum = arr[0] + arr[arr_length-1]
    pairs = arr_length / 2
    ans = end_sum * pairs
    
    if arr_length % 2 == 1:
        ans += end_sum/2

    return ans

    # n = len(arr)
    # ans = (n ** 2 / 2) + (n / 2)
    # if n % 2 == 1:
    #     ans += 1
    # return ans

def test_program():
    """ Tests the program! """
    in_arr = [1, 2, 3, 4, 5]
    ans = sum_consecutive_ints(in_arr)
    assert ans == 15, "Expected 15 but got %d" % ans

    in_arr = [1, 2, 3, 4, 5, 6, 7, 8]
    ans = sum_consecutive_ints(in_arr)
    assert ans == 36, "Expected 36 but got %d" % ans

    in_arr = [4, 5, 6, 7, 8]
    ans = sum_consecutive_ints(in_arr)
    assert ans == 30, "Expected 36 but got %d" % ans

    in_arr = [7, 8, 9, 10, 11]
    ans = sum_consecutive_ints(in_arr)
    assert ans == 45, "Expected 45 but got %d" % ans

    print "All tests passed"

test_program()
