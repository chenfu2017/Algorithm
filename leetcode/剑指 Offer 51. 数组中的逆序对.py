class Solution:
    def __init__(self):
        self.ans = 0

    def merge(self, nums, i, j, mid):
        l = i
        r = mid + 1
        temp = []
        while l <= mid and r <= j:
            if nums[l] <= nums[r]:
                temp.append(nums[l])
                l += 1
            else:
                self.ans += mid - l + 1
                temp.append(nums[r])
                r += 1
        while l <= mid:
            temp.append(nums[l])
            l += 1
        while r <= j:
            temp.append(nums[r])
            r += 1
        for index in range(len(temp)):
            nums[i + index] = temp[index]

    def mergesort(self, nums, i, j):
        if i >= j:
            return
        mid = (i + j) // 2
        self.mergesort(nums, i, mid)
        self.mergesort(nums, mid + 1, j)
        self.merge(nums, i, j, mid)

    def reversePairs(self, nums) -> int:
        self.mergesort(nums, 0, len(nums) - 1)
        return self.ans

Solution().reversePairs([7,5,6,4])
