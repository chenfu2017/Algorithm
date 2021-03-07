class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        maxm = [0] * 26
        minm = [float('inf')] * 26
        left = right = 0
        ans = 0
        while left < n:
            index = ord(s[right]) - ord('a')
            maxm[index] += 1
            if minm[index] == float('inf'):
                minm[index] = 1
            else:
                minm[index] += 1
            maxcount = max(maxm)
            mincount = min(minm)
            ans += maxcount - mincount
            right += 1
            if right == n:
                leftindex = ord(s[left]) - ord('a')
                maxm[leftindex] -= 1
                minm[leftindex] -= 1
                if minm[leftindex] == 0:
                    minm[leftindex] = float('inf')
                left += 1
                right = left
                maxm = [0] * 26
                minm = [float('inf')] * 26
        return ans


s = "aabcb"
print(Solution().beautySum(s))
