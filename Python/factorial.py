""" Factorial """
def factorial_sequence(number):
    """ calculates the factorial of n """
    if number == 0 or number == 1:
        return 1
    total = 1
    for x in range(1, number+1):
        total *= x

    return total

def factorial(number):
    """ calculates the factorial of n, recusively """
    if number == 0:
        return 1
    return number * factorial(number-1)


def test_program(test_factorial):

    """ tests the program """
    ans = test_factorial(4)
    assert ans == 24, "Expected 24 but got %d" % ans

    ans = test_factorial(1)
    assert ans == 1, "Expected 0 but got %d" % ans

    ans = test_factorial(1)
    assert ans == 1, "Expected 1 but got %d" % ans

    ans = test_factorial(10)
    assert ans == 3628800, "Expected 3628800 but got %d" %ans

    print "All tests passed"

test_program(factorial)
