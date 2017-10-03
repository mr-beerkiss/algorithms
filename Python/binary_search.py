""" Implements a simple binary search """
def binary_search(arr, target):
    """" returns the index of the item or -1 if it is not found """
    min_index = 0
    max_index = len(arr)

    bail = max_index
    counter = 0

    while max_index >= min_index:
        if counter >= bail:
            print "Bail condition hit :("
            return -1
        mid = min_index + ((max_index - min_index)/2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:            
            max_index = mid - 1
        else:
            min_index = mid + 1

        counter += 1

    return -1

def test_program():
    """ Tests the program """
    in1 = [1, 2, 3, 4, 5, 6]
    target1 = 3
    ans1 = 2
    res = binary_search(in1, target1)
    assert res == ans1, "expected %d, got %d" % (ans1, res)

    in2 = [5]
    target2 = 5
    ans2 = 0
    res = binary_search(in2, target2)
    assert res == ans2, "expected %d, got %d" % (ans1, res)

    in3 = [101, 152, 176, 203, 246, 285, 332, 381, 416, 484, 501, 507, 509]
    target3 = 507
    ans3 = len(in3) - 2
    res = binary_search(in3, target3)
    assert res == ans3, "expected %d, got %d" % (ans3, res)

    print "All tests have passed"

test_program()
