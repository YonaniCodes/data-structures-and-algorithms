# Problem: Largest Merge of Two Strings - https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = []
        word1 = list(word1)
        word2 = list(word2)

        while word1 and word2:
            if word1 > word2:
                merge.append(word1.pop(0))
            else:
                merge.append(word2.pop(0))

        merge.extend(word1)
        merge.extend(word2)
        return "".join(merge)
