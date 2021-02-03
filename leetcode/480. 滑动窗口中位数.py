import bisect


class Solution(object):
    def median(self, list):
        n = len(list)
        return (list[n // 2] + list[(n - 1) // 2]) / 2

    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        res = []
        a = sorted(nums[:k])
        res.append(self.median(a))
        for i, j in zip(nums[:-k], nums[k:]):
            a.pop(bisect.bisect_left(a, i))
            a.insert(bisect.bisect_left(a, j), j)
            res.append(self.median(a))
        return res


nums = [1, 4, 2, 3]
k = 4
print(Solution().medianSlidingWindow(nums, k))
