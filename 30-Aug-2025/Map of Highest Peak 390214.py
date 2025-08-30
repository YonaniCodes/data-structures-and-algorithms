# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n, m = len(isWater), len(isWater[0])
        
        def inbound(x, y):
            return 0 <= x < n and 0 <= y < m

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = [[-1 for _ in range(m)] for _ in range(n)]
        queue = deque()

        
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    result[i][j] = 0
                    queue.append((i, j))

        
        while queue:
            x, y = queue.popleft()
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if inbound(nx, ny) and result[nx][ny] == -1:
                    result[nx][ny] = result[x][y] + 1
                    queue.append((nx, ny))

        return result