""""""
"""Написать функцию на проверку палиндрома"""

def palindrome(s):
    s = s.lower()
    return "Palindrome" if s == s[::-1] else "Not a Palindrome"

print(palindrome("Madam"))


def palindrome_2(s):
    l = list(s.lower())
    l.reverse()
    return  "Palindrome" if "".join(l) == s.lower() else "Not a Palindrome"
print(palindrome_2("Madam"))



def palindrome_3(s):
    first, last = 0, -1
    for word in s:
        if s[first] != s[last]:
            return 'Not Palindrome'
        first += 1
        last -= 1
    return 'Palindrome'

print(palindrome_3('mad3am'))