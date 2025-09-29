# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        _dict = defaultdict(list)
        for i, lett in enumerate(s):
            c = ord(lett) - 97
            _dict[c].append(i)
        # print(_dict)

        count = 0
        for word in words:
            prev = -1
            flag = True
            for ch in word:
                c = ord(ch) - 97
                if c not in _dict:
                    flag = False
                    break
                
                pos_list = _dict[c]
                # print(pos_list)
                
                idx = bisect_right(pos_list, prev)
                # print('idx:',idx)
                if idx >= len(pos_list):  # this means if there is no idx position grater that the prev which means it exists previously
                    flag = False
                    break
                prev = pos_list[idx]  
            
            if flag:
                count += 1
        return count
