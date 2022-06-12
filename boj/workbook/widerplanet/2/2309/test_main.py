from unittest import TestCase

from main import solve


class Test(TestCase):
    def test_solve(self):
        test_cases = [
            [[20, 7, 23, 19, 10, 15, 25, 8, 13], [7, 8, 10, 13, 19, 20, 23]],
            [[99, 98, 25, 13, 12, 1, 24, 6, 19], [1, 6, 12, 13, 19, 24, 25]],
        ]

        for test_case in test_cases:
            data, expected = test_case

            actual = solve(data)

            self.assertEqual(expected, actual)
