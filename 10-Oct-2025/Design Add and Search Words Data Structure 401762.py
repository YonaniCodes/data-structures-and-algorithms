# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.child = [None]*27
        # so the 26 will be .
        self.isend = False



class WordDictionary:

    def __init__(self):
        self.root  = TrieNode()

        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            pos = ord(c)-97
            if curr.child[pos] == None:
                curr.child[pos] = TrieNode()
                # curr.child[27] = TrieNode()
            curr = curr.child[pos]
        curr.isend = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        n = len(word)

        queue = deque()
        queue.append((curr,0))

        while queue:
            
            curr,i = queue.popleft()
            if i == n:
                if curr.isend:
                    return True
                continue


            c = word[i]

            if c == '.':
                for j in range(26):
                    
                    if curr.child[j] != None:
                        queue.append((curr.child[j], i+1))
            else:
                pos = ord(c)-97
                if curr.child[pos] != None:
                    queue.append((curr.child[pos],i+1))

        return False