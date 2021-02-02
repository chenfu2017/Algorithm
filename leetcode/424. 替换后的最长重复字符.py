class Solution(object):
    def changeToIndex(self, s):
        return ord(s) - ord('A')

    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        hashm = [0] * 26
        maxn = left = right = 0
        while right < n:
            hashm[self.changeToIndex(s[right])] += 1
            maxn = max(maxn, hashm[self.changeToIndex(s[right])])
            if right - left + 1 - maxn > k:
                hashm[self.changeToIndex(s[left])] -=1
                left += 1
            right +=1
        return right - left
s = "AAABBBBB"
k = 0
print(Solution().characterReplacement(s, k))
