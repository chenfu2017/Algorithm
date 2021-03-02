from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        l = [0] * (num + 1)
        for i in range(1, num + 1):
            if i & 1 == 0:
                l[i] = l[i // 2]
            else:
                l[i] = l[i - 1] + 1
        return l


n = 2
print(Solution().countBits(n))
