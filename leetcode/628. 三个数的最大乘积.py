class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = [0] * 2002
        for i in nums:
            i += 1000
            d[i] += 1
        count = 2
        l = []
        i = 0
        while count != 0:
            while d[i] == 0:
                i += 1
            if count >= d[i]:
                l.extend([i-1000]*d[i])
                count -=d[i]
                i +=1
            else:
                l.extend([i-1000]*count)
                break
        # print(l)
        count = 3
        i = 2001
        while count != 0:
            while d[i] == 0:
                i -= 1
            if count >= d[i]:
                l.extend([i - 1000] * d[i])
                count -= d[i]
                i -= 1
            else:
                l.extend([i - 1000] * count)
                break
        # print(l)
        res1 = l[0] * l[1] * l[2]
        res2 = l[-1] * l[-2] * l[-3]
        return res1 if res1 > res2 else res2


nums = [-1, -2, -4]
print(Solution().maximumProduct(nums))
