# Problem: Minimize Hamming Distance After Swap Operations - https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description/

from collections import defaultdict, Counter
from typing import List

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        parent = list(range(len(source)))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
   
        for a, b in allowedSwaps:
            union(a, b)
 
        groups = defaultdict(list)
        for i in range(len(source)):
            groups[find(i)].append(i)
     
        ans = 0
        for indices in groups.values():
      
            src_count = Counter(source[i] for i in indices)
            tgt_count = Counter(target[i] for i in indices)
         
            for num, cnt in tgt_count.items():
                if num in src_count:
                    matched = min(src_count[num], cnt)
                    src_count[num] -= matched
            
           
            ans += sum(src_count.values())
        
        return ans
