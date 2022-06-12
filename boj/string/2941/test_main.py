from unittest import TestCase

from main import solve


class Test(TestCase):
    def test_solve(self):
        test_cases = [
            ['ljes=njak', 6],
            ['ddz=z=', 3],
            ['nljj', 3],
            ['c=c=', 2],
            ['dz=ak', 3],
        ]

        for test_case in test_cases:
            data, expected = test_case
            actual = solve(data)
            self.assertEqual(expected, actual)
