# 7 kyu
# Love vs friendship
# https://www.codewars.com/kata/59706036f6e5d1e22d000016/solutions/javascript
# If　a = 1, b = 2, c = 3 ... z = 26
# Then l + o + v + e = 54
# and f + r + i + e + n + d + s + h + i + p = 108
# So friendship is twice stronger than love :-)
# The input will always be in lowercase and never be empty.

import string


def words_to_marks(s):
    alphabet = ' ' + string.ascii_lowercase
    s1 = 0
    for letter in s:
        s1 += alphabet.index(letter)

    return s1

# ------------------------------------------------------------------

import string

def words_to_marks(s):
    alphabet = ' ' + string.ascii_lowercase
    return sum([alphabet.index(letter) for letter in s])