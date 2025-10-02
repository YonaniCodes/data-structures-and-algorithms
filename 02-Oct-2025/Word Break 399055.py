# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
     

        _set = set(wordDict)
        
        queue = deque([0])

        seen = set()
        seen.add(0)
        n = len(s)
        end = 0

        while queue:
            i = queue.popleft()
            
            

            if i == n:
                return True
            # print(i)

            for j in range(i+1,n+1):
                # print(i+1)
                if s[i:j] in _set and j not in seen:
                    queue.append(j)
                    seen.add(j)
            
        return False





        
