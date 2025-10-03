# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Step 1: Initialize a reachability matrix
        reachable = [[False] * numCourses for _ in range(numCourses)]
        
        # Step 2: Mark direct prerequisites
        for pre, course in prerequisites:
            reachable[pre][course] = True
        
        # Step 3: Compute transitive closure
        for k in range(numCourses):          # intermediate
            for i in range(numCourses):      # start
                if reachable[i][k]:
                    for j in range(numCourses):  # end
                        if reachable[k][j]:
                            reachable[i][j] = True
        
        # Step 4: Answer queries
        return [reachable[u][v] for u, v in queries]
