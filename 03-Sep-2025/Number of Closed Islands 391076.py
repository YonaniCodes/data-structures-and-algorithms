# Problem: Number of Closed Islands - https://leetcode.com/problems/number-of-closed-islands/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]

        def inbound(i, j):
            return 0 <= i < m and 0 <= j < n

        def dfs(i, j):
            if not inbound(i, j) or grid[i][j] == 1 or visited[i][j]:
                return True
            visited[i][j] = True

            # if we are on the border, it's NOT a closed island
            is_closed = not (i == 0 or i == m-1 or j == 0 or j == n-1)

            for a, b in dirs:
                if not dfs(i+a, j+b):
                    is_closed = False
            return is_closed

        components = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not visited[i][j]:
                    components += dfs(i,j)
        return components