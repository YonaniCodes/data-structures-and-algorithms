# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(n):
            if not visited[i]:
                stack = [i]
                while stack:
                    city = stack.pop()
                    if not visited[city]:
                        visited[city] = True
                        for neighbor in range(n):
                            if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                                stack.append(neighbor)
                provinces += 1

        return provinces
