from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = -1
        dis = float('inf')
        n = len(points)
        for i in range(n):
            point = points[i]
            if point[0] == x:
                temp = abs(point[1] - y)
                if temp < dis:
                    dis = temp
                    ans = i
            if point[1] == y:
                temp = abs(point[0] - x)
                if temp < dis:
                    dis = temp
                    ans = i
        return ans
x = 3
y = 4
points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
print(Solution().nearestValidPoint(x,y,points))