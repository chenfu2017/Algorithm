# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:

    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        #动态规划
        # n = len(intervals)
        # if n==0:
        #     return n
        # intervals.sort(key=lambda Interval: (Interval.start,Interval.end))
        # m = [1] * n
        # for i in range(1, n):
        #     for j in range(0, i):
        #         if intervals[i].start >= intervals[j].end:
        #             m[i] = max(m[i], 1 + m[j])
        # # print(m)
        # return n - max(m)
        #贪心
        n = len(intervals)
        if n==0:
            return n
        intervals.sort(key=lambda Interval: (Interval.end,Interval.start))
        res = 1
        pre = 0
        for i in range(1,n):
            if intervals[i].start >=intervals[pre].end:
                res +=1
                pre=i
        return n-res


intervals = [Interval(1, 3), Interval(2, 3), Interval(3, 4), Interval(1, 2)]
print(Solution().eraseOverlapIntervals(intervals))
