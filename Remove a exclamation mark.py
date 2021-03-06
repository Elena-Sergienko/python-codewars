# 8 kyu
# Exclamation marks series #1: Remove a exclamation mark from the end of string
# Description:
# Remove a exclamation mark from the end of string. For a beginner kata, you can assume that the input data is always a string, no need to verify it.
# Examples
# remove("Hi!") === "Hi"
# remove("Hi!!!") === "Hi!!"
# remove("!Hi") === "!Hi"
# remove("!Hi!") === "!Hi"
# remove("Hi! Hi!") === "Hi! Hi"
# remove("Hi") === "Hi"


def remove(s):
    if len(s) == 0:
        return s
    n = ''
    if s[-1] == '!':
        n = s[:-1]
    else:
        n = s

    return n