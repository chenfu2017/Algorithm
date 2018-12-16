class Solution:
    list = []
    visit = []
    def permute(self, nums):
        self.list.clear()
        if len(nums) == 0:
            return list
        l = []
        self.visit = [False]*len(nums)
        self.fun(nums, 0, l)
        return self.list

    def fun(self, nums, index, l):
        if index == len(nums):
            if l not in self.list:
                self.list.append(l.copy())
            return
        for i in range(len(nums)):
            if not self.visit[i]:
                l.append(nums[i])
                self.visit[i] =True
                self.fun(nums, index + 1, l)
                l.pop()
                self.visit[i] =False

result=Solution().permute(['a', 'a','c','c'])
for l in result:
    print(l)
