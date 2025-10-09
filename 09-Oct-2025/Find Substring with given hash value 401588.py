# Problem: Find Substring with given hash value - https://leetcode.com/problems/find-substring-with-given-hash-value/description/

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        result_index = 0
        hash_val = 0
        power_k = pow(power, k, modulo)
        
        for i in range(n - 1, -1, -1):
            val = ord(s[i]) - 96  # 'a' -> 1, ..., 'z' -> 26
            hash_val = (hash_val * power + val) % modulo

 
            if i + k < n:
                remove_val = ord(s[i + k]) - 96
                hash_val = (hash_val - remove_val * power_k) % modulo
 
            if (hash_val % modulo) == hashValue:
                result_index = i

        return s[result_index: result_index + k]
