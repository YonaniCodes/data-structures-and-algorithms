# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        manhat = []
        for i in range(n):
            for j in range(i+1,n):
                x = abs(points[i][0]-points[j][0])
                y = abs(points[i][1]-points[j][1])
                manhat.append((x+y,i,j))
        manhat.sort()
        

        parent = {i:i for i in range(n)}
        size = [1] * n
        

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x,y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                if size[root_x] > size[root_y]:
                    parent[root_y] = root_x
                    size[root_x]+=size[root_y]
                else:
                    
                    parent[root_x] = root_y
                    size[root_y]+=size[root_x]

        dist = 0  
        # visited = set()     
        for i in range(len(manhat)):
            
            x = manhat[i][1]
            y= manhat[i][2]
            dis= manhat[i][0]
            if find(x) != find(y):
                union(x,y)
                dist+=dis
                
        # print(parent)
        return dist
