class Solution:
    def maxSubsum(self, num, l, r):
        if r == l:
            return max(num[r], 0)
        mid = (l + r) // 2
        leftsum = self.maxSubsum(num, l, mid)
        rightnum = self.maxSubsum(num, mid + 1, r)
        s1, s2, lefts, rights, = 0, 0, 0, 0
        for i in range(mid, l - 1, -1):
            lefts += num[i]
            if lefts > s1:
                s1 = lefts
        for j in range(mid + 1, r + 1):
            rights += num[j]
            if rights > s2:
                s2 = rights
        return max(leftsum, rightnum, s1 + s2)


num = [-2, 11, -12, 15, -6, 5, 10, - 2]
print(Solution().maxSubsum(num, 0, len(num) - 1))
