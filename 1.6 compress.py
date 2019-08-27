# String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def compress(string):
    c = [string[0]]
    last = string[0]
    cont = 1
    for i in range(1, len(string)):
        if string[i] == last:
            cont += 1
        else:
            c.append(str(cont))
            c.append(string[i])
            last = string[i]
            cont = 1
    c.append(str(cont))

    result = "".join(c)
    if len(result) < len(string):
        return result
    else:
        return string


# Tests
import unittest

class Test(unittest.TestCase):
    cases = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abc', 'abc'),
        ('aabc', 'aabc'),
        ('zzz', 'z3'),
        ('zz', 'zz'),
        ('jkjjjfffssssssaaaasds','j1k1j3f3s6a4s1d1s1'),
        ('abcdef', 'abcdef'),
    ]

    def testCases(self):
        for param, expected in self.cases:
            with self.subTest(param=param, expected=expected):
                self.assertEqual(compress(param), expected)

if __name__ == '__main__':
    unittest.main()