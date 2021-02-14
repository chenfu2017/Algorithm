from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n <2:
            return n
        res = temp = 1
        flag = 1
        left = 0
        right = 1

        while right < n:
            if right == left + 1:
                if arr[right] > arr[left]:
                    temp = 2
                    flag = -1
                elif arr[right] < arr[left]:
                    temp = 2
                    flag = 1
                else:
                    left +=1
                right += 1
            else:
                while right < n and flag * arr[right - 1] < flag * arr[right]:
                    flag = -flag
                    right += 1
                    temp += 1
                if temp > res:
                    res = temp
                left = right - 1
            res = max(res,temp)
        return res


arr = [10,123,21,3,213,213,12,3,12,3]
print(Solution().maxTurbulenceSize(arr))
