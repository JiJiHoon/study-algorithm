from unittest import TestCase

from main import solve


class Test(TestCase):
    def test_solve(self):
        input = [
            3, 7, 9901
        ]
        expected = [
            3, 6, 12
        ]

        actual = solve(input)
        self.assertEqual(actual, expected)
