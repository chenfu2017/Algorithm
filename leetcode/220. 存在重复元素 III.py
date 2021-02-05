class Solution(object):
    def getId(self, x, w):
        return x // w if x >= 0 else (x + 1) // w - 1

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if len(nums) == 0 or k == 0 or k == 10000:
            return False
        m = {}
        w = t + 1
        for i in range(len(nums)):
            id = self.getId(nums[i], w)
            if id in m:
                return True
            if id - 1 in m and abs(m[id - 1] - nums[i]) <= t:
                return True
            if id + 1 in m and abs(m[id + 1] - nums[i]) <= t:
                return True
            m[id] = nums[i]
            if i >= k:
                m.pop(self.getId(nums[i - k], w))
        return False


nums = [1, 2, 3, 1]
k = 3
t = 0
print(Solution().containsNearbyAlmostDuplicate(nums, k, t))
