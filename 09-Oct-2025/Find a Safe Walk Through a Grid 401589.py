# Problem: Find a Safe Walk Through a Grid - https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])

        start_health = health - grid[0][0]
        if start_health <= 0:
            return False
     
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        
        seen = [[[False] * (health + 1) for _ in range(n)] for __ in range(m)]
        q = deque()
        q.append((0, 0, start_health))
        seen[0][0][start_health] = True
        
        while q:
            i, j, h = q.popleft()
            if i == m-1 and j == n-1 and h > 0:
                return True
            
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n:
                    nh = h - grid[ni][nj]
                    if nh > 0 and not seen[ni][nj][nh]:
                        seen[ni][nj][nh] = True
                        q.append((ni, nj, nh))
        
        return False
