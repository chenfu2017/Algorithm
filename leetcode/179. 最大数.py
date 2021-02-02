class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        m = map(str, nums)
        m = sorted(m, key=LargerNumKey)
        res = ''.join(m)
        return '0' if int(res)==0 else res


nums = [0,0]
print(Solution().largestNumber(nums))
