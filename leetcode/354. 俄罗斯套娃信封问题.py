from typing import List
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        dp = [1] * n
        envelopes.sort(key=lambda e: (e[0], -e[1],))
        f = [envelopes[0][1]]
        for i in range(1,n):
            num = envelopes[i][1]
            if  num > f[-1]:
                f.append(num)
            else:
                index = bisect.bisect_left(f,num)
                f[index] = num
        return len(f)


envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
print(Solution().maxEnvelopes(envelopes))
