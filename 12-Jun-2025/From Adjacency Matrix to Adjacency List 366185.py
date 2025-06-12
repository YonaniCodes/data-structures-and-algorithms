# Problem: From Adjacency Matrix to Adjacency List - https://www.eolymp.com/en/contests/9060/problems/78603

n = int(input())  # Number of vertices

# Read the adjacency matrix
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    neighbors = []
    for j in range(n):
        if matrix[i][j] == 1:
            neighbors.append(j + 1)  # Output should be 1-based
    print(len(neighbors), *sorted(neighbors))

