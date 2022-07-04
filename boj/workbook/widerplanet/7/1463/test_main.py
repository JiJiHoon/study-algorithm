from unittest import TestCase

from parameterized import parameterized

from main import solve


class Test(TestCase):
    @parameterized.expand([
        [2, 1],
        [3, 1],
        [10, 3],
        [1000000, 19]
    ])
    def test_solve(self, data, expected):
        actual = solve(data)
        self.assertEqual(expected, actual)
