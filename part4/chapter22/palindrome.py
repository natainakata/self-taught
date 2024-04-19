import math


def palindrome(word):
    word = word.lower()
    return word[::-1] == word


print(palindrome("Mother"))
print(palindrome("Mom"))


def palindrome_int(n):
    digits = int(math.log10(n)) + 1
    print(digits)


n = 120021
palindrome_int(n)
