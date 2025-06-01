# Problem: Check If Two String Arrays are Equivalent - https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        word_string1=""
        word_string2=""

        for char in word1:
            word_string1+=char

        for char in word2:
            word_string2+=char

        return word_string1==word_string2

        
        