from unittest import TestCase

from main import solve


class Test(TestCase):
    def test_solve(self):
        test_cases = [
            ['So when I die (the [first] I will see in (heaven) is a score list).', 'yes'],
            ['[ first in ] ( first out ).', 'yes'],
            ['Half Moon tonight (At least it is better than no Moon at all].', 'no'],
            ['A rope may form )( a trail in a maze.', 'no'],
            ['Help( I[m being held prisoner in a fortune cookie factory)].', 'no'],
            ['([ (([( [ ] ) ( ) (( ))] )) ]).', 'yes'],
            [' .', 'yes'],
        ]

        for test_case in test_cases:
            data, expected = test_case

            actual = solve(data)

            self.assertEqual(expected, actual)
