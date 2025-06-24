# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution(object):
    def isBipartite(self, graph):
        n = len(graph)
        color = [-1] * n  # -1 means unvisited

        for start in range(n):
            if color[start] == -1:
                queue = [start]
                color[start] = 0

                while queue:
                    node = queue.pop(0)
                    for neighbor in graph[node]:
                        if color[neighbor] == -1:
                            color[neighbor] = 1 - color[node]
                            queue.append(neighbor)
                        elif color[neighbor] == color[node]:
                            return False
        return True

