class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)
        if B >= H or E >= C or F >= D or A >= G:
            return area1 + area2
        right = min(C, G)
        top = min(D, H)
        down = max(B, F)
        left = max(A, E)

        return area1 - (top - down) * (right - left) + area2


A, B, C, D, E, F, G, H = -5, -5, -4, 0, -3, -3, 3, 3
print(Solution().computeArea(A, B, C, D, E, F, G, H))
