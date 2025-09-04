# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

from collections import defaultdict
from typing import List

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UnionFind:
            def __init__(self, n):
                self.parent = list(range(n))
            
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x, y):
                rootX, rootY = self.find(x), self.find(y)
                if rootX != rootY:
                    if rootX < rootY:
                        self.parent[rootY] = rootX
                    else:
                        self.parent[rootX] = rootY
        
        uf = UnionFind(len(s))
        for a, b in pairs:
            uf.union(a, b)
        
        groups = defaultdict(list)
        for i, char in enumerate(s):
            groups[uf.find(i)].append(char)
        
      
        for group in groups.values():
            group.sort(reverse=True)
        
 
        result = []
        for i in range(len(s)):
            result.append(groups[uf.find(i)].pop())
        
        return ''.join(result)
