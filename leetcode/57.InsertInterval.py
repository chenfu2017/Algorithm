# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        i = 0
        length = len(intervals)
        while i < length and intervals[i].end < newInterval.start:
            result.append(intervals[i])
            i += 1
        while i < length and intervals[i].start <= newInterval.end:
            newInterval.start = min(intervals[i].start, newInterval.start)
            newInterval.end = max(newInterval.end, intervals[i].end)
            i += 1
        result.append(newInterval)
        result.extend(intervals[i:][:])
        return result


intervals = [Interval(1,2),Interval(3,5),Interval(6, 7), Interval(8,10),Interval(12,16)]
result = Solution().insert(intervals, Interval(4,8))
for r in result:
    print(r.start, r.end)
