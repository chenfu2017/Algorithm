from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        res = 0
        sum = 0
        n =len(customers)
        for customer,flag in zip(customers,grumpy):
            if flag == 0:
                sum +=customer
        left = right = 0
        count = 0
        while right < n:
            count += 1
            if grumpy[right] == 1:
                sum +=customers[right]
            if count > X:
                if grumpy[left] == 1:
                    sum -=customers[left]
                left +=1
                count -=1
            res = max(res,sum)
            right +=1
        return res


customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
X = 3
print(Solution().maxSatisfied(customers, grumpy, X))
