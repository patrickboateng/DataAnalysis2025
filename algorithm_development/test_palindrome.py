import pytest

from palindrome import is_palindrome, is_palindrome_2



import pytest

@pytest.mark.parametrize(
    ("x", "expected"),
    [
        (0, True),           # single-digit
        (5, True),           # single-digit
        (11, True),          # smallest 2-digit palindrome
        (10, False),         # trailing zero breaks palindrome
        (101, True),         # odd digits
        (100, False),        # zeros inside, not palindrome
        (121, True),         # classic example
        (1221, True),        # even digits
        (12321, True),       # longer odd digits
        (123210, False),     # ends with zero
        (123454321, True),   # large palindrome
        (-121, False),       # negatives are not palindromes
        (-101, False),       # negatives are not palindromes
    ]
)
def test_is_palindrome(x, expected):
    assert is_palindrome(x) == expected
    assert is_palindrome_2(x) == expected
