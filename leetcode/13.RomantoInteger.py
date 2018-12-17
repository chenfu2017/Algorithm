class Solution:
    m ={
        'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
    }
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==1:
            return self.m.get(s)
        res = 0
        for i in range(1,len(s)):
            v1 = self.m.get(s[i-1])
            v2 = self.m.get(s[i])
            if v1<v2:
                v1 *=-1
            res +=v1
        res +=v2
        return res

print(Solution().romanToInt("VI"))



