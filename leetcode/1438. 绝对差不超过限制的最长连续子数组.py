from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 0
        n = len(nums)
        if n < 2:
            return n
        left = 0
        right = 0
        maxqueue, minqueue = deque(), deque()
        while right < n:
            while maxqueue and maxqueue[-1] < nums[right]:
                maxqueue.pop()
            while minqueue and minqueue[-1] > nums[right]:
                minqueue.pop()
            maxqueue.append(nums[right])
            minqueue.append(nums[right])
            while  maxqueue and minqueue and maxqueue[0] - minqueue[0] > limit:
                if nums[left] == minqueue[0]:
                    minqueue.popleft()
                if nums[left] == maxqueue[0]:
                    maxqueue.popleft()
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans


nums = [4, 2, 2, 2, 4, 4, 2, 2]
limit = 0
print(Solution().longestSubarray(nums, limit))
