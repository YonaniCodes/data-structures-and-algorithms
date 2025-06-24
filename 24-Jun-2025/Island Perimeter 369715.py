# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution(object):
    def islandPerimeter(self, grid):  # add 'self' here
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    if r > 0 and grid[r-1][c] == 1:  # top neighbor
                        perimeter -= 2
                    if c > 0 and grid[r][c-1] == 1:  # left neighbor
                        perimeter -= 2

        return perimeter
