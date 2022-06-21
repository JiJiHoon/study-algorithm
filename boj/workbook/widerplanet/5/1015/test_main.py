from unittest import TestCase

from main import solve


class Test(TestCase):
    def test_solve(self):
        test_cases = [
            [[2, 3, 1], [1, 2, 0]],
            [[2, 1, 3, 1], [2, 0, 3, 1]],
            [[4, 1, 6, 1, 3, 6, 1, 4], [4, 0, 6, 1, 3, 7, 2, 5]]
        ]

        for test_case in test_cases:
            data, expected = test_case

            actual = solve(data)

            self.assertEqual(expected, actual)
