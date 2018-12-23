# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x.start)
        l = [intervals[0]]
        for interval in intervals[1:]:
            if interval.start <= l[-1].end:
                l[-1].end = max(l[-1].end, interval.end)
            else:
                l.append(interval)
        return l


intervals = [Interval(1,3),Interval(2,6),Interval(8, 10), Interval(12,15)]
result=Solution().merge(intervals)
for r in result:
    print(r.start,r.end)
