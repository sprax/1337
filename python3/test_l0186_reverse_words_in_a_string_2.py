import unittest

from l0186_reverse_words_in_a_string_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('blue is sky the', Solution().reverseWords('the sky is blue'))
        self.assertEqual('world! hello', Solution().reverseWords('hello world!'))
        self.assertEqual('example good a', Solution().reverseWords('a good example'))
