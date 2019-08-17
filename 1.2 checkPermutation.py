# Check Permutation: Given two strings,write a method to decide if one is a permutation of the other.

# O(n + n log n)
# def checkPermutation(str1, str2):
#     if len(str1) != len(str2):
#         return False

#     lst1, lst2 = list(str1), list(str2)
#     lst1.sort()
#     lst2.sort()

#     for i in range(len(lst1)):
#         if lst1[i] != lst2[i]:
#             return False

#     return True


# without sorting the strings
# O(n)
def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        return False

    chars = [0]*256

    for c in str1:
        chars[ord(c)] += 1

    for c in str2:
        chars[ord(c)] -= 1
        if chars[ord(c)] < 0:
            print(chars)
            return False

    return True

# Tests
import unittest

class checkPermutationTestCase(unittest.TestCase):
    cases = [
        (('hola','hol'),False),
        (('hola','hloa'),True),
        (('hola','ahloa'),False),
        (('hola mundo','odnum aloh'),True),
        (('holaz','ahola'),False),
        (('holaa','holay'),False),
    ]

    def testCases(self):
        for param, expected in self.cases:
            with self.subTest(param=param, expected=expected):
                self.assertEqual(checkPermutation(*param), expected)

if __name__ == '__main__':
    unittest.main()