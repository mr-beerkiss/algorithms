""" power.py """
def power(x, n):
    "computes x to power of n using recursion"
    if n == 0:
        return 1
    elif n > 0:
        if n % 2 == 0:
            y = power(x, n/2)
            return y * y
        else:
            return x * power(x, n-1)
    else:
        return 1 / power(x, -n)

def test_program():
    """ tests the program """
    ans = pow(2, 2)
    exp = 2 ** 2
    assert ans == exp, "Expected %d but got %d" % (ans, exp)

    ans = pow(1, 2)
    exp = 1 ** 2
    assert ans == exp, "Expected %d but got %d" % (ans, exp)

    ans = pow(8, 0)
    exp = 8 ** 0
    assert ans == exp, "Expected %d but got %d" % (ans, exp)

    ans = pow(10, 12)
    exp = 10 ** 12
    assert ans == exp, "Expected %d but got %d" % (ans, exp)

    ans = pow(10, -1)
    exp = 10 ** -1
    assert ans == exp, "Expected %d but got %d" % (ans, exp)

    print("All tests have passed")

test_program()
