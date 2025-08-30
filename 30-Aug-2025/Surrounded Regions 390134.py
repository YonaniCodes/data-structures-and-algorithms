# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        _dir = {(0,1),(1,0),(0,-1),(-1,0)}

        def inbound(x,y):
            return 0 <= x < n and 0 <= y < m
        
        visited = set()
        
        def dfs(r,c):
            for dx,dy in _dir:
                nx,ny = dx+r,dy+c
                if inbound(nx,ny) and (nx,ny) not in visited:
                    if board[nx][ny] == 'O':
                        visited.add((nx,ny))
                        board[nx][ny] = '#'
                        dfs(nx,ny)
                
            

        for i in range(n):
            for j in range(m):
                if (i,j) not in visited and board[i][j] == 'O' and (i == 0 or j == 0 or i == n-1 or j == m-1):
                    visited.add((i,j))
                    board[i][j] = '#'
                    dfs(i,j)

        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
                
        
        


        