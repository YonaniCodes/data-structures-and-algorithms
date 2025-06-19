# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        from collections import defaultdict

        # Step 1: Build the graph (adjacency list)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Initialize visited set
        visited = set()

        # Step 3: Define the DFS function
        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False

        # Step 4: Start DFS from the source node
        return dfs(source)
