#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.


def verbing(s):
    length = len(s)

    if length > 2:
        if s[-3:] == 'ing':
            s += 'ly'
        else:
            s += 'ing'
    return s


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):

    ###### ASK FOR HELP TOMORROW!!!!! (How to put '!' for 2nd response) ######
    aight = s.find('not')
    solid = s.find('bad')

    # if aight > solid and solid > 0 and aight > 0:
    #     s = s.replace(s[solid:(aight + 4)], 'good')
    #     return s
    # else:
    #     return s

    # if aight != -1 and solid != -1 and solid > aight:
    #     s = s[:aight] + 'good' + s[solid + 3:]
    #     return s
    # else:
    #     return s

    if solid > aight:
        s = s.replace(s[aight:(solid + 4)], 'good')

    return s



# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    middle_a = len(a) / 2
    middle_b = len(b) / 2

    if len(a) % 2 == 1:
        middle_a = middle_a + 1
    if len(b) % 2 == 1:
        middle_b = middle_b + 1
    return a[:middle_a] + b[:middle_b] + a[middle_a:] + b[middle_b:]


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    """Your code goes here.  Edit this docstring."""
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    """Your code goes here.  Edit this docstring."""
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


# Standard boilerplate (python idiom) to call the main() function.
if __name__ == '__main__':
    main()
