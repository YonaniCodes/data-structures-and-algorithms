# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # was planning on using reverse of dijkstra 

        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        heap = [(-1.0, start_node)]  # max-heap (store negative prob)
        distance = [0.0] * n
        distance[start_node] = 1.0

        while heap:
            prob, node = heapq.heappop(heap)
            prob = -prob  # convert back to positive

            if prob < distance[node]:
                continue  # skip outdated entries

            for nei, w in graph[node]:
                new_prob = prob * w
                if new_prob > distance[nei]:
                    distance[nei] = new_prob
                    heapq.heappush(heap, (-new_prob, nei))

        return distance[end_node]