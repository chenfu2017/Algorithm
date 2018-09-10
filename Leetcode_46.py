class Solution:
    list = []
    visit = []
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.list.clear()
        if len(nums) == 0:
            return list
        l = []
        self.visit = [False]*len(nums)

        self.fun(nums, 0, l)
        return self.list

    def fun(self, nums, index, l):
        if index == len(nums):
            self.list.append(l.copy())
            return
        for i in range(len(nums)):
            if not self.visit[i]:
                l.append(nums[i])
                self.visit[i] =True
                self.fun(nums, index + 1, l)
                l.pop()
                self.visit[i] =False



Solution().permute([1, 2, 3])
