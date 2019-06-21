# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)

from collections import Counter

def palindromePermutation(string):
    normalized = string.lower().replace(' ','')

    counts = Counter()
    for c in normalized:
        counts[c] += 1
    
    odds = 0
    for c in counts:
        if counts[c] % 2 == 1:
            if len(normalized) % 2 == 0:
                # all characters should appear even times
                # in an an even-long normalized string
                return False
            elif odds > 0:
                # at max 1 character can appear only once
                # in an an odd-long normalized string
                return False
            else:
                odds += 1

    return True


# Tests
import unittest

class Test(unittest.TestCase):
    cases = [
        ('Tact Coa', True),
        ('Anita tina la lava ',True),
        ('a panama man a plan a canal ',True),
        ('a panama man a plan a canal e',False),
        ('Random Words', False),
        ('Random Words Random Words', True),
        ('Palindrome is not a palindrome', False),
        ('XYZ xyz', True)
    ]

    def testCases(self):
        for param, expected in self.cases:
            with self.subTest(param=param, expected=expected):
                self.assertEqual(palindromePermutation(param), expected)

if __name__ == '__main__':
    unittest.main()