# Problem: Sort Items by Groups Respecting Dependencies - https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

from collections import defaultdict, deque
from typing import List

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # Step 1: Assign a new group to items with no group (-1)
        new_group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = new_group_id
                new_group_id += 1

        # Step 2: Build item and group graphs
        item_graph = defaultdict(list)
        item_indegree = [0] * n

        group_graph = defaultdict(set)
        group_indegree = [0] * new_group_id

        group_to_items = defaultdict(list)
        for curr in range(n):
            group_to_items[group[curr]].append(curr)
            for prev in beforeItems[curr]:
                item_graph[prev].append(curr)
                item_indegree[curr] += 1
                if group[curr] != group[prev]:
                    if group[curr] not in group_graph[group[prev]]:
                        group_graph[group[prev]].add(group[curr])
                        group_indegree[group[curr]] += 1

        # Step 3: Topological sort function
        def topological_sort(graph, indegree, nodes):
            res = []
            queue = deque([node for node in nodes if indegree[node] == 0])
            while queue:
                node = queue.popleft()
                res.append(node)
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
            return res if len(res) == len(nodes) else []

        # Step 4: Topological sort on groups
        sorted_groups = topological_sort(group_graph, group_indegree, list(range(new_group_id)))
        if not sorted_groups:
            return []

        # Step 5: Topological sort on items within each group
        result = []
        for grp in sorted_groups:
            items = group_to_items[grp]
            if not items:
                continue
            sub_graph = defaultdict(list)
            sub_indegree = {item: 0 for item in items}
            for item in items:
                for nei in item_graph[item]:
                    if nei in sub_indegree:
                        sub_graph[item].append(nei)
                        sub_indegree[nei] += 1
            sorted_items = topological_sort(sub_graph, sub_indegree, items)
            if not sorted_items:
                return []
            result.extend(sorted_items)

        return result

