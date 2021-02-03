import heapq


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxqueue = []
        self.minqueue = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.maxqueue, -num)
        heapq.heappush(self.minqueue, -heapq.heappop(self.maxqueue))
        if len(self.minqueue) > len(self.maxqueue):
            heapq.heappush(self.maxqueue, -heapq.heappop(self.minqueue))

    def findMedian(self):
        """
        :rtype: float
        """
        print(self.minqueue)
        print(self.maxqueue)
        if len(self.minqueue) < len(self.maxqueue):
            return -self.maxqueue[0]
        else:
            return (-self.maxqueue[0] + self.minqueue[0]) * 0.5


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
param_2 = obj.findMedian()
print(param_2)
