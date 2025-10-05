# Problem: Path With Minimum Effort - https://leetcode.com/problems/path-with-minimum-effort/description/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        heap = [(0, 0, 0)]  # (effort, r, c)
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        effort = [[float('inf')] * col for _ in range(row)]
        effort[0][0] = 0

        def inbound(r, c):
            return 0 <= r < row and 0 <= c < col

        while heap:
            curr_effort, r, c = heapq.heappop(heap)

            if r == row-1 and c == col-1:
                return curr_effort

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if inbound(nr, nc):
                    new_effort = max(curr_effort, abs(heights[r][c] - heights[nr][nc]))
                    if new_effort < effort[nr][nc]:
                        effort[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))

        return effort[row-1][col-1]