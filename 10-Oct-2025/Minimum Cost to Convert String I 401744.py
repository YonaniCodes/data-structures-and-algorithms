# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

def minCost(self, grid: List[List[int]]) -> int:

        directions = {
            1: [0,1],
            2: [0,-1],
            3: [1,0],
            4: [-1,0],
        }

        queue = deque([(0,0,0)])
        mini_cost = {(0,0) : 0}
        R = len(grid)
        C = len(grid[0])

        def inbound(r,c):
            if 0 <= r < R and 0 <= c < C:
                return True
            return False
        

        while queue:
            r, c, cost = queue.popleft()
            if (r,c) == (R - 1, C - 1):
                return cost
            
            for d in directions:
                dr,dc = directions[d]
                nr,nc = dr + r, dc + c
                new_cost = cost if d == grid[r][c] else cost + 1

                if (
                    not inbound(nr,nc) or
                    new_cost >= mini_cost.get((nr,nc), float("inf"))
                ):
                    continue 

                mini_cost[(nr,nc)] = new_cost
                if d == grid[r][c]:
                    queue.appendleft((nr,nc, new_cost))
                else:
                    queue.append((nr,nc, new_cost))
