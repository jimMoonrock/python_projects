""""""
"""Написать функцию на проверку полиндрома"""

def palindrome(s):
    s = s.lower()
    return "Palindrome" if s == s[::-1] else "Not a Palindrome"

print(palindrome("Madam"))


def palindrome_2(s):
    l = list(s.lower())
    l.reverse()
    return  "Palindrome" if "".join(l) == s.lower() else "Not a Palindrome"
print(palindrome_2("Madam"))


