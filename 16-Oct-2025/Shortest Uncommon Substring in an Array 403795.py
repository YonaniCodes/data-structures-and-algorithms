# Problem: Shortest Uncommon Substring in an Array - https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description/

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        # use a dict to store all the substrings
        print('g'>'fn')
        _dict = defaultdict(int)
        for word in arr:
            n = len(word)
            seen = set()
            for i in range(n):
                for j in range(i,n):
                    sub = word[i:j+1]
                   
                    if sub not in seen:
                        _dict[sub] += 1
                        seen.add(sub)
        # print(_dict)
        ans = []
        for word in arr:
            n = len(word)
            _min = 'z'*21
            for i in range(n):
                for j in range(i,n):
                    sub = word[i:j+1]
                    
                    val = _dict[sub]

                    if val == 1:
                        if len(sub) < len(_min):
                            # print('min:',_min)
                            _min = sub
                            # print('min:',_min,'sub:',sub)
                        elif len(sub) == len(_min):
                            if sub < _min:
                                _min = sub
            if _min == ('z'*21):
                ans.append('')
            else:
                ans.append(_min)
        return ans


                    