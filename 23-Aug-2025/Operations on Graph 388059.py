# Problem: Operations on Graph - https://www.eolymp.com/en/contests/9060/problems/78602

from collections import defaultdict
vertices = int(input())
graph = defaultdict(list)
op = int(input())
for x in range(op):
    line = list(map(int, input().split()))
    if line[0] == 1:
        graph[line[1]].append(line[2])
        graph[line[2]].append(line[1])
    else:
        print (*graph[line[1]])