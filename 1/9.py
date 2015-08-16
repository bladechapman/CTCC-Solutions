"""
Problem 1.9
----------------
Assume you have a method isSubstring which checks if one word is a
substring of another. Given two strings, s1 and s2, write code to check
if s2 is a rotation of s1 using only one call to isSubstring
"""


import unittest


"""
Returns true if s2 is a substring of s1. Otherwise returns false
"""
def isSubstring(s1, s2):
    return (s2 in s1)


"""
Naive solution:
Double the original string to create s1_double. If the lengths
of s1 and s2 are the same, and isSubstring on s1_double against
s2 returns true, then the strings are rotations of each other.
"""
def naive_solution(s1, s2):
    if (len(s1) != len(s2)):
        return False

    s1_double = s1 * 2
    return isSubstring(s1_double, s2)


class TestSolution(unittest.TestCase):
    global original, rotated
    original = "waterbottle"
    rotated = "erbottlewat"

    def test_naive(self):
        self.assertTrue(naive_solution(original, rotated))
        self.assertFalse(naive_solution(original, 'waterbottlewat'))


if __name__ == '__main__':
    unittest.main()