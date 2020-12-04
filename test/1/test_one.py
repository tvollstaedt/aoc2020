import os
import unittest

from _1 import solve


class SolverTest(unittest.TestCase):

    def test_solve(self):
        f = open(os.path.dirname(__file__) + '/input', 'r')
        input = f.read()
        self.assertEqual(self, solve(input), 514579)


if __name__ == '__main__':
    unittest.main()
