def is_palindrome(string):
    true_string = str(string).lower()
    return true_string == true_string[::-1]


print(is_palindrome("Anna"))
print(is_palindrome("otto"))
print(is_palindrome(12321))
print(is_palindrome(123213))