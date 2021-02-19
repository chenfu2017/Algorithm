class Solution:
    def countHomogenous(self, s: str) -> int:
        length = 10**5+1
        m = [0] * length
        res = 0
        for i in range(1,length):
            m[i] +=(m[i-1]+i)%(10**9 +7)
        count = 0
        c = s[0]
        for i in s:
            if i == c:
                count +=1
            else:
                res += m[count]%(10**9 +7)
                count = 1
                c = i
        if s[-1] == c:
            res +=m[count]
        return res%(10**9 +7)






s = 'abbcccaa'
print(Solution().countHomogenous(s))