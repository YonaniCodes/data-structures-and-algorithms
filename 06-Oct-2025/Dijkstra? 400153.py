# Problem: Dijkstra? - https://codeforces.com/problemset/problem/20/C

import sys,heapq
from collections import defaultdict
input = sys.stdin.readline

n,m = map(int,input().split())
graph = defaultdict(list)
for _ in range(m):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))
    graph[e].append((s,w))

heap = [(0,1)]
distance= [float('inf')] * (n+1)
distance[1] = 0
seen = set()
path = {1:None}

ans = []
while heap:
    dist,node = heapq.heappop(heap)
    
    if node not in seen:

        seen.add(node)
        for neigh,w in graph[node]:
            cost = dist+w
            if cost < distance[neigh]:
                path[neigh] = node
                distance[neigh] = cost
                heapq.heappush(heap,(cost,neigh))
 
 
               

if distance[n] == float('inf'):
    print(-1)
else:
    ans = []
    while n:
        ans.append(n)
        n = path[n]
    print(*ans[::-1])