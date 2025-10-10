# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # so we try to do make a graph
        graph = defaultdict(list)
        for start,end,w in times:
            graph[start].append((end,w))

        # start processsing from k
        heap = [(0,k)]
        processed = set()
        distances = {node:float('inf') for node in range(1,n+1)}
        distances[k] = 0


        # now process the child and update the min distance
        while heap:
            dist,node = heapq.heappop(heap)

            if node not in processed:

                processed.add(node)

                for x,y in graph[node]:
                    n_dist = dist+y

                    if n_dist < distances[x]:
                        distances[x] = n_dist
                        heapq.heappush(heap,(n_dist,x))

        if len(processed) < n:
            return -1
        else:
            return max(distances.values())
       