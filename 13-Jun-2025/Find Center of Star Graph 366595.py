# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        node_count_map={}

        for edge in edges:
            edge1, edge2= edge[0],edge[1]
            if edge1 in node_count_map:
                node_count_map[edge1]+=1
            else:
                node_count_map[edge1]=1

            if edge2 in node_count_map:
                node_count_map[edge2]+=1
            else:
                node_count_map[edge2]=1

        for key in node_count_map.keys():
            if node_count_map[key]== len(edges):
                return key