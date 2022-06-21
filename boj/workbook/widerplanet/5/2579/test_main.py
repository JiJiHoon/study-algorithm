from unittest import TestCase

from main import solve


class Test(TestCase):
    def test_solve(self):
        test_cases = [
            [[10, 20, 15, 25, 10, 20], 75]
        ]

        for test_case in test_cases:
            data, expected = test_case

            actual = solve(data)

            self.assertEqual(expected, actual)
