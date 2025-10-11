# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        

        new = []
        for sub in folder:
            n = len(sub)
            arr = []
            x = ''
            for i in range(n):
                if sub[i] != '/':
                    x += sub[i]
                    # print('if:',x)
                else:
                    arr.append(x)
                    # print('else:',x,'arr:',arr)
                    x = ''   
            arr.append(x)  
            new.append(arr)
        # print(new)

        curr = new[0]
        m = len(curr)
        ans = [curr]
        _set = set()
        for sub in new[1:]:
            # print(curr)
            n = len(sub)
            if n >= m and sub[:m] == curr:
                continue
            ans.append(sub)
            curr = sub
            m = len(curr) 
        # print(ans)
        return ["/".join(path) for path in ans]