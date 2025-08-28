# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
 
        parent = [i for i in range(26)]
        
        # Find with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
 
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return
            if rootX < rootY:
                parent[rootY] = rootX
            else:
                parent[rootX] = rootY
        
        # Union all equivalent pairs
        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))
        
 
        result = []
        for c in baseStr:
            smallest_char = chr(find(ord(c) - ord('a')) + ord('a'))
            result.append(smallest_char)
        
        return "".join(result)
