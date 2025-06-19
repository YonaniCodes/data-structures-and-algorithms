# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # :type id: int
        # :type importance: int
        # :type subordinates: List[int]
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        # Step 1: Create a map from ID to Employee object for quick lookup
        emp_map = {emp.id: emp for emp in employees}

        # Step 2: Define recursive DFS to accumulate importance
        def dfs(emp_id):
            employee = emp_map[emp_id]
            total = employee.importance
            for sub_id in employee.subordinates:
                total += dfs(sub_id)
            return total

        # Step 3: Start DFS from the given ID
        return dfs(id)
