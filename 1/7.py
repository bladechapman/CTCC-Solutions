"""
Problem 1.7
----------------
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
write a mtheod to rotate the image by 90 degrees. Can you do this in place?
"""


import unittest


"""
Naive proposed_solution:
Iterate through each column and place the appropriate pixel in a return matrix

Runtime: O(n^2)
Space: O(n^2)
"""
def naive_solution(img):
    N = len(img)
    ret = []
    for x in range(0, N):
        ret.append([0] * N)
    for x in range(0, N):
        col = img[x]
        for y in reversed(range(0, N)):
            target_index = (N - 1) - y
            ret[y][x] = col[target_index]
    return ret


"""
Revised solution:
Rotate by depth of the square image.

Runtime: O(n^2)
Space: O(1)
"""
def revised_solution(img):
    depth = int(len(img)/2)
    for layer in range(0, depth):
        rotate_layer(img, layer)
def swap_2d_inplace(coord_1, coord_2, data):
    temp = data[coord_1[0]][coord_1[1]]
    data[coord_1[0]][coord_1[1]] = data[coord_2[0]][coord_2[1]]
    data[coord_2[0]][coord_2[1]] = temp
def rotate_layer(img, layer):
    distance_to = layer
    distance_from = (len(img) - 1) - layer
    for index in range(distance_to, distance_from):
        offset = (index - distance_to)
        swap_2d_inplace((index, distance_to), (distance_from, index), img)
        swap_2d_inplace((distance_to, distance_from - offset), (index, distance_to), img)
        swap_2d_inplace((distance_from - offset, distance_from), (distance_to, distance_from - offset), img)


class TestSolutions(unittest.TestCase):
    global unsolved, solved
    unsolved = [['A', 'E', 'I', 'M'], ['B', 'F', 'J', 'N'], ['C', 'G', 'K', 'O'], ['D', 'H', 'L', 'P']]
    solved = [['M', 'N', 'O', 'P'], ['I', 'J', 'K', 'L'], ['E', 'F', 'G', 'H'], ['A', 'B', 'C', 'D']]

    def test_naive(self):
        print '\n[TEST] - test_naive'
        proposed_solution = naive_solution(unsolved)
        for x in range(0, len(unsolved)):
            for y in range(0, len(unsolved[x])):
                self.assertEqual(proposed_solution[x][y], solved[x][y])

    def test_swap_2d_inplace(self):
        print '\n[TEST] - test_swap_2d_inplace'
        swap_unsolved = [['A', 'B'], ['C', 'D']]
        swap_solved = [['D', 'B'], ['C', 'A']]
        swap_2d_inplace((0, 0), (1, 1), swap_unsolved)
        self.assertEqual(swap_solved[0][0], swap_unsolved[0][0])
        self.assertEqual(swap_solved[1][1], swap_unsolved[1][1])
    def test_rotate_layer(self):
        print '\n[TEST] - test_rotate_layer'
        depth = 1
        unsolved_deep_copy = [['A', 'E', 'I', 'M'], ['B', 'F', 'J', 'N'], ['C', 'G', 'K', 'O'], ['D', 'H', 'L', 'P']]
        rotate_layer(unsolved_deep_copy, depth)

        N = len(unsolved_deep_copy[depth]) - depth
        for index in range(depth, N):
            self.assertEqual(unsolved_deep_copy[depth][index], solved[depth][index])
            self.assertEqual(unsolved_deep_copy[N - 1][index], solved[N - 1][index])
            self.assertEqual(unsolved_deep_copy[index][depth], solved[index][depth])
            self.assertEqual(unsolved_deep_copy[index][N - 1], solved[index][N - 1])
    def test_revised(self):
        print '\n[TEST] - test_revised'
        revised_solution(unsolved)
        for x in range(0, len(unsolved)):
            for y in range(0, len(unsolved[x])):
                self.assertEqual(unsolved[x][y], solved[x][y])

if __name__ == '__main__':
    unittest.main()