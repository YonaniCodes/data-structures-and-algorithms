# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        ans = []
        if len(s) > 12:
            return ans

        def test(i,dots,IP):
            if dots == 4 and i == len(s):
                ans.append(IP[:-1])
                return
            if dots > 4:
                return
            for j in range(i,min(i+3,len(s))):
                if int(s[i:j+1]) <= 255 and (i == j or s[i] != '0'):
                    test(j+1,dots+1,IP + s[i:j+1] + '.')

        test(0,0,'')

        return ans


