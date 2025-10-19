
# Pythonic version to check for palindrome
def is_palindrome(x: int)-> bool:
    x_str = str(x)
    reversed_x_str = x_str[::-1]
    return x_str == reversed_x_str

# Non-Pythonic version to check for palindrome
def is_palindrome_2(x: int) -> bool:
    if x < 0:
        return False # Negative numbers are not palindromes
    x_str = str(x)
    i = 0
    j = len(x_str) - 1
    while i < j:
        if x_str[i] != x_str[j]:
            return False
        i += 1
        j -= 1
    return True
