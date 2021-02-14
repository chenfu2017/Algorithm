class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = [0] * 26
        n = [0] * 26
        s1length = len(s1)
        s2length = len(s2)
        for s in s1:
            m[ord(s) - ord('a')] += 1
        pcount = wcount = 0
        for i in m:
            if i > 0:
                pcount += 1
        left = right = 0
        while right < s2length:
            rightindex = ord(s2[right])-ord('a')
            if m[rightindex] > 0:
                n[rightindex] +=1
                if n[rightindex] == m[rightindex]:
                    wcount +=1
            right +=1
            while pcount == wcount:
                if right - left == s1length:
                    return True
                leftindex = ord(s2[left])-ord('a')
                if m[leftindex] > 0:
                    n[leftindex] -=1
                    if n[leftindex] < m[leftindex]:
                        wcount -= 1
                left +=1
        return False


s1 = "ab"
s2 = "eidbbaoo"
print(Solution().checkInclusion(s1, s2))
