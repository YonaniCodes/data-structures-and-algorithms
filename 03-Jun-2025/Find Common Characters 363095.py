# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        common = Counter(words[0])
        
        for w in words[1:]:
            common &= Counter(w)
        # print(common.elements())
        return list(common.elements())