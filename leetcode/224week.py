class Solution(object):

    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        m = {}
        for i in rectangles:
            index = min(i[0], i[1])
            if index in m:
                m[index] += 1
            else:
                m[index] = 1
        res = max(m)
        return m[res]


rectangles = [[2, 3], [3, 7], [4, 3], [3, 7]]
print(Solution().countGoodRectangles(rectangles))
