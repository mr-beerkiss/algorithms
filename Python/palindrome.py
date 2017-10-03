""" Palindrome """
def is_palindrome(string):
    """ tests if a string is a palindrome """
    if len(string) <= 1:
        return True
    elif string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])

def test_program():
    """ tests the program """
    assert is_palindrome("rotor"), "expected rotor to be a palindrome function returned False"

    assert not is_palindrome("motor"), "expected motor not to be a palindrome function returned True"

    assert is_palindrome("redder"), "expected redder to be a palindrome function returned False"

    assert is_palindrome("a"), "expected a to be a palindrome function returned False"

    long_palindrome = "Able was I ere I saw Elba".lower()

    assert is_palindrome(long_palindrome), "Expected %s to be a palindrome but function returned false" % long_palindrome

    assert is_palindrome("tattarrattat"), "Exepected tattarrattat to be a palindrom but function returned False"

    print "All tests have passed"

test_program()
