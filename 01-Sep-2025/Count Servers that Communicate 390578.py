# Problem: Count Servers that Communicate - https://leetcode.com/problems/count-servers-that-communicate/description/

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        colServers = [0] * cols
        rowServers = [0] * rows

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    colServers[c] += 1
                    rowServers[r] += 1

        totalCommunicating = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if colServers[c] > 1 or rowServers[r] > 1:
                        totalCommunicating += 1

        return totalCommunicating
