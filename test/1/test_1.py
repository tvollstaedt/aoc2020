import os
import unittest

from _1 import solve


class SolverTest(unittest.TestCase):

    def test_solve(self):
        f = open(os.path.dirname(__file__) + '/test_input', 'r')
        input = f.read().splitlines()
        f.close()
        self.assertEqual(solve(input), 514579)

    def test_find_solution(self):
        f = open(os.path.dirname(__file__) + '/real_input', 'r')
        input = f.read().splitlines()
        f.close()
        print(solve(input))


if __name__ == '__main__':
    unittest.main()
