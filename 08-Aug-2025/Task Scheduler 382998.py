# Problem: Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for t in tasks:
            freq[ord(t) - ord('A')] += 1

        freq.sort(reverse=True)
        max_freq = freq[0]
        max_count = freq.count(max_freq)

        part_count = max_freq - 1
        part_length = n + 1

        min_length = part_count * part_length + max_count

        return max(len(tasks), min_length)

        