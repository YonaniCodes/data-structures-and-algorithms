# Problem: Course Schedule - https://leetcode.com/problems/course-schedule/

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        visited = [0] * numCourses  # 0=unvisited, 1=visiting, 2=visited
        
        def dfs(node):
            if visited[node] == 1:  # cycle found
                return False
            if visited[node] == 2:  # already processed
                return True
            
            visited[node] = 1  # mark as visiting
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = 2  # done visiting
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
