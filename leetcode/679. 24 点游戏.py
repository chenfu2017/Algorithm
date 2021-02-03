class Solution(object):

    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1:
            return abs(nums[0] - 24) < 1e-9
        isValid = False
        for i in range(n):
            for j in range(i + 1, n):
                a = nums[i]
                b = nums[j]
                l = []
                for k in range(n):
                    if k != i and k != j:
                        l.append(nums[k])
                isValid = isValid or self.judgePoint24(l + [a + b])
                isValid = isValid or self.judgePoint24(l + [a * b])
                isValid = isValid or self.judgePoint24(l + [a - b])
                isValid = isValid or self.judgePoint24(l + [b - a])
                if a != 0:
                    isValid = isValid or self.judgePoint24(l + [b / a])
                if b != 0:
                    isValid = isValid or self.judgePoint24(l + [a / b])
                if isValid:
                    return True
        return False


nums = [1,7,4,5]
print(Solution().judgePoint24(nums))
