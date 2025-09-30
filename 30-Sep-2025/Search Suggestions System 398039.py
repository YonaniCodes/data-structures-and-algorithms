# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

# class TrieNode:
#     def __init__(self):
#         self.child = [None]*26
#         self.isend = Fals

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # atmost 3 lexigraphically min
        products.sort()
        # print(products)

        n = len(searchWord)
        m = len(products)

        # ans = []
        out = []
        for i in range(n):
            ans = []
            for j in range(m):
                # print(i,j)
                if len(ans) < 3:
                   
                    if searchWord[:i+1] == products[j][:i+1]:
                        ans.append(products[j])
                else:
                    break
            out.append(ans)
        return out


        


        # bruteforce

        # 1.build
        # def __init__(self):
        #     self.root = TrieNode()

        # def insert(word):
        #     n = len(word)
        #     curr = self.root

        #     for i in range(n):
        #         c = word[i]
        #         pos = ord(c)-97
                
        #         if curr.child[pos] == None:
        #             curr.child[pos] = TrieNode()
        #         curr = curr.child[pos]
        #     curr.isend = True

        
       
        # insert(searchWord)
        
        # # 2.starts with
        # def startsWith(prefix):
        #     curr= self.root

        #     for c in prefix:
        #         pos = ord(c)-97
        #         if curr.child[pos] == None:
        #             return False
        #         curr = curr.child[pos]
        #     return True

        # n = len(searchWord)
        # ans = []
        # for i in range(n):

        #     x = 2
        #     while x:
        #         for words in products:
        #             if startswith(searchWord[:i+1]):
        #                 ans.append()




        # 3.just go until 3 

            