# Is Unique:
# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def isUnique(string):
    if not isinstance(string, str):
        return False

    return len(string) == len(set(list(string)))

import unittest
    
class isUniqueTestCase(unittest.TestCase):
    cases = [
        ('hola',True),
        ('aaaaa',False),
        ('a',True),
        ('',True),
        ('asdfghjklñ',True),
        (None, False),
        ('abca', False),
    ]

    def testCases(self):
        for param, expected in self.cases:
            with self.subTest(param=param, expected=expected):
                self.assertEqual(isUnique(param), expected)

if __name__ == '__main__':
    unittest.main()
