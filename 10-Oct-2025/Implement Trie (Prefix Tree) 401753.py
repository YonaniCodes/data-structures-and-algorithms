# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:

    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False


class Trie:


    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if  not curr.children[ord(c)- 97]:
                curr.children[ord(c)- 97] = TrieNode()
            
            curr = curr.children[ord(c)- 97]
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if not curr.children[ord(c) - 97]:
                return False
            curr = curr.children[ord(c) - 97]
        if curr.is_end == True:
            return True
    

      
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if not curr.children[ord(c) - 97]:
                return False
            curr = curr.children[ord(c) - 97]
        return True