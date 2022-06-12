from unittest import TestCase

from main import solve


class Test(TestCase):
    def test_solve(self):
        test_cases = [
            [9999, 2],
            [122, 2],
            [12635, 1],
            [888888, 6],
        ]

        for test_case in test_cases:
            data, expected = test_case

            actual = solve(data)

            self.assertEqual(expected, actual)
