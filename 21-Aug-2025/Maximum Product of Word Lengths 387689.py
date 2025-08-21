# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # keep a bitmask 
        # check the overlap using and operation

        
        precomputed_mask = []
        for k in range(len(words)):
            m = 0
            for ch in words[k]:
                pos = ord(ch)-97
                m|= 1<<pos
            precomputed_mask.append(m)
        # print(precomputed_mask)


        _max = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if precomputed_mask[i] & precomputed_mask[j] == 0:
                    _max = max(_max,len(words[i])*len(words[j]))
        return _max

