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



def palindrome_3(s):
    new_str = ''
    first, last = 0, -1
    for word in s:
        if s[first] == s[last]:
            new_str += word
            first += 1
            last -= 1
    return "Palindrome" if len(new_str) == len(s) else "Not Palindrome"

print(palindrome_3('madam'))