class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        n = len(s)
        left = right = 0
        m = {}
        while left < n:
            if s[right] not in m:
                m[s[right]] = 1
            else:
                m[s[right]] += 1
            flag = True
            for c in m:
                if m[c] < k:
                    flag = False
                    break
            if flag:
                res = max(res,right-left+1)
            right +=1
            if right == n:
                m.clear()
                left +=1
                right = left
        return res

s = "ababbc"
k = 2
print(Solution().longestSubstring(s,k))



