import os
import unittest

import _3 as solver


def readfile(filename):
    f = open(os.path.dirname(__file__) + '/' + filename, 'r')
    content = f.read().splitlines()
    f.close()
    return content


class SolverTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(7, solver.part1(readfile('test_input'), 3, 1))
        print("Day 3 Part 1 solution: ", solver.part1(readfile('real_input'), 3, 1))

    def test_part2(self):
        try_slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        self.assertEqual(336, solver.part2(readfile('test_input'), try_slopes))
        print("Day 3 Part 2 solution: ", solver.part2(readfile('real_input'), try_slopes))


if __name__ == '__main__':
    unittest.main()
