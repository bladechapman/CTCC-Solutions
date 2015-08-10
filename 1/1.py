"""
Problem 1.1
----------------
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""


import unittest


"""
Naive solution:
Use a dictionary to keep track of the number of occurances of each character.
Iterate through the dictionary to determine duplicates

Runtime: O(n)
Space: O(n)
"""
def naive_solution(input):
    input = input.upper()
    character_count = {}
    for character in input:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    for character in character_count:
        if character_count[character] > 1:
            return False
    return True


"""
Revised solution:
Reduce space usage by maintaining a constant size alphabet array that keeps track
of the count of each character

Runtime: O(n)
Space: O(n)
Caveat: Only a-z, A-Z are counted
"""
def revised_solution(input):
    input = input.upper()
    alphabet = [0] * 26
    for character in input:
        index = ord(character) - ord('A')
        if (index >= 0 and index <= 25):
            if alphabet[index] is 1:
                return False
            alphabet[index] += 1
    return True


class TestSolutions(unittest.TestCase):
    global failure_string
    global success_string
    failure_string = "This is a test"
    success_string = "This"

    def test_naive(self):
        self.assertEqual(False, naive_solution(failure_string))
        self.assertEqual(True, naive_solution(success_string))

    def test_revised(self):
        self.assertEqual(False, revised_solution(failure_string))
        self.assertEqual(True, revised_solution(success_string))

if __name__ == '__main__':
    unittest.main()