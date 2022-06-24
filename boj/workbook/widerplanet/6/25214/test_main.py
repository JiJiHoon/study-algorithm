from unittest import TestCase

from main import solve


class Test(TestCase):
    def test_solve(self):
        test_cases = [
            [[50, 100, 70, 110, 10, 100], [0, 50, 50, 60, 60, 90]],
            [[3, 3, 2, 8, 3, 1000000000], [0, 0, 0, 6, 6, 999999998]]
        ]

        for test_case in test_cases:
            data, expected = test_case

            actual = solve(data)

            self.assertEqual(expected, actual)
