# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges):

        n = len(edges)
        parent = [i for i in range(n+1)]  
        rank = [1] * (n+1) 
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])   
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False  # cycle detected
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]