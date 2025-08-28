# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = list(range(n))
        rank = [1] * n

        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
 
        email_to_index = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_index:
                    union(i, email_to_index[email])  # merge accounts with same email
                email_to_index[email] = i

    
        index_to_emails = {}
        for email, idx in email_to_index.items():
            root = find(idx)
            if root not in index_to_emails:
                index_to_emails[root] = []
            index_to_emails[root].append(email)

       
        result = []
        for idx, emails in index_to_emails.items():
            name = accounts[idx][0]
            result.append([name] + sorted(emails))

        return result
