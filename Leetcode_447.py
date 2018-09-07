class Solution:
    def numberOfBoomerangs(self, points):
        res = 0
        for p1 in points:
            m = {}
            for p2 in points:
                if p1 != p2:
                    if self.dis(p1, p2) in m:
                        m[self.dis(p1, p2)] += 1
                    else:
                        m[self.dis(p1, p2)] = 1
            for i in m:
                res += m[i] * (m[i] - 1)
        return res

    def dis(self,p1, p2):
        return (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])


list = [[0, 0], [1, 0], [2, 0]]
Solution().numberOfBoomerangs(list)
