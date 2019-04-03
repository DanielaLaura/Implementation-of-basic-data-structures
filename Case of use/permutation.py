#O(n)
import unittest
from collections import Counter


def check_perm(str1, str2):
    if len(str1)!=len(str2):
       return False
    counter= Counter()
    # counts the number of each char in the first string
    for c in str1:
        counter[c] +=1
    # checks the number of each char in the second string
    for c in str2:
        #doesn't find any c char of str1 in str2
        if counter[c]==0:
            return False
        #changes the value of counter[c] by minus one.
        counter[c] -= 1
    return True

class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()