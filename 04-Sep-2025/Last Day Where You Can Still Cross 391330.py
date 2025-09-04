# Problem: Last Day Where You Can Still Cross - https://leetcode.com/problems/last-day-where-you-can-still-cross/

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
                self.parent[self.find(y)] = self.find(x)
        
        n = len(s)
        uf = UnionFind(n)
        for a, b in pairs:
            uf.union(a, b)
        
        groups = defaultdict(list)
        for i in range(n):
            groups[uf.find(i)].append(s[i])
        
        for group in groups.values():
            group.sort(reverse=True)
        
        res = []
        for i in range(n):
            res.append(groups[uf.find(i)].pop())
        
        return "".join(res)
