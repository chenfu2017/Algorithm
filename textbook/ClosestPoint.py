class Solution:

    def close_point(self, points):
        if len(points) == 2:
            return points[1] - points[0]
        elif len(points) < 2:
            return float('inf')
        mid = len(points) // 2
        left = points[:mid]
        right = points[mid:]
        d = right[0] - left[-1]
        return min(self.close_point(left), self.close_point(right), d)


points = [1, 3, 7, 10, 15, 20, 25]
print(Solution().close_point(points))
