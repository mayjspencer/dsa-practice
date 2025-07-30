def countdown(n):
    if n == 0:
        print("Blast off!")
    else:
        print(n)
        countdown(n-1)

countdown(3)


# === 2.11 Recursion Basics Practice ===

def recursive_sum(n):
    """
    Given a number n, return the sum from 1 to n using recursion.
    E.g., recursive_sum(4) -> 10
    """
    if n == 1:
        return n
    else:
        return n + recursive_sum(n-1)

def power(base, exponent):
    """
    Compute base^exponent recursively.
    E.g., power(2, 3) -> 8
    """
    if exponent == 0:
        return 1
    else:
        return base * power(base, (exponent - 1))

def count_down(n):
    """
    Print numbers from n to 1 using recursion (no return).
    E.g., count_down(3) prints: 3 2 1
    """
    if n == 1:
        print(1)
    else:
        print(n)
        countdown(n-1)

def reverse_string(s):
    """
    Recursively reverse a string.
    E.g., reverse_string("cat") -> "tac"
    """
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])


    

def is_palindrome(s):
    """
    Recursively check if a string is a palindrome.
    E.g., is_palindrome("racecar") -> True
    """
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])



# === TESTS ===
if __name__ == "__main__":
    print("Testing recursive_sum...")
    assert recursive_sum(5) == 15
    assert recursive_sum(1) == 1

    print("Testing power...")
    assert power(2, 3) == 8
    assert power(5, 0) == 1

    print("Testing count_down...")
    count_down(3)  # Should print: 3 2 1

    print("Testing reverse_string...")
    assert reverse_string("hello") == "olleh"
    assert reverse_string("a") == "a"

    print("Testing is_palindrome...")
    assert is_palindrome("madam") is True
    assert is_palindrome("cat") is False

    print("✅ All tests passed!")
