# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        graph = defaultdict(list)
        degree = [0] * numCourses
        order = []

        for num, pre in prerequisites:
            graph[pre].append(num)
            degree[num] += 1

        queue = deque( i for i in range(numCourses) if degree[i] == 0)

        while queue:
            node  = queue.popleft()
            order.append(node)

            for neighbor in graph[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != numCourses:
            return []

        return order
        


         
        