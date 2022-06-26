from unittest import TestCase

from main import solve


class Test(TestCase):
    def test_solve(self):
        test_cases = [
            [['baekjoononlinejudge', 'startlink', 'codeplus', 'sundaycoding', 'codingsh'],
             ['baekjoon', 'star', 'start', 'code', 'sunday', 'coding', 'cod', 'online', 'judge', 'plus'],
             7]
        ]

        for test_case in test_cases:
            words, prefixes, expected = test_case

            actual = solve(words, prefixes)

            self.assertEqual(expected, actual)
