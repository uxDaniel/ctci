# One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

from collections import Counter

# O(n)
def oneAway(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    diff = abs(len1 - len2)
    
    if diff > 1:
        return False
    
    changes = 0
    if diff == 0:
        for i in range(len1):
            if string1[i] != string2[i]:
                changes += 1
                if changes > 1:
                    return False

        if changes == 0:
            return False
        else:
            return True
    
    if len1>len2:
        strings = [string2, string1]
    else:
        strings = [string1, string2]

    changes = 0
    i,j = 0,0
    while i < len(strings[0]):
        if strings[0][i] != strings[1][j]:
            changes += 1
            if changes > 1:
                return False
            i -= 1
        i += 1
        j += 1
    
    return True

# Tests
import unittest

class Test(unittest.TestCase):
    cases = [
        (('pale', 'ple'), True),
        (('pales', 'pale'), True),
        (('pale', 'pales'), True),
        (('pale', 'spale'), True),
        (('pale', 'bale'), True),
        (('pale', 'bake'), False),
        (('pale', 'elap'), False),
        (('pale', 'ela'), False),
        (('ela', 'pale'), False),
        (('pale', 'pale'), False),
        (('pale', 'plae'), False),
        (('pale', 'pze'), False)
    ]

    def testCases(self):
        for param, expected in self.cases:
            with self.subTest(param=param, expected=expected):
                self.assertEqual(oneAway(*param), expected)

if __name__ == '__main__':
    unittest.main()