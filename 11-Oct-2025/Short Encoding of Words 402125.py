# Problem: Short Encoding of Words - https://leetcode.com/problems/short-encoding-of-words/

class TrieNode:
    def __init__(self):
        self.child = [None]*26
        self.isend = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
    def startsWith(self, prefix: str) -> bool:
        curr= self.root

        for c in prefix:
            pos = ord(c)-97
            if curr.child[pos] == None:
                return False
            curr = curr.child[pos]
        return True
    def insert(self, word: str) -> None:
        n = len(word)
        curr = self.root

        for i in range(n):
            c = word[i]
            pos = ord(c)-97
            
            if curr.child[pos] == None:
                curr.child[pos] = TrieNode()
            curr = curr.child[pos]
        curr.isend = True
    def minimumLengthEncoding(self, words: List[str]) -> int:
        ans = 0
        
        x= []
       
        for word in words:
            word = word[::-1]
            x.append(word)
        x.sort(reverse = True)
        
        # print(x)
        for word in x:
            

            if not self.startsWith(word):
                self.insert(word)
                ans+= len(word)+1
        return ans