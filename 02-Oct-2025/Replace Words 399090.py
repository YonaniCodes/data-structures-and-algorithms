# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
        def __init__(self):
            self.child = [None]*26
            self.isend = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        n = len(word)
        curr = self.root
        for i in range(n):
            c = word[i]
            pos = ord(c)-97
            
            if curr.child[pos] == None:
                curr.child[pos] = TrieNode()
            curr = curr.child[pos]
        curr.isend = True
    
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        
        for word in dictionary:
            self.insert(word)
        ans = ''
        for word in words:
            curr= self.root
            
            n = len(word)
            for i in range(n):
                c = word[i]
                pos = ord(c)-97
                if curr.isend == True:
                    ans+=word[:i]
                    break
                elif curr.child[pos] is None:
                    ans+=word
                    break
                curr = curr.child[pos]
            else:
                ans+=word
            ans+=' '
        
        return ans.strip()




        