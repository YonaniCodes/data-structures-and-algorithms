# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Initialize indegree counts for all n nodes to 0
        indegree = [0] * n
        
        # For each edge u → v, increment indegree[v]
        for u, v in edges:
            indegree[v] += 1
        
        # Any node with indegree == 0 is a required start-vertex
        result = [node for node in range(n) if indegree[node] == 0]
        
        return result
