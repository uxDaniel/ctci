# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,and that you are given the "true" length of the string. (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"

def URLify(string):
    # length parameter is not needed in python
    return string.strip().replace(' ','%20')


# Tests
import unittest

class Test(unittest.TestCase):
    cases = [
        (("Mr John Smith ",),"Mr%20John%20Smith"),
    ]

    def testCases(self):
        for param, expected in self.cases:
            with self.subTest(param=param, expected=expected):
                self.assertEqual(URLify(*param), expected)

if __name__ == '__main__':
    unittest.main()