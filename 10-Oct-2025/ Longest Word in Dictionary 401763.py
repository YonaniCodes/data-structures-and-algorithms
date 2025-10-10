# Problem:  Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/description/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        word_set = set(words)
        longest = ''
        
        for word in words:
            is_valid = True
            for i in range(1, len(word)):
                if word[:i] not in word_set:
                    is_valid = False
                    break
            if is_valid:
                if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                    longest = word
        
        return longest