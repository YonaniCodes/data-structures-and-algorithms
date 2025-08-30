# Problem: Process Restricted Friend Requests - https://leetcode.com/problems/process-restricted-friend-requests/

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
         
        parent = list(range(n))
        
        def find(self, x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union( x, y):
            parent[find(x)] = find(y)]
        res = []

        for u, v in requests:
            root_u =find(u)
            root_v =find(v)
            
     
            can_friend = True
            for x, y in restrictions:
                root_x = find(x)
                root_y = find(y)
                if (root_u == root_x and root_v == root_y) or (root_u == root_y and root_v == root_x):
                    can_friend = False
                    break
            
            if can_friend:
                uf.union(u, v)
                res.append(True)
            else:
                res.append(False)
        
        return res