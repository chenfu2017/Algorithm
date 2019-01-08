class Solution:
    def sort(self, nums):
        def mergesort(nums, l, r):
            if l < r:
                mid = (l + r) // 2
                mergesort(nums, l, mid)
                mergesort(nums, mid + 1, r)
                self.merge(nums, l, mid, r)

        mergesort(nums, 0, len(nums) - 1)

    def merge(self, nums, l, mid, r):
        i = l
        j = mid + 1
        k = []
        while i <= mid and j <= r:
            if nums[i] < nums[j]:
                k.append(nums[i])
                i += 1
            else:
                k.append(nums[j])
                j += 1
        while i <= mid:
            k.append(nums[i])
            i += 1
        while j <= r:
            k.append(nums[j])
            j += 1
        nums[l:r + 1] = k[0:]


nums = [3, 2, 2, 4, 1]
Solution().sort(nums)
print(nums)
