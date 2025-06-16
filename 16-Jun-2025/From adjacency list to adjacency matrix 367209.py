# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

n = int(input())
adj_matrix = [[0] * n for _ in range(n)]

for i in range(n):
    parts = list(map(int, input().split()))
    k = parts[0]
    for j in range(1, k + 1):
        destination = parts[j] - 1  # convert to 0-based index
        adj_matrix[i][destination] = 1

for row in adj_matrix:
    print(' '.join(map(str, row)))
