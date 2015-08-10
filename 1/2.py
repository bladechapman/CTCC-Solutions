"""
Problem 1.2
----------------
Given two strings, write a method to decide if one is a permutation of the other
"""


import unittest


"""
Naive solution:
Use a dictionary to count the character occurance in one string, use the dictionary
to compare the character occurance in the second string. Short circuit False if
the lengths are unequal

Runtime: O(n)
Space: O(n)
"""
def naive_solution(A, B):
    if (len(A) != len(B)): return False

    A = A.upper()
    B = B.upper()
    char_dict = {}
    for character in A:
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
    for character in B:
        if character not in char_dict:
            return False
        else:
            char_dict[character] -= 1
    for character in char_dict:
        if char_dict[character] != 0:
            return False
    return True


class TestSolutions(unittest.TestCase):
    global A, B, C
    A = 'Kcat'
    B = 'Hat'
    C = 'Tack'

    def test_naive(self):
        self.assertEqual(False, naive_solution(A, B))
        self.assertEqual(False, naive_solution(C, B))
        self.assertEqual(True, naive_solution(A, C))

if __name__ == '__main__':
    unittest.main()