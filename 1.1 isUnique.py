# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

# O(n)
# def isUnique(string):
#     if not isinstance(string, str):
#         return False

#     return len(string) == len(set(list(string)))


# without aditional data structures ("bit vector")
# O(n)
def isUnique(string):
    if not isinstance(string, str):
        return False
    
    # Assuming character set is ASCII (256 characters)
    if len(string) > 256:
        return False

    char_set = [False] * 256
    
    for i in string:
        if char_set[ord(i)]:
            return False
        else:
            char_set[ord(i)] = True

    return True


# Tests
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