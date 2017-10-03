""" Module docstring :-p """
def two_sum(arr, target):
    """ Returns the indicies of the values in the list whose sum is target """
    arr_len = len(arr)
    for i in xrange(arr_len):
        for j in xrange(arr_len):
            if i == j:
                continue
            elif arr[i] + arr[j] == target:
                return [i, j]

def test_program():
    """ Tests the program """
    in1 = [1, 2, 3, 4, 5]
    target1 = 8
    ans1 = [2, 4]

    #print(twoSum(in1, target1))
    assert two_sum(in1, target1) == ans1

    print("All tests pass")

test_program()
