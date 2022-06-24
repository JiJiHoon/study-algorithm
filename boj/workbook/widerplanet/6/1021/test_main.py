from unittest import TestCase

from main import solve


class Test(TestCase):
    def test_solve(self):
        test_cases = [
            [10, 3, [1, 2, 3], 0],
            [10, 3, [2, 9, 5], 8],
            [32, 6, [27, 16, 30, 11, 6, 23], 59],
            [10, 10, [1, 6, 3, 2, 7, 9, 8, 4, 10, 5], 14]
        ]

        for test_case in test_cases:
            n, m, data, expected = test_case

            actual = solve(n, m, data)

            self.assertEqual(expected, actual)
