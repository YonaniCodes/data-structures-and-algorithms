# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution(object):
    def eventualSafeNodes(self, graph):
        num = len(graph)
        color = [0] * num

        def dfs(node):
            if color[node] != 0:
                return color[node] == 2
          
            color[node] = 1

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            color[node] = 2
            return True
        
        ans = []

        for i in range(num):
            if dfs(i):
                ans.append(i)

        return ans
        