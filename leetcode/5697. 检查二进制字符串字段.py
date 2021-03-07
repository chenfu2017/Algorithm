class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        ans = 0
        left = 0
        right = 0
        count = 0
        while right < n:
            if s[right] == '1':
                count += 1
            else:
                left = right + 1
                if count > 0:
                    ans +=1
                count = 0
            right += 1
        if count > 0:
            ans +=1
        return ans == 1

s = "111110"
print(Solution().checkOnesSegment(s))
