from unittest import TestCase

from main import solve


class Test(TestCase):
    def test_solve(self):
        test_cases = [
            [1, 1],
            [2, 4],
            [10, 87],
            [70, 4065],
            [10000, 82256014]
        ]

        for test_case in test_cases:
            data, expected = test_case

            actual = solve(data)

            self.assertEqual(expected, actual)
