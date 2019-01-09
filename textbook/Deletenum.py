class Solution:
    def delete(self, nums, k):
        l = []
        for i in nums:
            l.append(i)
        flag = False
        for i in range(k):
            for j in range(1, len(l)):
                flag = False
                if l[j] < l[j - 1]:
                    l.remove(l[j - 1])
                    flag = True
                    break
            if not flag:
                l.pop(-1)
        return ''.join(l)


nums = "1247"
print(Solution().delete(nums, 2))
