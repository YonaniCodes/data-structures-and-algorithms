# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

n, m = map(int, input().split())
degree = [0] * n  # initialize degree list

for _ in range(m):
    vertex,edge=map(int, input().split())
    degree[vertex-1]+=1
    degree [edge-1]+=1

if all([deg==degree[0] for deg in degree]):
    print("YES")
else:
    print("NO")

