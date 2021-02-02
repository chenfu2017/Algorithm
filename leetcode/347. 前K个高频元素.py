import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        l = []
        res = []
        print(d)
        for i in d:
            if len(l) < k:
                heapq.heappush(l, (d[i], i))
            else:
                if d[i] > l[0][0]:
                    heapq.heappushpop(l,(d[i], i))
        while len(l) > 0:
            res.append(heapq.heappop(l)[1])
        return res


nums = [4,1,-1,2,-1,2,3]
k = 2
print(Solution().topKFrequent(nums, k))
