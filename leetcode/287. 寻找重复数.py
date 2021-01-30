class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # m = set()
        # for num in nums:
        #     if num not in m:
        #         m.add(num)
        #     else:
        #         return num

        node = nums[0]
        tail = nums[0]
        while True:
            node = nums[node]
            tail = nums[nums[tail]]
            if node == tail:
                break
        node = nums[0]
        ptr = tail
        while node != ptr:
            node = nums[node]
            ptr = nums[ptr]
        return node


nums = [1, 3, 4, 2, 2]
print(Solution().findDuplicate(nums))
