"""
Problem 1.6
----------------
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabccccaaa would become a2b1c4a3. If the compressed string would not become
smaller than the original string, your method should return the original string. You can assume the
string has only uppercase and lowercase letters (a - z)
"""


import unittest


"""
Naive solution:
Iterate through the string and keep a count of each continuous segment.

Runtime: O(n)
Space: O(n)
"""
def naive_solution(input):
    last_char = None
    char_count = 1
    ret_buffer = ''
    for character in input:
        if last_char != character:
            if last_char != None:
                ret_buffer += (last_char + str(char_count))
            last_char = character
            char_count = 1
        else:
            char_count += 1
    ret_buffer += (last_char + str(char_count))

    if len(ret_buffer) < len(input):
        return ret_buffer
    else:
        return input


class TestSolutions(unittest.TestCase):
    def test_naive(self):
        self.assertEqual('a3b1c4a3', naive_solution('aaabccccaaa'))
        self.assertLessEqual(len(naive_solution('abcd')), len('abcd'))

if __name__ == '__main__':
    unittest.main()