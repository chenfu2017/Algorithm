class Solution:
    def containsNearbyDuplicate(self, nums, k):
        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            s.add(nums[i])
            if len(s) == k + 1:
                s.remove(nums[i - k])
        return False


nums = [1, 2, 3, 1]
k = 3
print(Solution().containsNearbyDuplicate(nums, k))
