from unittest import TestCase

from main import gcd
from main import lcm
from main import solve
from main import solve2
from main import solve3


class Test(TestCase):
    def test_solve(self):
        test_cases = [
            [10, 12, 3, 9, 33],
            [10, 12, 7, 2, -1],
            [13, 11, 5, 6, 83],
            [1, 1, 1, 1, 1],
            [2, 10, 1, 7, 7],
        ]
        for test_case in test_cases:
            n, m, x, y, expected = test_case
            actual = solve(n, m, x, y)
            self.assertEqual(expected, actual)

    def test_solve2(self):
        test_cases = [
            [2, 10, 1, 7, 7],
            [10, 12, 3, 9, 33],
            [13, 11, 5, 6, 83],
            [10, 12, 7, 2, -1],
            [10, 12, 2, 12, 12],
            [10, 10, 7, 7, 7],
            [1, 1, 1, 1, 1],
        ]
        for test_case in test_cases:
            n, m, x, y, expected = test_case
            actual = solve2(n, m, x, y)
            self.assertEqual(expected, actual)

    def test_solve3(self):
        test_cases = [
            [2, 10, 1, 7, 7],
            [10, 12, 3, 9, 33],
            [13, 11, 5, 6, 83],
            [10, 12, 7, 2, -1],
            [10, 12, 2, 12, 12],
            [10, 10, 7, 7, 7],
            [1, 1, 1, 1, 1],
        ]
        for test_case in test_cases:
            n, m, x, y, expected = test_case
            actual = solve3(n, m, x, y)
            self.assertEqual(expected, actual)

    def test_gcd(self):
        test_cases = [
            [78696, 19332, 36],
            [1071, 1029, 21],
        ]
        for test_case in test_cases:
            a, b, expected = test_case
            actual = gcd(a, b)
            self.assertEqual(expected, actual)

    def test_lcm(self):
        test_cases = [
            [1, 10, 10],
            [12, 10, 60],
            [12, 18, 36]
        ]
        for test_case in test_cases:
            a, b, expected = test_case
            actual = lcm(a, b)
            self.assertEqual(expected, actual)
