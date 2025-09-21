# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)

        # Build graph
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1.0 / val))

        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            visited = set()
            queue = deque([(start, 1.0)])

            while queue:
                node, product = queue.popleft()
                if node == end:
                    return product
                visited.add(node)
                for neighbor, weight in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, product * weight))
            return -1.0

        return [bfs(a, b) for a, b in queries]
