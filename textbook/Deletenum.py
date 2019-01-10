class Solution:
    def delete(self, nums, k):
        l = []
        for i in nums:
            l.append(i)
        for i in range(k):
            flag = False
            for j in range(1, len(l)):
                if l[j] < l[j - 1]:
                    l.remove(l[j - 1])
                    flag = True
                    break
            if not flag:
                l.pop(-1)
        return ''.join(l)


nums = "12947"
print(Solution().delete(nums, 2))
