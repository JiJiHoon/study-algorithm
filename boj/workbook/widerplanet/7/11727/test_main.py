from unittest import TestCase

from parameterized import parameterized

from main import solve


class Test(TestCase):
    @parameterized.expand([
        [1, 1],
        [2, 3],
        [8, 171],
        [12, 2731]
    ])
    def test_solve(self, data, expected):
        actual = solve(data)

        self.assertEqual(expected, actual)
