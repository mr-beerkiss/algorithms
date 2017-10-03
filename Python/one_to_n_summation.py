""" one_to_n_summation """
def one_to_n_summation(n):
    """ returns sum of ints from 1 to n """
    ans = (n ** 2 / 2) + (n / 2)
    if n % 2 == 1:
        ans += 1
    return ans

def test_program():
    """ Tests the program! """
    ans = one_to_n_summation(5)
    assert ans == 15, "Expected 15 but got %d" % ans

    ans = one_to_n_summation(8)
    assert ans == 36, "Expected 36 but got %d" % ans

    print "All tests passed"

test_program()
